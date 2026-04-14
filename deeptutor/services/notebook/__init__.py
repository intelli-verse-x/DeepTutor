"""Shared notebook service used by CLI, Web, and runtime."""

from .service import (
    Notebook,
    NotebookManager,
    NotebookRecord,
    RecordType,
    get_notebook_manager,
    notebook_manager,
)


def get_pg_notebook_manager():
    """Return PGNotebookManager if PG is initialised, else file-based NotebookManager."""
    try:
        from deeptutor.services.db.engine import get_session_factory
        get_session_factory()
        from deeptutor.services.notebook.pg_manager import PGNotebookManager
        _pg = getattr(get_pg_notebook_manager, "_pg", None)
        if _pg is None:
            _pg = PGNotebookManager()
            get_pg_notebook_manager._pg = _pg  # type: ignore[attr-defined]
        return _pg
    except RuntimeError:
        return notebook_manager


__all__ = [
    "Notebook",
    "NotebookManager",
    "NotebookRecord",
    "RecordType",
    "get_notebook_manager",
    "get_pg_notebook_manager",
    "notebook_manager",
]
