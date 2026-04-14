"""Shared SQLAlchemy declarative base for all models (exam, memory, sessions, etc.)."""

from __future__ import annotations

from typing import Any

from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    type_annotation_map = {dict[str, Any]: JSONB}
