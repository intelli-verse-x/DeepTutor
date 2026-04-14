"""
Per-user memory API: SUMMARY and PROFILE, backed by PostgreSQL.
"""

from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from deeptutor.api.middleware.tenant import require_user_id
from deeptutor.services.memory import MemoryFile, get_memory_service

router = APIRouter()

_VALID_FILES: set[MemoryFile] = {"summary", "profile"}


def _snap_dict(snap) -> dict:
    return {
        "summary": snap.summary,
        "profile": snap.profile,
        "summary_updated_at": snap.summary_updated_at,
        "profile_updated_at": snap.profile_updated_at,
    }


class FileUpdateRequest(BaseModel):
    file: MemoryFile
    content: str = ""


class MemoryRefreshRequest(BaseModel):
    session_id: str | None = None
    language: str = "en"


class MemoryClearRequest(BaseModel):
    file: MemoryFile | None = None


@router.get("")
async def get_memory(user_id: str = Depends(require_user_id)):
    snap = await get_memory_service().read_snapshot(user_id=user_id)
    return _snap_dict(snap)


@router.put("")
async def update_memory(
    payload: FileUpdateRequest,
    user_id: str = Depends(require_user_id),
):
    if payload.file not in _VALID_FILES:
        raise HTTPException(status_code=400, detail=f"Invalid file: {payload.file}")
    snap = await get_memory_service().write_file(
        payload.file, payload.content, user_id=user_id
    )
    return {**_snap_dict(snap), "saved": True}


@router.post("/refresh")
async def refresh_memory(
    payload: MemoryRefreshRequest,
    user_id: str = Depends(require_user_id),
):
    result = await get_memory_service().refresh_from_session(
        payload.session_id,
        language=payload.language,
        user_id=user_id,
    )
    snap = await get_memory_service().read_snapshot(user_id=user_id)
    return {**_snap_dict(snap), "changed": result.changed}


@router.post("/clear")
async def clear_memory(
    payload: MemoryClearRequest | None = None,
    user_id: str = Depends(require_user_id),
):
    svc = get_memory_service()
    target = payload.file if payload else None
    if target and target not in _VALID_FILES:
        raise HTTPException(status_code=400, detail=f"Invalid file: {target}")

    if target:
        snap = await svc.clear_file(target, user_id=user_id)
    else:
        snap = await svc.clear_memory(user_id=user_id)
    return {**_snap_dict(snap), "cleared": True}
