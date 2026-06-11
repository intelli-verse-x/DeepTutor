---
title: Channel Matrix
description: All built-in Partner channels, their connection model, required fields, and when to use each one.
---

Partner channels are delivery adapters around the same Partner brain. They do not create a second agent runtime: an inbound IM event becomes a scoped chat turn, and the reply is delivered back through the channel.

Use the web UI for most configuration: **Partners -> your partner -> Channels** renders the live schema from `/api/v1/partners/channels/schema`, masks secret fields, and lets you reload channels without rewriting YAML by hand.

## Built-in channels

| Channel | Key | Connection model | Best for | Required core fields |
| --- | --- | --- | --- | --- |
| WeChat | `weixin` | HTTP long-poll + QR login | Personal WeChat assistant | `allow_from`; optional `token`, `state_dir`, `route_tag`, `poll_timeout` |
| WeCom | `wecom` | WeCom AI Bot WebSocket | Enterprise WeChat / WeChat Work | `bot_id`, `secret`, `allow_from` |
| QQ | `qq` | Tencent botpy WebSocket | Official QQ bot deployments | `app_id`, `secret`, `allow_from`, `msg_format` |
| QQ (NapCat) | `napcat` | OneBot v11 WebSocket | Personal QQ via NapCat | `ws_url`, optional `access_token`, `allow_from`, `group_policy` |
| Telegram | `telegram` | Bot API polling | Simple personal or group bot | `token`, `allow_from` |
| Discord | `discord` | Gateway WebSocket | Discord servers and DMs | `token`, `allow_from`, group policy fields |
| Slack | `slack` | Socket Mode | Slack teams, DMs, threaded channel help | `bot_token`, `app_token`, `allow_from`, `group_policy` |
| Feishu / Lark | `feishu` | Lark SDK WebSocket | Feishu/Lark enterprise chat | `app_id`, `app_secret`, verification/encryption fields where used |
| DingTalk | `dingtalk` | Stream Mode | DingTalk enterprise chat | app credentials, `allow_from`, group policy fields |
| Matrix | `matrix` | Matrix sync loop | Decentralized rooms, optional E2EE setup | `homeserver`, user credentials or `access_token`, `allow_from`, `group_policy` |
| Zulip | `zulip` | Event queue | Stream + topic workflows | `email`, `api_key`, `site`, `allow_from`, `group_policy` |
| WhatsApp | `whatsapp` | Bridge WebSocket | WhatsApp via a bridge runtime | bridge URL/token, `allow_from` |
| Email | `email` | IMAP poll + SMTP send | Async email tutoring/helpdesk | IMAP host/user/password, SMTP host/user/password, `allow_from` |
| Mochat | `mochat` | Socket.IO or HTTP polling | Customer-service style chat panel | `base_url` / socket URL, `claw_token`, `allow_from` |
| Microsoft Teams | `msteams` | Built-in HTTP webhook listener | Teams DM-first Bot Framework integration | `app_id`, `app_password`, `tenant_id`, host/port/path |

## Shared delivery switches

Most channels inherit the same delivery controls:

| Field | Meaning |
| --- | --- |
| `enabled` | Whether the Partner should start this channel. |
| `send_progress` | Deliver narration/progress updates during long turns. |
| `send_tool_hints` | Deliver one-line tool-call hints. Useful while debugging, noisy in production. |
| `streaming` | Telegram, Discord, and Feishu only: stream the reply live by editing the message in place as text arrives (Feishu uses CardKit streaming cards). Requires `send_progress`. Off by default. |
| `allow_from` | User/chat allowlist. `*` is convenient for tests; explicit ids are safer for deployment. |

## Configuration workflow

1. Create and test the Partner in the web UI before enabling any IM channel.
2. Enable only one channel first.
3. Keep `send_progress` and `send_tool_hints` on while debugging.
4. Start with `allow_from: ["*"]` only in local/private tests.
5. Send a short message, inspect logs, then replace `*` with real sender ids.
6. Add more channels only after the first channel is stable.

## Choosing a channel

- Use **WeChat** for personal WeChat. It requires a human QR-code scan and persisted state.
- Use **WeCom**, **Feishu**, **DingTalk**, **Slack**, or **Teams** for enterprise/team deployments.
- Use **QQ** for official Tencent bot accounts; use **NapCat** only when you intentionally operate a personal QQ bridge.
- Use **Email** when asynchronous replies are acceptable and users prefer inbox workflows.
- Use **Matrix** or **Zulip** when room/topic structure matters more than consumer IM convenience.

## Where state lives

Channel runtime state is stored below the Partner runtime directory, for example:

```text
data/partners/<partner_id>/runtime/weixin/account.json
data/partners/<partner_id>/runtime/msteams/msteams_conversations.json
```

Persist the whole `data/partners/` tree in Docker or production hosts. Losing runtime state can force new QR scans or conversation-reference collection.

## Detailed pages

- [WeChat](/docs/partners/weixin/) — personal WeChat QR login and long-poll setup
- [WeCom](/docs/partners/wecom/) — Enterprise WeChat AI Bot setup
- [QQ / NapCat](/docs/partners/qq/) — official QQ bot and personal QQ bridge paths
