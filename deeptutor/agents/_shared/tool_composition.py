"""Per-turn tool composition policy shared by chat / quiz pipelines.

Owns the rule "given the user's composer toggles + the turn's context
flags, what tools should be enabled?". Lives outside any single pipeline
so chat and quiz can't disagree about which tools the user controls vs.
which the pipeline auto-mounts.

Two pieces:

* :data:`AUTO_MOUNTED_TOOLS` — tools whose mounting is owned by the
  pipeline (auto-on under specific conditions), not by user toggles.
  Membership here hides the tool from the user's composer / settings UI.
* :func:`compose_enabled_tools` — pure function that takes the user's
  toggled list + a :class:`ToolMountFlags` and returns the final, ordered
  enabled-tool list for one turn.

Callers resolve their own flags (chat checks selected KBs / source index
/ memory / notebooks; quiz reuses chat's policy verbatim).
"""

from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass
from typing import Any

from deeptutor.tools.builtin import BUILTIN_TOOL_NAMES, USER_TOGGLEABLE_TOOL_NAMES

# Tools whose mounting is owned by the pipeline (auto-on under specific
# context conditions), not by the user's composer toggles. Adding a tool
# here hides it from ``{tool_list}`` until its corresponding condition
# fires in :func:`compose_enabled_tools`.
AUTO_MOUNTED_TOOLS: frozenset[str] = frozenset(
    {
        "rag",
        "read_source",
        "read_memory",
        "write_memory",
        "read_skill",
        "load_tools",
        "exec",
        "code_execution",
        "list_notebook",
        "write_note",
        "ask_user",
        "web_fetch",
        "github",
        "cron",
    }
)

# Conditional auto-mounts: tool name -> the ``ToolMountFlags`` attribute that
# gates it. Single source of truth shared by the default composition (mount
# when the flag is set) and the authoritative capability path (a capability's
# declared built-in is dropped when its gate is unmet — e.g. ``rag`` without a KB).
# Insertion order fixes the default surface's conditional-tool order.
_CONDITIONAL_MOUNT_FLAGS: dict[str, str] = {
    "rag": "has_kb",
    "read_source": "has_sources",
    "read_memory": "has_memory",
    "list_notebook": "has_notebooks",
    "write_note": "has_notebooks",
    "read_skill": "has_skills",
    "load_tools": "has_deferred_tools",
    "exec": "has_exec",
    "code_execution": "has_code",
}


def default_optional_tools(excluded: Iterable[str] = ()) -> list[str]:
    """Return the user-toggleable tool list (chat's default set).

    Sourced from :mod:`deeptutor.tools.builtin` so the /settings/tools UI
    and the pipelines can never disagree about which tools the user
    actually controls.
    """
    excluded_set = frozenset(excluded)
    return [
        name
        for name in USER_TOGGLEABLE_TOOL_NAMES
        if name in BUILTIN_TOOL_NAMES
        and name not in excluded_set
        and name not in AUTO_MOUNTED_TOOLS
    ]


@dataclass(frozen=True)
class ToolMountFlags:
    """Per-turn flags that drive the auto-mount policy.

    Each capability resolves these from its own context (chat inspects
    ``UnifiedContext.knowledge_bases``, the source index, the memory
    service, the notebook manager; quiz reuses the same checks).
    """

    has_kb: bool = False
    has_sources: bool = False
    has_memory: bool = False
    has_notebooks: bool = False
    has_skills: bool = False
    has_deferred_tools: bool = False
    has_exec: bool = False
    has_code: bool = False


def compose_enabled_tools(
    *,
    registry: Any,
    requested_tools: list[str] | None,
    optional_whitelist: list[str],
    mount_flags: ToolMountFlags,
    capability_owned: Iterable[str] = (),
    exclusive: bool = False,
) -> list[str]:
    """Compose the per-turn enabled-tool list.

    Order:

    1. User-toggled tools (filtered through ``get_enabled`` so unknown tools
       never sneak in, intersected with ``optional_whitelist`` so only
       legitimate composer toggles are respected).
    2. Conditional auto-mounts (:data:`_CONDITIONAL_MOUNT_FLAGS`: ``rag`` if a
       KB is attached, ``read_source`` if a source index exists, …).
    3. Active loop capabilities' *owned* tools (``capability_owned``) — the
       capability's own tools, added on top.
    4. Always-on auto-mounts (``write_memory`` / ``web_fetch`` / ``github`` /
       ``ask_user`` / ``cron``).

    A loop capability (solve, mastery) reuses the *full* chat surface and only
    *adds* its owned tools — it never curates or suppresses the reused
    built-ins, so a capability turn respects the user's composer toggles
    exactly as a chat turn does.

    ``exclusive=True`` flips that for the *knowledge* category (an active
    :class:`~deeptutor.capabilities.protocol.KnowledgeCapability`): the turn
    runs only on ``capability_owned`` plus the ``ask_user`` floor — no built-ins,
    no composer toggles, no conditional mounts. The capability owns the surface.

    The result is ordered and deduplicated. ``optional_whitelist`` is still
    expected to exclude ``AUTO_MOUNTED_TOOLS`` via :func:`default_optional_tools`.
    """
    if exclusive:
        owned = [str(name) for name in capability_owned if str(name).strip()]
        return _ordered_unique([*owned, "ask_user"])

    composed: list[str] = [
        tool.name
        for tool in registry.get_enabled(requested_tools or [])
        if tool.name in optional_whitelist
    ]
    for tool_name, flag in _CONDITIONAL_MOUNT_FLAGS.items():
        if getattr(mount_flags, flag):
            composed.append(tool_name)
    composed.extend(str(name) for name in capability_owned if str(name).strip())
    composed.append("write_memory")
    composed.append("web_fetch")
    composed.append("github")
    composed.append("ask_user")
    composed.append("cron")
    return _ordered_unique(composed)


def _ordered_unique(names: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for name in names:
        if name in seen:
            continue
        seen.add(name)
        result.append(name)
    return result


def user_has_memory() -> bool:
    """Whether the active user has any L3 memory content.

    Drives the auto-mount of ``read_memory``. Per-user paths resolve via
    the multi-user ContextVars the runtime sets up. Fails closed (returns
    ``False``) on any error so a broken memory directory doesn't surface
    a tool with no payload to read.
    """
    try:
        from deeptutor.services.memory import get_memory_store

        store = get_memory_store()
        return any(
            store.read_raw("L3", slot).strip()
            for slot in ("recent", "profile", "scope", "preferences")
        )
    except Exception:
        return False


def user_has_notebooks() -> bool:
    """Whether the active user has at least one notebook.

    Auto-mount gate for ``list_notebook`` + ``write_note``. Same
    fail-closed posture as :func:`user_has_memory`.
    """
    try:
        from deeptutor.services.notebook import get_notebook_manager

        notebooks = get_notebook_manager().list_notebooks()
        return isinstance(notebooks, list) and any(
            nb for nb in notebooks if str(nb.get("id") or "").strip()
        )
    except Exception:
        return False


__all__ = [
    "AUTO_MOUNTED_TOOLS",
    "ToolMountFlags",
    "compose_enabled_tools",
    "default_optional_tools",
    "user_has_memory",
    "user_has_notebooks",
]
