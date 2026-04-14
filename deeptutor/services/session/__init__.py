"""
Session Management Module
=========================

Provides unified session management for all agent modules.

Usage:
    from deeptutor.services.session import BaseSessionManager
    
    class MySessionManager(BaseSessionManager):
        def __init__(self):
            super().__init__("my_module")
        
        def _get_session_id_prefix(self) -> str:
            return "my_"
        
        def _get_default_title(self) -> str:
            return "New My Session"
        
        # ... implement other abstract methods
"""

from .base_session_manager import BaseSessionManager
from .sqlite_store import SQLiteSessionStore, get_sqlite_session_store
from .turn_runtime import TurnRuntimeManager, get_turn_runtime_manager


def get_session_store():
    """Return PGSessionStore if PostgreSQL is initialised, else SQLiteSessionStore."""
    try:
        from deeptutor.services.db.engine import get_session_factory
        get_session_factory()
        from deeptutor.services.session.pg_store import PGSessionStore
        _pg = getattr(get_session_store, "_pg", None)
        if _pg is None:
            _pg = PGSessionStore()
            get_session_store._pg = _pg  # type: ignore[attr-defined]
        return _pg
    except RuntimeError:
        return get_sqlite_session_store()


__all__ = [
    "BaseSessionManager",
    "SQLiteSessionStore",
    "TurnRuntimeManager",
    "get_session_store",
    "get_sqlite_session_store",
    "get_turn_runtime_manager",
]
