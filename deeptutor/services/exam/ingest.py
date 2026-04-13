"""Question ingestion — loads question_bank.py into PostgreSQL exam_questions.

Run standalone:  python -m deeptutor.services.exam.ingest
Or called after seed.py during startup.
"""

from __future__ import annotations

import asyncio
import logging
import uuid

from sqlalchemy import func, select

from deeptutor.services.exam.db import get_session, init_pg
from deeptutor.services.exam.models import ExamPack, ExamQuestion
from deeptutor.services.exam.question_bank import QUESTIONS

logger = logging.getLogger("exam.ingest")


async def ingest_questions() -> int:
    """Insert questions from the static question bank for every exam pack.
    Skips if questions already exist for a pack.
    Returns total questions inserted.
    """
    total = 0
    async for session in get_session():
        packs_stmt = select(ExamPack)
        packs = (await session.execute(packs_stmt)).scalars().all()
        pack_map = {p.name: p for p in packs}

        for exam_name, questions in QUESTIONS.items():
            pack = pack_map.get(exam_name)
            if not pack:
                logger.warning("No exam pack found for '%s' — skipping", exam_name)
                continue

            existing = (await session.execute(
                select(func.count())
                .select_from(ExamQuestion)
                .where(ExamQuestion.exam_pack_id == pack.id)
            )).scalar()
            if existing and existing > 0:
                logger.info("Pack '%s' already has %d questions — skipping", exam_name, existing)
                continue

            for q_data in questions:
                q = ExamQuestion(
                    exam_pack_id=pack.id,
                    subject=q_data["subject"],
                    year=q_data.get("year"),
                    source=q_data.get("source"),
                    difficulty=q_data.get("difficulty", "medium"),
                    question_text=q_data["question_text"],
                    options=q_data["options"],
                    correct_answer=q_data["correct_answer"],
                    explanation=q_data.get("explanation"),
                    tags=q_data.get("tags", []),
                )
                session.add(q)
                total += 1

            pack.question_count = max(pack.question_count, len(questions))
            logger.info("Ingested %d questions for '%s'", len(questions), exam_name)

        await session.commit()
    return total


async def _main():
    ok = await init_pg()
    if not ok:
        print("PG_HOST not set — cannot ingest")
        return
    from deeptutor.services.exam.seed import seed_exam_packs
    await seed_exam_packs()
    n = await ingest_questions()
    print(f"Ingested {n} questions total")


if __name__ == "__main__":
    asyncio.run(_main())
