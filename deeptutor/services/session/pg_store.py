"""
PostgreSQL-backed session store — drop-in replacement for SQLiteSessionStore
with per-user isolation via user_id.
"""

from __future__ import annotations

import json
import time
import uuid
from typing import Any

from sqlalchemy import delete, func, select, update

from deeptutor.api.middleware.tenant import get_current_user_id
from deeptutor.services.db.engine import get_session_factory
from deeptutor.services.db.models.session import (
    ChatMessage,
    ChatSession,
    ChatTurn,
    ChatTurnEvent,
)


def _json_dumps(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False)


def _json_loads(value: str | None, default: Any) -> Any:
    if not value:
        return default
    try:
        return json.loads(value)
    except json.JSONDecodeError:
        return default


def _uid(user_id: str | None = None) -> str:
    return (user_id or "").strip() or get_current_user_id()


class PGSessionStore:
    """Persist unified chat sessions in PostgreSQL with per-user isolation."""

    async def create_session(
        self,
        title: str | None = None,
        session_id: str | None = None,
        *,
        user_id: str | None = None,
    ) -> dict[str, Any]:
        uid = _uid(user_id)
        now = time.time()
        sid = session_id or f"unified_{int(now * 1000)}_{uuid.uuid4().hex[:8]}"
        resolved_title = (title or "New conversation").strip() or "New conversation"

        factory = get_session_factory()
        async with factory() as session:
            row = ChatSession(
                id=sid,
                user_id=uid,
                title=resolved_title[:100],
                created_at=now,
                updated_at=now,
            )
            session.add(row)
            await session.commit()

        return {
            "id": sid,
            "session_id": sid,
            "title": resolved_title[:100],
            "created_at": now,
            "updated_at": now,
            "compressed_summary": "",
            "summary_up_to_msg_id": 0,
        }

    async def get_session(
        self, session_id: str, *, user_id: str | None = None
    ) -> dict[str, Any] | None:
        uid = _uid(user_id)
        factory = get_session_factory()
        async with factory() as session:
            stmt = select(ChatSession).where(
                ChatSession.id == session_id, ChatSession.user_id == uid
            )
            result = await session.execute(stmt)
            row = result.scalar_one_or_none()
            if row is None:
                return None

            # latest turn info
            t_stmt = (
                select(ChatTurn)
                .where(ChatTurn.session_id == session_id)
                .order_by(ChatTurn.created_at.desc())
                .limit(1)
            )
            t_result = await session.execute(t_stmt)
            latest_turn = t_result.scalar_one_or_none()

            active_stmt = (
                select(ChatTurn.id)
                .where(
                    ChatTurn.session_id == session_id,
                    ChatTurn.events.any(),  # type: ignore[attr-defined]
                )
                .limit(1)
            )

        payload: dict[str, Any] = {
            "id": row.id,
            "session_id": row.id,
            "title": row.title,
            "created_at": row.created_at,
            "updated_at": row.updated_at,
            "compressed_summary": row.compressed_summary or "",
            "summary_up_to_msg_id": row.summary_up_to_msg_id or 0,
            "preferences": _json_loads(row.preferences_json, {}),
            "status": "idle",
            "active_turn_id": "",
            "capability": "",
        }
        if latest_turn:
            payload["capability"] = latest_turn.capability or ""
            # for simplicity we don't track status in PG turns;
            # it's derived from the turn's lifecycle
        return payload

    async def ensure_session(
        self, session_id: str | None = None, *, user_id: str | None = None
    ) -> dict[str, Any]:
        if session_id:
            s = await self.get_session(session_id, user_id=user_id)
            if s is not None:
                return s
        return await self.create_session(user_id=user_id)

    async def create_turn(
        self, session_id: str, capability: str = "", *, user_id: str | None = None
    ) -> dict[str, Any]:
        uid = _uid(user_id)
        now = time.time()
        turn_id = f"turn_{int(now * 1000)}_{uuid.uuid4().hex[:10]}"

        factory = get_session_factory()
        async with factory() as session:
            row = ChatTurn(
                id=turn_id,
                session_id=session_id,
                user_id=uid,
                capability=capability or "",
                created_at=now,
            )
            session.add(row)
            await session.commit()

        return {
            "id": turn_id,
            "turn_id": turn_id,
            "session_id": session_id,
            "capability": capability or "",
            "status": "running",
            "error": "",
            "created_at": now,
            "updated_at": now,
            "finished_at": None,
            "last_seq": 0,
        }

    async def get_turn(self, turn_id: str) -> dict[str, Any] | None:
        factory = get_session_factory()
        async with factory() as session:
            stmt = select(ChatTurn).where(ChatTurn.id == turn_id)
            result = await session.execute(stmt)
            row = result.scalar_one_or_none()
        if row is None:
            return None
        return {
            "id": row.id,
            "turn_id": row.id,
            "session_id": row.session_id,
            "capability": row.capability or "",
            "status": "completed",
            "error": "",
            "created_at": row.created_at,
            "updated_at": row.created_at,
            "finished_at": None,
            "last_seq": 0,
        }

    async def get_active_turn(self, session_id: str) -> dict[str, Any] | None:
        return None  # PG store doesn't track running state in DB

    async def list_active_turns(self, session_id: str) -> list[dict[str, Any]]:
        return []

    async def update_turn_status(self, turn_id: str, status: str, error: str = "") -> bool:
        return True  # no-op for PG; status tracked in-memory by turn_runtime

    async def append_turn_event(
        self, turn_id: str, event: dict[str, Any]
    ) -> dict[str, Any]:
        now = time.time()
        factory = get_session_factory()
        async with factory() as session:
            # get next seq
            max_stmt = select(func.coalesce(func.max(ChatTurnEvent.id), 0))
            seq = event.get("seq") or 0

            evt = ChatTurnEvent(
                turn_id=turn_id,
                event_type=event.get("type", ""),
                data={
                    "source": event.get("source", ""),
                    "stage": event.get("stage", ""),
                    "content": event.get("content", ""),
                    "metadata": event.get("metadata", {}),
                    "seq": seq,
                },
                created_at=float(event.get("timestamp") or now),
            )
            session.add(evt)
            await session.commit()

        payload = dict(event)
        payload["turn_id"] = turn_id
        return payload

    async def get_turn_events(
        self, turn_id: str, after_seq: int = 0
    ) -> list[dict[str, Any]]:
        factory = get_session_factory()
        async with factory() as session:
            stmt = (
                select(ChatTurnEvent)
                .where(ChatTurnEvent.turn_id == turn_id)
                .order_by(ChatTurnEvent.id.asc())
            )
            result = await session.execute(stmt)
            rows = result.scalars().all()

        events = []
        for row in rows:
            d = row.data or {}
            seq_val = d.get("seq", 0)
            if seq_val <= after_seq:
                continue
            events.append({
                "type": row.event_type,
                "source": d.get("source", ""),
                "stage": d.get("stage", ""),
                "content": d.get("content", ""),
                "metadata": d.get("metadata", {}),
                "turn_id": row.turn_id,
                "seq": seq_val,
                "timestamp": row.created_at,
            })
        return events

    async def update_session_title(
        self, session_id: str, title: str, *, user_id: str | None = None
    ) -> bool:
        uid = _uid(user_id)
        factory = get_session_factory()
        async with factory() as session:
            stmt = (
                update(ChatSession)
                .where(ChatSession.id == session_id, ChatSession.user_id == uid)
                .values(
                    title=(title.strip() or "New conversation")[:100],
                    updated_at=time.time(),
                )
            )
            result = await session.execute(stmt)
            await session.commit()
        return result.rowcount > 0  # type: ignore[union-attr]

    async def delete_session(
        self, session_id: str, *, user_id: str | None = None
    ) -> bool:
        uid = _uid(user_id)
        factory = get_session_factory()
        async with factory() as session:
            stmt = delete(ChatSession).where(
                ChatSession.id == session_id, ChatSession.user_id == uid
            )
            result = await session.execute(stmt)
            await session.commit()
        return result.rowcount > 0  # type: ignore[union-attr]

    async def add_message(
        self,
        session_id: str,
        role: str,
        content: str,
        capability: str = "",
        events: list[dict[str, Any]] | None = None,
        attachments: list[dict[str, Any]] | None = None,
        *,
        user_id: str | None = None,
    ) -> int:
        uid = _uid(user_id)
        now = time.time()
        factory = get_session_factory()
        async with factory() as session:
            msg = ChatMessage(
                session_id=session_id,
                user_id=uid,
                role=role,
                content=content or "",
                timestamp=now,
                metadata_={
                    "capability": capability or "",
                    "events": events or [],
                    "attachments": attachments or [],
                },
            )
            session.add(msg)

            # Auto-title on first user message
            if role == "user":
                s_stmt = select(ChatSession).where(ChatSession.id == session_id)
                s_result = await session.execute(s_stmt)
                s_row = s_result.scalar_one_or_none()
                if s_row and s_row.title == "New conversation":
                    trimmed = (content or "").strip()
                    if trimmed:
                        s_row.title = trimmed[:50] + ("..." if len(trimmed) > 50 else "")

            # Update session timestamp
            u_stmt = (
                update(ChatSession)
                .where(ChatSession.id == session_id)
                .values(updated_at=now)
            )
            await session.execute(u_stmt)
            await session.commit()
            return msg.id

    async def get_messages(
        self, session_id: str, *, user_id: str | None = None
    ) -> list[dict[str, Any]]:
        uid = _uid(user_id)
        factory = get_session_factory()
        async with factory() as session:
            stmt = (
                select(ChatMessage)
                .where(
                    ChatMessage.session_id == session_id,
                    ChatMessage.user_id == uid,
                )
                .order_by(ChatMessage.id.asc())
            )
            result = await session.execute(stmt)
            rows = result.scalars().all()

        return [
            {
                "id": r.id,
                "session_id": r.session_id,
                "role": r.role,
                "content": r.content,
                "capability": (r.metadata_ or {}).get("capability", ""),
                "events": (r.metadata_ or {}).get("events", []),
                "attachments": (r.metadata_ or {}).get("attachments", []),
                "created_at": r.timestamp,
            }
            for r in rows
        ]

    async def get_messages_for_context(
        self, session_id: str, *, user_id: str | None = None
    ) -> list[dict[str, Any]]:
        uid = _uid(user_id)
        factory = get_session_factory()
        async with factory() as session:
            stmt = (
                select(ChatMessage.id, ChatMessage.role, ChatMessage.content)
                .where(
                    ChatMessage.session_id == session_id,
                    ChatMessage.user_id == uid,
                    ChatMessage.role.in_(["user", "assistant", "system"]),
                )
                .order_by(ChatMessage.id.asc())
            )
            result = await session.execute(stmt)
            rows = result.all()

        return [
            {"id": r.id, "role": r.role, "content": r.content or ""}
            for r in rows
        ]

    async def list_sessions(
        self,
        limit: int = 50,
        offset: int = 0,
        *,
        user_id: str | None = None,
    ) -> list[dict[str, Any]]:
        uid = _uid(user_id)
        factory = get_session_factory()
        async with factory() as session:
            stmt = (
                select(ChatSession)
                .where(ChatSession.user_id == uid)
                .order_by(ChatSession.updated_at.desc())
                .limit(limit)
                .offset(offset)
            )
            result = await session.execute(stmt)
            rows = result.scalars().all()

        sessions = []
        for r in rows:
            sessions.append({
                "id": r.id,
                "session_id": r.id,
                "title": r.title,
                "created_at": r.created_at,
                "updated_at": r.updated_at,
                "compressed_summary": r.compressed_summary or "",
                "summary_up_to_msg_id": r.summary_up_to_msg_id or 0,
                "preferences": _json_loads(r.preferences_json, {}),
                "status": "idle",
                "active_turn_id": "",
                "capability": "",
                "message_count": 0,
                "last_message": "",
            })
        return sessions

    async def update_summary(
        self, session_id: str, summary: str, up_to_msg_id: int
    ) -> bool:
        factory = get_session_factory()
        async with factory() as session:
            stmt = (
                update(ChatSession)
                .where(ChatSession.id == session_id)
                .values(
                    compressed_summary=summary,
                    summary_up_to_msg_id=max(0, int(up_to_msg_id)),
                )
            )
            result = await session.execute(stmt)
            await session.commit()
        return result.rowcount > 0  # type: ignore[union-attr]

    async def update_session_preferences(
        self, session_id: str, preferences: dict[str, Any]
    ) -> bool:
        factory = get_session_factory()
        async with factory() as session:
            s_stmt = select(ChatSession).where(ChatSession.id == session_id)
            s_result = await session.execute(s_stmt)
            row = s_result.scalar_one_or_none()
            if row is None:
                return False
            merged = {**_json_loads(row.preferences_json, {}), **(preferences or {})}
            row.preferences_json = _json_dumps(merged)
            row.updated_at = time.time()
            await session.commit()
        return True

    async def get_session_with_messages(
        self, session_id: str, *, user_id: str | None = None
    ) -> dict[str, Any] | None:
        s = await self.get_session(session_id, user_id=user_id)
        if s is None:
            return None
        s["messages"] = await self.get_messages(session_id, user_id=user_id)
        s["active_turns"] = []
        return s
