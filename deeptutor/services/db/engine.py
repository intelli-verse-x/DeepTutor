"""Async PostgreSQL connection manager (shared across all subsystems).

Reads PG_HOST / PG_PORT / PG_USER / PG_PASSWORD / PG_DATABASE from env.
If PG_HOST is unset the engine is not created and accessors raise RuntimeError.
"""

from __future__ import annotations

import logging
import os
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

logger = logging.getLogger("db.engine")

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
    """Create the async engine + ensure pgvector extension and all tables."""
    global _engine, _session_factory

    dsn = _build_dsn()
    if dsn is None:
        logger.info("PG_HOST not set — PostgreSQL disabled")
        return False

    _engine = create_async_engine(
        dsn,
        pool_size=5,
        max_overflow=10,
        pool_pre_ping=True,
        echo=False,
    )

    _session_factory = async_sessionmaker(_engine, expire_on_commit=False)

    from deeptutor.services.db.base import Base  # noqa: F811
    import deeptutor.services.db.models  # noqa: F401  — register new models
    import deeptutor.services.exam.models  # noqa: F401  — register exam models

    async with _engine.begin() as conn:
        await conn.execute(
            __import__("sqlalchemy").text("CREATE EXTENSION IF NOT EXISTS vector")
        )
        await conn.run_sync(Base.metadata.create_all)

    logger.info("PostgreSQL initialised (%s)", os.getenv("PG_HOST"))
    return True


async def close_pg() -> None:
    global _engine, _session_factory
    if _engine:
        await _engine.dispose()
        _engine = None
        _session_factory = None
        logger.info("PostgreSQL connection closed")


def get_engine() -> AsyncEngine:
    if _engine is None:
        raise RuntimeError(
            "PostgreSQL not initialised — ensure PG_HOST is set and init_pg() "
            "was called during application startup."
        )
    return _engine


def get_session_factory() -> async_sessionmaker[AsyncSession]:
    if _session_factory is None:
        raise RuntimeError(
            "PostgreSQL not initialised — ensure PG_HOST is set and init_pg() "
            "was called during application startup."
        )
    return _session_factory


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    factory = get_session_factory()
    async with factory() as session:
        yield session
