"""SQLAlchemy ORM models for the Exam subsystem.

Covers:
  - Exam Packs & Questions (with pgvector embeddings)
  - Adaptive Diagnostic Tests
  - Personalised Study Plans
  - Score Predictions
  - Knowledge‑Base tables
"""

from __future__ import annotations

import uuid
from datetime import datetime
from typing import Any, Optional

from sqlalchemy import (
    Boolean,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
    Text,
    func,
)
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from deeptutor.services.db.base import Base  # shared declarative base

try:
    from pgvector.sqlalchemy import Vector
except ImportError:  # graceful fallback when pgvector isn't installed yet
    Vector = None  # type: ignore[assignment,misc]


# ---------------------------------------------------------------------------
# Exam Packs
# ---------------------------------------------------------------------------

class ExamPack(Base):
    __tablename__ = "exam_packs"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    country_code: Mapped[str] = mapped_column(String(4), index=True)
    country_name: Mapped[str] = mapped_column(String(64))
    name: Mapped[str] = mapped_column(String(128))
    tier: Mapped[int] = mapped_column(Integer, default=1)
    price_display: Mapped[str] = mapped_column(String(32), default="Free")
    currency: Mapped[str] = mapped_column(String(8), default="USD")
    question_count: Mapped[int] = mapped_column(Integer, default=0)
    is_coming_soon: Mapped[bool] = mapped_column(Boolean, default=False)
    metadata_: Mapped[dict[str, Any]] = mapped_column("metadata", JSONB, default=dict)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    subjects: Mapped[list["ExamSubject"]] = relationship(back_populates="exam_pack", cascade="all, delete-orphan")
    questions: Mapped[list["ExamQuestion"]] = relationship(back_populates="exam_pack", cascade="all, delete-orphan")


class ExamSubject(Base):
    __tablename__ = "exam_subjects"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    exam_pack_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("exam_packs.id", ondelete="CASCADE"))
    name: Mapped[str] = mapped_column(String(128))
    order: Mapped[int] = mapped_column(Integer, default=0)

    exam_pack: Mapped["ExamPack"] = relationship(back_populates="subjects")


class ExamQuestion(Base):
    __tablename__ = "exam_questions"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    exam_pack_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("exam_packs.id", ondelete="CASCADE"), index=True)
    subject: Mapped[str] = mapped_column(String(128), index=True)
    year: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    source: Mapped[Optional[str]] = mapped_column(String(256), nullable=True)
    difficulty: Mapped[str] = mapped_column(String(16), default="medium")
    question_text: Mapped[str] = mapped_column(Text)
    options: Mapped[dict[str, Any]] = mapped_column(JSONB, default=dict)
    correct_answer: Mapped[str] = mapped_column(String(8))
    explanation: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    tags: Mapped[dict[str, Any]] = mapped_column(JSONB, default=list)
    embedding = mapped_column(Vector(1536), nullable=True) if Vector else mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    exam_pack: Mapped["ExamPack"] = relationship(back_populates="questions")


class UserExamProgress(Base):
    __tablename__ = "user_exam_progress"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: Mapped[str] = mapped_column(String(128), index=True)
    exam_pack_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("exam_packs.id", ondelete="CASCADE"), index=True)
    questions_attempted: Mapped[int] = mapped_column(Integer, default=0)
    questions_correct: Mapped[int] = mapped_column(Integer, default=0)
    completion_pct: Mapped[float] = mapped_column(Float, default=0.0)
    last_activity: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    detail: Mapped[dict[str, Any]] = mapped_column(JSONB, default=dict)


# ---------------------------------------------------------------------------
# Adaptive Diagnostic Test
# ---------------------------------------------------------------------------

class DiagnosticSession(Base):
    __tablename__ = "diagnostic_sessions"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: Mapped[str] = mapped_column(String(128), index=True)
    exam_type: Mapped[str] = mapped_column(String(64))
    total_questions: Mapped[int] = mapped_column(Integer, default=13)
    current_index: Mapped[int] = mapped_column(Integer, default=0)
    current_difficulty: Mapped[str] = mapped_column(String(16), default="medium")
    status: Mapped[str] = mapped_column(String(24), default="in_progress")
    ability_estimate: Mapped[float] = mapped_column(Float, default=0.0)
    result: Mapped[dict[str, Any]] = mapped_column(JSONB, default=dict)
    started_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    completed_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)

    answers: Mapped[list["DiagnosticAnswer"]] = relationship(back_populates="session", cascade="all, delete-orphan")


class DiagnosticAnswer(Base):
    __tablename__ = "diagnostic_answers"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    session_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("diagnostic_sessions.id", ondelete="CASCADE"))
    question_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True))
    subject: Mapped[str] = mapped_column(String(128))
    difficulty: Mapped[str] = mapped_column(String(16))
    selected_answer: Mapped[str] = mapped_column(String(8))
    is_correct: Mapped[bool] = mapped_column(Boolean)
    time_taken_sec: Mapped[float] = mapped_column(Float, default=0.0)
    answered_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    session: Mapped["DiagnosticSession"] = relationship(back_populates="answers")


# ---------------------------------------------------------------------------
# Personalised Study Plan
# ---------------------------------------------------------------------------

class StudyPlan(Base):
    __tablename__ = "study_plans"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: Mapped[str] = mapped_column(String(128), index=True)
    exam_type: Mapped[str] = mapped_column(String(64))
    diagnostic_session_id: Mapped[Optional[uuid.UUID]] = mapped_column(UUID(as_uuid=True), nullable=True)
    plan_data: Mapped[dict[str, Any]] = mapped_column(JSONB, default=dict)
    total_days: Mapped[int] = mapped_column(Integer, default=5)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    regenerated_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)

    tasks: Mapped[list["StudyPlanTask"]] = relationship(back_populates="plan", cascade="all, delete-orphan")


class StudyPlanTask(Base):
    __tablename__ = "study_plan_tasks"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    plan_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("study_plans.id", ondelete="CASCADE"))
    day: Mapped[int] = mapped_column(Integer)
    title: Mapped[str] = mapped_column(String(256))
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    is_completed: Mapped[bool] = mapped_column(Boolean, default=False)
    completed_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    order: Mapped[int] = mapped_column(Integer, default=0)

    plan: Mapped["StudyPlan"] = relationship(back_populates="tasks")


# ---------------------------------------------------------------------------
# Score Predictor
# ---------------------------------------------------------------------------

class ScorePrediction(Base):
    __tablename__ = "score_predictions"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: Mapped[str] = mapped_column(String(128), index=True)
    exam_type: Mapped[str] = mapped_column(String(64))
    predicted_score: Mapped[float] = mapped_column(Float)
    max_score: Mapped[float] = mapped_column(Float)
    percentile: Mapped[float] = mapped_column(Float, default=0.0)
    predicted_rank: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    subject_breakdown: Mapped[dict[str, Any]] = mapped_column(JSONB, default=dict)
    ai_insights: Mapped[dict[str, Any]] = mapped_column(JSONB, default=dict)
    questions_analyzed: Mapped[int] = mapped_column(Integer, default=0)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())


# ---------------------------------------------------------------------------
# Knowledge Base
# ---------------------------------------------------------------------------

class KBQuestion(Base):
    __tablename__ = "kb_questions"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    exam_type: Mapped[str] = mapped_column(String(64), index=True)
    subject: Mapped[str] = mapped_column(String(128), index=True)
    question_text: Mapped[str] = mapped_column(Text)
    options: Mapped[dict[str, Any]] = mapped_column(JSONB, default=dict)
    correct_answer: Mapped[str] = mapped_column(String(8))
    explanation: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    difficulty: Mapped[str] = mapped_column(String(16), default="medium")
    source_id: Mapped[Optional[uuid.UUID]] = mapped_column(UUID(as_uuid=True), ForeignKey("kb_sources.id"), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())


class KBEmbedding(Base):
    __tablename__ = "kb_embeddings"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    question_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("kb_questions.id", ondelete="CASCADE"), unique=True)
    embedding = mapped_column(Vector(1536)) if Vector else mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())


class KBSource(Base):
    __tablename__ = "kb_sources"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(256))
    url: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    source_type: Mapped[str] = mapped_column(String(32), default="pdf")
    metadata_: Mapped[dict[str, Any]] = mapped_column("metadata", JSONB, default=dict)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())


class KBEnrichmentLog(Base):
    __tablename__ = "kb_enrichment_logs"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    exam_type: Mapped[str] = mapped_column(String(64))
    questions_added: Mapped[int] = mapped_column(Integer, default=0)
    duplicates_skipped: Mapped[int] = mapped_column(Integer, default=0)
    source_id: Mapped[Optional[uuid.UUID]] = mapped_column(UUID(as_uuid=True), nullable=True)
    status: Mapped[str] = mapped_column(String(24), default="completed")
    detail: Mapped[dict[str, Any]] = mapped_column(JSONB, default=dict)
    ran_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
