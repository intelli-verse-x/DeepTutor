"""Backend registry — the single place that knows which subagents exist.

Add a new local agent CLI by writing a :class:`SubagentBackend` and listing it
here; the capability, API and UI all discover it through these helpers.
"""

from __future__ import annotations

import asyncio

from deeptutor.services.subagent.base import SubagentBackend
from deeptutor.services.subagent.claude_code import ClaudeCodeBackend
from deeptutor.services.subagent.codex import CodexBackend
from deeptutor.services.subagent.types import DetectResult

_BACKENDS: dict[str, SubagentBackend] = {
    backend.kind: backend
    for backend in (ClaudeCodeBackend(), CodexBackend())
}


def list_backend_kinds() -> list[str]:
    return list(_BACKENDS.keys())


def get_backend(kind: str) -> SubagentBackend | None:
    return _BACKENDS.get(str(kind or "").strip())


async def detect_all() -> list[DetectResult]:
    """Probe every backend for installability on this machine, concurrently."""
    results = await asyncio.gather(
        *(backend.detect() for backend in _BACKENDS.values()),
        return_exceptions=True,
    )
    detections: list[DetectResult] = []
    for backend, result in zip(_BACKENDS.values(), results, strict=True):
        if isinstance(result, DetectResult):
            detections.append(result)
        else:
            detections.append(
                DetectResult(
                    kind=backend.kind,
                    display_name=backend.display_name,
                    available=False,
                    detail=str(result),
                )
            )
    return detections


__all__ = ["list_backend_kinds", "get_backend", "detect_all"]
