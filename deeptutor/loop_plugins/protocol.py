"""Protocol shared by the chat loop and loop plugins."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Protocol

from deeptutor.core.context import UnifiedContext


@dataclass(frozen=True, slots=True)
class PromptBlock:
    """One named prompt fragment contributed to the loop system prompt."""

    name: str
    content: str


class LoopPlugin(Protocol):
    """Optional per-turn extension point for the chat agent loop."""

    name: str

    def is_active(self, context: UnifiedContext) -> bool:
        """Whether this plugin participates in the current turn."""

    def tool_types(self, context: UnifiedContext) -> tuple[str, ...]:
        """Tool names this plugin auto-mounts for the current turn."""

    def system_block(
        self,
        context: UnifiedContext,
        *,
        language: str,
        prompts: dict[str, Any],
    ) -> PromptBlock | None:
        """Optional system prompt block contributed by the plugin."""

    def augment_kwargs(
        self,
        tool_name: str,
        kwargs: dict[str, Any],
        context: UnifiedContext,
    ) -> dict[str, Any]:
        """Inject server-owned private kwargs for plugin tools."""

    def pre_loop_seed(self, context: UnifiedContext) -> str:
        """Optional text appended to the initial user message seed."""


__all__ = ["LoopPlugin", "PromptBlock"]
