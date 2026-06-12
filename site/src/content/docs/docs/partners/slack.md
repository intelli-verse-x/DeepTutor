---
title: Slack
description: Configure the Slack channel for a Partner — Socket Mode app, bot and app tokens, thread replies, and DM policy.
---

<img src="/channel-icons/slack.svg" alt="" width="40" height="40" />

The `slack` channel connects a Partner to a Slack workspace over **Socket Mode**: the bot opens a WebSocket to Slack through `slack-sdk`, so no public URL, webhook, or reverse proxy is needed. It is the most team-oriented channel — DMs, channel @mentions, threaded replies, and an acknowledgement reaction on the triggering message.

Two tokens are involved and they are easy to mix up: the **Bot Token** (`xoxb-…`, from OAuth & Permissions) authorizes API calls, and the **App Token** (`xapp-…`, from Socket Mode) authorizes the WebSocket connection. Unlike Telegram and Discord, the Slack card has no **Streaming** switch — replies arrive as complete messages, with narration delivered as separate messages when **Send Progress** is on.

![Slack channel configuration](/screenshots/partners-channel-slack.png)

## Install requirements

Slack support ships with the Partners extra, which already includes `slack-sdk` (Socket Mode client) and `slackify-markdown` (Markdown -> Slack mrkdwn conversion). Nothing extra to install.

```bash
pip install -e ".[partners]"
# or, from an installed release when partners extras are available:
pip install "deeptutor[partners]"
```

## Create the Slack app

1. Go to <https://api.slack.com/apps> -> **Create New App** -> **From scratch**. Name it and pick your workspace.
2. Left sidebar -> **Socket Mode** -> toggle **Enable Socket Mode**. When prompted, generate an App-Level Token with the `connections:write` scope and copy it — this is your **App Token** (`xapp-…`).
3. Left sidebar -> **OAuth & Permissions** -> **Scopes** -> **Bot Token Scopes**, add: `chat:write`, `chat:write.public`, `files:write`, `reactions:write`, `users:read`, `app_mentions:read`, `im:history`, `im:read`, `channels:history` (and `groups:history` if you want private channels).
4. Left sidebar -> **Event Subscriptions** -> **Subscribe to bot events**: `app_mention`, `message.im`, and `message.channels` if the bot should listen in channels beyond @mentions.
5. Back in **OAuth & Permissions**, click **Install to Workspace** and authorize. Copy the **Bot User OAuth Token** (`xoxb-…`) — this is your **Bot Token**.

## Configure the channel card

Open **Partners -> your partner -> Channels -> Slack**.

| Field | What to enter |
| --- | --- |
| **Send Progress** | Keep on while testing. It delivers narration updates during long turns. |
| **Send Tool Hints** | Keep on for debugging; turn off if users should not see one-line tool calls. |
| **Enabled** | Turn on only when you are ready to start the channel. |
| **Mode** | `socket` is the only supported mode. Leave it unchanged. |
| **Webhook Path** | Reserved for a future webhook mode; unused while **Mode** is `socket`. Leave the default `/slack/events`. |
| **Bot Token** | The `xoxb-…` token from **OAuth & Permissions**. Stored as a secret and masked after save. |
| **App Token** | The `xapp-…` App-Level Token from **Socket Mode** (needs `connections:write`). Also a secret. Do not swap it with the Bot Token. |
| **User Token Read Only** | Keep the default (on). |
| **Reply In Thread** | On (default): the bot answers in a thread under the triggering message and keeps following that thread. Off: replies go straight into the channel. |
| **React Emoji** | Emoji name (no colons) the bot adds to your message as a receipt acknowledgement. Default `eyes`. |
| **Allow From** | One value per line. Use `*` for an open test bot, or Slack user ids (`U…`). Empty denies everyone. |
| **Group Policy** | `mention` (default): in channels the bot only answers @mentions. `open`: it answers every message in channels it is in. `allowlist`: only channels listed in **Group Allow From**. |
| **Group Allow From** | Channel ids (`C…`), one per line. Used when **Group Policy** is `allowlist`. |
| **Dm** | DM sub-policy: **Enabled** toggles DMs as a whole; **Policy** `open` answers any DM, `allowlist` restricts DMs to the ids in its own **Allow From** list. |

## After you save

1. Click **Save**, then turn **Enabled** on.
2. Start the partner (or restart it / use the reload action on the Channels panel if it is already running).
3. From an allowed account, DM the bot, or `/invite @your-bot` into a channel and @mention it.
4. Watch the partner logs: you should see the Socket Mode connection and the inbound event.
5. Once you have confirmed the sender id in the logs, replace `*` in **Allow From** with real ids.

## Verify it is healthy

- The logs show the Socket Mode WebSocket connected with no auth errors.
- Your test message gets the acknowledgement reaction (`eyes` by default) within a second or two.
- The reply arrives in a thread under your message (with the default **Reply In Thread** on).

## Troubleshooting

### `invalid_auth` / `not_authed` from the Slack API

The two tokens are swapped — `xoxb-…` belongs in **Bot Token** and `xapp-…` in **App Token**. This is the single most common Slack setup mistake.

### The socket never connects

Socket Mode must be **enabled** on the app, and the App-Level Token must carry the `connections:write` scope. If you generated the token before enabling Socket Mode, generate a fresh one.

### The bot ignores channel messages, but DMs work

Three gates to check:

1. The bot must be invited to the channel: `/invite @your-bot`.
2. With **Group Policy** = `mention`, your message must @mention the bot.
3. The `app_mention` (and `message.channels`, if you rely on it) bot events must be subscribed under **Event Subscriptions**.

### Replies land in a thread and follow-ups get ignored

That is **Reply In Thread** at work: the bot starts a thread and listens inside it. Continue the conversation in the thread, not with a new top-level channel message. If you prefer flat channel replies, turn **Reply In Thread** off.

## See also

- [Channel Matrix](/docs/partners/channels/) — all channels at a glance
- [Discord](/docs/partners/discord/) — similar developer-portal setup over a Gateway WebSocket
