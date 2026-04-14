"""
Proxy router for fetching a user's notes from Intelliverse-X-AI.

This allows the QuizVerse SPA (and other DeepTutor clients) to display
notes the user created in the Unity app without needing Cognito auth.

The DeepTutor backend calls Intelliverse-X-AI server-to-server using
Cognito OAuth client_credentials to obtain an access token automatically.

Env vars:
  INTELLIVERSE_API_URL     - Base URL (default: https://ai.intelli-verse-x.ai)
  INTELLIVERSE_API_KEY     - Optional pre-shared Bearer token (skips OAuth if set)
  COGNITO_OAUTH2_URL       - Cognito token endpoint for client_credentials flow
  COGNITO_S2S_CLIENT_ID    - Cognito app-client ID for service-to-service calls
  COGNITO_S2S_CLIENT_SECRET- Cognito app-client secret
"""

from __future__ import annotations

import logging
import os
import time
from typing import Any

import httpx
from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel

from deeptutor.api.middleware.tenant import require_user_id

logger = logging.getLogger(__name__)

router = APIRouter()

_INTELLIVERSE_API_URL = os.getenv(
    "INTELLIVERSE_API_URL", "https://ai.intelli-verse-x.ai"
)
_INTELLIVERSE_API_KEY = os.getenv("INTELLIVERSE_API_KEY", "")

_COGNITO_OAUTH2_URL = os.getenv("COGNITO_OAUTH2_URL", "")
_COGNITO_S2S_CLIENT_ID = os.getenv("COGNITO_S2S_CLIENT_ID", "")
_COGNITO_S2S_CLIENT_SECRET = os.getenv("COGNITO_S2S_CLIENT_SECRET", "")

_TIMEOUT = 15.0

# ── OAuth token cache ──────────────────────────────────────────────
_token_cache: dict[str, Any] = {"token": None, "expires_at": 0}


async def _get_oauth_token() -> str | None:
    """Acquire a Cognito access_token via client_credentials grant.

    Caches the token and refreshes 60 s before expiry.
    """
    if _token_cache["token"] and time.time() < _token_cache["expires_at"] - 60:
        return _token_cache["token"]

    if not (_COGNITO_OAUTH2_URL and _COGNITO_S2S_CLIENT_ID and _COGNITO_S2S_CLIENT_SECRET):
        return None

    try:
        async with httpx.AsyncClient(timeout=10) as client:
            resp = await client.post(
                _COGNITO_OAUTH2_URL,
                data={
                    "grant_type": "client_credentials",
                    "scope": os.getenv("COGNITO_S2S_SCOPE", "yourapi/all"),
                },
                auth=(_COGNITO_S2S_CLIENT_ID, _COGNITO_S2S_CLIENT_SECRET),
                headers={"Content-Type": "application/x-www-form-urlencoded"},
            )
            resp.raise_for_status()
            body = resp.json()
            _token_cache["token"] = body["access_token"]
            _token_cache["expires_at"] = time.time() + body.get("expires_in", 3600)
            logger.info("Cognito S2S token acquired (expires in %ss)", body.get("expires_in"))
            return _token_cache["token"]
    except Exception as e:
        logger.error("Failed to acquire Cognito S2S token: %s", e)
        return None


async def _build_auth_headers() -> dict[str, str]:
    """Build Authorization header using static key or OAuth token."""
    headers: dict[str, str] = {"Accept": "application/json"}

    if _INTELLIVERSE_API_KEY:
        headers["Authorization"] = f"Bearer {_INTELLIVERSE_API_KEY}"
        return headers

    token = await _get_oauth_token()
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


async def _proxy_get(
    path: str, *, params: dict[str, Any] | None = None
) -> dict[str, Any] | list[Any] | None:
    """Call Intelliverse-X-AI API and return the JSON response."""
    url = f"{_INTELLIVERSE_API_URL}{path}"
    headers = await _build_auth_headers()

    async with httpx.AsyncClient(timeout=_TIMEOUT) as client:
        resp = await client.get(url, headers=headers, params=params)
        if resp.status_code == 404:
            return None
        resp.raise_for_status()
        return resp.json()


class ImportToKBRequest(BaseModel):
    note_id: str
    kb_name: str
    title: str = ""
    content: str = ""


@router.get("/notes")
async def list_user_notes(
    user_id: str = Depends(require_user_id),
    page: int = Query(default=1, ge=1),
    page_size: int = Query(default=20, ge=1, le=100),
    order_by: str = Query(default="updatedAt"),
    order: str = Query(default="DESC"),
    note_type: str | None = Query(default=None, alias="type"),
    folder_id: str | None = Query(default=None),
):
    """List notes for the current user from Intelliverse-X-AI."""
    try:
        params: dict[str, Any] = {
            "page": page,
            "pageSize": page_size,
            "orderBy": order_by,
            "order": order,
        }
        if note_type:
            params["type"] = note_type
        if folder_id:
            params["folderId"] = folder_id

        data = await _proxy_get(
            f"/api/ai/notes/user/{user_id}", params=params
        )
        if data is None:
            return {"notes": [], "total": 0, "source": "intelliverse-x"}

        if isinstance(data, dict) and data.get("status") is not False:
            payload = data.get("data", {})
            notes = payload.get("notes") or payload.get("data") or []
            total = payload.get("total", len(notes))
            return {
                "notes": notes,
                "total": total,
                "page": payload.get("page", page),
                "page_size": payload.get("pageSize", page_size),
                "source": "intelliverse-x",
            }

        return {"notes": [], "total": 0, "source": "intelliverse-x"}
    except httpx.HTTPStatusError as e:
        logger.warning("Intelliverse-X-AI notes fetch failed: %s", e)
        return {"notes": [], "total": 0, "error": str(e), "source": "intelliverse-x"}
    except Exception as e:
        logger.warning("Intelliverse-X-AI notes fetch failed: %s", e)
        return {"notes": [], "total": 0, "error": str(e), "source": "intelliverse-x"}


@router.get("/notes/{note_id}")
async def get_note_detail(
    note_id: str,
    user_id: str = Depends(require_user_id),
):
    """Get full note detail (including content) from Intelliverse-X-AI."""
    try:
        data = await _proxy_get(f"/api/ai/notes/{note_id}")
        if data is None:
            raise HTTPException(status_code=404, detail="Note not found")
        if isinstance(data, dict) and data.get("success") is not False:
            return data.get("data", {})
        return data
    except HTTPException:
        raise
    except Exception as e:
        logger.warning("Note detail fetch failed: %s", e)
        raise HTTPException(status_code=502, detail=f"Upstream error: {e}")


@router.get("/folders")
async def list_user_folders(
    user_id: str = Depends(require_user_id),
):
    """List folders for the current user from Intelliverse-X-AI."""
    try:
        data = await _proxy_get("/api/ai/folders", params={"userId": user_id})
        if data is None:
            return {"folders": [], "source": "intelliverse-x"}
        if isinstance(data, dict) and data.get("success") is not False:
            return {
                "folders": data.get("data", {}).get("folders", []),
                "source": "intelliverse-x",
            }
        return {"folders": [], "source": "intelliverse-x"}
    except Exception as e:
        logger.warning("Folders fetch failed: %s", e)
        return {"folders": [], "error": str(e), "source": "intelliverse-x"}


@router.post("/notes/import-to-kb")
async def import_note_to_kb(
    request: ImportToKBRequest,
    user_id: str = Depends(require_user_id),
):
    """Import a note's content into a DeepTutor Knowledge Base.

    Fetches the full note from Intelliverse-X-AI, writes it as a
    text file into the KB's raw/ directory, and triggers the
    standard add_documents ingestion pipeline.
    """
    import re

    try:
        data = await _proxy_get(f"/api/ai/notes/{request.note_id}")
        if data is None:
            raise HTTPException(status_code=404, detail="Note not found on Intelliverse-X-AI")

        note = (
            data.get("data", {}).get("note", {})
            if isinstance(data, dict) and data.get("success") is not False
            else data
        )

        content = (
            request.content
            or note.get("content")
            or note.get("studyNote")
            or note.get("summary")
            or ""
        )
        title = request.title or note.get("title") or f"Note {request.note_id}"

        if not content.strip():
            raise HTTPException(
                status_code=400,
                detail="Note has no text content to import",
            )

        from deeptutor.knowledge.tenant_manager import (
            get_tenant_kb_manager,
            get_tenant_kb_base_dir,
        )

        kb_manager = get_tenant_kb_manager(user_id)
        if request.kb_name not in kb_manager.list_knowledge_bases():
            raise HTTPException(
                status_code=404,
                detail=f"Knowledge base '{request.kb_name}' not found",
            )

        kb_path = kb_manager.get_knowledge_base_path(request.kb_name)
        raw_dir = kb_path / "raw"
        raw_dir.mkdir(parents=True, exist_ok=True)

        safe_title = re.sub(r"[^\w\s-]", "", title)[:80].strip().replace(" ", "_")
        file_name = f"note_{request.note_id[:8]}_{safe_title}.txt"
        doc_path = raw_dir / file_name
        doc_path.write_text(
            f"# {title}\n\n{content}", encoding="utf-8"
        )

        from deeptutor.knowledge.add_documents import add_documents as kb_add_documents

        processed = await kb_add_documents(
            kb_name=request.kb_name,
            source_files=[str(doc_path)],
            base_dir=str(get_tenant_kb_base_dir(user_id)),
            allow_duplicates=False,
        )

        return {
            "success": True,
            "message": f"Note '{title}' imported into KB '{request.kb_name}'",
            "note_id": request.note_id,
            "kb_name": request.kb_name,
            "content_length": len(content),
            "documents_processed": processed,
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error("Import note to KB failed: %s", e, exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))
