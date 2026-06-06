---
title: Discord
description: TutorBot on Discord — Developer Portal registration, Gateway WebSocket connection, group policies.
---

Discord uses a **Gateway WebSocket** rather than polling. DeepTutor implements the gateway protocol directly (no `discord.py` dependency), with automatic reconnect on disconnect.

## What you need

- A Discord account
- A server you control (for testing the bot)
- 5 minutes on the Discord Developer Portal

## Step 1 — Create a Discord Application

1. Open <https://discord.com/developers/applications>
2. Click **New Application**
3. Give it a name (e.g., "Math Mentor")
4. Save

## Step 2 — Create a Bot user

1. In the left sidebar of your application: **Bot**
2. Click **Add Bot** → confirm
3. Under **TOKEN**, click **Reset Token**, then **Copy** — this is your `token`
4. Under **Privileged Gateway Intents**, enable:
   - **Message Content Intent** *(required to read message text)*
   - **Server Members Intent** *(recommended)*

## Step 3 — Invite the bot to your server

1. Left sidebar → **OAuth2** → **URL Generator**
2. Scopes: check `bot`
3. Bot Permissions: check `Send Messages`, `Read Message History`, `Attach Files`, `Embed Links`, `Add Reactions`
4. Copy the generated URL, open it in a new tab, pick a server, **Authorize**

## Step 4 — Configure

Edit `data/tutorbot/<bot_id>/agents.yaml`:

```yaml
channels:
  discord:
    enabled: true
    token: "YOUR_BOT_TOKEN"
    allow_from:
      - "USER_ID_1"           # right-click user in Discord → Copy User ID (Dev Mode required)
      # - "*"                 # open
    group_policy: "mention"   # or "open"
    intents: 37377            # default — covers messages + guilds
```

> **Dev Mode for User IDs:** In Discord settings → **Advanced** → enable **Developer Mode**. Then right-click any user → Copy User ID.

## Step 5 — Start

```bash
deeptutor bot start my-math-tutor
```

```text
[bot:my-math-tutor] channel:discord → connecting (gateway wss://...)
[bot:my-math-tutor] channel:discord → ready (heartbeat 41250ms)
```

## Config reference

| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| `enabled` | bool | yes | `false` | |
| `token` | string | yes | — | Bot token from the Developer Portal |
| `allow_from` | list[string] | yes | `[]` | User ids or `"*"` |
| `group_policy` | `"mention" \| "open"` | optional | `"mention"` | Group chat behavior |
| `gateway_url` | string | optional | `wss://gateway.discord.gg/?v=10&encoding=json` | Override only if you proxy |
| `intents` | int | optional | `37377` | Bitfield; default covers messages + guilds + members |

## Capabilities on Discord

| Feature | Supported |
|---------|-----------|
| DMs | ✅ |
| Guild text channels | ✅ |
| Threads | ⚠️ partial — bot replies in the parent channel for now |
| File uploads | ✅ *(up to 20 MB)* |
| File downloads | ✅ |
| Markdown / mention rendering | ✅ *(Discord's flavored markdown)* |
| Typing indicator | ✅ |
| Reactions | ⚠️ only outbound (bot adds reactions, doesn't respond to user reactions) |

## Group policy

| Policy | Behavior |
|--------|----------|
| `mention` | Bot only replies to messages that @mention it |
| `open` | Bot replies to every message in the channel *(loud — only for dedicated bot channels)* |

In DMs, the bot always responds regardless of policy.

## Keep-alive specifics

DeepTutor's Discord channel maintains the gateway WebSocket with a **heartbeat every ~41 seconds** (per Discord's protocol). On disconnect:

- Auto-reconnect after 5 seconds
- Session resume attempted first (no rejoining channels)
- Falls back to full reconnect if resume fails

You shouldn't need any external supervision — the channel manager handles all reconnection.

## Common issues

### `4014: Disallowed intent`

You requested an intent in the config that you didn't enable in the Developer Portal. Most common: Message Content Intent.

Fix: Developer Portal → your app → **Bot** → enable **Message Content Intent**.

### Bot is online but doesn't respond

Check `allow_from`. The same rule as Telegram: empty list denies everyone.

Also confirm Message Content Intent is enabled — without it, the bot sees messages with empty `content`.

### Messages > 2000 chars get cut off

Discord's per-message limit is 2000 chars. The bot auto-splits longer responses. For Deep Research outputs, consider sending the long response as a file:

```yaml
channels:
  discord:
    send_long_as_file: true   # attach .md when response > 2000 chars
```

### 429 rate limits

Discord rate-limits per channel. If your bot sends many messages quickly (e.g., a chatty `open` policy in a busy channel), you'll see 429s. The channel auto-retries with backoff but consider switching to `mention`.

## See also

- [**Telegram**](/docs/tutorbot/telegram/) — simpler gateway model for comparison
- [**Slack**](/docs/tutorbot/slack/) — also socket-mode, similar setup feel
