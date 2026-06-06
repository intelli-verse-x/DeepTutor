"""
Chat API Router
================

WebSocket endpoint for lightweight chat with session management.
REST endpoints for session operations.
"""

import asyncio
import logging

from fastapi import APIRouter, HTTPException, WebSocket, WebSocketDisconnect
from pydantic import BaseModel, Field

from deeptutor.agents.chat import ChatAgent, SessionManager
from deeptutor.services.config import PROJECT_ROOT, load_config_with_main
from deeptutor.services.kb import push_user_chat
from deeptutor.services.llm.config import get_llm_config, get_vision_llm_config
from deeptutor.services.settings.interface_settings import get_ui_language

config = load_config_with_main("main.yaml", PROJECT_ROOT)
log_dir = config.get("paths", {}).get("user_log_dir") or config.get("logging", {}).get("log_dir")
logger = logging.getLogger(__name__)

router = APIRouter()


def _get_session_manager() -> SessionManager:
    return SessionManager()


# =============================================================================
# REST Endpoints for Session Management
# =============================================================================


@router.get("/chat/sessions")
async def list_sessions(limit: int = 20):
    return _get_session_manager().list_sessions(limit=limit, include_messages=False)


@router.get("/chat/sessions/{session_id}")
async def get_session(session_id: str):
    session = _get_session_manager().get_session(session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    return session


@router.delete("/chat/sessions/{session_id}")
async def delete_session(session_id: str):
    if _get_session_manager().delete_session(session_id):
        return {"status": "deleted", "session_id": session_id}
    raise HTTPException(status_code=404, detail="Session not found")


# =============================================================================
# HTTP chat (non-streaming) — same session + ChatAgent logic as WebSocket /chat
# =============================================================================


class ChatHttpRequest(BaseModel):
    """Body for POST /api/v1/chat (QuizVerse site, guided learning, HTTP fallback)."""

    message: str = ""
    user_id: str | None = Field(default=None, description="Client user id (optional; echoed in logs)")
    session_id: str | None = None
    tutor_type: str | None = Field(default=None, description="Tutor persona hint (optional)")
    kb_name: str = ""
    enable_rag: bool = False
    enable_web_search: bool = False
    history: list[dict[str, str]] | None = Field(
        default=None,
        description="Optional explicit history override (same shape as WebSocket)",
    )


@router.post("/chat")
async def http_chat(body: ChatHttpRequest):
    """
    Single-turn or multi-turn chat over HTTP (non-streaming).

    Returns JSON compatible with QuizVerse ``httpChat`` / guided learning helpers:
    ``session_id``, ``content``, ``response``, ``text``.
    """
    message = body.message.strip()
    if not message:
        raise HTTPException(status_code=400, detail="Message is required")

    language = get_ui_language(default=config.get("system", {}).get("language", "en"))
    session_id = body.session_id
    kb_name = body.kb_name or ""
    enable_rag = body.enable_rag
    enable_web_search = body.enable_web_search
    explicit_history = body.history

    logger.info(
        f"HTTP chat: session={session_id}, user={body.user_id}, tutor_type={body.tutor_type}, "
        f"message={message[:50]}..., rag={enable_rag}, web={enable_web_search}"
    )

    session_manager = _get_session_manager()

    try:
        if session_id:
            session = session_manager.get_session(session_id)
            if not session:
                session = session_manager.create_session(
                    title=message[:50] + ("..." if len(message) > 50 else ""),
                    settings={
                        "kb_name": kb_name,
                        "enable_rag": enable_rag,
                        "enable_web_search": enable_web_search,
                    },
                )
                session_id = session["session_id"]
        else:
            session = session_manager.create_session(
                title=message[:50] + ("..." if len(message) > 50 else ""),
                settings={
                    "kb_name": kb_name,
                    "enable_rag": enable_rag,
                    "enable_web_search": enable_web_search,
                },
            )
            session_id = session["session_id"]

        if explicit_history is not None:
            history = explicit_history
        else:
            history = [
                {"role": msg["role"], "content": msg["content"]}
                for msg in session.get("messages", [])
            ]

        session_manager.add_message(
            session_id=session_id,
            role="user",
            content=message,
        )

        try:
            llm_config = get_llm_config()
            api_key = llm_config.api_key
            base_url = llm_config.base_url
            api_version = getattr(llm_config, "api_version", None)
        except Exception:
            api_key = None
            base_url = None
            api_version = None

        agent = ChatAgent(
            language=language,
            config=config,
            api_key=api_key,
            base_url=base_url,
            api_version=api_version,
        )

        result = await agent.process(
            message=message,
            history=history,
            kb_name=kb_name,
            enable_rag=enable_rag,
            enable_web_search=enable_web_search,
            stream=False,
        )
        full_response = result["response"]
        sources = result.get("sources", {"rag": [], "web": []})

        session_manager.add_message(
            session_id=session_id,
            role="assistant",
            content=full_response,
            sources=sources if (sources.get("rag") or sources.get("web")) else None,
        )

        # KB v2: push this turn into qv_u_<uid>_chat. Fire-and-forget — the
        # writer swallows its own errors and never blocks the response.
        # No-ops automatically when user_id is missing/invalid.
        asyncio.create_task(
            push_user_chat(
                user_id=body.user_id,
                session_id=session_id,
                user_message=message,
                assistant_response=full_response,
                language=language,
                sources=sources,
                tutor_type=body.tutor_type,
            )
        )

        logger.info(f"HTTP chat completed: session={session_id}, {len(full_response)} chars")

        return {
            "session_id": session_id,
            "content": full_response,
            "response": full_response,
            "text": full_response,
            "sources": sources,
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"HTTP chat processing error: {e}")
        raise HTTPException(status_code=500, detail=str(e)) from e


# =============================================================================
# Vision Analysis Endpoint
# =============================================================================


@router.post("/chat/vision")
async def chat_vision_analyze(request: dict):
    """
    Vision analysis endpoint for chat interface.
    Forwards to the vision solver service.
    
    Expected request format:
    {
        "question": str,              // Standard field name
        "prompt": str,                // Alternative field name (frontend uses this)
        "image": str | null,          // Frontend sends as "image"
        "image_base64": str | null,   // Alternative field name
        "image_url": str | null,
        "session_id": str | null
    }
    """
    # Frontend sends "image" but backend expects "image_base64"
    # Accept both field names for compatibility
    image_data = request.get("image") or request.get("image_base64")
    image_url = request.get("image_url")
    
    # Frontend sends "prompt" but backend expects "question"
    # Accept both field names for compatibility
    question = request.get("question") or request.get("prompt", "")
    
    try:
        # Import vision solver function
        from deeptutor.api.routers.vision_solver import analyze_image
        from deeptutor.api.routers.vision_solver import VisionAnalyzeRequest
        
        # Convert dict to VisionAnalyzeRequest model
        vision_request = VisionAnalyzeRequest(
            question=question,
            image_base64=image_data,
            image_url=image_url,
            session_id=request.get("session_id")
        )
        
        # Call the vision analyze function
        result = await analyze_image(vision_request)
        
        # Convert result to dict
        result_dict = result.model_dump() if hasattr(result, 'model_dump') else result.dict()
        
        return result_dict
        
    except Exception as e:
        logger.error(f"[VISION] Vision analysis error: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))


# =============================================================================
# WebSocket Endpoint for Chat
# =============================================================================


@router.websocket("/chat")
async def websocket_chat(websocket: WebSocket):
    from deeptutor.api.routers.auth import ws_auth_failed, ws_require_auth
    from deeptutor.multi_user.context import reset_current_user

    user_token = await ws_require_auth(websocket)
    if user_token is ws_auth_failed:
        return

    await websocket.accept()

    try:
        while True:
            data = await websocket.receive_json()
            requested_language = str(data.get("language") or "").lower().strip()
            language = (
                "zh"
                if requested_language.startswith("zh")
                else "en"
                if requested_language.startswith("en")
                else get_ui_language(default=config.get("system", {}).get("language", "en"))
            )
            message = data.get("message", "").strip()
            session_id = data.get("session_id")
            explicit_history = data.get("history")
            kb_name = data.get("kb_name", "")
            enable_rag = data.get("enable_rag", False)
            enable_web_search = data.get("enable_web_search", False)
            ws_user_id = data.get("user_id")  # Optional, used for KB v2 user push.
            ws_tutor_type = data.get("tutor_type")

            if not message:
                await websocket.send_json({"type": "error", "message": "Message is required"})
                continue

            logger.info(
                f"Chat request: session={session_id}, "
                f"message={message[:50]}..., rag={enable_rag}, web={enable_web_search}"
            )

            try:
                sm = _get_session_manager()

                if session_id:
                    session = sm.get_session(session_id)
                    if not session:
                        session = sm.create_session(
                            title=message[:50] + ("..." if len(message) > 50 else ""),
                            settings={
                                "kb_name": kb_name,
                                "enable_rag": enable_rag,
                                "enable_web_search": enable_web_search,
                            },
                        )
                        session_id = session["session_id"]
                else:
                    session = sm.create_session(
                        title=message[:50] + ("..." if len(message) > 50 else ""),
                        settings={
                            "kb_name": kb_name,
                            "enable_rag": enable_rag,
                            "enable_web_search": enable_web_search,
                        },
                    )
                    session_id = session["session_id"]

                await websocket.send_json(
                    {
                        "type": "session",
                        "session_id": session_id,
                    }
                )

                if explicit_history is not None:
                    history = explicit_history
                else:
                    history = [
                        {"role": msg["role"], "content": msg["content"]}
                        for msg in session.get("messages", [])
                    ]

                sm.add_message(
                    session_id=session_id,
                    role="user",
                    content=message,
                )

                try:
                    llm_config = get_llm_config()
                    api_key = llm_config.api_key
                    base_url = llm_config.base_url
                    api_version = getattr(llm_config, "api_version", None)
                except Exception:
                    api_key = None
                    base_url = None
                    api_version = None

                agent = ChatAgent(
                    language=language,
                    config=config,
                    api_key=api_key,
                    base_url=base_url,
                    api_version=api_version,
                )

                if enable_rag and kb_name:
                    await websocket.send_json(
                        {
                            "type": "status",
                            "stage": "rag",
                            "message": f"Searching knowledge base: {kb_name}...",
                        }
                    )

                if enable_web_search:
                    await websocket.send_json(
                        {
                            "type": "status",
                            "stage": "web",
                            "message": "Searching the web...",
                        }
                    )

                await websocket.send_json(
                    {
                        "type": "status",
                        "stage": "generating",
                        "message": "Generating response...",
                    }
                )

                full_response = ""
                sources = {"rag": [], "web": []}

                stream_generator = await agent.process(
                    message=message,
                    history=history,
                    kb_name=kb_name,
                    enable_rag=enable_rag,
                    enable_web_search=enable_web_search,
                    stream=True,
                )

                async for chunk_data in stream_generator:
                    if chunk_data["type"] == "chunk":
                        await websocket.send_json(
                            {
                                "type": "stream",
                                "content": chunk_data["content"],
                            }
                        )
                        full_response += chunk_data["content"]
                    elif chunk_data["type"] == "complete":
                        full_response = chunk_data["response"]
                        sources = chunk_data.get("sources", {"rag": [], "web": []})

                if sources.get("rag") or sources.get("web"):
                    await websocket.send_json({"type": "sources", **sources})

                await websocket.send_json(
                    {
                        "type": "result",
                        "content": full_response,
                    }
                )

                sm.add_message(
                    session_id=session_id,
                    role="assistant",
                    content=full_response,
                    sources=sources if (sources.get("rag") or sources.get("web")) else None,
                )

                # KB v2: push the completed turn into qv_u_<uid>_chat.
                # Fire-and-forget; the helper swallows errors and no-ops
                # for anonymous sessions.
                asyncio.create_task(
                    push_user_chat(
                        user_id=ws_user_id,
                        session_id=session_id,
                        user_message=message,
                        assistant_response=full_response,
                        language=language,
                        sources=sources,
                        tutor_type=ws_tutor_type,
                    )
                )

                logger.info(f"Chat completed: session={session_id}, {len(full_response)} chars")

            except Exception as e:
                logger.error(f"Chat processing error: {e}")
                await websocket.send_json({"type": "error", "message": str(e)})

    except WebSocketDisconnect:
        logger.debug("Client disconnected from chat")
    except Exception as e:
        logger.error(f"WebSocket error: {e}")
        try:
            await websocket.send_json({"type": "error", "message": str(e)})
        except Exception:
            pass
    finally:
        if user_token is not None:
            try:
                reset_current_user(user_token)
            except Exception:
                pass
