"""Per-user guided learning sessions (replaces JSON files on disk)."""

from __future__ import annotations

import uuid
from datetime import datetime
from typing import Any

from sqlalchemy import DateTime, Integer, String, Text, func
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column

from deeptutor.services.db.base import Base


class GuideSessionModel(Base):
    __tablename__ = "guide_sessions"

    id: Mapped[str] = mapped_column(String(32), primary_key=True)
    user_id: Mapped[str] = mapped_column(String(128), nullable=False, index=True)
    notebook_id: Mapped[str | None] = mapped_column(String(64), nullable=True)
    notebook_name: Mapped[str] = mapped_column(String(256), default="")
    status: Mapped[str] = mapped_column(String(32), default="active")
    knowledge_points: Mapped[dict[str, Any]] = mapped_column(JSONB, default=list)
    current_index: Mapped[int] = mapped_column(Integer, default=0)
    chat_history: Mapped[dict[str, Any]] = mapped_column(JSONB, default=list)
    summary: Mapped[str] = mapped_column(Text, default="")
    notebook_context: Mapped[str] = mapped_column(Text, default="")
    html_pages: Mapped[dict[str, Any]] = mapped_column(JSONB, default=dict)
    page_statuses: Mapped[dict[str, Any]] = mapped_column(JSONB, default=dict)
    page_errors: Mapped[dict[str, Any]] = mapped_column(JSONB, default=dict)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )
