"""Exams API router — Exam Packs, Diagnostic Test, Study Plan,
Score Predictor, and Knowledge-Base endpoints.

All endpoints are additive — they only work when PG_HOST is configured.
"""

from __future__ import annotations

import logging
import math
import uuid
from datetime import datetime, timezone
from typing import Any, Optional

from fastapi import APIRouter, Depends, Header, HTTPException, Query
from pydantic import BaseModel, Field
from sqlalchemy import Integer, func, select
from sqlalchemy.ext.asyncio import AsyncSession

from deeptutor.services.exam.db import get_session
from deeptutor.services.exam.models import (
    DiagnosticAnswer,
    DiagnosticSession,
    ExamPack,
    ExamQuestion,
    ExamSubject,
    KBEmbedding,
    KBEnrichmentLog,
    KBQuestion,
    KBSource,
    ScorePrediction,
    StudyPlan,
    StudyPlanTask,
    UserExamProgress,
)

logger = logging.getLogger("routers.exams")
router = APIRouter()


# ---------------------------------------------------------------------------
# Pydantic schemas
# ---------------------------------------------------------------------------

class ExamPackOut(BaseModel):
    id: str
    country_code: str
    country_name: str
    name: str
    tier: int
    price_display: str
    currency: str
    question_count: int
    is_coming_soon: bool
    subjects: list[str]
    metadata: dict[str, Any] = {}

class QuestionOut(BaseModel):
    id: str
    subject: str
    difficulty: str
    question_text: str
    options: dict[str, Any]
    year: Optional[int] = None
    tags: list[Any] = []

class SubmitRequest(BaseModel):
    answers: dict[str, str] = Field(..., description="Map of question_id -> selected answer")

class SubmitResult(BaseModel):
    total: int
    correct: int
    score_pct: float
    per_question: list[dict[str, Any]]

class DiagStartRequest(BaseModel):
    exam_type: str = "jee_main"

class DiagAnswerRequest(BaseModel):
    session_id: str
    question_id: str
    selected: str

class DiagResultOut(BaseModel):
    session_id: str
    status: str
    total_questions: int
    correct: int
    score_pct: float
    subject_scores: dict[str, Any]
    difficulty_progression: list[str]

class StudyPlanOut(BaseModel):
    id: str
    exam_type: str
    days: list[dict[str, Any]]
    generated_at: str

class TaskCompleteRequest(BaseModel):
    task_id: str

class ScorePredictRequest(BaseModel):
    exam_type: str = "jee_main"

class ScorePredictOut(BaseModel):
    predicted_score: float
    max_score: float
    percentile: float
    predicted_rank: Optional[int] = None
    subject_breakdown: dict[str, Any]
    ai_insights: dict[str, Any]

class KBSearchRequest(BaseModel):
    query: str
    exam_type: Optional[str] = None
    limit: int = 10


class KBSourceCreateRequest(BaseModel):
    name: str
    url: Optional[str] = None
    source_type: str = "pdf"
    metadata: dict[str, Any] = {}


class KBIngestItem(BaseModel):
    exam_type: str
    subject: str
    question_text: str
    options: dict[str, Any]
    correct_answer: str
    explanation: Optional[str] = None
    difficulty: str = "medium"


class KBBulkIngestRequest(BaseModel):
    source_id: Optional[str] = None
    questions: list[KBIngestItem]


class KBEmbedRequest(BaseModel):
    """Trigger embedding generation for KB questions missing embeddings."""
    exam_type: Optional[str] = None
    batch_size: int = Field(50, ge=1, le=500)


# ---------------------------------------------------------------------------
# 1. Exam Packs CRUD
# ---------------------------------------------------------------------------

@router.get("", response_model=list[ExamPackOut])
async def list_exam_packs(
    country: Optional[str] = None,
    session: AsyncSession = Depends(get_session),
):
    stmt = select(ExamPack)
    if country:
        stmt = stmt.where(ExamPack.country_code == country.upper())
    stmt = stmt.order_by(ExamPack.tier, ExamPack.name)
    rows = (await session.execute(stmt)).scalars().all()

    result = []
    for ep in rows:
        subj_stmt = select(ExamSubject).where(ExamSubject.exam_pack_id == ep.id).order_by(ExamSubject.order)
        subjects = (await session.execute(subj_stmt)).scalars().all()
        result.append(ExamPackOut(
            id=str(ep.id),
            country_code=ep.country_code,
            country_name=ep.country_name,
            name=ep.name,
            tier=ep.tier,
            price_display=ep.price_display,
            currency=ep.currency,
            question_count=ep.question_count,
            is_coming_soon=ep.is_coming_soon,
            subjects=[s.name for s in subjects],
            metadata=ep.metadata_ or {},
        ))
    return result


@router.get("/{exam_id}/questions", response_model=list[QuestionOut])
async def list_questions(
    exam_id: str,
    subject: Optional[str] = None,
    difficulty: Optional[str] = None,
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=100),
    session: AsyncSession = Depends(get_session),
):
    stmt = select(ExamQuestion).where(
        ExamQuestion.exam_pack_id == uuid.UUID(exam_id)
    )
    if subject:
        stmt = stmt.where(ExamQuestion.subject == subject)
    if difficulty:
        stmt = stmt.where(ExamQuestion.difficulty == difficulty)
    stmt = stmt.offset((page - 1) * limit).limit(limit)
    rows = (await session.execute(stmt)).scalars().all()
    return [
        QuestionOut(
            id=str(q.id),
            subject=q.subject,
            difficulty=q.difficulty,
            question_text=q.question_text,
            options=q.options,
            year=q.year,
            tags=q.tags if isinstance(q.tags, list) else [],
        )
        for q in rows
    ]


@router.get("/{exam_id}/practice-test", response_model=list[QuestionOut])
async def generate_practice_test(
    exam_id: str,
    count: int = Query(30, ge=5, le=100),
    session: AsyncSession = Depends(get_session),
):
    stmt = (
        select(ExamQuestion)
        .where(ExamQuestion.exam_pack_id == uuid.UUID(exam_id))
        .order_by(func.random())
        .limit(count)
    )
    rows = (await session.execute(stmt)).scalars().all()
    if not rows:
        raise HTTPException(404, "No questions found for this exam pack")
    return [
        QuestionOut(
            id=str(q.id),
            subject=q.subject,
            difficulty=q.difficulty,
            question_text=q.question_text,
            options=q.options,
            year=q.year,
            tags=q.tags if isinstance(q.tags, list) else [],
        )
        for q in rows
    ]


@router.post("/{exam_id}/submit", response_model=SubmitResult)
async def submit_answers(
    exam_id: str,
    body: SubmitRequest,
    session: AsyncSession = Depends(get_session),
):
    qids = [uuid.UUID(k) for k in body.answers]
    stmt = select(ExamQuestion).where(ExamQuestion.id.in_(qids))
    rows = (await session.execute(stmt)).scalars().all()
    correct_map = {str(q.id): q.correct_answer for q in rows}

    per_q: list[dict[str, Any]] = []
    correct_count = 0
    for qid_str, selected in body.answers.items():
        is_correct = correct_map.get(qid_str, "") == selected
        if is_correct:
            correct_count += 1
        per_q.append({"question_id": qid_str, "selected": selected, "correct": is_correct})

    total = len(body.answers)
    return SubmitResult(
        total=total,
        correct=correct_count,
        score_pct=round((correct_count / total) * 100, 1) if total else 0,
        per_question=per_q,
    )


# ---------------------------------------------------------------------------
# 2. Adaptive Diagnostic Test
# ---------------------------------------------------------------------------

DIFFICULTY_LEVELS = ["easy", "medium", "hard"]
DIAG_TOTAL_QUESTIONS = 13
DIAG_SUBJECTS = ["Physics", "Chemistry", "Mathematics", "Biology", "English", "Reasoning"]


@router.post("/diagnostic/start")
async def diagnostic_start(
    body: DiagStartRequest,
    x_user_id: str = Header(),
    session: AsyncSession = Depends(get_session),
):
    ds = DiagnosticSession(
        user_id=x_user_id,
        exam_type=body.exam_type,
        total_questions=DIAG_TOTAL_QUESTIONS,
        current_difficulty="medium",
        status="in_progress",
    )
    session.add(ds)
    await session.flush()

    first_q = await _pick_diagnostic_question(session, body.exam_type, "medium", DIAG_SUBJECTS[0], set())
    if not first_q:
        raise HTTPException(404, "No diagnostic questions available for this exam type")

    await session.commit()
    return {
        "session_id": str(ds.id),
        "question": _q_dict(first_q),
        "question_number": 1,
        "total": DIAG_TOTAL_QUESTIONS,
    }


@router.post("/diagnostic/answer")
async def diagnostic_answer(
    body: DiagAnswerRequest,
    session: AsyncSession = Depends(get_session),
):
    ds = await session.get(DiagnosticSession, uuid.UUID(body.session_id))
    if not ds or ds.status != "in_progress":
        raise HTTPException(400, "Invalid or completed session")

    q = await session.get(ExamQuestion, uuid.UUID(body.question_id))
    if not q:
        raise HTTPException(404, "Question not found")

    is_correct = q.correct_answer == body.selected
    answer_count = (await session.execute(
        select(func.count()).where(DiagnosticAnswer.session_id == ds.id)
    )).scalar() or 0

    da = DiagnosticAnswer(
        session_id=ds.id,
        question_id=q.id,
        selected_answer=body.selected,
        is_correct=is_correct,
        difficulty=q.difficulty,
        subject=q.subject,
    )
    session.add(da)

    new_number = answer_count + 2
    if new_number > DIAG_TOTAL_QUESTIONS:
        ds.status = "completed"
        await session.commit()
        return {"status": "completed", "session_id": str(ds.id)}

    answered_ids_stmt = select(DiagnosticAnswer.question_id).where(DiagnosticAnswer.session_id == ds.id)
    answered_ids = set((await session.execute(answered_ids_stmt)).scalars().all())
    answered_ids.add(q.id)

    if is_correct:
        idx = min(DIFFICULTY_LEVELS.index(ds.current_difficulty) + 1, 2)
    else:
        idx = max(DIFFICULTY_LEVELS.index(ds.current_difficulty) - 1, 0)
    ds.current_difficulty = DIFFICULTY_LEVELS[idx]

    subj_index = (answer_count + 1) % len(DIAG_SUBJECTS)
    next_subj = DIAG_SUBJECTS[subj_index]

    next_q = await _pick_diagnostic_question(session, ds.exam_type, ds.current_difficulty, next_subj, answered_ids)
    if not next_q:
        next_q = await _pick_diagnostic_question(session, ds.exam_type, ds.current_difficulty, None, answered_ids)
    if not next_q:
        ds.status = "completed"
        await session.commit()
        return {"status": "completed", "session_id": str(ds.id)}

    await session.commit()
    return {
        "session_id": str(ds.id),
        "question": _q_dict(next_q),
        "question_number": new_number,
        "total": DIAG_TOTAL_QUESTIONS,
        "current_difficulty": ds.current_difficulty,
    }


@router.get("/diagnostic/{session_id}/results", response_model=DiagResultOut)
async def diagnostic_results(
    session_id: str,
    session: AsyncSession = Depends(get_session),
):
    ds = await session.get(DiagnosticSession, uuid.UUID(session_id))
    if not ds:
        raise HTTPException(404, "Session not found")

    answers_stmt = select(DiagnosticAnswer).where(DiagnosticAnswer.session_id == ds.id)
    answers = (await session.execute(answers_stmt)).scalars().all()

    subj_scores: dict[str, dict[str, int]] = {}
    diff_progression = []
    correct_total = 0
    for a in answers:
        s = a.subject or "Unknown"
        if s not in subj_scores:
            subj_scores[s] = {"correct": 0, "total": 0}
        subj_scores[s]["total"] += 1
        if a.is_correct:
            subj_scores[s]["correct"] += 1
            correct_total += 1
        diff_progression.append(a.difficulty or "medium")

    total = len(answers)
    return DiagResultOut(
        session_id=session_id,
        status=ds.status,
        total_questions=total,
        correct=correct_total,
        score_pct=round((correct_total / total) * 100, 1) if total else 0,
        subject_scores=subj_scores,
        difficulty_progression=diff_progression,
    )


async def _pick_diagnostic_question(
    session: AsyncSession,
    exam_type: str,
    difficulty: str,
    subject: Optional[str],
    exclude_ids: set,
) -> ExamQuestion | None:
    stmt = (
        select(ExamQuestion)
        .join(ExamPack)
        .where(ExamQuestion.difficulty == difficulty)
        .where(ExamPack.name.ilike(f"%{exam_type}%"))
    )
    if subject:
        stmt = stmt.where(ExamQuestion.subject == subject)
    if exclude_ids:
        stmt = stmt.where(ExamQuestion.id.notin_(exclude_ids))
    stmt = stmt.order_by(func.random()).limit(1)
    return (await session.execute(stmt)).scalar_one_or_none()


def _q_dict(q: ExamQuestion) -> dict[str, Any]:
    return {
        "id": str(q.id),
        "subject": q.subject,
        "difficulty": q.difficulty,
        "question_text": q.question_text,
        "options": q.options,
    }


# ---------------------------------------------------------------------------
# 3. Personalized Study Plan
# ---------------------------------------------------------------------------

@router.post("/study-plan/generate")
async def generate_study_plan(
    exam_type: str = "jee_main",
    diagnostic_session_id: Optional[str] = None,
    x_user_id: str = Header(),
    session: AsyncSession = Depends(get_session),
):
    weak_subjects: list[str] = []
    if diagnostic_session_id:
        ds = await session.get(DiagnosticSession, uuid.UUID(diagnostic_session_id))
        if ds:
            answers_stmt = select(DiagnosticAnswer).where(DiagnosticAnswer.session_id == ds.id)
            answers = (await session.execute(answers_stmt)).scalars().all()
            subj_scores: dict[str, dict[str, int]] = {}
            for a in answers:
                s = a.subject or "Unknown"
                if s not in subj_scores:
                    subj_scores[s] = {"correct": 0, "total": 0}
                subj_scores[s]["total"] += 1
                if a.is_correct:
                    subj_scores[s]["correct"] += 1
            weak_subjects = [
                s for s, v in subj_scores.items()
                if v["total"] > 0 and (v["correct"] / v["total"]) < 0.6
            ]

    if not weak_subjects:
        weak_subjects = ["Mathematics", "Physics", "Chemistry"]

    days_data = _build_study_plan_days(weak_subjects, exam_type)

    plan = StudyPlan(user_id=x_user_id, exam_type=exam_type, plan_data=days_data, diagnostic_session_id=uuid.UUID(diagnostic_session_id) if diagnostic_session_id else None)
    session.add(plan)
    await session.flush()

    for i, day in enumerate(days_data):
        for j, task_text in enumerate(day.get("tasks", [])):
            t = StudyPlanTask(
                plan_id=plan.id,
                day=i + 1,
                title=task_text,
                order=j,
            )
            session.add(t)

    await session.commit()
    return StudyPlanOut(
        id=str(plan.id),
        exam_type=exam_type,
        days=days_data,
        generated_at=plan.created_at.isoformat() if plan.created_at else datetime.now(timezone.utc).isoformat(),
    )


@router.get("/study-plan/{plan_id}")
async def get_study_plan(
    plan_id: str,
    session: AsyncSession = Depends(get_session),
):
    plan = await session.get(StudyPlan, uuid.UUID(plan_id))
    if not plan:
        raise HTTPException(404, "Plan not found")

    tasks_stmt = select(StudyPlanTask).where(StudyPlanTask.plan_id == plan.id).order_by(StudyPlanTask.day, StudyPlanTask.order)
    tasks = (await session.execute(tasks_stmt)).scalars().all()

    return {
        "id": str(plan.id),
        "exam_type": plan.exam_type,
        "days": plan.plan_data,
        "tasks": [
            {"id": str(t.id), "day": t.day, "title": t.title, "completed": t.is_completed}
            for t in tasks
        ],
        "generated_at": plan.created_at.isoformat() if plan.created_at else None,
    }


@router.post("/study-plan/complete-task")
async def complete_task(
    body: TaskCompleteRequest,
    session: AsyncSession = Depends(get_session),
):
    task = await session.get(StudyPlanTask, uuid.UUID(body.task_id))
    if not task:
        raise HTTPException(404, "Task not found")
    task.is_completed = True
    task.completed_at = datetime.now(timezone.utc)
    await session.commit()
    return {"status": "ok", "task_id": str(task.id)}


def _build_study_plan_days(weak_subjects: list[str], exam_type: str) -> list[dict[str, Any]]:
    templates = {
        "Mathematics": ["Review core formulas (MathBot)", "Solve 10 practice problems", "Watch concept animation", "Practice test: 15 questions"],
        "Physics": ["Theory review (SciBot)", "Solve 10 numerical problems", "Visual simulation", "Practice test: 15 questions"],
        "Chemistry": ["IUPAC / concept rules", "Practice naming / equations", "Reaction mechanisms quiz", "Practice test: 15 questions"],
        "Biology": ["Diagram-based review", "Practice MCQs: 20 questions", "Lab technique quiz"],
        "English": ["Grammar rules review", "Reading comprehension practice", "Vocabulary building exercise"],
        "Reasoning": ["Pattern recognition drills", "Logical deduction problems", "Data interpretation practice"],
    }
    days = []
    for i, subj in enumerate(weak_subjects[:4]):
        tasks = templates.get(subj, templates["Mathematics"])
        days.append({
            "day": i + 1,
            "label": f"Day {i + 1}" + (" · Today" if i == 0 else (" · Tomorrow" if i == 1 else "")),
            "subject": subj,
            "title": f"{exam_type.upper().replace('_', ' ')} {subj}",
            "tasks": tasks,
        })
    days.append({
        "day": len(days) + 1,
        "label": f"Day {len(days) + 1}",
        "subject": "Review",
        "title": "Weekly Review + Mock Test",
        "tasks": [
            "Revision: weak areas from previous days",
            "Mini mock test (45 min, 30 Qs)",
            "Analyze mistakes with AI tutor",
        ],
    })
    return days


# ---------------------------------------------------------------------------
# 4. Score Predictor
# ---------------------------------------------------------------------------

@router.post("/score-predict", response_model=ScorePredictOut)
async def predict_score(
    body: ScorePredictRequest,
    session: AsyncSession = Depends(get_session),
    x_user_id: str = Header(),
):
    total_answered = (await session.execute(
        select(func.count())
        .select_from(DiagnosticAnswer)
        .join(DiagnosticSession)
        .where(DiagnosticSession.user_id == x_user_id)
    )).scalar() or 0

    if total_answered == 0:
        raise HTTPException(400, "No question history found — take a diagnostic test first")

    subj_stmt = (
        select(
            DiagnosticAnswer.subject,
            func.count().label("total"),
            func.sum(func.cast(DiagnosticAnswer.is_correct, Integer)).label("correct"),
        )
        .join(DiagnosticSession)
        .where(DiagnosticSession.user_id == x_user_id)
        .group_by(DiagnosticAnswer.subject)
    )
    subj_rows = (await session.execute(subj_stmt)).all()

    max_score = 300.0
    subj_breakdown: dict[str, Any] = {}
    weighted_score = 0.0
    for subj, total, correct in subj_rows:
        pct = (correct / total) * 100 if total else 0
        subject_max = 100.0
        predicted = round(pct * subject_max / 100, 1)
        subj_breakdown[subj] = {"predicted": predicted, "max": subject_max, "accuracy_pct": round(pct, 1)}
        weighted_score += predicted

    percentile = min(99.9, max(1.0, _score_to_percentile(weighted_score, max_score)))
    rank = max(1, int(1_200_000 * (1 - percentile / 100)))

    focus_areas = [s for s, v in subj_breakdown.items() if v["accuracy_pct"] < 70]
    insight = f"Focus on {', '.join(focus_areas)} to improve your score." if focus_areas else "Great performance across all subjects!"

    ai_insights = {"summary": insight, "focus_areas": focus_areas}

    pred = ScorePrediction(
        user_id=x_user_id,
        exam_type=body.exam_type,
        predicted_score=weighted_score,
        max_score=max_score,
        percentile=percentile,
        predicted_rank=rank,
        subject_breakdown=subj_breakdown,
        ai_insights=ai_insights,
        questions_analyzed=total_answered,
    )
    session.add(pred)
    await session.commit()

    return ScorePredictOut(
        predicted_score=weighted_score,
        max_score=max_score,
        percentile=percentile,
        predicted_rank=rank,
        subject_breakdown=subj_breakdown,
        ai_insights=ai_insights,
    )


def _score_to_percentile(score: float, max_score: float) -> float:
    ratio = score / max_score if max_score else 0
    return round(50 + 50 * math.erf((ratio - 0.5) * 2.5), 1)


# ---------------------------------------------------------------------------
# 5. Knowledge Base — sources, ingest, embeddings, semantic search
# ---------------------------------------------------------------------------

@router.post("/kb/sources")
async def create_kb_source(
    body: KBSourceCreateRequest,
    session: AsyncSession = Depends(get_session),
):
    src = KBSource(
        name=body.name,
        url=body.url,
        source_type=body.source_type,
        metadata_=body.metadata,
    )
    session.add(src)
    await session.commit()
    return {"id": str(src.id), "name": src.name}


@router.post("/kb/ingest")
async def kb_bulk_ingest(
    body: KBBulkIngestRequest,
    session: AsyncSession = Depends(get_session),
):
    """Bulk-ingest questions into the knowledge base (called by n8n webhook).
    Deduplicates by (exam_type, question_text) and logs the enrichment run."""

    added = 0
    skipped = 0
    source_uuid = uuid.UUID(body.source_id) if body.source_id else None

    for item in body.questions:
        dup_stmt = (
            select(func.count())
            .select_from(KBQuestion)
            .where(KBQuestion.exam_type == item.exam_type)
            .where(KBQuestion.question_text == item.question_text)
        )
        exists = (await session.execute(dup_stmt)).scalar() or 0
        if exists:
            skipped += 1
            continue

        q = KBQuestion(
            exam_type=item.exam_type,
            subject=item.subject,
            question_text=item.question_text,
            options=item.options,
            correct_answer=item.correct_answer,
            explanation=item.explanation,
            difficulty=item.difficulty,
            source_id=source_uuid,
        )
        session.add(q)
        added += 1

    log_entry = KBEnrichmentLog(
        exam_type=body.questions[0].exam_type if body.questions else "unknown",
        questions_added=added,
        duplicates_skipped=skipped,
        source_id=source_uuid,
        status="completed",
        detail={"total_submitted": len(body.questions)},
    )
    session.add(log_entry)
    await session.commit()

    return {
        "status": "ok",
        "added": added,
        "skipped": skipped,
        "enrichment_log_id": str(log_entry.id),
    }


@router.post("/kb/embeddings/generate")
async def kb_generate_embeddings(
    body: KBEmbedRequest,
    session: AsyncSession = Depends(get_session),
):
    """Generate embeddings for KB questions that don't have one yet."""

    from deeptutor.services.embedding.client import EmbeddingClient
    from deeptutor.services.embedding.config import EmbeddingConfig, get_embedding_config

    base_cfg = get_embedding_config()
    kb_cfg = EmbeddingConfig(
        model=base_cfg.model,
        api_key=base_cfg.api_key,
        base_url=base_cfg.base_url,
        effective_url=base_cfg.effective_url,
        binding=base_cfg.binding,
        provider_name=base_cfg.provider_name,
        provider_mode=base_cfg.provider_mode,
        api_version=base_cfg.api_version,
        extra_headers=base_cfg.extra_headers,
        dim=1536,
        request_timeout=base_cfg.request_timeout,
        batch_size=base_cfg.batch_size,
        batch_delay=base_cfg.batch_delay,
    )
    client = EmbeddingClient(config=kb_cfg)

    already_embedded = select(KBEmbedding.question_id)
    stmt = select(KBQuestion).where(KBQuestion.id.notin_(already_embedded))
    if body.exam_type:
        stmt = stmt.where(KBQuestion.exam_type == body.exam_type)
    stmt = stmt.limit(body.batch_size)

    rows = (await session.execute(stmt)).scalars().all()
    if not rows:
        return {"status": "ok", "embedded": 0, "message": "All questions already have embeddings"}

    texts = [q.question_text for q in rows]
    vectors = await client.embed(texts)

    for q, vec in zip(rows, vectors):
        emb = KBEmbedding(question_id=q.id, embedding=vec)
        session.add(emb)

    await session.commit()
    return {"status": "ok", "embedded": len(rows)}


@router.post("/kb/search")
async def kb_search(
    body: KBSearchRequest,
    session: AsyncSession = Depends(get_session),
):
    """Semantic search using pgvector cosine distance when embeddings exist,
    falling back to ILIKE text match otherwise."""

    try:
        from deeptutor.services.embedding.client import EmbeddingClient
        from deeptutor.services.embedding.config import EmbeddingConfig, get_embedding_config

        base_cfg = get_embedding_config()
        kb_cfg = EmbeddingConfig(
            model=base_cfg.model,
            api_key=base_cfg.api_key,
            base_url=base_cfg.base_url,
            effective_url=base_cfg.effective_url,
            binding=base_cfg.binding,
            provider_name=base_cfg.provider_name,
            provider_mode=base_cfg.provider_mode,
            api_version=base_cfg.api_version,
            extra_headers=base_cfg.extra_headers,
            dim=1536,
            request_timeout=base_cfg.request_timeout,
            batch_size=base_cfg.batch_size,
            batch_delay=base_cfg.batch_delay,
        )
        client = EmbeddingClient(config=kb_cfg)
        query_vec = (await client.embed([body.query]))[0]

        stmt = (
            select(
                KBQuestion,
                KBEmbedding.embedding.cosine_distance(query_vec).label("distance"),
            )
            .join(KBEmbedding, KBEmbedding.question_id == KBQuestion.id)
        )
        if body.exam_type:
            stmt = stmt.where(KBQuestion.exam_type == body.exam_type)
        stmt = stmt.order_by("distance").limit(body.limit)

        rows = (await session.execute(stmt)).all()
        return [
            {
                "id": str(q.id),
                "exam_type": q.exam_type,
                "subject": q.subject,
                "question_text": q.question_text,
                "options": q.options,
                "correct_answer": q.correct_answer,
                "explanation": q.explanation,
                "difficulty": q.difficulty,
                "similarity": round(1 - dist, 4),
            }
            for q, dist in rows
        ]

    except Exception as e:
        logger.warning("pgvector semantic search unavailable, falling back to ILIKE: %s", e)
        stmt = select(KBQuestion)
        if body.exam_type:
            stmt = stmt.where(KBQuestion.exam_type == body.exam_type)
        stmt = stmt.where(KBQuestion.question_text.ilike(f"%{body.query}%")).limit(body.limit)
        rows = (await session.execute(stmt)).scalars().all()
        return [
            {
                "id": str(q.id),
                "exam_type": q.exam_type,
                "subject": q.subject,
                "question_text": q.question_text,
                "options": q.options,
                "correct_answer": q.correct_answer,
                "explanation": q.explanation,
                "difficulty": q.difficulty,
            }
            for q in rows
        ]


# ---------------------------------------------------------------------------
# Health check
# ---------------------------------------------------------------------------

@router.get("/health")
async def exams_health():
    try:
        from deeptutor.services.exam.db import get_engine
        engine = get_engine()
        return {"status": "ok", "pg_pool_size": engine.pool.size()}
    except RuntimeError:
        return {"status": "disabled", "reason": "PG_HOST not configured"}


