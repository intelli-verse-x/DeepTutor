"""Outbound writers for KB_USER (`qv_u_<uid>_<kind>`).

Three fire-and-forget producers feed the user-side knowledge base from
DeepTutor:

* ``push_user_chat``           — one document per (user, session, turn) into
                                  ``qv_u_<uid>_chat``. Called from
                                  ``deeptutor.api.routers.chat`` (HTTP + WS).
* ``push_user_diagnostic``     — one document per recorded diagnostic
                                  answer into ``qv_u_<uid>_diagnostic``.
                                  Called from ``/api/v1/exams/diagnostic/answer``.
* ``push_user_score_prediction`` — one document per persisted score
                                    prediction into ``qv_u_<uid>_insights``.
                                    Called from ``/api/v1/exams/score-predict``.

All three:

* are ``async`` and intended to run via ``asyncio.create_task(...)``
* swallow every error path (regex mismatch, missing secret, 5xx, timeout)
* log at INFO on success, WARNING on a real failure, DEBUG on no-op skips
* never raise — KB writes must never block or crash a user-facing response

The BFF endpoint (`Quizverse-web-frontend/web/app/api/kb/ingest/[source]/route.ts`)
expects ``POST /api/kb/ingest/user`` with header ``x-qv-kb-secret`` and JSON::

    {
      "user_id":  "<id>",                 # ^[A-Za-z0-9_-]{4,128}$
      "doc_kind": "chat" | "diagnostic" | "insights" | ...,  # USER_DOC_KINDS
      "documents": [
        { "doc_id": "...", "text": "<markdown>", "language": "en", "metadata": {} }
      ]
    }

Configuration (env)
-------------------
* ``QV_KB_BASE_URL``                — defaults to ``https://quizverse.world``
* ``QV_KB_INGEST_USER_SECRET``      — required; if unset, every push no-ops
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


async def _post_user_ingest(
    *,
    user_id: str,
    doc_kind: str,
    documents: list[dict[str, Any]],
    log_tag: str,
) -> None:
    """Shared low-level POST to /api/kb/ingest/user.

    Caller must pre-validate ``user_id``. ``log_tag`` is a free-form short
    string that's interpolated into log lines so the same source file can
    distinguish chat / diagnostic / insight pushes in CloudWatch.
    """
    if not documents:
        return
    base_url = os.environ.get("QV_KB_BASE_URL", "https://quizverse.world").rstrip("/")
    secret = os.environ.get("QV_KB_INGEST_USER_SECRET", "")
    if not secret:
        logger.debug(f"skip kb push ({log_tag}): QV_KB_INGEST_USER_SECRET not set")
        return

    payload = {"user_id": user_id, "doc_kind": doc_kind, "documents": documents}
    headers = {"content-type": "application/json", "x-qv-kb-secret": secret}
    url = f"{base_url}/api/kb/ingest/user"

    try:
        async with httpx.AsyncClient(timeout=POST_TIMEOUT_S) as client:
            res = await client.post(url, json=payload, headers=headers)
        if res.status_code >= 400:
            logger.warning(
                f"kb push failed ({log_tag}): user={user_id} kind={doc_kind} "
                f"HTTP {res.status_code} — {res.text[:200]}"
            )
            return
        logger.info(
            f"kb push ok ({log_tag}): user={user_id} kind={doc_kind} "
            f"docs={len(documents)} HTTP {res.status_code}"
        )
    except httpx.HTTPError as exc:
        logger.warning(
            f"kb push network error ({log_tag}): user={user_id} kind={doc_kind} — {exc}"
        )
    except Exception as exc:  # never let kb writes break the user response
        logger.warning(
            f"kb push unexpected error ({log_tag}): user={user_id} kind={doc_kind} — {exc}"
        )


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
        logger.debug(f"skip kb push: user_id {user_id!r} failed regex")
        return
    if not assistant_response.strip():
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

    await _post_user_ingest(
        user_id=user_id,
        doc_kind="chat",
        documents=[doc],
        log_tag="chat",
    )


# ─────────────────────────────────────────────────────────────────────────
# Diagnostic answer writer (KB v2 §5.3 — qv_u_<uid>_diagnostic)
# ─────────────────────────────────────────────────────────────────────────


def _build_diagnostic_doc(
    *,
    answer_id: str,
    session_id: str,
    exam_type: Optional[str],
    subject: Optional[str],
    difficulty: Optional[str],
    question_text: str,
    options: Optional[dict[str, Any]],
    selected_answer: str,
    correct_answer: Optional[str],
    is_correct: bool,
    language: str,
) -> dict[str, Any]:
    """Render one diagnostic answer into an ingest-ready document.

    ``doc_id`` shape: ``diagnostic:<session_id>:<answer_id>`` — answer_id
    is the DB primary key so re-runs on the same answer overwrite.
    """
    correctness = "correct" if is_correct else "incorrect"
    body_parts: list[str] = [
        "## Diagnostic answer",
        "",
        f"- exam: {exam_type or '(unknown)'}",
        f"- subject: {subject or '(unknown)'}",
        f"- difficulty: {difficulty or '(unknown)'}",
        f"- result: {correctness}",
        "",
        "### Question",
        "",
        (question_text or "").strip()[:1500] or "(no question text)",
    ]
    if isinstance(options, dict) and options:
        body_parts.extend(["", "### Options"])
        for k, v in list(options.items())[:8]:
            body_parts.append(f"- {k}: {str(v)[:200]}")
    body_parts.extend([
        "",
        f"### Selected: {selected_answer}",
    ])
    if correct_answer:
        body_parts.append(f"### Correct: {correct_answer}")
    text = _truncate("\n".join(body_parts).rstrip() + "\n")

    metadata: dict[str, Any] = {
        "kind": "diagnostic_answer",
        "session_id": session_id,
        "answer_id": answer_id,
        "is_correct": bool(is_correct),
        "title": f"{(subject or 'diagnostic').title()} · {correctness}",
    }
    if exam_type:
        metadata["exam_type"] = exam_type
    if subject:
        metadata["subject"] = subject
    if difficulty:
        metadata["difficulty"] = difficulty

    return {
        "doc_id": f"diagnostic:{session_id}:{answer_id}",
        "text": text,
        "language": language or "en",
        "metadata": metadata,
    }


async def push_user_diagnostic(
    *,
    user_id: Optional[str],
    session_id: Optional[str],
    answer_id: str,
    exam_type: Optional[str],
    subject: Optional[str],
    difficulty: Optional[str],
    question_text: str,
    options: Optional[dict[str, Any]],
    selected_answer: str,
    correct_answer: Optional[str],
    is_correct: bool,
    language: str = "en",
) -> None:
    """Fire-and-forget POST of one diagnostic answer into ``qv_u_<uid>_diagnostic``.

    Callers should schedule via ``asyncio.create_task(...)`` immediately
    after the DB commit that persists the answer.
    """
    if not user_id or not session_id or not answer_id:
        return
    if not USER_ID_REGEX.match(user_id):
        logger.debug(f"skip diagnostic push: user_id {user_id!r} failed regex")
        return

    doc = _build_diagnostic_doc(
        answer_id=str(answer_id),
        session_id=str(session_id),
        exam_type=exam_type,
        subject=subject,
        difficulty=difficulty,
        question_text=question_text or "",
        options=options,
        selected_answer=selected_answer or "",
        correct_answer=correct_answer,
        is_correct=is_correct,
        language=language,
    )
    await _post_user_ingest(
        user_id=user_id,
        doc_kind="diagnostic",
        documents=[doc],
        log_tag="diagnostic",
    )


# ─────────────────────────────────────────────────────────────────────────
# Score prediction writer (KB v2 §5.3 — qv_u_<uid>_insights)
# ─────────────────────────────────────────────────────────────────────────


def _build_score_prediction_doc(
    *,
    prediction_id: str,
    exam_type: str,
    predicted_score: float,
    max_score: float,
    percentile: float,
    predicted_rank: Optional[int],
    subject_breakdown: Optional[dict[str, Any]],
    ai_insights: Optional[dict[str, Any]],
    questions_analyzed: int,
    language: str,
) -> dict[str, Any]:
    """Render one persisted ``ScorePrediction`` row into an insight document."""
    pct = (predicted_score / max_score * 100.0) if max_score else 0.0
    body_parts: list[str] = [
        f"## Score prediction · {exam_type}",
        "",
        f"- predicted: **{predicted_score:.1f} / {max_score:.0f}**  ({pct:.1f}%)",
        f"- percentile: {percentile:.1f}",
    ]
    if predicted_rank is not None:
        body_parts.append(f"- predicted rank: {predicted_rank}")
    body_parts.append(f"- based on: {questions_analyzed} answered questions")

    if isinstance(subject_breakdown, dict) and subject_breakdown:
        body_parts.extend(["", "### Subject breakdown"])
        for k, v in list(subject_breakdown.items())[:12]:
            body_parts.append(f"- {k}: {v}")

    if isinstance(ai_insights, dict) and ai_insights:
        weak = ai_insights.get("weak_areas") or ai_insights.get("weak") or []
        strong = ai_insights.get("strong_areas") or ai_insights.get("strong") or []
        recs = ai_insights.get("recommendations") or ai_insights.get("next") or []
        if weak:
            body_parts.extend(["", "### Weak areas", *(f"- {x}" for x in weak[:6])])
        if strong:
            body_parts.extend(["", "### Strong areas", *(f"- {x}" for x in strong[:6])])
        if recs:
            body_parts.extend(["", "### Next steps", *(f"- {x}" for x in recs[:6])])

    text = _truncate("\n".join(body_parts).rstrip() + "\n")

    metadata: dict[str, Any] = {
        "kind": "score_prediction",
        "exam_type": exam_type,
        "prediction_id": prediction_id,
        "predicted_score": float(predicted_score),
        "max_score": float(max_score),
        "percentile": float(percentile),
        "questions_analyzed": int(questions_analyzed),
        "title": f"{exam_type.upper()} score prediction · {pct:.1f}%",
    }
    if predicted_rank is not None:
        metadata["predicted_rank"] = int(predicted_rank)

    return {
        "doc_id": f"score:{exam_type}:{prediction_id}",
        "text": text,
        "language": language or "en",
        "metadata": metadata,
    }


async def push_user_score_prediction(
    *,
    user_id: Optional[str],
    prediction_id: str,
    exam_type: str,
    predicted_score: float,
    max_score: float,
    percentile: float = 0.0,
    predicted_rank: Optional[int] = None,
    subject_breakdown: Optional[dict[str, Any]] = None,
    ai_insights: Optional[dict[str, Any]] = None,
    questions_analyzed: int = 0,
    language: str = "en",
) -> None:
    """Fire-and-forget POST of one score prediction into ``qv_u_<uid>_insights``.

    Score predictions are routed to the ``insights`` doc-kind because they
    are LLM-derived signals about the user (per the master plan §5.3:
    insights collection holds ``LLM-generated insights``). The cron-based
    insights producer (WF-44) writes alongside this with its own doc_ids;
    both share the same collection and read path.
    """
    if not user_id or not prediction_id or not exam_type:
        return
    if not USER_ID_REGEX.match(user_id):
        logger.debug(f"skip score push: user_id {user_id!r} failed regex")
        return

    doc = _build_score_prediction_doc(
        prediction_id=str(prediction_id),
        exam_type=exam_type,
        predicted_score=float(predicted_score),
        max_score=float(max_score) if max_score else 0.0,
        percentile=float(percentile),
        predicted_rank=predicted_rank,
        subject_breakdown=subject_breakdown,
        ai_insights=ai_insights,
        questions_analyzed=int(questions_analyzed),
        language=language,
    )
    await _post_user_ingest(
        user_id=user_id,
        doc_kind="insights",
        documents=[doc],
        log_tag="score_prediction",
    )
