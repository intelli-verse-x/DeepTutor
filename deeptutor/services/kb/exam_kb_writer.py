"""Outbound writer for KB_EXAM (`qv_exam_<slug>_<doc_kind>`).

When DeepTutor finalizes a generated mimic / sample paper, this writer
ships the freshly created question-answer pairs to
``POST /api/kb/ingest/exam`` so they become searchable via the unified
read API (`POST /api/v1/kb/search { kb: 'exam', exam: '<slug>', ... }`).

This is the live-append counterpart to ``scripts/sync_exam_kb.py`` —
the script does the one-shot historical dump from ``exam_questions``;
this writer does the every-paper trickle.

Configuration (env)
-------------------
* ``QV_KB_BASE_URL``                 — defaults to ``https://quizverse.world``
* ``QV_KB_INGEST_EXAM_SECRET``       — required; if unset, every push no-ops

Failure semantics
-----------------
Identical to ``user_kb_writer``: every error is swallowed, every push is
logged, and nothing in this module is allowed to raise into the calling
agent / coordinator path. KB writes must never break paper generation.
"""

from __future__ import annotations

import logging
import os
import re
from typing import Any, Optional

import httpx

logger = logging.getLogger(__name__)

EXAM_SLUG_REGEX = re.compile(r"^[a-z0-9_]{2,40}$")


def normalize_exam_slug(raw: Optional[str]) -> Optional[str]:
    """Convert a free-form exam name into the BFF's canonical slug.

    Examples
    --------
    >>> normalize_exam_slug("JEE Main")
    'jee_main'
    >>> normalize_exam_slug("CBSE 12th")
    'cbse_12th'
    >>> normalize_exam_slug("GRE")
    'gre'
    >>> normalize_exam_slug("not an exam!@#")
    'not_an_exam'

    Returns ``None`` for empty input or a slug that fails the validator.
    """
    if not raw:
        return None
    s = raw.strip().lower()
    s = re.sub(r"[^a-z0-9]+", "_", s).strip("_")
    if not s:
        return None
    s = s[:40]
    return s if EXAM_SLUG_REGEX.match(s) else None

# Maximum length per ingested document text — chunker on the Memory
# Service splits further as needed. Kept generous because each "doc" is
# a question + options + answer + explanation.
MAX_EMBED_CHARS = 8000

# httpx timeout — kept short. Paper generation can dispatch dozens of
# documents; we batch them in chunks of <= INGEST_BATCH below to stay
# inside the BFF's 4-second upstream budget.
POST_TIMEOUT_S = 6.0
INGEST_BATCH = 8


def _truncate(text: str, limit: int = MAX_EMBED_CHARS) -> str:
    if len(text) <= limit:
        return text
    return text[: limit - 32] + "\n\n…[truncated for KB ingest]"


def _format_question_text(qa: dict[str, Any]) -> str:
    """Flatten one mimic-generated QA pair into a single retrievable doc."""
    parts: list[str] = []

    stem = (qa.get("question") or qa.get("stem") or "").strip()
    if stem:
        parts.extend(["## Question", "", stem])

    opts = qa.get("options") or qa.get("choices")
    if isinstance(opts, dict) and opts:
        parts.extend(["", "### Options"])
        for k, v in list(opts.items())[:8]:
            parts.append(f"- {k}: {str(v)[:300]}")
    elif isinstance(opts, list) and opts:
        parts.extend(["", "### Options"])
        for i, v in enumerate(opts[:8]):
            label = chr(ord("A") + i)
            parts.append(f"- {label}: {str(v)[:300]}")

    correct = qa.get("correct_answer") or qa.get("answer")
    if correct:
        parts.extend(["", f"### Correct answer", "", str(correct)[:200]])

    expl = qa.get("explanation") or qa.get("solution") or qa.get("reasoning")
    if expl:
        parts.extend(["", "### Explanation", "", str(expl)[:3000]])

    return _truncate("\n".join(parts).rstrip() + "\n")


def _build_paper_doc(
    *,
    batch_id: str,
    idx: int,
    qa: dict[str, Any],
    exam_slug: str,
    paper_title: Optional[str],
) -> Optional[dict[str, Any]]:
    text = _format_question_text(qa)
    # Skip silently if the QA pair is too thin to be useful in retrieval
    if len(text.strip()) < 40:
        return None

    qid = qa.get("id") or qa.get("question_id") or f"q{idx:03d}"
    metadata: dict[str, Any] = {
        "source": "deeptutor.mimic",
        "batch_id": batch_id,
        "paper_title": paper_title or "Generated paper",
    }
    subject = qa.get("subject") or qa.get("topic")
    if subject:
        metadata["subject"] = subject
    difficulty = qa.get("difficulty")
    if difficulty:
        metadata["difficulty"] = difficulty
    template_id = qa.get("template_id") or qa.get("template")
    if template_id:
        metadata["template_id"] = template_id

    return {
        "doc_id": f"mimic:{batch_id}:{qid}",
        "text": text,
        "language": qa.get("language") or "en",
        "metadata": metadata,
    }


async def _post_exam_ingest(
    *,
    exam_slug: str,
    doc_kind: str,
    documents: list[dict[str, Any]],
    log_tag: str,
) -> None:
    if not documents:
        return
    base_url = os.environ.get("QV_KB_BASE_URL", "https://quizverse.world").rstrip("/")
    secret = os.environ.get("QV_KB_INGEST_EXAM_SECRET", "")
    if not secret:
        logger.debug(f"skip exam push ({log_tag}): QV_KB_INGEST_EXAM_SECRET not set")
        return

    payload = {
        "exam_slug": exam_slug,
        "doc_kind": doc_kind,
        "documents": documents,
    }
    headers = {"content-type": "application/json", "x-qv-kb-secret": secret}
    url = f"{base_url}/api/kb/ingest/exam"

    try:
        async with httpx.AsyncClient(timeout=POST_TIMEOUT_S) as client:
            res = await client.post(url, json=payload, headers=headers)
        if res.status_code >= 400:
            logger.warning(
                f"exam push failed ({log_tag}): exam={exam_slug} kind={doc_kind} "
                f"HTTP {res.status_code} — {res.text[:200]}"
            )
            return
        logger.info(
            f"exam push ok ({log_tag}): exam={exam_slug} kind={doc_kind} "
            f"docs={len(documents)} HTTP {res.status_code}"
        )
    except httpx.HTTPError as exc:
        logger.warning(
            f"exam push network error ({log_tag}): exam={exam_slug} kind={doc_kind} — {exc}"
        )
    except Exception as exc:
        logger.warning(
            f"exam push unexpected error ({log_tag}): exam={exam_slug} kind={doc_kind} — {exc}"
        )


async def push_exam_paper_questions(
    *,
    exam_slug: str,
    batch_id: str,
    qa_pairs: list[dict[str, Any]],
    paper_title: Optional[str] = None,
) -> None:
    """Fire-and-forget POST of generated paper QAs into ``qv_exam_<slug>_questions``.

    ``qa_pairs`` is the ``results`` list from the mimic coordinator's
    summary — each item is expected to have at least ``question`` /
    ``correct_answer`` /  ``explanation`` keys (others are best-effort).
    Documents that don't satisfy the minimum-length check are dropped
    silently; the caller is never told.

    Anything that would normally raise (regex mismatch, missing secret,
    upstream 5xx, network timeout) is logged and swallowed. The caller
    does not need a try/except.
    """
    if not exam_slug or not EXAM_SLUG_REGEX.match(exam_slug):
        logger.debug(f"skip exam push: exam_slug {exam_slug!r} invalid")
        return
    if not qa_pairs:
        return

    docs: list[dict[str, Any]] = []
    for i, qa in enumerate(qa_pairs):
        if not isinstance(qa, dict):
            continue
        # A failed QA from the coordinator carries success=False — don't
        # dump those into the KB, they're noise.
        if qa.get("success") is False:
            continue
        d = _build_paper_doc(
            batch_id=batch_id,
            idx=i,
            qa=qa,
            exam_slug=exam_slug,
            paper_title=paper_title,
        )
        if d is not None:
            docs.append(d)

    if not docs:
        logger.debug(
            f"skip exam push: no valid documents from batch={batch_id} "
            f"exam={exam_slug} (in={len(qa_pairs)})"
        )
        return

    # Fan out in small batches so a slow upstream embed doesn't time us
    # out for the whole paper.
    for i in range(0, len(docs), INGEST_BATCH):
        chunk = docs[i : i + INGEST_BATCH]
        await _post_exam_ingest(
            exam_slug=exam_slug,
            doc_kind="questions",
            documents=chunk,
            log_tag=f"paper:{batch_id}:{i // INGEST_BATCH}",
        )
