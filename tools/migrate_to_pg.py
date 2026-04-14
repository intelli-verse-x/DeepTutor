#!/usr/bin/env python
"""
One-time migration: move legacy file/SQLite data into PostgreSQL
under a configurable user_id (default: "default").

Run from project root:
    python tools/migrate_to_pg.py [--user-id <uid>] [--dry-run]

Requires PG_HOST etc. to be set in the environment.
"""

from __future__ import annotations

import argparse
import asyncio
import json
import logging
import sqlite3
import sys
from datetime import datetime
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(levelname)s  %(message)s")
log = logging.getLogger("migrate")

PROJECT_ROOT = Path(__file__).resolve().parent.parent


async def migrate_memory(uid: str, *, dry_run: bool) -> None:
    """Migrate SUMMARY.md / PROFILE.md into the user_memory table."""
    from deeptutor.services.db.engine import get_session_factory
    from deeptutor.services.db.models.memory import UserMemory
    from sqlalchemy import select

    mem_dir = PROJECT_ROOT / "data" / "memory"
    summary = ""
    profile = ""
    for name, attr in [("SUMMARY.md", "summary"), ("PROFILE.md", "profile")]:
        f = mem_dir / name
        if f.exists():
            val = f.read_text(encoding="utf-8").strip()
            if attr == "summary":
                summary = val
            else:
                profile = val

    if not summary and not profile:
        log.info("  No memory files to migrate")
        return

    log.info(f"  summary={len(summary)} chars, profile={len(profile)} chars")
    if dry_run:
        return

    factory = get_session_factory()
    async with factory() as session:
        stmt = select(UserMemory).where(UserMemory.user_id == uid)
        result = await session.execute(stmt)
        row = result.scalar_one_or_none()
        if row is None:
            row = UserMemory(user_id=uid, summary=summary, profile=profile)
            session.add(row)
        else:
            if summary:
                row.summary = summary
            if profile:
                row.profile = profile
        await session.commit()
    log.info("  Memory migrated")


async def migrate_sessions(uid: str, *, dry_run: bool) -> None:
    """Migrate SQLite chat_history.db into chat_sessions / chat_messages tables."""
    from deeptutor.services.db.engine import get_session_factory
    from deeptutor.services.db.models.session import ChatSession, ChatMessage

    db_path = PROJECT_ROOT / "data" / "user" / "chat_history.db"
    if not db_path.exists():
        log.info("  No SQLite chat_history.db found")
        return

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row

    sessions = conn.execute(
        "SELECT id, title, created_at, updated_at, compressed_summary, "
        "summary_up_to_msg_id, preferences_json FROM sessions"
    ).fetchall()
    log.info(f"  Found {len(sessions)} sessions")

    messages = conn.execute(
        "SELECT id, session_id, role, content, capability, events_json, "
        "attachments_json, created_at FROM messages ORDER BY id"
    ).fetchall()
    log.info(f"  Found {len(messages)} messages")
    conn.close()

    if dry_run:
        return

    factory = get_session_factory()
    async with factory() as session:
        for s in sessions:
            cs = ChatSession(
                id=s["id"],
                user_id=uid,
                title=s["title"] or "New conversation",
                created_at=s["created_at"],
                updated_at=s["updated_at"],
                compressed_summary=s["compressed_summary"] or "",
                summary_up_to_msg_id=s["summary_up_to_msg_id"] or 0,
                preferences_json=s["preferences_json"] or "{}",
            )
            session.add(cs)

        for m in messages:
            meta = {}
            try:
                meta["capability"] = m["capability"] or ""
                meta["events"] = json.loads(m["events_json"] or "[]")
                meta["attachments"] = json.loads(m["attachments_json"] or "[]")
            except Exception:
                pass
            cm = ChatMessage(
                session_id=m["session_id"],
                user_id=uid,
                role=m["role"],
                content=m["content"] or "",
                timestamp=m["created_at"],
                metadata_=meta,
            )
            session.add(cm)

        await session.commit()
    log.info("  Sessions migrated")


async def migrate_notebooks(uid: str, *, dry_run: bool) -> None:
    """Migrate JSON-based notebooks into the notebooks / notebook_records tables."""
    from deeptutor.services.db.engine import get_session_factory
    from deeptutor.services.db.models.notebook import (
        Notebook as NotebookModel,
        NotebookRecord as NotebookRecordModel,
    )

    nb_dir = PROJECT_ROOT / "data" / "user" / "workspace" / "notebook"
    index_file = nb_dir / "notebooks_index.json"
    if not index_file.exists():
        log.info("  No notebooks_index.json found")
        return

    try:
        index = json.loads(index_file.read_text(encoding="utf-8"))
    except Exception:
        log.info("  Failed to read notebooks_index.json")
        return

    nb_ids = [nb["id"] for nb in index.get("notebooks", [])]
    log.info(f"  Found {len(nb_ids)} notebooks")

    if dry_run:
        return

    factory = get_session_factory()
    async with factory() as session:
        for nid in nb_ids:
            nb_file = nb_dir / f"{nid}.json"
            if not nb_file.exists():
                continue
            try:
                nb_data = json.loads(nb_file.read_text(encoding="utf-8"))
            except Exception:
                continue

            nb = NotebookModel(
                id=nid,
                user_id=uid,
                name=nb_data.get("name", ""),
                description=nb_data.get("description", ""),
                color=nb_data.get("color", "#3B82F6"),
                icon=nb_data.get("icon", "book"),
            )
            session.add(nb)

            for rec in nb_data.get("records", []):
                r = NotebookRecordModel(
                    id=rec.get("id", ""),
                    notebook_id=nid,
                    user_id=uid,
                    record_type=rec.get("type", "chat"),
                    title=rec.get("title", ""),
                    summary=rec.get("summary", ""),
                    user_query=rec.get("user_query", ""),
                    output=rec.get("output", ""),
                    metadata_=rec.get("metadata", {}),
                    kb_name=rec.get("kb_name"),
                )
                session.add(r)

        await session.commit()
    log.info("  Notebooks migrated")


async def migrate_knowledge_bases(uid: str, *, dry_run: bool) -> None:
    """Move existing KB directories under the user's subdirectory."""
    import shutil

    kb_root = PROJECT_ROOT / "data" / "knowledge_bases"
    user_kb_dir = kb_root / uid

    if not kb_root.exists():
        log.info("  No knowledge_bases directory found")
        return

    moved = 0
    for item in kb_root.iterdir():
        if not item.is_dir() or item.name.startswith(("__", ".")) or item.name == uid:
            continue
        dest = user_kb_dir / item.name
        if dest.exists():
            log.info(f"  Skipping {item.name} (already exists at dest)")
            continue
        log.info(f"  Moving KB '{item.name}' -> {uid}/{item.name}")
        if not dry_run:
            user_kb_dir.mkdir(parents=True, exist_ok=True)
            shutil.move(str(item), str(dest))
        moved += 1

    log.info(f"  Moved {moved} knowledge bases")


async def migrate_guide_sessions(uid: str, *, dry_run: bool) -> None:
    """Move existing guide session files under the user's subdirectory."""
    import shutil

    guide_dir = PROJECT_ROOT / "data" / "user" / "workspace" / "guide"
    user_guide_dir = PROJECT_ROOT / "data" / "user" / uid / "workspace" / "guide"

    if not guide_dir.exists():
        log.info("  No guide sessions directory found")
        return

    files = list(guide_dir.glob("session_*.json"))
    log.info(f"  Found {len(files)} guide session files")

    if dry_run or not files:
        return

    user_guide_dir.mkdir(parents=True, exist_ok=True)
    for f in files:
        dest = user_guide_dir / f.name
        if not dest.exists():
            shutil.copy2(str(f), str(dest))
    log.info("  Guide sessions copied")


async def main():
    parser = argparse.ArgumentParser(description="Migrate legacy data to PostgreSQL")
    parser.add_argument("--user-id", default="default", help="User ID for migrated data")
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing")
    args = parser.parse_args()

    uid = args.user_id
    dry_run = args.dry_run
    prefix = "[DRY RUN] " if dry_run else ""

    log.info(f"{prefix}Migrating data for user_id='{uid}'")

    # Initialize PG
    from deeptutor.services.db.engine import init_pg

    ok = await init_pg()
    if not ok:
        log.error("PostgreSQL not configured (PG_HOST not set). Aborting.")
        sys.exit(1)

    log.info("Memory:")
    await migrate_memory(uid, dry_run=dry_run)

    log.info("Sessions:")
    await migrate_sessions(uid, dry_run=dry_run)

    log.info("Notebooks:")
    await migrate_notebooks(uid, dry_run=dry_run)

    log.info("Knowledge Bases:")
    await migrate_knowledge_bases(uid, dry_run=dry_run)

    log.info("Guide Sessions:")
    await migrate_guide_sessions(uid, dry_run=dry_run)

    from deeptutor.services.db.engine import close_pg

    await close_pg()

    log.info(f"{prefix}Migration complete!")


if __name__ == "__main__":
    asyncio.run(main())
