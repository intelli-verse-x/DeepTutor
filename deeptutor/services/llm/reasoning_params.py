"""Reasoning/thinking parameters for OpenAI-compatible provider calls."""

from __future__ import annotations

from typing import Any

_THINKING_STYLE_MAP = {
    "thinking_type": lambda enabled: {"thinking": {"type": "enabled" if enabled else "disabled"}},
    "enable_thinking": lambda enabled: {"enable_thinking": enabled},
    "reasoning_split": lambda enabled: {"reasoning_split": enabled},
}
_PROVIDER_THINKING_STYLES = {
    "deepseek": "thinking_type",
    "volcengine": "thinking_type",
    "volcengine_coding_plan": "thinking_type",
    "byteplus": "thinking_type",
    "byteplus_coding_plan": "thinking_type",
    "dashscope": "enable_thinking",
    "minimax": "reasoning_split",
}
_PROVIDER_REASONING_PATTERNS = {
    "deepseek": ("deepseek-v4-pro", "deepseek-reasoner"),
    "dashscope": ("qwen3", "qwen-3", "qwq", "qwen-plus"),
}
_CUSTOM_MODEL_THINKING_STYLES: tuple[tuple[tuple[str, ...], str], ...] = (
    (("qwen3", "qwen-3", "qwq", "qwen-plus"), "enable_thinking"),
    (("deepseek-v4-pro", "deepseek-reasoner"), "thinking_type"),
)
_THINKING_DISABLED_BY_DEFAULT: tuple[tuple[str, str], ...] = (("deepseek", "deepseek-v4-flash"),)


def _spec_name(spec: Any, binding: str | None) -> str:
    return str(getattr(spec, "name", None) or binding or "").strip().lower()


def _matches(model_name: str, patterns: tuple[str, ...]) -> bool:
    model_lower = model_name.lower()
    return any(pattern.lower() in model_lower for pattern in patterns)


def _custom_thinking_style(model_name: str) -> tuple[str, tuple[str, ...]]:
    for patterns, style in _CUSTOM_MODEL_THINKING_STYLES:
        if _matches(model_name, patterns):
            return style, patterns
    return "", ()


def _disable_thinking_by_default(provider_name: str, model_name: str) -> bool:
    normalized = model_name.strip().lower()
    return any(
        provider_name == provider and pattern in normalized
        for provider, pattern in _THINKING_DISABLED_BY_DEFAULT
    )


def build_openai_compatible_reasoning_kwargs(
    *,
    spec: Any,
    binding: str | None,
    model: str | None,
    reasoning_effort: str | None,
) -> dict[str, Any]:
    """Return reasoning kwargs for OpenAI-compatible Chat Completions calls.

    Some OpenAI-compatible providers expose thinking controls through
    ``extra_body`` instead of the top-level ``reasoning_effort`` field.  Direct
    ``custom`` bindings need model-family inference because their endpoint is
    user supplied and therefore cannot be identified by provider name alone.
    """
    provider_name = _spec_name(spec, binding)
    model_name = model or ""
    thinking_style = str(getattr(spec, "thinking_style", "") or "")
    patterns = tuple(getattr(spec, "reasoning_model_patterns", ()) or ())

    if not thinking_style:
        thinking_style = _PROVIDER_THINKING_STYLES.get(provider_name, "")
    if not patterns:
        patterns = _PROVIDER_REASONING_PATTERNS.get(provider_name, ())
    if provider_name == "custom":
        custom_style, custom_patterns = _custom_thinking_style(model_name)
        if custom_style:
            thinking_style = custom_style
            patterns = custom_patterns

    resolved_effort = reasoning_effort
    if resolved_effort is None and patterns and _matches(model_name, patterns):
        resolved_effort = "high"

    semantic_effort: str | None = None
    if isinstance(resolved_effort, str):
        semantic_effort = resolved_effort.lower()
        if semantic_effort == "minimum":
            semantic_effort = "minimal"

    kwargs: dict[str, Any] = {}
    if resolved_effort:
        suppress_top_level = bool(
            thinking_style and (semantic_effort == "minimal" or thinking_style == "enable_thinking")
        )
        if not suppress_top_level:
            kwargs["reasoning_effort"] = resolved_effort

    if thinking_style and resolved_effort is not None:
        thinking_enabled = semantic_effort != "minimal"
        extra = _THINKING_STYLE_MAP.get(thinking_style, lambda _enabled: None)(thinking_enabled)
        if extra:
            kwargs.setdefault("extra_body", {}).update(extra)
    elif thinking_style and _disable_thinking_by_default(provider_name, model_name):
        extra = _THINKING_STYLE_MAP.get(thinking_style, lambda _enabled: None)(False)
        if extra:
            kwargs.setdefault("extra_body", {}).update(extra)

    return kwargs


__all__ = ["build_openai_compatible_reasoning_kwargs"]
