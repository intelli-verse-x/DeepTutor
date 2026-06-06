#!/usr/bin/env python
"""
Thin mimic entrypoint.

The orchestration now lives in deeptutor/agents/question/coordinator.py.
"""

from __future__ import annotations

import asyncio
import os
from pathlib import Path
from typing import Any, Callable

from deeptutor.agents.question import AgentCoordinator
from deeptutor.services.kb import (
    normalize_exam_slug,
    push_exam_paper_questions,
)
from deeptutor.services.llm.config import get_llm_config

WsCallback = Callable[[str, dict[str, Any]], Any]


async def mimic_exam_questions(
    pdf_path: str | None = None,
    paper_dir: str | None = None,
    kb_name: str | None = None,
    output_dir: str | None = None,
    max_questions: int | None = None,
    ws_callback: WsCallback | None = None,
) -> dict[str, Any]:
    """
    Backward utility wrapper that delegates to the new coordinator pipeline.
    """
    if not pdf_path and not paper_dir:
        return {"success": False, "error": "Either pdf_path or paper_dir must be provided."}
    if pdf_path and paper_dir:
        return {"success": False, "error": "pdf_path and paper_dir cannot be used together."}

    llm_config = get_llm_config()
    coordinator = AgentCoordinator(
        api_key=llm_config.api_key,
        base_url=llm_config.base_url,
        api_version=getattr(llm_config, "api_version", None),
        kb_name=kb_name,
        output_dir=output_dir,
    )

    if ws_callback:

        async def _forward(data: dict[str, Any]) -> None:
            event_type = data.get("type", "progress")
            await ws_callback(event_type, data)

        coordinator.set_ws_callback(_forward)

    if pdf_path:
        summary = await coordinator.generate_from_exam(
            exam_paper_path=pdf_path,
            max_questions=max_questions or 10,
            paper_mode="upload",
        )
    else:
        summary = await coordinator.generate_from_exam(
            exam_paper_path=paper_dir or "",
            max_questions=max_questions or 10,
            paper_mode="parsed",
        )

    generated_questions = [r.get("qa_pair", {}) for r in summary.get("results", [])]

    # KB v2: live-append the freshly generated paper into KB_EXAM so it
    # becomes immediately searchable via /api/v1/kb/search { kb:'exam' }.
    # We only push when:
    #   • the run actually produced something (success flag true OR at
    #     least one question was generated),
    #   • we can derive a valid exam_slug from kb_name (or env override),
    #   • the writer's secret is configured (it no-ops cleanly otherwise).
    # Fire-and-forget; never blocks the caller, never raises.
    try:
        if generated_questions:
            slug_source = kb_name or os.environ.get("QV_KB_DEFAULT_EXAM_SLUG", "")
            exam_slug = normalize_exam_slug(slug_source)
            if exam_slug:
                batch_dir = summary.get("batch_dir") or ""
                batch_id = Path(batch_dir).name if batch_dir else "adhoc"
                paper_title = (
                    Path(pdf_path).stem
                    if pdf_path
                    else (Path(paper_dir).name if paper_dir else None)
                )
                asyncio.create_task(
                    push_exam_paper_questions(
                        exam_slug=exam_slug,
                        batch_id=batch_id,
                        qa_pairs=generated_questions,
                        paper_title=paper_title,
                    )
                )
    except Exception:
        # Never let a KB-side issue (event loop edge case, logger
        # misuse, etc.) break paper generation. Mirrors the same guard
        # philosophy as user_kb_writer.
        pass

    return {
        "success": bool(summary.get("success", False)),
        "summary": summary,
        "generated_questions": generated_questions,
        "failed_questions": [r for r in summary.get("results", []) if not r.get("success")],
        "total_reference_questions": summary.get("template_count", 0),
    }
