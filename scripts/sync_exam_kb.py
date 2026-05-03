#!/usr/bin/env python
"""
Exam KB sync — DeepTutor → QuizVerse KB v2 (`qv_exam_<slug>_<kind>`).
====================================================================

This script bridges DeepTutor's structured exam tables (``exam_packs`` /
``exam_questions`` / ``kb_questions``) into the Memory Service's
``qv_exam_<exam_slug>_<doc_kind>`` collections via the QuizVerse BFF
ingest webhook at ``POST /api/kb/ingest/exam``.

It exists because the live KB pipeline is *write-by-webhook only* —
nothing else can mint new ``qv_exam_*`` rows. Until the JIT-ingestion
hook in `routers/exams.py` learns to dual-write into the Memory Service,
this is the canonical way to bulk-seed and to recover from drift.

Idempotent
----------
Documents are POSTed with a stable ``doc_id = "question:{exam_pack_id}:{question_id}"``
(or ``"kb_q:{kb_question_id}"`` when reading from ``kb_questions``).
The Memory Service upserts on ``(collection_id, doc_id)``, so re-running
this script just overwrites the previous embedding.

Usage
-----
    PG_HOST / PG_PORT / PG_DATABASE / PG_USER / PG_PASSWORD   # DeepTutor DB
    QV_KB_BASE_URL=https://quizverse.world                    # default
    QV_KB_INGEST_EXAM_SECRET=<hex>                            # required

    python scripts/sync_exam_kb.py                  # all packs, doc_kind=questions
    python scripts/sync_exam_kb.py --slug jee_main  # one pack
    python scripts/sync_exam_kb.py --slug gre --batch 25
    python scripts/sync_exam_kb.py --source kb      # use kb_questions instead of exam_questions
    python scripts/sync_exam_kb.py --dry-run        # print payloads, don't POST

Args
----
  --slug         <slug>          filter by exam_slug; default = all packs
  --source       exam|kb         table to read; default = exam_packs/exam_questions
  --doc-kind     <kind>          override target doc_kind (default: "questions")
                                 must be one of EXAM_DOC_KINDS in the BFF
  --batch        <N>             docs per POST (default 25; max 50)
  --limit        <N>             cap total questions per pack (debug)
  --dry-run                      print what would be sent, don't POST
"""

from __future__ import annotations

import argparse
import asyncio
import json
import logging
import os
import re
import sys
from pathlib import Path
from typing import Any, Optional

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

import httpx  # noqa: E402
from sqlalchemy import select  # noqa: E402
from sqlalchemy.orm import load_only  # noqa: E402

from deeptutor.services.db.engine import get_session_factory, init_pg  # noqa: E402
from deeptutor.services.exam.models import (  # noqa: E402
    ExamPack,
    ExamQuestion,
    KBQuestion,
)

# Columns we actually need. Excluding `embedding` is critical: it's a
# pgvector column whose deserialiser blows up if libdir/vector isn't
# loaded on whatever PG node the query lands on. We never use embeddings
# from this script — the Memory Service computes its own.
EXAM_Q_COLS = (
    ExamQuestion.id,
    ExamQuestion.exam_pack_id,
    ExamQuestion.subject,
    ExamQuestion.year,
    ExamQuestion.source,
    ExamQuestion.difficulty,
    ExamQuestion.question_text,
    ExamQuestion.options,
    ExamQuestion.correct_answer,
    ExamQuestion.explanation,
    ExamQuestion.tags,
    ExamQuestion.created_at,
)
KB_Q_COLS = (
    KBQuestion.id,
    KBQuestion.exam_type,
    KBQuestion.subject,
    KBQuestion.question_text,
    KBQuestion.options,
    KBQuestion.correct_answer,
    KBQuestion.explanation,
    KBQuestion.difficulty,
    KBQuestion.created_at,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger("sync_exam_kb")


# Mirrors the BFF allow-list at
# Quizverse-web-frontend/web/app/api/kb/ingest/[source]/route.ts
EXAM_DOC_KINDS = {
    "questions",
    "syllabus",
    "tips",
    "papers",
    "cutoff",
    "blog_exam",
    "score_band",
}
EXAM_SLUG_REGEX = re.compile(r"^[a-z0-9_]{2,40}$")
MAX_BATCH = 50


def slugify_pack(name: str) -> str:
    """Convert "JEE Main" → "jee_main" / "GRE General Test" → "gre_general_test".

    The shape must satisfy the BFF's ``EXAM_SLUG_REGEX``; anything that
    fails validation will be rejected upstream and counted as 0 ingested.
    """
    s = name.strip().lower()
    s = re.sub(r"[^a-z0-9]+", "_", s).strip("_")
    if len(s) > 40:
        s = s[:40].rstrip("_")
    return s


def build_question_text(q: ExamQuestion | KBQuestion) -> str:
    """Render a question row into a single Markdown blob suitable for embedding.

    The Memory Service chunker is line-aware, so Markdown headers help it
    keep the question, options, answer, and explanation in the same chunk
    when they're short, and split cleanly when they're long.
    """
    options = q.options or {}
    if isinstance(options, dict):
        opt_lines = [f"- **{k}**: {v}" for k, v in options.items()]
    elif isinstance(options, list):
        opt_lines = [f"- {v}" for v in options]
    else:
        opt_lines = []

    parts: list[str] = [
        f"## Question",
        "",
        (q.question_text or "").strip() or "(no question text)",
        "",
    ]
    if opt_lines:
        parts.extend(["### Options", *opt_lines, ""])
    if getattr(q, "correct_answer", None):
        parts.extend([f"**Correct answer:** {q.correct_answer}", ""])
    explanation = (getattr(q, "explanation", None) or "").strip()
    if explanation:
        parts.extend(["### Explanation", explanation, ""])
    return "\n".join(parts).rstrip() + "\n"


def question_metadata(q: ExamQuestion | KBQuestion, exam_slug: str) -> dict[str, Any]:
    meta: dict[str, Any] = {
        "exam_slug": exam_slug,
        "subject": getattr(q, "subject", None),
        "difficulty": getattr(q, "difficulty", None),
        "correct_answer": getattr(q, "correct_answer", None),
        "title": f"{exam_slug.upper()} {getattr(q, 'subject', 'general')} — {str(q.id)[:8]}",
    }
    year = getattr(q, "year", None)
    if year is not None:
        meta["year"] = year
    source = getattr(q, "source", None)
    if source:
        meta["source"] = source
    tags = getattr(q, "tags", None)
    if tags:
        meta["tags"] = tags
    return {k: v for k, v in meta.items() if v is not None}


async def fetch_packs(slug_filter: Optional[str]) -> list[tuple[str, str]]:
    """Return ``(exam_slug, exam_pack_id_str)`` pairs.

    ``slug_filter`` matches the *slugified* pack name, not the raw name.
    """
    factory = get_session_factory()
    async with factory() as session:
        rows = (await session.execute(select(ExamPack))).scalars().all()
    packs: list[tuple[str, str]] = []
    for p in rows:
        slug = slugify_pack(p.name or "")
        if not slug or not EXAM_SLUG_REGEX.match(slug):
            logger.warning("skipping pack %s — slug %r failed regex", p.id, slug)
            continue
        if slug_filter and slug != slug_filter:
            continue
        packs.append((slug, str(p.id)))
    return packs


async def fetch_exam_questions(
    pack_id_str: str, limit: Optional[int]
) -> list[ExamQuestion]:
    import uuid as _uuid

    pack_uuid = _uuid.UUID(pack_id_str)
    factory = get_session_factory()
    async with factory() as session:
        stmt = (
            select(ExamQuestion)
            .options(load_only(*EXAM_Q_COLS, raiseload=True))
            .where(ExamQuestion.exam_pack_id == pack_uuid)
            .order_by(ExamQuestion.created_at.asc())
        )
        if limit:
            stmt = stmt.limit(limit)
        return (await session.execute(stmt)).scalars().all()


async def fetch_kb_questions(
    exam_type: str, limit: Optional[int]
) -> list[KBQuestion]:
    factory = get_session_factory()
    async with factory() as session:
        stmt = (
            select(KBQuestion)
            .options(load_only(*KB_Q_COLS, raiseload=True))
            .where(KBQuestion.exam_type == exam_type)
            .order_by(KBQuestion.created_at.asc())
        )
        if limit:
            stmt = stmt.limit(limit)
        return (await session.execute(stmt)).scalars().all()


def to_ingest_doc(
    q: ExamQuestion | KBQuestion, exam_slug: str, prefix: str
) -> dict[str, Any]:
    return {
        "doc_id": f"{prefix}:{q.id}",
        "text": build_question_text(q),
        "language": "en",
        "metadata": question_metadata(q, exam_slug),
    }


async def post_batch(
    client: httpx.AsyncClient,
    base_url: str,
    secret: str,
    exam_slug: str,
    doc_kind: str,
    documents: list[dict[str, Any]],
    dry_run: bool,
) -> tuple[bool, str]:
    payload = {
        "exam_slug": exam_slug,
        "doc_kind": doc_kind,
        "documents": documents,
    }
    if dry_run:
        sample = json.dumps(payload, default=str)[:600]
        logger.info("[dry-run] %s/%s: %d docs — %s…", exam_slug, doc_kind, len(documents), sample)
        return True, "dry-run"
    url = f"{base_url.rstrip('/')}/api/kb/ingest/exam"
    # The /api/kb/ingest/<source> routes look for `x-qv-kb-secret`, not
    # `Authorization: Bearer …` (see validateSecret in route.ts).
    headers = {
        "content-type": "application/json",
        "x-qv-kb-secret": secret,
    }
    try:
        res = await client.post(url, json=payload, headers=headers, timeout=30.0)
    except httpx.HTTPError as exc:
        return False, f"network error: {exc}"
    body_text = res.text
    if res.status_code >= 400:
        return False, f"HTTP {res.status_code}: {body_text[:300]}"
    try:
        parsed = res.json()
    except Exception:
        parsed = {"raw": body_text[:300]}
    return True, f"HTTP {res.status_code} ingested={parsed.get('ingested', '?')}"


async def sync_pack(
    client: httpx.AsyncClient,
    base_url: str,
    secret: str,
    exam_slug: str,
    pack_id_str: str,
    source: str,
    doc_kind: str,
    batch: int,
    limit: Optional[int],
    dry_run: bool,
) -> tuple[int, int]:
    """Returns ``(success_doc_count, failure_doc_count)``."""
    if source == "exam":
        rows = await fetch_exam_questions(pack_id_str, limit)
        prefix = f"question:{pack_id_str}"
    else:
        rows = await fetch_kb_questions(exam_slug, limit)
        prefix = "kb_q"
    logger.info(
        "%s: %d question rows from %s%s",
        exam_slug,
        len(rows),
        source,
        f" (limit={limit})" if limit else "",
    )
    if not rows:
        return 0, 0

    docs = [to_ingest_doc(q, exam_slug, prefix) for q in rows]
    ok_count = 0
    fail_count = 0
    for i in range(0, len(docs), batch):
        chunk = docs[i : i + batch]
        ok, msg = await post_batch(
            client, base_url, secret, exam_slug, doc_kind, chunk, dry_run
        )
        if ok:
            ok_count += len(chunk)
            logger.info("  + %s/%s batch %d: %s", exam_slug, doc_kind, i // batch + 1, msg)
        else:
            fail_count += len(chunk)
            logger.error("  ! %s/%s batch %d: %s", exam_slug, doc_kind, i // batch + 1, msg)
    return ok_count, fail_count


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--slug", help="filter by exam_slug (slugified pack name)")
    p.add_argument("--source", choices=["exam", "kb"], default="exam")
    p.add_argument("--doc-kind", default="questions")
    p.add_argument("--batch", type=int, default=25)
    p.add_argument("--limit", type=int, help="cap questions per pack (debug)")
    p.add_argument("--dry-run", action="store_true")
    return p.parse_args()


async def amain() -> int:
    args = parse_args()
    if args.doc_kind not in EXAM_DOC_KINDS:
        logger.error("--doc-kind %r not in %s", args.doc_kind, sorted(EXAM_DOC_KINDS))
        return 2
    if args.batch < 1 or args.batch > MAX_BATCH:
        logger.error("--batch must be in [1, %d]", MAX_BATCH)
        return 2

    base_url = os.environ.get("QV_KB_BASE_URL", "https://quizverse.world").rstrip("/")
    secret = os.environ.get("QV_KB_INGEST_EXAM_SECRET", "")
    if not secret and not args.dry_run:
        logger.error("QV_KB_INGEST_EXAM_SECRET is required (or pass --dry-run)")
        return 2

    if not os.environ.get("PG_HOST"):
        logger.error("PG_HOST not set — DeepTutor exam DB unreachable")
        return 2
    await init_pg()

    packs = await fetch_packs(args.slug)
    if not packs:
        logger.error("no exam packs match filter slug=%r", args.slug)
        return 1
    logger.info(
        "%d pack(s) targeted: %s (source=%s doc_kind=%s)",
        len(packs),
        ", ".join(slug for slug, _ in packs),
        args.source,
        args.doc_kind,
    )

    grand_ok = 0
    grand_fail = 0
    async with httpx.AsyncClient() as client:
        for slug, pack_id in packs:
            ok, fail = await sync_pack(
                client,
                base_url,
                secret,
                slug,
                pack_id,
                args.source,
                args.doc_kind,
                args.batch,
                args.limit,
                args.dry_run,
            )
            grand_ok += ok
            grand_fail += fail

    logger.info(
        "DONE total ingested=%d failed=%d packs=%d", grand_ok, grand_fail, len(packs)
    )
    return 0 if grand_fail == 0 else 1


def main() -> None:
    rc = asyncio.run(amain())
    sys.exit(rc)


if __name__ == "__main__":
    main()
