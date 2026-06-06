---
title: Feishu / Lark
description: TutorBot on Feishu (国内) / Lark (international) — WebSocket long-connection via lark-oapi SDK.
---

Feishu (飞书) is the most popular workplace chat in mainland China; Lark is its international counterpart. They share the same API. DeepTutor supports both via the official `lark-oapi` SDK over a long-lived WebSocket.

## What you need

- A Feishu / Lark developer account
- Access to the [**Feishu Open Platform**](https://open.feishu.cn/) (mainland) or [**Lark Open Platform**](https://open.larksuite.com/) (international)
- Optionally: a Feishu/Lark organization where you can install the bot

## Step 1 — Create an app

1. Open the relevant platform → **Create App** → **Custom App**
2. Fill in basic info (name, description, icon)
3. Once created, copy these from the **Credentials & Basic Info** page:
   - **App ID**
   - **App Secret**
   - **Verification Token**
   - **Encrypt Key**

## Step 2 — Enable bot capability

1. Left sidebar → **Features** → **Bot** → **Enable**
2. Configure the bot's display name and avatar

## Step 3 — Configure event subscription

1. Left sidebar → **Event Subscriptions** → **Subscribe to events**
2. Add events you care about:
   - `im.message.receive_v1` — receive direct messages
   - `im.message.message_read_v1` — track read receipts (optional)
3. **Enable Long Connection Mode** so you don't need a public webhook URL. This makes the bot use WebSocket instead of webhooks.

## Step 4 — Add permissions

Left sidebar → **Permissions & Scopes**:

- `im:message:send_as_bot` — send messages
- `im:resource` — read media attachments
- `contact:user.id:readonly` — resolve user ids

Then **Release** the version *(internal release for internal apps)*.

## Step 5 — Configure DeepTutor

```yaml
channels:
  feishu:
    enabled: true
    app_id: "cli_xxxxxxxxxxxxxxxx"
    app_secret: "YOUR_APP_SECRET"
    verification_token: "YOUR_VERIFICATION_TOKEN"
    encrypt_key: "YOUR_ENCRYPT_KEY"
    allow_from: []
    group_policy: "mention"
```

## Step 6 — Start

```bash
deeptutor bot start my-math-tutor
```

```text
[bot:my-math-tutor] channel:feishu → connecting (long-connection)
[bot:my-math-tutor] channel:feishu → ready (app_id=cli_xxx)
```

## Config reference

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| `enabled` | bool | yes | |
| `app_id` | string | yes | `cli_...` |
| `app_secret` | string | yes | |
| `verification_token` | string | yes | Used for event signature verification |
| `encrypt_key` | string | yes | Used to decrypt incoming events |
| `allow_from` | list[string] | optional | User ids; `["*"]` open |
| `group_policy` | `"mention" \| "open"` | optional | Default `"mention"` |

## Capabilities on Feishu

| Feature | Supported |
|---------|-----------|
| DMs | ✅ |
| Group chats | ✅ |
| **Interactive cards** | ✅ *(rich Feishu card messages with buttons)* |
| Markdown | ✅ |
| File / image uploads / downloads | ✅ |
| Audio transcription | ✅ *(if `transcription_api_key` set)* |
| Reactions | ⚠️ outbound only |
| Mention routing | ✅ |

## Long-connection vs webhook mode

Feishu supports two delivery modes:

| Mode | Pros | Cons |
|------|------|------|
| **Long connection** *(recommended)* | No public IP needed; works from anywhere | One DeepTutor instance per app |
| Webhook | Multiple endpoints possible; standard request/response | Needs a publicly reachable URL with HTTPS |

DeepTutor uses long connection by default. To switch to webhooks (if you have load-balancing needs), you'd run a separate webhook receiver — not currently supported in stock DeepTutor.

## Keep-alive specifics

The lark-oapi SDK manages the WebSocket with auto-reconnect. A background thread runs the WebSocket listener and forwards events to DeepTutor's async bus.

If the bot disappears from Feishu (status shows offline):

```bash
deeptutor bot stop my-math-tutor
deeptutor bot start my-math-tutor
```

For persistent uptime, use systemd or Docker `restart: unless-stopped`.

## Common issues

### "Invalid app_secret" on startup

Double-check **App Secret** in Feishu's Credentials page — it can rotate. Also confirm you're on the right platform (`open.feishu.cn` for mainland, `open.larksuite.com` for international — secrets aren't transferable).

### Bot says it's online but no messages received

Two checks:

1. **Permissions** — `im:message:send_as_bot` and event subscriptions are added AND **released** (new version)
2. **Long connection mode** is enabled in Event Subscriptions

### Verification token mismatch

If you regenerated the verification token in Feishu, update the config and restart the bot. The token is signed into every incoming event for integrity.

### Encrypt key mismatch

Same as above — if you regenerated the encrypt key in Feishu (Settings → Event Subscriptions), update config + restart.

## See also

- [**WeCom**](/docs/tutorbot/wecom/) — Tencent's enterprise chat platform, similar registration UX
- [**DingTalk**](/docs/tutorbot/dingtalk/) — Alibaba's equivalent in enterprise chat
