"""
Unified session history API (multi-tenant).
"""

from __future__ import annotations

from pydantic import BaseModel, Field
from fastapi import APIRouter, Depends, HTTPException, Query

from deeptutor.api.middleware.tenant import require_user_id
from deeptutor.services.session import get_session_store

router = APIRouter()


# --- Oversized event-payload truncation (upstream PR #524) -----------------
# Session GET can replay tool results / observations whose payloads are huge
# (a full scraped page, a file dump, etc.). Trim them before returning so the
# history response stays small — the live WebSocket stream already delivered
# the full content to the client at the time it was produced.
MAX_EVENT_PAYLOAD = 50_000  # characters
_TRUNCATION_NOTICE = "\n\n…[truncated]"
_TRUNCATABLE_EVENT_TYPES = {"tool_result", "observation"}
_TRUNCATABLE_NESTED_FIELDS = ("content", "answer")


def _truncate_str(value: object) -> tuple[object, bool]:
    """Return (possibly-truncated value, was_truncated)."""
    if isinstance(value, str) and len(value) > MAX_EVENT_PAYLOAD:
        return value[:MAX_EVENT_PAYLOAD] + _TRUNCATION_NOTICE, True
    return value, False


def _truncate_oversized_events(messages: object) -> None:
    """Trim oversized tool-result/observation payloads in place.

    Mutates each message's parsed ``events`` list. Tolerant of missing or
    malformed ``events`` (does nothing for those). Only top-level ``content``
    and ``metadata.tool_metadata.{content,answer}`` are trimmed, and only for
    truncatable event types.
    """
    if not isinstance(messages, list):
        return
    for message in messages:
        if not isinstance(message, dict):
            continue
        events = message.get("events")
        if not isinstance(events, list):
            continue
        for event in events:
            if not isinstance(event, dict):
                continue
            if event.get("type") not in _TRUNCATABLE_EVENT_TYPES:
                continue
            truncated = False
            if "content" in event:
                new_val, did = _truncate_str(event["content"])
                if did:
                    event["content"] = new_val
                    truncated = True
            metadata = event.get("metadata")
            if isinstance(metadata, dict):
                tool_metadata = metadata.get("tool_metadata")
                if isinstance(tool_metadata, dict):
                    for field in _TRUNCATABLE_NESTED_FIELDS:
                        if field in tool_metadata:
                            new_val, did = _truncate_str(tool_metadata[field])
                            if did:
                                tool_metadata[field] = new_val
                                truncated = True
            if truncated:
                event["_truncated"] = True


class SessionRenameRequest(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)


class QuizResultItem(BaseModel):
    question_id: str = ""
    question: str = Field(..., min_length=1)
    user_answer: str = ""
    correct_answer: str = ""
    is_correct: bool


class QuizResultsRequest(BaseModel):
    answers: list[QuizResultItem] = Field(default_factory=list)


def _format_quiz_results_message(answers: list[QuizResultItem]) -> str:
    total = len(answers)
    correct = sum(1 for item in answers if item.is_correct)
    score_pct = round((correct / total) * 100) if total else 0
    lines = ["[Quiz Performance]"]
    for idx, item in enumerate(answers, 1):
        question = item.question.strip().replace("\n", " ")
        user_answer = (item.user_answer or "").strip() or "(blank)"
        status = "Correct" if item.is_correct else "Incorrect"
        suffix = f" ({status})"
        if not item.is_correct and (item.correct_answer or "").strip():
            suffix = f" ({status}, correct: {(item.correct_answer or '').strip()})"
        qid = f"[{item.question_id}] " if item.question_id else ""
        lines.append(f"{idx}. {qid}Q: {question} -> Answered: {user_answer}{suffix}")
    lines.append(f"Score: {correct}/{total} ({score_pct}%)")
    return "\n".join(lines)


@router.get("")
async def list_sessions(
    limit: int = Query(default=50, ge=1, le=200),
    offset: int = Query(default=0, ge=0),
    user_id: str = Depends(require_user_id),
):
    store = get_session_store()
    sessions = await store.list_sessions(limit=limit, offset=offset)
    return {"sessions": sessions}


@router.get("/{session_id}")
async def get_session(
    session_id: str,
    user_id: str = Depends(require_user_id),
):
    store = get_session_store()
    session = await store.get_session_with_messages(session_id)
    if session is None:
        raise HTTPException(status_code=404, detail="Session not found")
    if isinstance(session, dict):
        _truncate_oversized_events(session.get("messages"))
    return session


@router.patch("/{session_id}")
async def rename_session(
    session_id: str,
    payload: SessionRenameRequest,
    user_id: str = Depends(require_user_id),
):
    store = get_session_store()
    updated = await store.update_session_title(session_id, payload.title)
    if not updated:
        raise HTTPException(status_code=404, detail="Session not found")
    session = await store.get_session(session_id)
    return {"session": session}


@router.delete("/{session_id}")
async def delete_session(
    session_id: str,
    user_id: str = Depends(require_user_id),
):
    store = get_session_store()
    deleted = await store.delete_session(session_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Session not found")
    return {"deleted": True, "session_id": session_id}


@router.post("/{session_id}/quiz-results")
async def record_quiz_results(
    session_id: str,
    payload: QuizResultsRequest,
    user_id: str = Depends(require_user_id),
):
    if not payload.answers:
        raise HTTPException(status_code=400, detail="Quiz results are required")
    store = get_session_store()
    session = await store.get_session(session_id)
    if session is None:
        raise HTTPException(status_code=404, detail="Session not found")
    content = _format_quiz_results_message(payload.answers)
    await store.add_message(
        session_id=session_id,
        role="user",
        content=content,
        capability="deep_question",
    )
    return {
        "recorded": True,
        "session_id": session_id,
        "answer_count": len(payload.answers),
        "content": content,
    }
