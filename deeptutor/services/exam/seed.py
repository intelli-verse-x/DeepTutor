"""Seed script — populates exam_packs + exam_subjects with the 16 exam types.

Run standalone:  python -m deeptutor.services.exam.seed
Or called from application startup when tables are empty.
"""

from __future__ import annotations

import asyncio
import logging
import uuid

from sqlalchemy import func, select

from deeptutor.services.exam.db import get_session, init_pg
from deeptutor.services.exam.models import ExamPack, ExamSubject

logger = logging.getLogger("exam.seed")

EXAM_PACKS: list[dict] = [
    # India
    {"country_code": "IN", "country_name": "India", "name": "JEE Main", "tier": 1, "price_display": "₹499/mo", "currency": "INR", "question_count": 2400, "subjects": ["Physics", "Chemistry", "Mathematics"]},
    {"country_code": "IN", "country_name": "India", "name": "JEE Advanced", "tier": 1, "price_display": "₹699/mo", "currency": "INR", "question_count": 1800, "subjects": ["Physics", "Chemistry", "Mathematics"]},
    {"country_code": "IN", "country_name": "India", "name": "NEET UG", "tier": 1, "price_display": "₹499/mo", "currency": "INR", "question_count": 3200, "subjects": ["Physics", "Chemistry", "Biology"]},
    {"country_code": "IN", "country_name": "India", "name": "CBSE 10th", "tier": 2, "price_display": "₹199/mo", "currency": "INR", "question_count": 2000, "subjects": ["Mathematics", "Science", "English", "SST"]},
    {"country_code": "IN", "country_name": "India", "name": "CBSE 12th", "tier": 2, "price_display": "₹299/mo", "currency": "INR", "question_count": 2500, "subjects": ["Physics", "Chemistry", "Mathematics"]},
    {"country_code": "IN", "country_name": "India", "name": "CAT", "tier": 2, "price_display": "₹599/mo", "currency": "INR", "question_count": 1500, "subjects": ["Quant", "VARC", "DILR"]},
    {"country_code": "IN", "country_name": "India", "name": "GATE (CS)", "tier": 2, "price_display": "₹499/mo", "currency": "INR", "question_count": 1800, "subjects": ["DSA", "OS", "DBMS", "Networks"]},
    {"country_code": "IN", "country_name": "India", "name": "UPSC Prelims", "tier": 3, "price_display": "₹799/mo", "currency": "INR", "question_count": 3000, "subjects": ["GS", "CSAT", "Current Affairs"]},
    # USA
    {"country_code": "US", "country_name": "USA", "name": "SAT", "tier": 1, "price_display": "$9.99/mo", "currency": "USD", "question_count": 2000, "subjects": ["Math", "Reading", "Writing"]},
    {"country_code": "US", "country_name": "USA", "name": "ACT", "tier": 1, "price_display": "$9.99/mo", "currency": "USD", "question_count": 1800, "subjects": ["English", "Math", "Reading", "Science"]},
    {"country_code": "US", "country_name": "USA", "name": "AP Calculus AB", "tier": 2, "price_display": "$7.99/mo", "currency": "USD", "question_count": 800, "subjects": ["Limits", "Derivatives", "Integrals"]},
    {"country_code": "US", "country_name": "USA", "name": "AP Physics 1", "tier": 2, "price_display": "$7.99/mo", "currency": "USD", "question_count": 700, "subjects": ["Mechanics", "Waves", "Circuits"]},
    {"country_code": "US", "country_name": "USA", "name": "AP Chemistry", "tier": 2, "price_display": "$7.99/mo", "currency": "USD", "question_count": 750, "subjects": ["Atomic", "Bonding", "Reactions"]},
    {"country_code": "US", "country_name": "USA", "name": "GRE", "tier": 2, "price_display": "$14.99/mo", "currency": "USD", "question_count": 1500, "subjects": ["Quant", "Verbal", "AWA"]},
    {"country_code": "US", "country_name": "USA", "name": "GMAT", "tier": 2, "price_display": "$14.99/mo", "currency": "USD", "question_count": 1200, "subjects": ["Quant", "Verbal", "IR", "AWA"]},
    # China
    {"country_code": "CN", "country_name": "China", "name": "高考 (Gaokao)", "tier": 1, "price_display": "¥39/月", "currency": "CNY", "question_count": 3000, "is_coming_soon": True, "subjects": ["语文", "数学", "英语", "理综/文综"]},
    {"country_code": "CN", "country_name": "China", "name": "中考 (Zhongkao)", "tier": 2, "price_display": "¥29/月", "currency": "CNY", "question_count": 2000, "is_coming_soon": True, "subjects": ["语文", "数学", "英语", "物理", "化学"]},
]


async def seed_exam_packs() -> int:
    """Insert all exam packs if the table is empty.  Returns count inserted."""
    created = 0
    async for session in get_session():
        count = (await session.execute(select(func.count()).select_from(ExamPack))).scalar()
        if count and count > 0:
            logger.info("Exam packs already seeded (%d rows) — skipping", count)
            return 0

        for ep_data in EXAM_PACKS:
            subjects = ep_data.pop("subjects")
            is_coming_soon = ep_data.pop("is_coming_soon", False)
            ep = ExamPack(is_coming_soon=is_coming_soon, **ep_data)
            session.add(ep)
            await session.flush()

            for i, subj_name in enumerate(subjects):
                session.add(ExamSubject(exam_pack_id=ep.id, name=subj_name, order=i))

            created += 1

        await session.commit()
        logger.info("Seeded %d exam packs", created)
    return created


async def _main():
    ok = await init_pg()
    if not ok:
        print("PG_HOST not set — cannot seed")
        return
    n = await seed_exam_packs()
    print(f"Seeded {n} exam packs")


if __name__ == "__main__":
    asyncio.run(_main())
