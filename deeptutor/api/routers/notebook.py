"""
Notebook API Router (multi-tenant)
"""

import json
from typing import AsyncGenerator, Literal

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from deeptutor.agents.notebook import NotebookSummarizeAgent
from deeptutor.api.middleware.tenant import require_user_id
from deeptutor.services.notebook import get_pg_notebook_manager

router = APIRouter()


class CreateNotebookRequest(BaseModel):
    name: str
    description: str = ""
    color: str = "#3B82F6"
    icon: str = "book"


class UpdateNotebookRequest(BaseModel):
    name: str | None = None
    description: str | None = None
    color: str | None = None
    icon: str | None = None


class AddRecordRequest(BaseModel):
    notebook_ids: list[str]
    record_type: Literal["solve", "question", "research", "co_writer", "chat", "guided_learning"]
    title: str
    summary: str = ""
    user_query: str
    output: str
    metadata: dict = {}
    kb_name: str | None = None


class RemoveRecordRequest(BaseModel):
    record_id: str


class UpdateRecordRequest(BaseModel):
    title: str | None = None
    summary: str | None = None
    user_query: str | None = None
    output: str | None = None
    metadata: dict | None = None
    kb_name: str | None = None


async def _build_record_summary(request: AddRecordRequest) -> str:
    if request.summary.strip():
        return request.summary.strip()
    agent = NotebookSummarizeAgent(language=str(request.metadata.get("ui_language", "en")))
    return await agent.summarize(
        title=request.title,
        record_type=request.record_type,
        user_query=request.user_query,
        output=request.output,
        metadata=request.metadata,
    )


async def _stream_add_record_with_summary(
    request: AddRecordRequest,
) -> AsyncGenerator[str, None]:
    try:
        mgr = get_pg_notebook_manager()
        agent = NotebookSummarizeAgent(language=str(request.metadata.get("ui_language", "en")))
        summary_parts: list[str] = []
        if request.summary.strip():
            summary_parts.append(request.summary.strip())
            yield f"data: {json.dumps({'type': 'summary_chunk', 'content': request.summary.strip()}, ensure_ascii=False)}\n\n"
        else:
            async for chunk in agent.stream_summary(
                title=request.title,
                record_type=request.record_type,
                user_query=request.user_query,
                output=request.output,
                metadata=request.metadata,
            ):
                if not chunk:
                    continue
                summary_parts.append(chunk)
                yield f"data: {json.dumps({'type': 'summary_chunk', 'content': chunk}, ensure_ascii=False)}\n\n"

        summary = "".join(summary_parts).strip()
        result = await mgr.add_record(
            notebook_ids=request.notebook_ids,
            record_type=request.record_type,
            title=request.title,
            summary=summary,
            user_query=request.user_query,
            output=request.output,
            metadata=request.metadata,
            kb_name=request.kb_name,
        )
        payload = {
            "type": "result",
            "success": True,
            "summary": summary,
            "record": result["record"],
            "added_to_notebooks": result["added_to_notebooks"],
        }
        yield f"data: {json.dumps(payload, ensure_ascii=False)}\n\n"
    except Exception as exc:
        payload = {"type": "error", "detail": str(exc)}
        yield f"data: {json.dumps(payload, ensure_ascii=False)}\n\n"


@router.get("/list")
async def list_notebooks(user_id: str = Depends(require_user_id)):
    mgr = get_pg_notebook_manager()
    notebooks = await mgr.list_notebooks()
    return {"notebooks": notebooks, "total": len(notebooks)}


@router.get("/statistics")
async def get_statistics(user_id: str = Depends(require_user_id)):
    mgr = get_pg_notebook_manager()
    return await mgr.get_statistics()


@router.post("/create")
async def create_notebook(
    request: CreateNotebookRequest,
    user_id: str = Depends(require_user_id),
):
    mgr = get_pg_notebook_manager()
    notebook = await mgr.create_notebook(
        name=request.name,
        description=request.description,
        color=request.color,
        icon=request.icon,
    )
    return {"success": True, "notebook": notebook}


@router.get("/{notebook_id}")
async def get_notebook(
    notebook_id: str,
    user_id: str = Depends(require_user_id),
):
    mgr = get_pg_notebook_manager()
    notebook = await mgr.get_notebook(notebook_id)
    if not notebook:
        raise HTTPException(status_code=404, detail="Notebook not found")
    return notebook


@router.put("/{notebook_id}")
async def update_notebook(
    notebook_id: str,
    request: UpdateNotebookRequest,
    user_id: str = Depends(require_user_id),
):
    mgr = get_pg_notebook_manager()
    notebook = await mgr.update_notebook(
        notebook_id=notebook_id,
        name=request.name,
        description=request.description,
        color=request.color,
        icon=request.icon,
    )
    if not notebook:
        raise HTTPException(status_code=404, detail="Notebook not found")
    return {"success": True, "notebook": notebook}


@router.delete("/{notebook_id}")
async def delete_notebook(
    notebook_id: str,
    user_id: str = Depends(require_user_id),
):
    mgr = get_pg_notebook_manager()
    success = await mgr.delete_notebook(notebook_id)
    if not success:
        raise HTTPException(status_code=404, detail="Notebook not found")
    return {"success": True, "message": "Notebook deleted successfully"}


@router.post("/add_record")
async def add_record(
    request: AddRecordRequest,
    user_id: str = Depends(require_user_id),
):
    mgr = get_pg_notebook_manager()
    summary = await _build_record_summary(request)
    result = await mgr.add_record(
        notebook_ids=request.notebook_ids,
        record_type=request.record_type,
        title=request.title,
        summary=summary,
        user_query=request.user_query,
        output=request.output,
        metadata=request.metadata,
        kb_name=request.kb_name,
    )
    return {
        "success": True,
        "summary": summary,
        "record": result["record"],
        "added_to_notebooks": result["added_to_notebooks"],
    }


@router.post("/add_record_with_summary")
async def add_record_with_summary(request: AddRecordRequest):
    return StreamingResponse(
        _stream_add_record_with_summary(request),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )


@router.delete("/{notebook_id}/records/{record_id}")
async def remove_record(
    notebook_id: str,
    record_id: str,
    user_id: str = Depends(require_user_id),
):
    mgr = get_pg_notebook_manager()
    success = await mgr.remove_record(notebook_id, record_id)
    if not success:
        raise HTTPException(status_code=404, detail="Record not found")
    return {"success": True, "message": "Record removed successfully"}


@router.put("/{notebook_id}/records/{record_id}")
async def update_record(
    notebook_id: str,
    record_id: str,
    request: UpdateRecordRequest,
    user_id: str = Depends(require_user_id),
):
    mgr = get_pg_notebook_manager()
    updated = await mgr.update_record(
        notebook_id=notebook_id,
        record_id=record_id,
        title=request.title,
        summary=request.summary,
        user_query=request.user_query,
        output=request.output,
        metadata=request.metadata,
        kb_name=request.kb_name,
    )
    if not updated:
        raise HTTPException(status_code=404, detail="Record not found")
    return {"success": True, "record": updated}


@router.get("/health")
async def health_check():
    return {"status": "healthy", "service": "notebook"}
