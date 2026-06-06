---
title: Zulip
description: TutorBot on Zulip — stream + topic addressing, KaTeX math rendering, since v1.3.9.
---

Zulip was added in **v1.3.9** (2026-05-09). It uses Zulip's event-queue long-polling and supports Zulip's distinctive **stream + topic** addressing.

## What you need

- A Zulip server (any version — Zulip Cloud or self-hosted)
- Admin access to create bots in your organization

## Step 1 — Create a bot

1. In Zulip, click the ⚙️ icon (top right) → **Organization** → **Bots & integrations**
2. Click **Add a new bot**
3. Bot type: **Generic bot**
4. Name: "Math Mentor"
5. Bot email: auto-generated, e.g., `math-mentor-bot@your-zulip.example.com`
6. Click **Create bot**
7. **Download API key** or **Show API key** and copy

## Step 2 — Subscribe the bot to streams

By default, generic bots can be sent direct messages but won't see public streams unless you subscribe them. In the bot's settings: **Streams subscribed** → add the streams you want the bot to watch.

You can also do this from the config (the `subscribe_streams` field).

## Step 3 — Configure

```yaml
channels:
  zulip:
    enabled: true
    site: "https://your-zulip.example.com"
    email: "math-mentor-bot@your-zulip.example.com"
    api_key: "YOUR_API_KEY"
    allow_from: ["*"]
    group_policy: "mention"        # mention vs open in subscribed streams
    subscribe_streams:
      - "study-help"
      - "homework"
    timeout: 60.0                  # event queue poll timeout, seconds
```

## Step 4 — Start

```bash
deeptutor bot start my-math-tutor
```

```text
[bot:my-math-tutor] channel:zulip → register event queue
[bot:my-math-tutor] channel:zulip → subscribed: [study-help, homework]
[bot:my-math-tutor] channel:zulip → ready (queue_id=q_abc)
```

## Config reference

| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| `enabled` | bool | yes | `false` | |
| `site` | url | yes | — | Your Zulip server |
| `email` | string | yes | — | Bot email from Zulip |
| `api_key` | string | yes | — | From bot creation page |
| `allow_from` | list[string] | optional | `[]` | User ids or emails; `["*"]` open |
| `group_policy` | `"mention" \| "open"` | optional | `"mention"` | In streams |
| `subscribe_streams` | list[string] | optional | `[]` | Streams to auto-subscribe |
| `timeout` | float | optional | `60.0` | Event-queue poll timeout (seconds) |

## Stream + topic addressing (Zulip-specific)

Zulip splits messages into **streams** (like channels) and **topics** (subjects within a stream). DeepTutor scopes sessions to **(stream, topic)** pairs:

- A new topic = a new DeepTutor session
- Same topic across days = same session, persistent memory
- Different topics in the same stream = different sessions

This is great for classroom use: each homework problem can have its own topic, the bot tracks each independently.

## Capabilities on Zulip

| Feature | Supported |
|---------|-----------|
| Direct messages | ✅ |
| Stream messages + topics | ✅ *(topic-scoped sessions)* |
| Markdown | ✅ |
| **LaTeX / KaTeX math** | ✅ *(Zulip renders `$$...$$` natively)* |
| File uploads/downloads | ✅ |
| Mention or open mode | ✅ |
| Reactions | ⚠️ outbound only |

## Keep-alive specifics

Zulip's **event-queue API** is a long-poll with auto-recovery:

- The bot calls `/api/v1/events?queue_id=...` with `timeout=60s`
- New events come back as JSON; empty response after timeout
- If `queue_id` expires (server restarts, idle too long), the bot auto-registers a new one

A background thread runs the listener and bridges events to DeepTutor's async bus. The thread runs until the bot is stopped.

## Common issues

### "Bad event queue id"

The queue expired (server restart or > 10 min idle). The channel auto-recovers — no action needed. If it keeps happening, your Zulip server might be unhealthy.

### Bot doesn't see stream messages

Did you subscribe it? Either via the Zulip UI (bot settings → Streams) or via the `subscribe_streams` config.

### Math doesn't render

The bot has to output math in Zulip's expected format:

```text
Inline: $x^2$

Display:
```math
\int_0^\infty e^{-x^2} dx = \frac{\sqrt{\pi}}{2}
```
```

DeepTutor's Zulip channel auto-converts standard `$...$` and `$$...$$` to Zulip's format.

## See also

- [**Explore TutorBot**](/docs/tutorbot/) — overall architecture
- [Zulip Bot API docs](https://zulip.com/api/) — reference
