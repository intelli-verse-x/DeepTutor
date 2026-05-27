---
title: Slack
description: TutorBot on Slack — Socket Mode app, thread-scoped sessions, channel and DM policies.
---

Slack is the most full-featured gateway: DMs, channel mentions, **thread-scoped sessions** (each thread becomes its own DeepTutor session), Slack-flavored markdown, file uploads, and acknowledgement reactions.

Connection is **Socket Mode** — no public IP or webhook required.

## What you need

- A Slack workspace where you can install apps (own or admin-blessed)
- 5 minutes at <https://api.slack.com/apps>

## Step 1 — Create the Slack app

1. Go to <https://api.slack.com/apps> → **Create New App** → **From scratch**
2. Name it (e.g., "Math Mentor"), pick the workspace
3. Once created, go to **Socket Mode** (left sidebar) → **Enable Socket Mode** *(toggle on)*
4. When prompted, generate an App-Level Token with `connections:write` scope and copy it — this is your **`app_token`** (starts with `xapp-`)

## Step 2 — Configure OAuth scopes

Still in your app:

1. Left sidebar → **OAuth & Permissions**
2. Under **Scopes** → **Bot Token Scopes**, add:
   - `chat:write` — send messages
   - `chat:write.public` — send to channels without joining
   - `files:write` — upload files
   - `reactions:write` — add reactions (`:eyes:` acknowledgement)
   - `users:read` — resolve user ids to names
   - `app_mentions:read` — receive @mentions
   - `im:history` — read DM history
   - `im:read` — read DM channel info
   - `channels:history` — read public channel history
   - `groups:history` — *(optional)* private channels
3. Click **Install to Workspace** → authorize
4. Copy the **Bot User OAuth Token** (starts with `xoxb-`) — this is your **`bot_token`**

## Step 3 — Subscribe to events

1. Left sidebar → **Event Subscriptions**
2. **Subscribe to bot events**:
   - `app_mention`
   - `message.im`
   - `message.channels` *(only if you want channel listening; otherwise skip)*

## Step 4 — Configure

```yaml
channels:
  slack:
    enabled: true
    mode: "socket"                  # the only mode supported
    bot_token: "xoxb-XXX..."        # from OAuth & Permissions
    app_token: "xapp-XXX..."        # from Socket Mode
    reply_in_thread: true           # keep replies in the message thread
    react_emoji: "eyes"             # reaction to acknowledge receipt
    allow_from: ["*"]               # user ids; "*" = open
    group_policy: "mention"         # in channels: only respond to mentions
    group_allow_from: []            # specific channel ids if group_policy=mention
    dm:
      enabled: true
      policy: "open"                # in DMs: always respond, or "allowlist"
      allow_from: []
```

## Step 5 — Start

```bash
deeptutor bot start my-math-tutor
```

```text
[bot:my-math-tutor] channel:slack → connecting (socket mode)
[bot:my-math-tutor] channel:slack → ready
```

In Slack, DM the bot or @mention it in a channel.

## Config reference

| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| `enabled` | bool | yes | `false` | |
| `mode` | string | yes | `"socket"` | Only `socket` is supported |
| `bot_token` | string | yes | — | `xoxb-…` |
| `app_token` | string | yes | — | `xapp-…` (Socket Mode token) |
| `reply_in_thread` | bool | optional | `true` | Reply in thread vs new message |
| `react_emoji` | string | optional | `"eyes"` | Emoji name for ack reaction |
| `allow_from` | list[string] | yes | `[]` | User ids or `"*"` |
| `group_policy` | `"mention" \| "open"` | optional | `"mention"` | In channels |
| `group_allow_from` | list[string] | optional | `[]` | Channel ids (if you want to restrict to specific channels) |
| `dm.enabled` | bool | optional | `true` | |
| `dm.policy` | `"open" \| "allowlist"` | optional | `"open"` | |
| `dm.allow_from` | list[string] | optional | `[]` | Used when `policy=allowlist` |

## Thread-scoped sessions

This is the killer Slack feature: **each Slack thread becomes its own DeepTutor session**. When you @mention the bot in a channel:

1. Bot replies, opening a new thread
2. Subsequent replies in that thread feed into the same session (with all its history, attached KB, etc.)
3. Threads in different channels are different sessions
4. DMs are their own sessions (one per user)

This means a team can have many parallel ongoing tutor conversations in one channel without context bleed.

To turn this off (force every reply to start fresh):

```yaml
channels:
  slack:
    reply_in_thread: false
    # bonus: makes the bot reply directly in the channel, not in a thread
```

## Capabilities on Slack

| Feature | Supported |
|---------|-----------|
| DMs | ✅ |
| Channel mentions | ✅ |
| Threads (session-scoped) | ✅ |
| File uploads | ✅ |
| File downloads | ✅ |
| Markdown → mrkdwn | ✅ *(auto-converted by the channel)* |
| Code blocks | ✅ |
| LaTeX math | ⚠️ rendered as code blocks (Slack doesn't render LaTeX) |
| Reactions outbound | ✅ *(via `react_emoji`)* |
| Slash commands | ⚠️ not yet — use DMs/mentions |

## Markdown to mrkdwn

Slack uses its own flavored markdown ("mrkdwn"). DeepTutor's Slack channel auto-converts:

| Standard markdown | mrkdwn output |
|-------------------|---------------|
| `**bold**` | `*bold*` |
| `*italic*` | `_italic_` |
| `# heading` | `*heading*` (bold) |
| `` `code` `` | `` `code` `` |
| ` ```code``` ` | ` ```code``` ` |
| `[link](url)` | `<url|link>` |
| `- bullet` | `• bullet` |
| `> quote` | `> quote` |

## Common issues

### Bot says hi but never responds to followups

Check `reply_in_thread`:

```yaml
reply_in_thread: true
```

If true, the bot only listens in threads it started (the `thread_ts` matches). If you DM in a non-thread message after the initial response, the bot won't see it.

### "Not authorized" / 401 from Slack API

Token mismatch — make sure you put `xoxb-` token in `bot_token` and `xapp-` token in `app_token`. Easy to swap by accident.

### Bot doesn't respond in channels

Two requirements:
1. The bot must be **invited to the channel** (`/invite @bot`)
2. Your message must @mention the bot (`@math-mentor what is...`) if `group_policy: mention`

### Long messages get truncated

Slack messages cap at 40,000 chars (much longer than Telegram/Discord). DeepTutor doesn't split — but extremely long responses (e.g., 50+ page Deep Research outputs) should be sent as files instead.

## Keep-alive specifics

Socket Mode opens a single WebSocket to Slack. The channel:
- Sends pings every 30 seconds
- Auto-reconnects on drop, with backoff
- No external supervision needed

## See also

- [**Discord**](/docs/tutorbot/discord/) — similar developer-portal model
- [**Explore TutorBot**](/docs/tutorbot/) — overall architecture
