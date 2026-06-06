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
from .protocol import SessionStoreProtocol
from .sqlite_store import SQLiteSessionStore, get_sqlite_session_store
from .turn_runtime import TurnRuntimeManager, get_turn_runtime_manager


def get_session_store() -> SessionStoreProtocol:
    """
    Return the active session store backend.

    Backend selection order (fork = multi-tenant / k8s friendly):
      1. PostgreSQL (PGSessionStore) when PG_HOST is configured — required for
         multi-replica deployments where per-pod sqlite/files do not persist.
      2. PocketBase (upstream) when integrations.pocketbase_url is configured.
      3. Local SQLiteSessionStore (default, zero-config behaviour).
    """
    # 1. PostgreSQL (preferred for multi-tenant horizontal scaling).
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
        pass

    # 2. PocketBase (upstream optional integration).
    from deeptutor.services.pocketbase_client import is_pocketbase_enabled

    if is_pocketbase_enabled():
        from .pocketbase_store import PocketBaseSessionStore

        return PocketBaseSessionStore()

    # 3. Local SQLite fallback.
    return get_sqlite_session_store()


__all__ = [
    "BaseSessionManager",
    "SessionStoreProtocol",
    "SQLiteSessionStore",
    "TurnRuntimeManager",
    "get_session_store",
    "get_sqlite_session_store",
    "get_turn_runtime_manager",
]
