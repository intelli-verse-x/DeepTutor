"""Backward-compatible shim — delegates to the shared db engine.

Existing code that does `from deeptutor.services.exam.db import init_pg, get_session`
continues to work unchanged.
"""

from __future__ import annotations

from deeptutor.services.db.engine import (
    init_pg,
    close_pg,
    get_engine,
    get_session,
)

__all__ = ["init_pg", "close_pg", "get_engine", "get_session"]
