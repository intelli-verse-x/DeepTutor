"""Turn-scoped chat loop plugins.

Each plugin lives in its own subpackage under :mod:`deeptutor.loop_plugins`.
The chat loop imports only the generic registry/protocol from this package;
feature-specific prompts, tools, and kwargs injection stay inside each plugin
subpackage.
"""

from deeptutor.loop_plugins.protocol import LoopPlugin, PromptBlock
from deeptutor.loop_plugins.registry import LOOP_PLUGINS, active_loop_plugins

__all__ = ["LOOP_PLUGINS", "LoopPlugin", "PromptBlock", "active_loop_plugins"]
