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
    path: str, *, params: dict[str, Any] | None = None, timeout: float | None = None
) -> dict[str, Any] | list[Any] | None:
    """Call Intelliverse-X-AI API and return the JSON response."""
    url = f"{_INTELLIVERSE_API_URL}{path}"
    headers = await _build_auth_headers()

    async with httpx.AsyncClient(timeout=timeout or _TIMEOUT) as client:
        resp = await client.get(url, headers=headers, params=params)
        if resp.status_code == 404:
            return None
        resp.raise_for_status()
        return resp.json()


async def _proxy_post(
    path: str,
    *,
    json_body: dict[str, Any] | None = None,
    timeout: float | None = None,
) -> dict[str, Any] | list[Any] | None:
    """POST to Intelliverse-X-AI API and return the JSON response."""
    url = f"{_INTELLIVERSE_API_URL}{path}"
    headers = await _build_auth_headers()
    headers["Content-Type"] = "application/json"

    async with httpx.AsyncClient(timeout=timeout or _TIMEOUT) as client:
        resp = await client.post(url, headers=headers, json=json_body or {})
        if resp.status_code == 404:
            return None
        resp.raise_for_status()
        return resp.json()


def _unwrap_ai_payload(data: Any) -> dict[str, Any]:
    """Normalize Intelliverse-X-AI envelope { status, data } vs flat body."""
    if not isinstance(data, dict):
        return {}
    if data.get("data") and isinstance(data["data"], dict):
        return data["data"]
    return data


class ImportToKBRequest(BaseModel):
    note_id: str
    kb_name: str
    title: str = ""
    content: str = ""


class CreateLinkNoteRequest(BaseModel):
    type: str = "website"
    url: str
    title: str = ""


class GenerateStudyMaterialsRequest(BaseModel):
    note_id: str


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


@router.post("/notes/create")
async def create_link_note(
    request: CreateLinkNoteRequest,
    user_id: str = Depends(require_user_id),
):
    """Kick off URL/YouTube ingestion on Intelliverse-X-AI for the current user."""
    note_type = (request.type or "website").strip().lower()
    body: dict[str, Any] = {
        "type": note_type,
        "url": request.url,
        "ownerUserId": user_id,
        "sourceChannel": "web_chat",
        "autoGenerateStudyMaterials": False,
    }
    if request.title.strip():
        body["title"] = request.title.strip()
    if note_type == "youtube":
        body["youtubeUrl"] = request.url

    try:
        data = await _proxy_post("/api/ai/notes/create", json_body=body, timeout=20.0)
        if data is None:
            raise HTTPException(status_code=502, detail="Notes create returned 404")
        payload = _unwrap_ai_payload(data)
        job_id = payload.get("jobId") or payload.get("job_id")
        note_id = payload.get("noteId") or payload.get("note_id")
        status = payload.get("status") or "queued"
        if not job_id and not note_id:
            raise HTTPException(status_code=502, detail="Notes create missing jobId/noteId")
        return {
            "success": True,
            "job_id": job_id,
            "note_id": note_id,
            "status": status,
            "source": "intelliverse-x",
        }
    except HTTPException:
        raise
    except httpx.HTTPStatusError as e:
        logger.warning("Notes create failed: %s", e)
        raise HTTPException(status_code=502, detail=f"Upstream error: {e}") from e
    except Exception as e:
        logger.error("Notes create failed: %s", e, exc_info=True)
        raise HTTPException(status_code=500, detail=str(e)) from e


@router.get("/notes/jobs/{job_id}/status")
async def get_link_note_job_status(
    job_id: str,
    user_id: str = Depends(require_user_id),
):
    """Poll ingestion job status for a link note."""
    del user_id  # tenancy enforced upstream via ownerUserId at create time
    try:
        data = await _proxy_get(f"/api/ai/notes/jobs/{job_id}/status")
        if data is None:
            raise HTTPException(status_code=404, detail="Job not found")
        payload = _unwrap_ai_payload(data)
        return {
            "success": True,
            "job_id": job_id,
            "status": payload.get("status") or "unknown",
            "note_id": payload.get("noteId") or payload.get("note_id"),
            "error": payload.get("error"),
            "source": "intelliverse-x",
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.warning("Job status fetch failed: %s", e)
        raise HTTPException(status_code=502, detail=str(e)) from e


@router.post("/notes/generate-study-materials")
async def generate_link_study_materials(
    request: GenerateStudyMaterialsRequest,
    user_id: str = Depends(require_user_id),
):
    """Generate flashcards + quiz for an ingested note."""
    del user_id
    note_id = request.note_id.strip()
    if not note_id:
        raise HTTPException(status_code=400, detail="note_id is required")

    try:
        data = await _proxy_post(
            f"/api/ai/notes/{note_id}/generate-flashcards-quizzes",
            json_body={},
            timeout=120.0,
        )
        if data is None:
            raise HTTPException(status_code=404, detail="Note not found")

        envelope = data if isinstance(data, dict) else {}
        if envelope.get("status") is False:
            raise HTTPException(status_code=502, detail="Generation failed upstream")

        payload = _unwrap_ai_payload(envelope)
        flashcards_raw = payload.get("flashcards") or []
        quiz_raw = payload.get("quiz") or {}

        flashcards: list[dict[str, str]] = []
        if isinstance(flashcards_raw, list):
            for item in flashcards_raw:
                if not isinstance(item, dict):
                    continue
                front = str(item.get("question") or item.get("front") or "").strip()
                back = str(item.get("answer") or item.get("back") or "").strip()
                if front and back:
                    flashcards.append({"front": front, "back": back})

        questions: list[dict[str, Any]] = []
        quiz_questions = quiz_raw.get("questions") if isinstance(quiz_raw, dict) else None
        if isinstance(quiz_questions, list):
            for q in quiz_questions:
                if not isinstance(q, dict):
                    continue
                stem = str(q.get("question") or q.get("stem") or "").strip()
                opts = q.get("options") or q.get("choices") or []
                if not stem or not isinstance(opts, list) or len(opts) < 2:
                    continue
                options = [str(o) for o in opts]
                correct = q.get("correct")
                if isinstance(correct, int):
                    correct_idx = correct
                elif isinstance(correct, str):
                    correct_idx = options.index(correct) if correct in options else -1
                else:
                    ans = str(q.get("answer") or q.get("correctAnswer") or "").strip()
                    correct_idx = next(
                        (i for i, o in enumerate(options) if o.strip().lower() == ans.lower()),
                        -1,
                    )
                if correct_idx < 0 or correct_idx >= len(options):
                    continue
                questions.append(
                    {
                        "q": stem,
                        "opts": options,
                        "correct": correct_idx,
                        "explanation": str(q.get("explanation") or ""),
                    }
                )

        return {
            "success": True,
            "note_id": note_id,
            "title": quiz_raw.get("title") if isinstance(quiz_raw, dict) else None,
            "flashcards": flashcards,
            "questions": questions,
            "flash_count": len(flashcards),
            "quiz_count": len(questions),
            "source": "intelliverse-x",
        }
    except HTTPException:
        raise
    except httpx.HTTPStatusError as e:
        logger.warning("Study materials generation failed: %s", e)
        raise HTTPException(status_code=502, detail=f"Upstream error: {e}") from e
    except Exception as e:
        logger.error("Study materials generation failed: %s", e, exc_info=True)
        raise HTTPException(status_code=500, detail=str(e)) from e


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
