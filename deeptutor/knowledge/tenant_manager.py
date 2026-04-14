"""
Multi-tenant wrapper around KnowledgeBaseManager.

Each user gets their own subdirectory under the KB base dir:
  data/knowledge_bases/{user_id}/

This provides complete filesystem isolation without changing
the existing KnowledgeBaseManager or RAG pipeline internals.
"""

from __future__ import annotations

import os
from pathlib import Path

from deeptutor.api.middleware.tenant import get_current_user_id
from deeptutor.knowledge.manager import KnowledgeBaseManager
from deeptutor.services.config import PROJECT_ROOT


_KB_ROOT = PROJECT_ROOT / "data" / "knowledge_bases"
_managers: dict[str, KnowledgeBaseManager] = {}


def get_tenant_kb_manager(user_id: str | None = None) -> KnowledgeBaseManager:
    """Return a KnowledgeBaseManager scoped to the current user's directory."""
    uid = (user_id or "").strip() or get_current_user_id()
    if uid not in _managers:
        user_kb_dir = _KB_ROOT / uid
        user_kb_dir.mkdir(parents=True, exist_ok=True)
        _managers[uid] = KnowledgeBaseManager(base_dir=str(user_kb_dir))
    return _managers[uid]


def get_tenant_kb_base_dir(user_id: str | None = None) -> Path:
    """Return the base dir path for the current user's KBs."""
    uid = (user_id or "").strip() or get_current_user_id()
    p = _KB_ROOT / uid
    p.mkdir(parents=True, exist_ok=True)
    return p
