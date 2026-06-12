---
title: Partners & Channels
description: Operator guide for DeepTutor Partners, channel configuration, workspace layout, and IM delivery behavior.
---

Partners are persistent DeepTutor companions that can live in the web UI and in external IM apps. They are not a second bot engine. Every incoming message becomes a normal chat-agent turn scoped to that Partner:

```text
IM / Web message -> PartnerRunner -> ChatOrchestrator -> AgenticChatPipeline -> tools -> reply
```

## What changed from TutorBot

| Old TutorBot | New Partner |
| --- | --- |
| Separate bot engine and `data/tutorbot/<id>/` workspace | Same Chat loop, scoped workspace under `data/partners/<id>/workspace/` |
| Bot-specific CLI commands such as `deeptutor bot ...` | `deeptutor partner list/create/start/stop` |
| Channels edited in bot YAML | Schema-driven channel cards in the Partners UI |
| Bot skills / memory handled separately | Assigned KBs, skills, notebooks, tools, and memory are mounted like normal chat context |

Old `/docs/tutorbot/*` links are retained as short migration notices so external links do not hard 404.

## Recommended setup flow

1. Create the Partner in **Partners -> New partner**.
2. Fill **Identity** and **Soul** before enabling any channel. The first IM reply uses this soul.
3. In **Mind**, pick a model and keep optional tools minimal while testing.
4. In **Library**, assign one small KB or skill first. Assets are copied into the Partner workspace.
5. In **Channels**, enable exactly one channel and start with a private/local test.
6. Keep `send_progress` and `send_tool_hints` on during debugging, then quiet them down for production.
7. Replace `allow_from: ["*"]` with explicit sender ids before opening a channel to real users.

![Partner detail](/screenshots/partners-detail.png)

## Channel entry points

| Channel | Use when | Page |
| --- | --- | --- |
| <img src="/channel-icons/weixin.svg" alt="" width="16" height="16" /> WeChat (`weixin`) | Personal WeChat via QR-code login and HTTP long-poll | [WeChat](/docs/partners/weixin/) |
| <img src="/channel-icons/wecom.svg" alt="" width="16" height="16" /> WeCom (`wecom`) | Enterprise WeChat / WeChat Work AI Bot platform | [WeCom](/docs/partners/wecom/) |
| <img src="/channel-icons/qq.svg" alt="" width="16" height="16" /> QQ (`qq`) | Official Tencent QQ bot account via botpy | [QQ / NapCat](/docs/partners/qq/) |
| <img src="/channel-icons/napcat.svg" alt="" width="16" height="16" /> NapCat (`napcat`) | Personal QQ account through OneBot v11 / NapCat | [QQ / NapCat](/docs/partners/qq/) |
| <img src="/channel-icons/telegram.svg" alt="" width="16" height="16" /> Telegram (`telegram`) | Fastest setup — BotFather token, no public IP | [Telegram](/docs/partners/telegram/) |
| <img src="/channel-icons/discord.svg" alt="" width="16" height="16" /> Discord (`discord`) | Discord servers and DMs via Gateway WebSocket | [Discord](/docs/partners/discord/) |
| <img src="/channel-icons/slack.svg" alt="" width="16" height="16" /> Slack (`slack`) | Slack teams over Socket Mode, threaded replies | [Slack](/docs/partners/slack/) |
| <img src="/channel-icons/feishu.svg" alt="" width="16" height="16" /> Feishu (`feishu`) | Feishu / Lark with CardKit streaming cards | [Feishu](/docs/partners/feishu/) |
| <img src="/channel-icons/dingtalk.svg" alt="" width="16" height="16" /> DingTalk (`dingtalk`) | DingTalk enterprise bot over Stream Mode | [DingTalk](/docs/partners/dingtalk/) |
| <img src="/channel-icons/matrix.svg" alt="" width="16" height="16" /> Matrix (`matrix`) | Decentralized rooms, optional E2EE | [Matrix](/docs/partners/matrix/) |
| <img src="/channel-icons/zulip.svg" alt="" width="16" height="16" /> Zulip (`zulip`) | Stream + topic structured team chat | [Zulip](/docs/partners/zulip/) |
| <img src="/channel-icons/whatsapp.svg" alt="" width="16" height="16" /> WhatsApp (`whatsapp`) | WhatsApp through a bridge runtime | [WhatsApp](/docs/partners/whatsapp/) |
| <img src="/channel-icons/email.svg" alt="" width="16" height="16" /> Email (`email`) | Async inbox workflows over IMAP/SMTP | [Email](/docs/partners/email/) |
| <img src="/channel-icons/mochat.svg" alt="" width="16" height="16" /> Mochat (`mochat`) | Customer-service style chat panels | [Mochat](/docs/partners/mochat/) |
| <img src="/channel-icons/msteams.svg" alt="" width="16" height="16" /> Microsoft Teams (`msteams`) | Teams via Bot Framework webhook listener | [Microsoft Teams](/docs/partners/msteams/) |

For a side-by-side comparison of connection models, required fields, and delivery switches, see the [Channel Matrix](/docs/partners/channels/).

## Runtime state

```text
data/partners/<partner_id>/
├── config.yaml                  # Partner identity, model, channels, tools
├── sessions.db                  # Partner conversation store
├── workspace/
│   ├── knowledge_bases/         # Copied assigned KBs
│   └── user/
│       ├── workspace/SOUL.md
│       ├── workspace/skills/<name>/SKILL.md
│       ├── workspace/notebook/
│       └── workspace/memory/
└── runtime/
    └── <channel>/...            # QR tokens, cursors, conversation refs
```

The Partner workspace stores copies of assigned resources. This is intentional: the Partner keeps a stable library even if the original user's workspace later changes.

## Web UI vs CLI

Use the Web UI for channel configuration because it renders the live schema from `/api/v1/partners/channels/schema` and masks secret-looking fields. Use the CLI for lifecycle checks:

```bash
deeptutor partner list
deeptutor partner start math-tutor
deeptutor partner stop math-tutor
```
