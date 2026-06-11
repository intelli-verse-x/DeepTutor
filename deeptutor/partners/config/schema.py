"""Configuration schema — Pydantic models for partner channels."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel


class Base(BaseModel):
    """Base model that accepts both camelCase and snake_case keys."""

    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)


class DeliveryOverrides(Base):
    """Per-channel delivery switches, ANDed with the partner-level flags.

    A channel only receives progress / tool-hint messages when BOTH the
    partner-level flag (ChannelsConfig) and the channel's own flag are on,
    so the partner-level switches stay coarse master switches.
    """

    send_progress: bool = Field(
        default=True,
        description="Deliver agent narration progress to this channel (ANDed with the partner-level switch).",
    )
    send_tool_hints: bool = Field(
        default=True,
        description="Deliver one-line tool-call hints to this channel (ANDed with the partner-level switch).",
    )


class StreamingSupport(Base):
    """Opt-in live streaming for channels that can edit messages in place."""

    streaming: bool = Field(
        default=False,
        description=(
            "Stream replies live by editing the message in place as text arrives. "
            "Requires send_progress: narration rounds stream as they happen."
        ),
    )


class ChannelsConfig(Base):
    """Configuration for chat channels.

    Built-in and plugin channel configs are stored as extra fields (dicts).
    Each channel parses its own config in __init__.
    """

    model_config = ConfigDict(extra="allow")

    # Both default ON so IM users see the partner's live working process
    # (per-round narration text + one-line tool calls), mirroring the web
    # chat's activity trace at IM-appropriate granularity.
    send_progress: bool = True  # stream agent narration to the channel
    send_tool_hints: bool = True  # stream tool-call hints (e.g. rag("…"))
    # Outbound delivery failures retry with exponential backoff (1s/2s/4s…).
    send_max_retries: int = 3
