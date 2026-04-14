"""
Per-user persistent memory backed by PostgreSQL.

Each user has one row in `user_memory` with `summary` and `profile` text
columns. Falls back to the old file-based system when PG is unavailable.
"""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Literal

from sqlalchemy import select

from deeptutor.api.middleware.tenant import get_current_user_id
from deeptutor.services.llm import stream as llm_stream

MemoryFile = Literal["summary", "profile"]
MEMORY_FILES: list[MemoryFile] = ["summary", "profile"]

_NO_CHANGE = "NO_CHANGE"

logger = logging.getLogger(__name__)


@dataclass
class MemorySnapshot:
    summary: str
    profile: str
    summary_updated_at: str | None
    profile_updated_at: str | None


@dataclass
class MemoryUpdateResult:
    content: str
    changed: bool
    updated_at: str | None


def _user_id_or_default(user_id: str | None) -> str:
    return (user_id or "").strip() or get_current_user_id()


class MemoryService:
    """Per-user memory: SUMMARY + PROFILE in PostgreSQL."""

    # ── Read ──────────────────────────────────────────────────────────

    async def read_file(self, which: MemoryFile, *, user_id: str | None = None) -> str:
        uid = _user_id_or_default(user_id)
        row = await self._get_row(uid)
        if row is None:
            return ""
        return getattr(row, which, "") or ""

    async def read_summary(self, *, user_id: str | None = None) -> str:
        return await self.read_file("summary", user_id=user_id)

    async def read_profile(self, *, user_id: str | None = None) -> str:
        return await self.read_file("profile", user_id=user_id)

    async def read_snapshot(self, *, user_id: str | None = None) -> MemorySnapshot:
        uid = _user_id_or_default(user_id)
        row = await self._get_row(uid)
        if row is None:
            return MemorySnapshot(
                summary="", profile="",
                summary_updated_at=None, profile_updated_at=None,
            )
        ts = row.updated_at.isoformat() if row.updated_at else None
        return MemorySnapshot(
            summary=row.summary or "",
            profile=row.profile or "",
            summary_updated_at=ts,
            profile_updated_at=ts,
        )

    # ── Write ─────────────────────────────────────────────────────────

    async def write_file(
        self, which: MemoryFile, content: str, *, user_id: str | None = None
    ) -> MemorySnapshot:
        uid = _user_id_or_default(user_id)
        normalized = str(content or "").strip()
        await self._upsert(uid, **{which: normalized})
        return await self.read_snapshot(user_id=uid)

    async def write_memory(self, content: str, *, user_id: str | None = None) -> MemorySnapshot:
        return await self.write_file("profile", content, user_id=user_id)

    async def clear_file(
        self, which: MemoryFile, *, user_id: str | None = None
    ) -> MemorySnapshot:
        return await self.write_file(which, "", user_id=user_id)

    async def clear_memory(self, *, user_id: str | None = None) -> MemorySnapshot:
        uid = _user_id_or_default(user_id)
        await self._upsert(uid, summary="", profile="")
        return await self.read_snapshot(user_id=uid)

    # ── Context building (injected into LLM prompts) ─────────────────

    async def build_memory_context(
        self, max_chars: int = 4000, *, user_id: str | None = None
    ) -> str:
        snap = await self.read_snapshot(user_id=user_id)
        parts: list[str] = []
        if snap.profile:
            parts.append(f"### User Profile\n{snap.profile}")
        if snap.summary:
            parts.append(f"### Learning Context\n{snap.summary}")
        if not parts:
            return ""
        combined = "\n\n".join(parts)
        if len(combined) > max_chars:
            combined = combined[:max_chars].rstrip() + "\n...[truncated]"
        return (
            "## Background Memory\n"
            "Use this memory sparingly — only when directly relevant.\n\n"
            f"{combined}"
        )

    async def get_preferences_text(self, *, user_id: str | None = None) -> str:
        profile = await self.read_profile(user_id=user_id)
        return f"## User Profile\n{profile}" if profile else ""

    # ── Auto-refresh from conversation ────────────────────────────────

    async def refresh_from_turn(
        self,
        *,
        user_message: str,
        assistant_message: str,
        session_id: str = "",
        capability: str = "",
        language: str = "en",
        timestamp: str = "",
        user_id: str | None = None,
    ) -> MemoryUpdateResult:
        uid = _user_id_or_default(user_id)
        if not user_message.strip() or not assistant_message.strip():
            return MemoryUpdateResult(content="", changed=False, updated_at=None)

        source = (
            f"[Session] {session_id or '(unknown)'}\n"
            f"[Capability] {capability or 'chat'}\n"
            f"[Timestamp] {timestamp or datetime.now().isoformat()}\n\n"
            f"[User]\n{user_message.strip()}\n\n"
            f"[Assistant]\n{assistant_message.strip()}"
        )

        p_changed = await self._rewrite_one("profile", source, language, uid)
        s_changed = await self._rewrite_one("summary", source, language, uid)

        snap = await self.read_snapshot(user_id=uid)
        return MemoryUpdateResult(
            content=snap.profile,
            changed=p_changed or s_changed,
            updated_at=snap.profile_updated_at,
        )

    async def refresh_from_session(
        self,
        session_id: str | None = None,
        *,
        language: str = "en",
        max_messages: int = 10,
        user_id: str | None = None,
    ) -> MemoryUpdateResult:
        uid = _user_id_or_default(user_id)
        from deeptutor.services.session.sqlite_store import get_sqlite_session_store
        store = get_sqlite_session_store()

        target = (session_id or "").strip()
        if not target:
            sessions = await store.list_sessions(limit=1)
            if sessions:
                target = str(sessions[0].get("session_id", "") or "")
        if not target:
            return MemoryUpdateResult(content="", changed=False, updated_at=None)

        messages = await store.get_messages_for_context(target)
        relevant = [
            m for m in messages
            if str(m.get("role", "")) in {"user", "assistant"}
            and str(m.get("content", "") or "").strip()
        ][-max_messages:]
        if not relevant:
            return MemoryUpdateResult(content="", changed=False, updated_at=None)

        transcript = "\n\n".join(
            f"{'User' if m.get('role') == 'user' else 'Assistant'}: "
            f"{str(m.get('content', '') or '').strip()}"
            for m in relevant
        )

        cap = ""
        sess = await store.get_session(target)
        if sess:
            cap = str(sess.get("capability", "") or "")

        source = (
            f"[Session] {target}\n"
            f"[Capability] {cap or 'chat'}\n\n"
            f"[Recent Transcript]\n{transcript}"
        )

        p_changed = await self._rewrite_one("profile", source, language, uid)
        s_changed = await self._rewrite_one("summary", source, language, uid)

        snap = await self.read_snapshot(user_id=uid)
        return MemoryUpdateResult(
            content=snap.profile,
            changed=p_changed or s_changed,
            updated_at=snap.profile_updated_at,
        )

    # ── LLM rewrite for individual files ──────────────────────────────

    async def _rewrite_one(
        self, which: MemoryFile, source: str, language: str, uid: str
    ) -> bool:
        current = await self.read_file(which, user_id=uid)
        zh = str(language).lower().startswith("zh")

        if which == "profile":
            sys_prompt, user_prompt = self._profile_prompts(current, source, zh)
        else:
            sys_prompt, user_prompt = self._summary_prompts(current, source, zh)

        chunks: list[str] = []
        async for c in llm_stream(
            prompt=user_prompt,
            system_prompt=sys_prompt,
            temperature=0.2,
            max_tokens=900,
        ):
            chunks.append(c)

        raw = _strip_code_fence("".join(chunks)).strip()
        if not raw or raw == _NO_CHANGE:
            return False
        if raw == current:
            return False

        await self.write_file(which, raw, user_id=uid)
        return True

    @staticmethod
    def _profile_prompts(current: str, source: str, zh: bool) -> tuple[str, str]:
        if zh:
            return (
                "你负责维护一份用户画像文档。只保留稳定的用户身份、偏好、知识水平。"
                f"如果无需修改，请只返回 {_NO_CHANGE}。",
                "如果需要更新，请重写用户画像，可使用以下标题：\n"
                "## Identity\n## Learning Style\n## Knowledge Level\n## Preferences\n\n"
                "规则：保持简短，删除过时内容，不要记录临时对话。\n\n"
                f"[当前画像]\n{current or '(empty)'}\n\n"
                f"[新增材料]\n{source}"
            )
        return (
            "You maintain a user profile document. Only keep stable identity, "
            "preferences, and knowledge levels. "
            f"If nothing should change, return exactly {_NO_CHANGE}.",
            "Rewrite the user profile if needed. Suggested sections:\n"
            "## Identity\n## Learning Style\n## Knowledge Level\n## Preferences\n\n"
            "Rules: keep it short, remove stale items, no transient chatter.\n\n"
            f"[Current profile]\n{current or '(empty)'}\n\n"
            f"[New material]\n{source}"
        )

    @staticmethod
    def _summary_prompts(current: str, source: str, zh: bool) -> tuple[str, str]:
        if zh:
            return (
                "你负责维护一份学习旅程摘要。记录用户正在学什么、完成了什么、有哪些待解决的问题。"
                f"如果无需修改，请只返回 {_NO_CHANGE}。",
                "如果需要更新，请重写学习旅程摘要，可使用以下标题：\n"
                "## Current Focus\n## Accomplishments\n## Open Questions\n\n"
                "规则：保持简短，删除已完成或过时的条目。\n\n"
                f"[当前摘要]\n{current or '(empty)'}\n\n"
                f"[新增材料]\n{source}"
            )
        return (
            "You maintain a learning journey summary. Track what the user is studying, "
            "what they've accomplished, and what open questions remain. "
            f"If nothing should change, return exactly {_NO_CHANGE}.",
            "Rewrite the learning summary if needed. Suggested sections:\n"
            "## Current Focus\n## Accomplishments\n## Open Questions\n\n"
            "Rules: keep it short, remove completed/stale items.\n\n"
            f"[Current summary]\n{current or '(empty)'}\n\n"
            f"[New material]\n{source}"
        )

    # ── DB helpers ────────────────────────────────────────────────────

    async def _get_row(self, uid: str):
        from deeptutor.services.db.models.memory import UserMemory
        from deeptutor.services.db.engine import get_session_factory
        try:
            factory = get_session_factory()
        except RuntimeError:
            return None
        async with factory() as session:
            stmt = select(UserMemory).where(UserMemory.user_id == uid)
            result = await session.execute(stmt)
            return result.scalar_one_or_none()

    async def _upsert(self, uid: str, **fields: str) -> None:
        from deeptutor.services.db.models.memory import UserMemory
        from deeptutor.services.db.engine import get_session_factory
        factory = get_session_factory()
        async with factory() as session:
            stmt = select(UserMemory).where(UserMemory.user_id == uid)
            result = await session.execute(stmt)
            row = result.scalar_one_or_none()
            if row is None:
                row = UserMemory(user_id=uid, **fields)
                session.add(row)
            else:
                for k, v in fields.items():
                    setattr(row, k, v)
            await session.commit()


def _strip_code_fence(content: str) -> str:
    cleaned = str(content or "").strip()
    if cleaned.startswith("```"):
        cleaned = re.sub(r"^```[a-zA-Z0-9_-]*\n?", "", cleaned)
        cleaned = re.sub(r"\n?```$", "", cleaned)
    return cleaned.strip()


_memory_service: MemoryService | None = None


def get_memory_service() -> MemoryService:
    global _memory_service
    if _memory_service is None:
        _memory_service = MemoryService()
    return _memory_service


__all__ = [
    "MemoryFile",
    "MemoryService",
    "MemorySnapshot",
    "MemoryUpdateResult",
    "get_memory_service",
]
