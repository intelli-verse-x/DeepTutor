"""Built-in loop plugin registry."""

from __future__ import annotations

from deeptutor.core.context import UnifiedContext
from deeptutor.loop_plugins.mastery import MasteryLoopPlugin
from deeptutor.loop_plugins.protocol import LoopPlugin

LOOP_PLUGINS: tuple[LoopPlugin, ...] = (MasteryLoopPlugin(),)


def active_loop_plugins(context: UnifiedContext) -> tuple[LoopPlugin, ...]:
    """Return active plugins for this turn in stable registry order."""
    return tuple(plugin for plugin in LOOP_PLUGINS if plugin.is_active(context))


__all__ = ["LOOP_PLUGINS", "active_loop_plugins"]
