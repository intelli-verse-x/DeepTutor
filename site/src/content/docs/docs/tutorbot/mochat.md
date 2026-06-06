---
title: Mochat
description: TutorBot on Mochat — customer-support style chat panel with Socket.IO or HTTP polling.
---

[Mochat](https://github.com/microsoft/mochat) is an open-source customer-support / chat panel. DeepTutor's Mochat channel connects via **Socket.IO** (preferred) or **HTTP polling** as a fallback. Useful when you want a tutor bot embedded in your existing website's support widget.

## What you need

- A running Mochat instance (self-hosted or managed)
- A bot account with an access token (Claw Token)

## Step 1 — Create a bot in Mochat

1. Sign in to your Mochat admin panel
2. **Bots** → **Create**
3. Copy the bot's **Claw Token**

## Step 2 — Configure

```yaml
channels:
  mochat:
    enabled: true
    service_url: "https://mochat.example.com"
    claw_token: "YOUR_BOT_TOKEN"
    allow_from: []                    # user ids; [] = open
    use_http_polling: false           # fallback if Socket.IO unavailable
    polling_interval_ms: 1000
    delayed_message_timeout_s: 5
```

## Step 3 — Start

```bash
deeptutor bot start my-math-tutor
```

```text
[bot:my-math-tutor] channel:mochat → connecting (socket.io to mochat.example.com)
[bot:my-math-tutor] channel:mochat → ready
```

## Config reference

| Field | Type | Required | Default |
|-------|------|----------|---------|
| `enabled` | bool | yes | `false` |
| `service_url` | url | yes | — |
| `claw_token` | string | yes | — |
| `allow_from` | list[string] | optional | `[]` (open) |
| `use_http_polling` | bool | optional | `false` |
| `polling_interval_ms` | int | optional | `1000` |
| `delayed_message_timeout_s` | int | optional | `5` |

## Capabilities on Mochat

| Feature | Supported |
|---------|-----------|
| Customer chat panel messaging | ✅ |
| Group / room messaging | ✅ |
| Markdown | ✅ |
| File uploads | ✅ |
| Delayed message batching | ✅ *(for efficiency on fast user input)* |

## Delayed message batching

Mochat users often type messages in bursts (e.g., "Hi!\nQuick question.\nIs the bot online?"). To avoid generating one bot reply per fragment, the channel **batches messages** received within `delayed_message_timeout_s` (default 5s):

- First message arrives → start a timer
- More messages within timeout → append, restart timer
- Timer expires → bundle all messages into one user turn

Adjust `delayed_message_timeout_s` based on how chatty your users are.

## Keep-alive specifics

The Socket.IO connection auto-reconnects on drop. If Socket.IO repeatedly fails, the channel falls back to HTTP polling:

```yaml
use_http_polling: true
polling_interval_ms: 2000     # poll every 2 seconds
```

This trades latency for robustness — useful behind picky corporate proxies.

## Common issues

### "Cannot connect" but Mochat is up

Mochat sometimes requires the bot to be **approved** in the admin panel before its token is active. Check the bot status.

### Replies arrive but users don't see them

Mochat has channel-level visibility settings. Ensure the bot is added to the channels where users are chatting.

### Socket.IO version mismatch

If your Mochat is on an older Socket.IO version, force HTTP polling instead of debugging the version mismatch — `use_http_polling: true`.

## See also

- [**Explore TutorBot**](/docs/tutorbot/) — overall architecture
