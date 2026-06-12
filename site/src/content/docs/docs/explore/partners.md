---
title: Partners
description: Persistent IM-connected companions that run on the same chat agent loop as DeepTutor Chat.
---

Partners are persistent companions with their own identity, soul, model policy, assigned library, and channel configuration. They replace the old TutorBot engine: every inbound web or IM message is routed through the same `ChatOrchestrator -> AgenticChatPipeline` loop used by the main Chat workspace.

![Partners workspace](/screenshots/partners.png)

## Mental model

A Partner is a **synthetic user workspace** under `data/partners/<id>/workspace/`. The workspace contains the partner's soul, copied knowledge bases, copied skills, notebooks, memory, and channel runtime state. Because the layout matches the chat workspace, tools such as RAG, `read_skill`, notebooks, memory, and MCP-deferred tools work without a separate bot implementation.

![Partners architecture](/screenshots/partners-architecture.png)

## Create a partner

Open **Partners -> New partner** and complete the wizard:

![Partner creation wizard, Identity step](/screenshots/partners-new.png)

1. **Identity** — name, avatar, description, and default reply language.
2. **Soul** — the partner's role and communication style. This becomes `SOUL.md`.
3. **Mind** — model selection, enabled system tools, MCP tools, and delivery preferences.
4. **Library** — assign knowledge bases, skills, and notebooks. These are copied into the partner workspace so the partner can use them even when the original owner changes context.
5. **Review** — confirm the workspace and channel setup before starting.

![Partner detail](/screenshots/partners-detail.png)

Everything chosen in the wizard stays editable afterwards: the partner detail page pairs the web **Chat** view with a **Configure** tab covering identity, soul, mind, and library, plus a **Channels** tab for delivery setup.

![Partner detail, Configure tab](/screenshots/partners-configure.png)

## Channels

Channels are delivery adapters around the same partner brain. Common switches appear on most channel cards:

| Field | Meaning |
| --- | --- |
| **Enabled** | Start this channel for the partner. Leave off while collecting credentials. |
| **Send Progress** | Send narration/progress messages for long-running turns. Useful for IM apps where a silent 60-second wait feels broken. |
| **Send Tool Hints** | Send one-line tool-call hints such as `rag(query=...)`. Turn off for quieter production channels. |
| **Allow From** | Allowlist of user ids, group ids, email addresses, or `*`. Empty usually denies all access; `*` opens the channel. |

Each channel has its own configuration page with credentials, setup steps, and troubleshooting — see the [**Channel Matrix**](/docs/partners/channels/) for the full list. Start with [**WeChat**](/docs/partners/weixin/) if you are configuring a personal WeChat account, [**WeCom**](/docs/partners/wecom/) for Enterprise WeChat, or [**QQ / NapCat**](/docs/partners/qq/) for Tencent consumer QQ paths.

## CLI mirror

```bash
deeptutor partner list
deeptutor partner create math-tutor --soul "Socratic math tutor"
deeptutor partner start math-tutor
deeptutor partner stop math-tutor
```

The CLI is useful for smoke tests, but the web UI is the recommended place to configure channel fields because it masks secrets and shows the channel schema inline.
