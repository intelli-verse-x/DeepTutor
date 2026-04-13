"""Async PostgreSQL connection manager for the Exam subsystem.

Reads connection parameters from environment variables (PG_HOST, PG_PORT, etc.)
and exposes a shared SQLAlchemy async engine + session factory.

The module is deliberately *additive* — existing SQLite functionality is
untouched.  If PG_HOST is not configured the engine simply won't be created
and every accessor raises a clear error.
"""

from __future__ import annotations

import os
import logging
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

logger = logging.getLogger("exam.db")

_engine: AsyncEngine | None = None
_session_factory: async_sessionmaker[AsyncSession] | None = None


def _build_dsn() -> str | None:
    host = os.getenv("PG_HOST")
    if not host:
        return None
    port = os.getenv("PG_PORT", "5432")
    user = os.getenv("PG_USER", "postgres")
    password = os.getenv("PG_PASSWORD", "")
    database = os.getenv("PG_DATABASE", "deeptutor_exams")
    return f"postgresql+asyncpg://{user}:{password}@{host}:{port}/{database}"


async def init_pg() -> bool:
    """Create the async engine and ensure the ``vector`` extension + all
    tables exist.  Returns *True* on success, *False* when PG is not
    configured.
    """
    global _engine, _session_factory

    dsn = _build_dsn()
    if dsn is None:
        logger.info("PG_HOST not set — Exam Packs PostgreSQL disabled")
        return False

    _engine = create_async_engine(
        dsn,
        pool_size=5,
        max_overflow=10,
        pool_pre_ping=True,
        echo=False,
    )

    _session_factory = async_sessionmaker(_engine, expire_on_commit=False)

    from deeptutor.services.exam.models import Base  # noqa: F811

    async with _engine.begin() as conn:
        await conn.execute(
            __import__("sqlalchemy").text("CREATE EXTENSION IF NOT EXISTS vector")
        )
        await conn.run_sync(Base.metadata.create_all)

    logger.info("Exam Packs PostgreSQL initialised (%s)", os.getenv("PG_HOST"))
    return True


async def close_pg() -> None:
    global _engine, _session_factory
    if _engine:
        await _engine.dispose()
        _engine = None
        _session_factory = None
        logger.info("Exam Packs PostgreSQL connection closed")


def get_engine() -> AsyncEngine:
    if _engine is None:
        raise RuntimeError(
            "PostgreSQL not initialised — ensure PG_HOST is set and init_pg() "
            "was called during application startup."
        )
    return _engine


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    if _session_factory is None:
        raise RuntimeError(
            "PostgreSQL not initialised — ensure PG_HOST is set and init_pg() "
            "was called during application startup."
        )
    async with _session_factory() as session:
        yield session
