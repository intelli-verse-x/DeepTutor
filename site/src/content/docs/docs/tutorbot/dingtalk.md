---
title: DingTalk (钉钉)
description: TutorBot on DingTalk — Alibaba's enterprise chat, Stream Mode connection.
---

DingTalk (钉钉) is Alibaba's enterprise messaging product. DeepTutor uses the official `dingtalk-stream` SDK in **Stream Mode** — no public webhook needed.

## What you need

- A DingTalk organization with admin access
- Access to the [**DingTalk Open Platform**](https://open.dingtalk.com/)

## Step 1 — Create an app

1. Sign in to <https://open.dingtalk.com/>
2. **App Development** → **Create Application**
3. Pick **Internal Robot** (机器人) type
4. Fill in name, description, icon
5. Once created, copy **AppKey (Client ID)** and **AppSecret (Client Secret)** from the Credentials page

## Step 2 — Enable Stream Mode

1. In the app settings → **Stream Mode** → **Enable**
2. This avoids needing a public webhook URL

## Step 3 — Permissions

Request these scopes:
- Send messages
- Read message content
- (Optional) Voice-to-text for transcription

## Step 4 — Configure

```yaml
channels:
  dingtalk:
    enabled: true
    client_id: "dingxxxxxxxxxxxxxxxx"
    client_secret: "YOUR_CLIENT_SECRET"
    allow_from: []
```

## Step 5 — Start

```bash
deeptutor bot start my-math-tutor
```

```text
[bot:my-math-tutor] channel:dingtalk → connecting (stream mode)
[bot:my-math-tutor] channel:dingtalk → ready
```

## Config reference

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| `enabled` | bool | yes | |
| `client_id` | string | yes | AppKey from DingTalk |
| `client_secret` | string | yes | AppSecret |
| `allow_from` | list[string] | optional | DingTalk user ids |

## Capabilities on DingTalk

| Feature | Supported |
|---------|-----------|
| DMs | ✅ |
| Group chats | ✅ |
| Markdown / rich text | ✅ |
| Action cards (interactive buttons) | ✅ |
| File uploads | ✅ |
| **Voice → text transcription** | ✅ *(built into DingTalk's speech-to-text)* |
| Mention routing | ✅ |

## Keep-alive specifics

The dingtalk-stream SDK manages the long-poll callback connection. On disconnect, it auto-reconnects.

## Common issues

### "Invalid client_secret"

Check DingTalk Open Platform → your app → Credentials. The secret can be rotated.

### Bot is "online" but doesn't respond

Confirm the bot is installed for the target users / departments. In DingTalk, robots have to be explicitly added to an organization before they can chat.

### Stream mode not connecting

Stream Mode requires the bot to be released (not just in draft). Click **Release** in the DingTalk app page.

## See also

- [**Feishu**](/docs/tutorbot/feishu/) — China's other major enterprise chat
- [**WeCom**](/docs/tutorbot/wecom/) — Tencent's enterprise messenger
