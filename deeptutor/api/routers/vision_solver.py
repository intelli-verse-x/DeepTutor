"""Vision Solver API Router.

WebSocket endpoint for real-time image analysis with GeoGebra visualization.
"""

import asyncio
from typing import Any

from fastapi import APIRouter, HTTPException, WebSocket, WebSocketDisconnect
from pydantic import BaseModel, Field, field_validator

from deeptutor.agents.vision_solver import VisionSolverAgent
from deeptutor.logging import get_logger
from deeptutor.services.llm import get_llm_config, get_vision_llm_config
from deeptutor.services.settings.interface_settings import get_ui_language
from deeptutor.tools.vision import ImageError, resolve_image_input
from deeptutor.utils.image_validator import validate_image_for_api

logger = get_logger("VisionSolverAPI", level="INFO")

router = APIRouter()


# ==================== Request/Response Models ====================


class VisionAnalyzeRequest(BaseModel):
    """Request for image analysis."""

    question: str = Field(..., min_length=1, max_length=5000, description="Question about the image")
    image_base64: str | None = Field(None, description="Base64 encoded image")
    image_url: str | None = Field(None, description="URL to image")
    session_id: str | None = Field(None, description="Optional session identifier")
    
    @field_validator('question')
    @classmethod
    def validate_question(cls, v: str) -> str:
        """Validate question is not empty."""
        if not v or not v.strip():
            raise ValueError("Question cannot be empty")
        return v.strip()



class VisionAnalyzeResponse(BaseModel):
    """Response from image analysis."""

    session_id: str
    has_image: bool
    answer: str | None = None  # Direct answer to the question
    explanation: str | None = None  # Detailed explanation
    extracted_text: str | None = None  # Text extracted from image


# ==================== REST Endpoints ====================


@router.post("/vision/analyze")
async def analyze_image(request: VisionAnalyzeRequest) -> VisionAnalyzeResponse:
    """Analyze a math problem image and return answer with explanation.

    Args:
        request: Analysis request with question and image

    Returns:
        Analysis response with answer and explanation
        
    Raises:
        HTTPException: On validation or processing errors
    """
    session_id = request.session_id or f"vision_{id(request)}"

    try:
        # Resolve image input with timeout (download URL or use base64)
        try:
            image_base64 = await asyncio.wait_for(
                resolve_image_input(
                    image_base64=request.image_base64,
                    image_url=request.image_url,
                ),
                timeout=30.0  # 30 second timeout for image download
            )
        except asyncio.TimeoutError:
            logger.error(f"[{session_id}] Image download timeout")
            raise HTTPException(
                status_code=408,
                detail="Image download timeout. Please try again or use base64 encoding."
            )
        except ImageError as e:
            logger.error(f"[{session_id}] Image resolution error: {e}")
            raise HTTPException(status_code=400, detail=str(e))
        
        # Validate image after resolving
        if image_base64:
            try:
                validation_result = validate_image_for_api(
                    image_base64=image_base64,
                    max_size_mb=10.0,
                )
                logger.info(
                    f"[{session_id}] Image validated: {validation_result['format']}, "
                    f"{validation_result['width']}x{validation_result['height']}px, "
                    f"{validation_result['size_mb']:.2f}MB"
                )
            except Exception as e:
                logger.error(f"[{session_id}] Image validation failed: {e}")
                raise HTTPException(
                    status_code=400,
                    detail=f"Image validation failed: {str(e)}"
                )

        if not image_base64:
            return VisionAnalyzeResponse(
                session_id=session_id,
                has_image=False,
            )

        # Get vision-specific LLM config (falls back to regular config if not set)
        try:
            vision_config = get_vision_llm_config()
            api_key = vision_config.api_key
            base_url = vision_config.base_url
            model = vision_config.model
            # Sanitize API key in logs
            masked_key = f"{api_key[:8]}...{api_key[-4:]}" if api_key and len(api_key) > 12 else "***"
            logger.info(f"Using vision model: {model} from {base_url} (key: {masked_key})")
        except Exception as e:
            logger.error(f"Failed to get vision LLM config: {e}")
            raise HTTPException(status_code=500, detail="Vision service configuration error")

        # Initialize agent with vision model
        language = get_ui_language(default="en")
        agent = VisionSolverAgent(
            api_key=api_key,
            base_url=base_url,
            model=model,
            vision_model=model,
            language=language,
        )

        # Process with timeout (simple answer mode only)
        try:
            result = await asyncio.wait_for(
                agent.answer_question(
                    question_text=request.question,
                    image_base64=image_base64,
                ),
                timeout=60.0  # 1 minute timeout
            )
            result["session_id"] = session_id
        except asyncio.TimeoutError:
            logger.error(f"[{session_id}] Vision analysis timeout")
            raise HTTPException(
                status_code=504,
                detail="Analysis took too long. Please try with a simpler question or smaller image."
            )
        
        return VisionAnalyzeResponse(
            session_id=session_id,
            has_image=result.get("has_image", False),
            answer=result.get("answer"),
            explanation=result.get("explanation"),
            extracted_text=result.get("extracted_text"),
        )

    except HTTPException:
        raise
    except ImageError as e:
        logger.error(f"Image error: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"[{session_id}] Analysis failed: {e}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail="Analysis failed. Please check your image and try again."
        )


# ==================== WebSocket Endpoint ====================


@router.websocket("/vision/solve")
async def websocket_vision_solve(websocket: WebSocket):
    """WebSocket endpoint for streaming image analysis.

    Protocol:
    1. Client sends: {"question": "...", "image_base64": "...", "session_id": "..."}
    2. Server streams:
       - {"type": "session", "session_id": "..."}
       - {"type": "analysis_start", "data": {...}}
       - {"type": "bbox_complete", "data": {...}}
       - {"type": "analysis_complete", "data": {...}}
       - {"type": "ggbscript_complete", "data": {...}}
       - {"type": "reflection_complete", "data": {...}}
       - {"type": "analysis_message_complete", "data": {...}}
       - {"type": "answer_start", "data": {...}}
       - {"type": "text", "content": "..."}
       - {"type": "done"}
    """
    await websocket.accept()

    connection_closed = asyncio.Event()

    async def safe_send_json(data: dict[str, Any]) -> bool:
        """Safely send JSON, checking if connection is closed."""
        if connection_closed.is_set():
            return False
        try:
            await websocket.send_json(data)
            return True
        except (WebSocketDisconnect, RuntimeError, ConnectionError) as e:
            logger.debug(f"WebSocket connection closed: {e}")
            connection_closed.set()
            return False
        except Exception as e:
            logger.debug(f"Error sending WebSocket message: {e}")
            return False

    session_id = None

    try:
        # 1. Receive initial message
        data = await websocket.receive_json()
        question = data.get("question")
        image_base64 = data.get("image_base64")
        image_url = data.get("image_url")
        mode = data.get("mode", "answer")  # Default to answer mode
        session_id = data.get("session_id", f"vision_{id(data)}")

        if not question:
            await safe_send_json({"type": "error", "content": "Question is required"})
            return

        # Send session ID
        await safe_send_json({"type": "session", "session_id": session_id})

        # 2. Resolve and validate image input
        try:
            resolved_image = await asyncio.wait_for(
                resolve_image_input(
                    image_base64=image_base64,
                    image_url=image_url,
                ),
                timeout=30.0  # 30 second timeout for image download
            )
            
            # Validate image if resolved
            if resolved_image:
                try:
                    validation_result = validate_image_for_api(
                        image_base64=resolved_image,
                        max_size_mb=10.0,
                    )
                    logger.info(
                        f"[{session_id}] Image validated: {validation_result['format']}, "
                        f"{validation_result['width']}x{validation_result['height']}px, "
                        f"{validation_result['size_mb']}MB"
                    )
                except Exception as e:
                    logger.error(f"[{session_id}] Image validation failed: {e}")
                    await safe_send_json({
                        "type": "error",
                        "content": f"Image validation failed: {str(e)}"
                    })
                    return
                    
        except asyncio.TimeoutError:
            await safe_send_json({
                "type": "error",
                "content": "Image download timeout. Please try again or use base64 encoding."
            })
            return
        except ImageError as e:
            await safe_send_json({"type": "error", "content": str(e)})
            return

        if not resolved_image:
            await safe_send_json({"type": "no_image", "data": {}})
            await safe_send_json({"type": "done"})
            return

        # 3. Initialize agent with vision-specific config
        try:
            vision_config = get_vision_llm_config()
            api_key = vision_config.api_key
            base_url = vision_config.base_url
            model = vision_config.model
            logger.info(f"[{session_id}] Using vision model: {model} from {base_url}")
        except Exception as e:
            logger.error(f"Failed to get vision LLM config: {e}")
            await safe_send_json({"type": "error", "content": f"Vision LLM configuration error: {e}"})
            return

        language = get_ui_language(default="en")
        agent = VisionSolverAgent(
            api_key=api_key,
            base_url=base_url,
            model=model,
            vision_model=model,
            language=language,
        )

        logger.info(f"[{session_id}] Starting vision analysis (mode={mode}): {question[:50]}...")

        # 4. Stream analysis based on mode
        if mode == "geometry":
            # Full geometry analysis with GeoGebra (original mode)
            async for event in agent.stream_process_with_tutor(
                question_text=question,
                image_base64=resolved_image,
                session_id=session_id,
            ):
                event_type = event.get("event", "unknown")
                event_data = event.get("data", {})

                if not await safe_send_json({"type": event_type, "data": event_data}):
                    break
        else:
            # Simple question answering mode
            await safe_send_json({"type": "analysis_start", "data": {"mode": "answer"}})
            
            result = await agent.answer_question(
                question_text=question,
                image_base64=resolved_image,
            )
            
            await safe_send_json({"type": "answer_complete", "data": result})

        logger.info(f"[{session_id}] Vision analysis and tutor response completed")

    except WebSocketDisconnect:
        logger.info(f"[{session_id}] WebSocket disconnected")
    except Exception as e:
        connection_closed.set()
        await safe_send_json({"type": "error", "content": str(e)})
        logger.error(f"[{session_id}] Vision solve failed: {e}", exc_info=True)
    finally:
        connection_closed.set()
        try:
            if hasattr(websocket, "client_state"):
                state = websocket.client_state
                if hasattr(state, "name") and state.name != "DISCONNECTED":
                    await websocket.close()
            else:
                await websocket.close()
        except (WebSocketDisconnect, RuntimeError, ConnectionError):
            pass
        except Exception as e:
            logger.debug(f"Error closing WebSocket: {e}")
