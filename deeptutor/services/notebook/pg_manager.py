"""
PostgreSQL-backed notebook manager with per-user isolation.
"""

from __future__ import annotations

import time
import uuid
from typing import Any

from sqlalchemy import delete, select, update

from deeptutor.api.middleware.tenant import get_current_user_id
from deeptutor.services.db.engine import get_session_factory
from deeptutor.services.db.models.notebook import (
    Notebook as NotebookModel,
    NotebookRecord as NotebookRecordModel,
)


def _uid(user_id: str | None = None) -> str:
    return (user_id or "").strip() or get_current_user_id()


class PGNotebookManager:
    """Manage notebooks in PostgreSQL with per-user isolation."""

    async def create_notebook(
        self,
        name: str,
        description: str = "",
        color: str = "#3B82F6",
        icon: str = "book",
        *,
        user_id: str | None = None,
    ) -> dict:
        uid = _uid(user_id)
        nid = str(uuid.uuid4())[:8]
        now = time.time()

        factory = get_session_factory()
        async with factory() as session:
            row = NotebookModel(
                id=nid,
                user_id=uid,
                name=name,
                description=description,
                color=color,
                icon=icon,
            )
            session.add(row)
            await session.commit()

        return {
            "id": nid,
            "name": name,
            "description": description,
            "created_at": now,
            "updated_at": now,
            "records": [],
            "color": color,
            "icon": icon,
        }

    async def list_notebooks(self, *, user_id: str | None = None) -> list[dict]:
        uid = _uid(user_id)
        factory = get_session_factory()
        async with factory() as session:
            stmt = (
                select(NotebookModel)
                .where(NotebookModel.user_id == uid)
                .order_by(NotebookModel.updated_at.desc())
            )
            result = await session.execute(stmt)
            rows = result.scalars().all()

        notebooks = []
        for r in rows:
            notebooks.append({
                "id": r.id,
                "name": r.name,
                "description": r.description or "",
                "created_at": r.created_at.timestamp() if r.created_at else 0,
                "updated_at": r.updated_at.timestamp() if r.updated_at else 0,
                "record_count": 0,
                "color": r.color or "#3B82F6",
                "icon": r.icon or "book",
            })
        return notebooks

    async def get_notebook(
        self, notebook_id: str, *, user_id: str | None = None
    ) -> dict | None:
        uid = _uid(user_id)
        factory = get_session_factory()
        async with factory() as session:
            stmt = select(NotebookModel).where(
                NotebookModel.id == notebook_id,
                NotebookModel.user_id == uid,
            )
            result = await session.execute(stmt)
            nb = result.scalar_one_or_none()
            if nb is None:
                return None

            rec_stmt = (
                select(NotebookRecordModel)
                .where(NotebookRecordModel.notebook_id == notebook_id)
                .order_by(NotebookRecordModel.created_at.desc())
            )
            rec_result = await session.execute(rec_stmt)
            recs = rec_result.scalars().all()

        records = []
        for r in recs:
            records.append({
                "id": r.id,
                "type": r.record_type,
                "title": r.title,
                "summary": r.summary or "",
                "user_query": r.user_query or "",
                "output": r.output or "",
                "metadata": r.metadata_ or {},
                "created_at": r.created_at.timestamp() if r.created_at else 0,
                "kb_name": r.kb_name,
            })

        return {
            "id": nb.id,
            "name": nb.name,
            "description": nb.description or "",
            "created_at": nb.created_at.timestamp() if nb.created_at else 0,
            "updated_at": nb.updated_at.timestamp() if nb.updated_at else 0,
            "records": records,
            "color": nb.color or "#3B82F6",
            "icon": nb.icon or "book",
        }

    async def update_notebook(
        self,
        notebook_id: str,
        name: str | None = None,
        description: str | None = None,
        color: str | None = None,
        icon: str | None = None,
        *,
        user_id: str | None = None,
    ) -> dict | None:
        uid = _uid(user_id)
        factory = get_session_factory()
        async with factory() as session:
            stmt = select(NotebookModel).where(
                NotebookModel.id == notebook_id,
                NotebookModel.user_id == uid,
            )
            result = await session.execute(stmt)
            nb = result.scalar_one_or_none()
            if nb is None:
                return None
            if name is not None:
                nb.name = name
            if description is not None:
                nb.description = description
            if color is not None:
                nb.color = color
            if icon is not None:
                nb.icon = icon
            await session.commit()

        return await self.get_notebook(notebook_id, user_id=uid)

    async def delete_notebook(
        self, notebook_id: str, *, user_id: str | None = None
    ) -> bool:
        uid = _uid(user_id)
        factory = get_session_factory()
        async with factory() as session:
            stmt = delete(NotebookModel).where(
                NotebookModel.id == notebook_id,
                NotebookModel.user_id == uid,
            )
            result = await session.execute(stmt)
            await session.commit()
        return result.rowcount > 0  # type: ignore[union-attr]

    async def add_record(
        self,
        notebook_ids: list[str],
        record_type: str,
        title: str,
        user_query: str,
        output: str,
        summary: str = "",
        metadata: dict | None = None,
        kb_name: str | None = None,
        *,
        user_id: str | None = None,
    ) -> dict:
        uid = _uid(user_id)
        record_id = str(uuid.uuid4())[:8]

        record_dict: dict[str, Any] = {
            "id": record_id,
            "type": str(record_type),
            "title": title,
            "summary": summary,
            "user_query": user_query,
            "output": output,
            "metadata": metadata or {},
            "created_at": time.time(),
            "kb_name": kb_name,
        }

        added_to: list[str] = []
        factory = get_session_factory()
        async with factory() as session:
            for nid in notebook_ids:
                nb_stmt = select(NotebookModel).where(
                    NotebookModel.id == nid, NotebookModel.user_id == uid
                )
                nb_result = await session.execute(nb_stmt)
                nb = nb_result.scalar_one_or_none()
                if nb is None:
                    continue
                rec = NotebookRecordModel(
                    id=record_id,
                    notebook_id=nid,
                    user_id=uid,
                    record_type=str(record_type),
                    title=title,
                    summary=summary,
                    user_query=user_query,
                    output=output,
                    metadata_=metadata or {},
                    kb_name=kb_name,
                )
                session.add(rec)
                added_to.append(nid)
                # use a fresh id for each notebook if adding to multiple
                if len(notebook_ids) > 1:
                    record_id = str(uuid.uuid4())[:8]
            await session.commit()

        return {"record": record_dict, "added_to_notebooks": added_to}

    async def get_records(
        self, notebook_id: str, record_ids: list[str] | None = None, *, user_id: str | None = None
    ) -> list[dict]:
        uid = _uid(user_id)
        factory = get_session_factory()
        async with factory() as session:
            stmt = select(NotebookRecordModel).where(
                NotebookRecordModel.notebook_id == notebook_id,
                NotebookRecordModel.user_id == uid,
            )
            if record_ids:
                stmt = stmt.where(NotebookRecordModel.id.in_(record_ids))
            result = await session.execute(stmt)
            rows = result.scalars().all()

        return [
            {
                "id": r.id,
                "type": r.record_type,
                "title": r.title,
                "summary": r.summary or "",
                "user_query": r.user_query or "",
                "output": r.output or "",
                "metadata": r.metadata_ or {},
                "created_at": r.created_at.timestamp() if r.created_at else 0,
                "kb_name": r.kb_name,
            }
            for r in rows
        ]

    async def get_record(
        self, notebook_id: str, record_id: str, *, user_id: str | None = None
    ) -> dict | None:
        records = await self.get_records(notebook_id, [record_id], user_id=user_id)
        return records[0] if records else None

    async def get_records_by_references(
        self, notebook_references: list[dict], *, user_id: str | None = None
    ) -> list[dict]:
        resolved: list[dict] = []
        for ref in notebook_references:
            nid = str(ref.get("notebook_id", "") or "").strip()
            if not nid:
                continue
            record_ids = [
                str(rid).strip()
                for rid in (ref.get("record_ids") or [])
                if str(rid).strip()
            ]
            nb = await self.get_notebook(nid, user_id=user_id)
            if not nb:
                continue
            records = await self.get_records(nid, record_ids, user_id=user_id)
            for r in records:
                resolved.append({**r, "notebook_id": nid, "notebook_name": nb.get("name", nid)})
        return resolved

    async def remove_record(
        self, notebook_id: str, record_id: str, *, user_id: str | None = None
    ) -> bool:
        uid = _uid(user_id)
        factory = get_session_factory()
        async with factory() as session:
            stmt = delete(NotebookRecordModel).where(
                NotebookRecordModel.id == record_id,
                NotebookRecordModel.notebook_id == notebook_id,
                NotebookRecordModel.user_id == uid,
            )
            result = await session.execute(stmt)
            await session.commit()
        return result.rowcount > 0  # type: ignore[union-attr]

    async def update_record(
        self,
        notebook_id: str,
        record_id: str,
        *,
        title: str | None = None,
        summary: str | None = None,
        user_query: str | None = None,
        output: str | None = None,
        metadata: dict | None = None,
        kb_name: str | None = None,
        user_id: str | None = None,
    ) -> dict | None:
        uid = _uid(user_id)
        factory = get_session_factory()
        async with factory() as session:
            stmt = select(NotebookRecordModel).where(
                NotebookRecordModel.id == record_id,
                NotebookRecordModel.notebook_id == notebook_id,
                NotebookRecordModel.user_id == uid,
            )
            result = await session.execute(stmt)
            rec = result.scalar_one_or_none()
            if rec is None:
                return None
            if title is not None:
                rec.title = title
            if summary is not None:
                rec.summary = summary
            if user_query is not None:
                rec.user_query = user_query
            if output is not None:
                rec.output = output
            if metadata is not None:
                current = rec.metadata_ or {}
                rec.metadata_ = {**current, **metadata}
            if kb_name is not None:
                rec.kb_name = kb_name
            await session.commit()

        return await self.get_record(notebook_id, record_id, user_id=uid)

    async def get_statistics(self, *, user_id: str | None = None) -> dict:
        notebooks = await self.list_notebooks(user_id=user_id)
        type_counts: dict[str, int] = {
            "solve": 0, "question": 0, "research": 0,
            "co_writer": 0, "chat": 0, "guided_learning": 0,
        }
        total_records = 0

        uid = _uid(user_id)
        factory = get_session_factory()
        async with factory() as session:
            stmt = select(NotebookRecordModel).where(NotebookRecordModel.user_id == uid)
            result = await session.execute(stmt)
            recs = result.scalars().all()

        for r in recs:
            total_records += 1
            rt = r.record_type or ""
            if rt in type_counts:
                type_counts[rt] += 1

        return {
            "total_notebooks": len(notebooks),
            "total_records": total_records,
            "records_by_type": type_counts,
            "recent_notebooks": notebooks[:5],
        }
