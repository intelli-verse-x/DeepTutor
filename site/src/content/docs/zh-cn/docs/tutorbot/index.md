---
title: TutorBot 概览
description: TutorBot —— 持久化、多渠道的自主导师。架构、生命周期、保活策略，以及每个渠道一页文档。
---

**TutorBot** 是一个住在 DeepTutor 里的持久化、自主 AI 导师，可以同时连到一个或多个 **外部聊天渠道**（Telegram、Slack、飞书 等），让你的用户在他们已有的工具里和它对话。

本章节是运维指南：系统怎么工作、怎么保活，以及 **每个渠道一页专属文档**（注册流程、配置项、故障排查）。

## 架构图

```text
┌─────────────────────────────────────────────────────────────────────┐
│                          DeepTutor server                           │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐    │
│  │                      Bot orchestrator                       │    │
│  │           （nanobot 推理引擎驱动的 agent loop）              │    │
│  └──────────┬──────────────────────────────────────────────────┘    │
│             │                                                       │
│   ┌─────────┼─────────┐                                             │
│   ▼         ▼         ▼                                             │
│ ┌───┐    ┌─────┐   ┌───────┐   每个 bot 是一个独立的 asyncio task   │
│ │bot│    │ bot │   │  bot  │   独立工作区位于                       │
│ │ A │    │  B  │   │   C   │   data/tutorbot/<bot_id>/              │
│ └─┬─┘    └──┬──┘   └───┬───┘                                        │
│   │         │          │                                            │
│   │ ┌───────┼──────────┼───────────────────────────────────┐        │
│   ▼ ▼       ▼          ▼                                   ▼        │
│  ┌──────────────────────────────────────────────────┐               │
│  │             Channel registry (12 个渠道)          │              │
│  └──────────────────────────────────────────────────┘               │
└────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬──┬──┬───┘
     │     │     │     │     │     │     │     │     │     │  │  │
     ▼     ▼     ▼     ▼     ▼     ▼     ▼     ▼     ▼     ▼  ▼  ▼
   Telegram Discord Slack Matrix Zulip 飞书 企业微信 钉钉 QQ WhatsApp 邮件 Mochat
```

关键特性：

- **同进程**：所有 bot 都是 DeepTutor server 进程里的 asyncio task。不需要单独的进程、Docker sidecar 或 systemd unit。
- **一个 bot 多渠道**：一个 bot 可以同时在 Telegram **和** Slack **和** Matrix 上对话。
- **隔离的工作区**：每个 bot 都有自己的 `agents.yaml`、soul 模板、skills、cron 任务和本地 session 库，存在 `data/tutorbot/<bot_id>/` 下。
- **共享 Memory**：所有 bot 看的是 **同一个用户的 L3 记忆**（`data/memory/L3/`），通过 per-channel L1 trace 来分辨来源。
- **渠道重连不用重启**：渠道层级的断线（比如临时网络抖动）会自动恢复。

## 生命周期

```bash
# 创建
deeptutor bot create my-math-tutor \
  --name "Math Mentor" \
  --persona "专注于微积分和线性代数的 Socratic 导师" \
  --model gpt-4o

# 配置渠道（编辑 data/tutorbot/my-math-tutor/agents.yaml）

# 启动（为每个启用的渠道 fork 出 asyncio task）
deeptutor bot start my-math-tutor

# 查看状态
deeptutor bot list

# 停止
deeptutor bot stop my-math-tutor
```

## 渠道一览

| 渠道 | 页面 |
|------|------|
| Telegram | [docs/tutorbot/telegram](/zh-cn/docs/tutorbot/telegram/) |
| Discord | [docs/tutorbot/discord](/zh-cn/docs/tutorbot/discord/) |
| Slack | [docs/tutorbot/slack](/zh-cn/docs/tutorbot/slack/) |
| Matrix | [docs/tutorbot/matrix](/zh-cn/docs/tutorbot/matrix/) |
| Zulip | [docs/tutorbot/zulip](/zh-cn/docs/tutorbot/zulip/) |
| 飞书 / Lark | [docs/tutorbot/feishu](/zh-cn/docs/tutorbot/feishu/) |
| 企业微信 | [docs/tutorbot/wecom](/zh-cn/docs/tutorbot/wecom/) |
| 钉钉 | [docs/tutorbot/dingtalk](/zh-cn/docs/tutorbot/dingtalk/) |
| QQ | [docs/tutorbot/qq](/zh-cn/docs/tutorbot/qq/) |
| WhatsApp | [docs/tutorbot/whatsapp](/zh-cn/docs/tutorbot/whatsapp/) |
| 邮件 | [docs/tutorbot/email](/zh-cn/docs/tutorbot/email/) |
| Mochat | [docs/tutorbot/mochat](/zh-cn/docs/tutorbot/mochat/) |

> 各渠道页面目前仍为英文版（已为中文站点准备好链接结构）。
