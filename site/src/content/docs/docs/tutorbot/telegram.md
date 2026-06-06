---
title: Telegram
description: Run a TutorBot on Telegram — registration via BotFather, config keys, and operational notes.
---

Telegram is the easiest gateway to wire up — there's no public IP requirement, no webhook signing, and the BotFather registration takes about a minute.

## What you need

- A Telegram account
- A chat with [@BotFather](https://t.me/BotFather)

That's it. No business verification, no developer console signup.

## Step 1 — Register a bot with BotFather

Open Telegram, search for `@BotFather`, start a chat. Then:

```text
You> /newbot

BotFather> Alright, a new bot. How are we going to call it?
          Please choose a name for your bot.

You> Math Mentor

BotFather> Good. Now let's choose a username for your bot.
          It must end in 'bot'. Like this, for example: TetrisBot.

You> hku_math_mentor_bot

BotFather> Done! Congratulations on your new bot.
          You will find it at t.me/hku_math_mentor_bot.

          Use this token to access the HTTP API:
          123456789:ABC-DEF1234ghIkl-zyx57W2v1u123ew11
```

**Copy that token.** You'll paste it into `agents.yaml` in a moment.

## Step 2 — Find your Telegram user id

You need your own user id to put in `allow_from` (otherwise the bot won't respond to anyone). The simplest way: chat with [@userinfobot](https://t.me/userinfobot), which replies with your id.

```text
You> hi

userinfobot> Id: 123456789
             First: Frank
             Last:
             Username: @frank
             Language: zh
```

## Step 3 — Configure your bot

Edit `data/tutorbot/<bot_id>/agents.yaml`:

```yaml
agent:
  id: my-math-tutor
  name: Math Mentor
  persona: "Socratic math tutor specializing in calculus and linear algebra."
  model: gpt-4o

channels:
  telegram:
    enabled: true
    token: "123456789:ABC-DEF1234ghIkl-zyx57W2v1u123ew11"
    allow_from:
      - "123456789"       # your Telegram user id
      # - "*"             # uncomment to open the bot to everyone (careful)
```

## Step 4 — Start the bot

```bash
deeptutor bot start my-math-tutor
```

```text
[bot:my-math-tutor] starting...
[bot:my-math-tutor] channel:telegram → connecting
[bot:my-math-tutor] channel:telegram → ok (long-polling)
[bot:my-math-tutor] running.
```

Now open Telegram, search for `@hku_math_mentor_bot`, send `/start` — and you're talking to the bot.

## Config reference

| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| `enabled` | bool | yes | `false` | Start the channel |
| `token` | string | yes | — | HTTP API token from BotFather |
| `allow_from` | list[string] | yes | `[]` *(denies all)* | User ids or `"*"` for open |

## Capabilities on Telegram

| Feature | Supported |
|---------|-----------|
| Direct messages | ✅ |
| Group chats | ✅ *(bot must be added to the group + group_policy applies)* |
| Markdown rendering | ✅ *(via Telegram's markdown_v2 parser)* |
| LaTeX math | ⚠️ rendered as plain text — Telegram doesn't render `$...$` |
| File uploads | ✅ *(up to Telegram's 20 MB / 2 GB limit)* |
| File downloads | ✅ *(the bot can receive PDFs, images, voice messages)* |
| Audio transcription | ✅ *(if `transcription_api_key` is configured globally)* |
| Reply-in-thread | ⚠️ partial — Telegram has reply-to-message, not threads |

## Groups

To use the bot in a Telegram group:

1. Add the bot to the group (Add Member → search for `@your_bot`)
2. Disable **Group Privacy** in BotFather: `/mybots` → select bot → **Bot Settings** → **Group Privacy** → **Turn OFF**
3. Mention the bot to address it (`@hku_math_mentor_bot question?`)

Set `group_policy` in the config:

```yaml
channels:
  telegram:
    group_policy: "mention"   # only respond when @mentioned
    # group_policy: "open"    # respond to every message (chatty!)
```

## Keep-alive specifics

The Telegram connection uses **long polling** by default — the bot pulls updates from Telegram's servers in a long-lived loop. This is robust to network blips:

- A network drop just makes the next `getUpdates` call fail
- The channel retries with exponential backoff
- When connectivity returns, polling resumes

You don't need a public IP, webhook, or reverse proxy. Telegram's BotFather doesn't require any URL configuration on your end.

## Common issues

### Bot doesn't respond to my messages

99% of the time it's `allow_from`:

```yaml
allow_from:
  - "123456789"   # your actual id, in quotes (it's a string field)
```

Empty `allow_from: []` means "deny everyone" — even you. Use `["*"]` to allow all.

### Bot doesn't respond in groups

Two things to check:

1. BotFather → `/mybots` → your bot → Group Privacy → **Disabled**
2. In config: `group_policy: "mention"` (set) and you actually `@mentioned` the bot in your message

### "Conflict: terminated by other getUpdates request"

You started the same bot in two places at once (e.g., `deeptutor bot start` twice, or two DeepTutor instances). Telegram allows only one polling client per token. Stop the duplicate.

### Messages > 4096 chars get cut off

Telegram messages are capped at 4096 chars. The bot auto-splits longer messages into multiple sends. For very long responses (e.g., Deep Research reports), prefer sending a file:

```yaml
channels:
  telegram:
    send_long_as_file: true   # auto-attach .md when response > 4096 chars
```

## Audio messages

If you've set `TRANSCRIPTION_API_KEY` (and a transcription provider like Groq Whisper) in `.env`, the bot transcribes voice messages and treats them like text input. Otherwise voice messages are ignored.

## Files and images

When a user uploads a file or image:

- **Image** → Sent to the model as a vision input
- **PDF / DOCX** → Parsed and treated as an attachment (full text available via `read_source` tool)
- **Other** → Acknowledged but ignored

## Multi-tenant deployments

In multi-user mode, each user can have their own Telegram bot. Bot ids are scoped per user, so `alice` and `bob` can each have a `my-tutor` without collision.

For organization-wide bots (one bot shared by many users), keep the bot under the admin account but configure `allow_from` to a long list, or use `["*"]` with care.

## See also

- [**Explore TutorBot**](/docs/tutorbot/) — architecture and lifecycle
- [**CLI → bot commands**](/docs/cli/commands/#deeptutor-bot--tutorbot-lifecycle)
