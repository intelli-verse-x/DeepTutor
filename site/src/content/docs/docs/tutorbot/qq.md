---
title: QQ
description: TutorBot on QQ — Tencent's consumer messenger, via the official botpy SDK.
---

QQ is Tencent's flagship consumer messenger. DeepTutor uses Tencent's official **botpy** SDK over a WebSocket connection.

## What you need

- A [**QQ Bot Development Platform**](https://bot.q.qq.com/) account
- Tencent Cloud account (for some advanced features)

## Step 1 — Register a QQ bot

1. Sign in to <https://bot.q.qq.com/>
2. **Create New Bot** → fill in name and description
3. Copy **App ID** and **Secret**
4. Enable the message types you need: C2C (direct messages) and group messages

## Step 2 — Configure

```yaml
channels:
  qq:
    enabled: true
    app_id: "YOUR_APP_ID"
    secret: "YOUR_SECRET"
    allow_from: []
    msg_format: "plain"      # or "markdown"
```

## Step 3 — Start

```bash
deeptutor bot start my-math-tutor
```

## Config reference

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| `enabled` | bool | yes | |
| `app_id` | string | yes | From bot platform |
| `secret` | string | yes | From bot platform |
| `allow_from` | list[string] | optional | QQ user ids |
| `msg_format` | `"plain" \| "markdown"` | optional | Reply formatting style |

## Capabilities on QQ

| Feature | Supported |
|---------|-----------|
| C2C (direct) messages | ✅ |
| Group messages | ✅ |
| Markdown | ✅ *(if `msg_format: "markdown"`)* |
| File / image attachments | ✅ |
| Image generation in replies | ✅ |
| Mention routing | ✅ |

## Common issues

### Duplicate message handling

QQ's gateway occasionally redelivers messages. The channel keeps a deque of the last 1000 message ids and silently drops duplicates. If you see duplicates, the deque may have wrapped — restart the bot.

### "Auth failed" on connect

Wrong `app_id` / `secret`, or your bot wasn't approved for the requested message types. Check the QQ Bot platform.

### Markdown not rendering

QQ's markdown rendering varies by client version. Some clients render `**bold**`, others want `<b>bold</b>`. If users complain, try setting `msg_format: "plain"`.

## See also

- [**Explore TutorBot**](/docs/tutorbot/) — overall architecture
