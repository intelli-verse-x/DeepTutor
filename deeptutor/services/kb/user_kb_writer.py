"""Outbound writer: push DeepTutor chat turns into ``qv_u_<uid>_chat``.

Invoked from ``deeptutor.api.routers.chat`` at the end of each turn.
Calling code should *always* schedule this via ``asyncio.create_task``
so the user-facing response isn't blocked on an upstream embed.

KB v2 surface
-------------
The BFF (`Quizverse-web-frontend/web/app/api/kb/ingest/[source]/route.ts`)
expects::

    POST /api/kb/ingest/user
    Authorization: Bearer ${QV_KB_INGEST_USER_SECRET}
    {
      "user_id":  "<id>",                 # ^[A-Za-z0-9_-]{4,128}$
      "doc_kind": "chat",                 # one of USER_DOC_KINDS
      "documents": [
        {
          "doc_id":   "chat:<sid>:<turn>",
          "text":     "<markdown>",
          "language": "en",
          "metadata": { ... }
        }
      ]
    }

Failure modes
-------------
This helper is intentionally *very* permissive. Any of:

* missing/invalid ``user_id``
* missing ``QV_KB_INGEST_USER_SECRET`` env var
* unreachable BFF / 5xx upstream
* network timeout

…will cause it to log a warning and exit cleanly. We do **not** retry
because the BFF + Memory Service have their own retry queue, and a
failed chat-turn write is far less costly than a failed user response.
"""

from __future__ import annotations

import os
import re
import time
from typing import Any, Optional

import httpx

from deeptutor.logging import get_logger

logger = get_logger("services.kb.user_kb_writer", level="INFO")

USER_ID_REGEX = re.compile(r"^[A-Za-z0-9_-]{4,128}$")

# Maximum length for combined user+assistant text we'll embed in a single
# turn. Anything longer is truncated with a marker — the chunker on the
# Memory Service side will split further as needed.
MAX_EMBED_CHARS = 6000

# httpx.AsyncClient timeout for the fire-and-forget POST. Kept short so
# slow upstreams can never tail-latency the chat response.
POST_TIMEOUT_S = 4.0


def _truncate(text: str, limit: int = MAX_EMBED_CHARS) -> str:
    if len(text) <= limit:
        return text
    return text[: limit - 32] + "\n\n…[truncated for KB ingest]"


def _build_doc(
    *,
    user_id: str,
    session_id: str,
    user_message: str,
    assistant_response: str,
    language: str,
    sources: Optional[dict[str, Any]],
    tutor_type: Optional[str],
) -> dict[str, Any]:
    """Render one chat turn into an ingest-ready document.

    ``doc_id`` shape: ``chat:<session_id>:<unix_seconds>``. Using a
    timestamp suffix means a single (user, session) chat keeps a
    growing trail of turn-level rows, which is what the
    `attempts/insights` analytics flow expects later.
    """
    body_parts: list[str] = ["## User", "", user_message.strip(), "", "## Assistant", "", assistant_response.strip()]
    rag = (sources or {}).get("rag") or []
    web = (sources or {}).get("web") or []
    if rag or web:
        body_parts.extend(["", "### Sources"])
        for s in rag[:5]:
            title = (s or {}).get("title") or (s or {}).get("doc_id") or "rag-snippet"
            body_parts.append(f"- rag · {title}")
        for s in web[:5]:
            title = (s or {}).get("title") or (s or {}).get("url") or "web-snippet"
            body_parts.append(f"- web · {title}")
    text = _truncate("\n".join(body_parts).rstrip() + "\n")

    turn_id = int(time.time() * 1000)
    metadata: dict[str, Any] = {
        "kind": "chat_turn",
        "session_id": session_id,
        "turn_at_ms": turn_id,
        "title": (user_message.strip().splitlines() or [""])[0][:120] or "chat turn",
    }
    if tutor_type:
        metadata["tutor_type"] = tutor_type

    return {
        "doc_id": f"chat:{session_id}:{turn_id}",
        "text": text,
        "language": language or "en",
        "metadata": metadata,
    }


async def push_user_chat(
    *,
    user_id: Optional[str],
    session_id: Optional[str],
    user_message: str,
    assistant_response: str,
    language: str = "en",
    sources: Optional[dict[str, Any]] = None,
    tutor_type: Optional[str] = None,
) -> None:
    """Fire-and-forget POST of one chat turn into ``qv_u_<uid>_chat``.

    No-ops cleanly when the inputs aren't valid for KB v2 (e.g. anonymous
    users, no session id, missing config). Always returns ``None`` and
    never raises — callers may ``asyncio.create_task`` this without
    bothering with try/except.
    """
    if not user_id or not session_id:
        return
    if not USER_ID_REGEX.match(user_id):
        logger.debug("skip kb push: user_id %r failed regex", user_id)
        return
    if not assistant_response.strip():
        return

    base_url = os.environ.get("QV_KB_BASE_URL", "https://quizverse.world").rstrip("/")
    secret = os.environ.get("QV_KB_INGEST_USER_SECRET", "")
    if not secret:
        logger.debug("skip kb push: QV_KB_INGEST_USER_SECRET not set")
        return

    doc = _build_doc(
        user_id=user_id,
        session_id=session_id,
        user_message=user_message or "",
        assistant_response=assistant_response,
        language=language,
        sources=sources,
        tutor_type=tutor_type,
    )

    payload = {
        "user_id": user_id,
        "doc_kind": "chat",
        "documents": [doc],
    }
    # The /api/kb/ingest/user route validates with `x-qv-kb-secret`,
    # not `Authorization: Bearer …` (see validateSecret in route.ts).
    headers = {
        "content-type": "application/json",
        "x-qv-kb-secret": secret,
    }
    url = f"{base_url}/api/kb/ingest/user"

    try:
        async with httpx.AsyncClient(timeout=POST_TIMEOUT_S) as client:
            res = await client.post(url, json=payload, headers=headers)
        if res.status_code >= 400:
            logger.warning(
                "kb push failed: user=%s sid=%s HTTP %s — %s",
                user_id,
                session_id,
                res.status_code,
                res.text[:200],
            )
            return
        logger.debug(
            "kb push ok: user=%s sid=%s HTTP %s", user_id, session_id, res.status_code
        )
    except httpx.HTTPError as exc:
        logger.warning("kb push network error: user=%s sid=%s — %s", user_id, session_id, exc)
    except Exception as exc:  # never let kb writes break the chat response
        logger.warning("kb push unexpected error: user=%s sid=%s — %s", user_id, session_id, exc)
