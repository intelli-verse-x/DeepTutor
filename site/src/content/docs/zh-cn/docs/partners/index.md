---
title: 伙伴与渠道
description: DeepTutor Partners 的运维文档：渠道配置、工作区布局和 IM 投递行为。
---

Partners 是可以存在于 Web UI 和外部 IM 应用里的持久 DeepTutor 伙伴。它不是第二套 bot engine。每条入站消息都会变成一个作用域在该 Partner 下的普通 chat-agent turn：

```text
IM / Web message -> PartnerRunner -> ChatOrchestrator -> AgenticChatPipeline -> tools -> reply
```

## 和旧 TutorBot 的区别

| 旧 TutorBot | 新 Partner |
| --- | --- |
| 独立 bot engine，工作区在 `data/tutorbot/<id>/` | 复用 Chat loop，作用域在 `data/partners/<id>/workspace/` |
| `deeptutor bot ...` 命令 | `deeptutor partner list/create/start/stop` |
| 手写 bot YAML 里的 channels | Partners UI 中按 schema 渲染的 channel cards |
| bot skills / memory 独立处理 | 分配的 KB、skills、notebooks、tools、memory 像普通 chat context 一样挂载 |

旧 `/docs/tutorbot/*` 链接会保留为简短迁移提示页，避免外部链接硬 404。

## 推荐配置流程

1. 在 **Partners -> New partner** 创建 Partner。
2. 启用任何 channel 前，先填好 **Identity** 和 **Soul**。第一条 IM 回复就会使用这个 soul。
3. 在 **Mind** 里选择模型；测试阶段先少开可选工具。
4. 在 **Library** 里先分配一个小 KB 或 skill。资源会复制进 Partner workspace。
5. 在 **Channels** 里先只启用一个 channel，并从本地/私有测试开始。
6. 调试时保留 `send_progress` 和 `send_tool_hints`，生产环境再按需要关闭。
7. 对真实用户开放前，把 `allow_from: ["*"]` 换成明确 sender ids。

![Partner 详情](/screenshots/partners-detail.png)

## Channel 入口

| Channel | 适用场景 | 页面 |
| --- | --- | --- |
| <img src="/channel-icons/weixin.svg" alt="" width="16" height="16" /> WeChat (`weixin`) | 个人微信，扫码登录，HTTP long-poll | [WeChat](/zh-cn/docs/partners/weixin/) |
| <img src="/channel-icons/wecom.svg" alt="" width="16" height="16" /> WeCom (`wecom`) | 企业微信 / WeChat Work AI Bot 平台 | [WeCom](/zh-cn/docs/partners/wecom/) |
| <img src="/channel-icons/qq.svg" alt="" width="16" height="16" /> QQ (`qq`) | 腾讯官方 QQ Bot，botpy SDK | [QQ / NapCat](/zh-cn/docs/partners/qq/) |
| <img src="/channel-icons/napcat.svg" alt="" width="16" height="16" /> NapCat (`napcat`) | 个人 QQ，通过 OneBot v11 / NapCat 接入 | [QQ / NapCat](/zh-cn/docs/partners/qq/) |
| <img src="/channel-icons/telegram.svg" alt="" width="16" height="16" /> Telegram (`telegram`) | 上手最快——BotFather 拿 token，无需公网 IP | [Telegram](/zh-cn/docs/partners/telegram/) |
| <img src="/channel-icons/discord.svg" alt="" width="16" height="16" /> Discord (`discord`) | Discord server 和 DM，Gateway WebSocket | [Discord](/zh-cn/docs/partners/discord/) |
| <img src="/channel-icons/slack.svg" alt="" width="16" height="16" /> Slack (`slack`) | Slack team，Socket Mode，线程回复 | [Slack](/zh-cn/docs/partners/slack/) |
| <img src="/channel-icons/feishu.svg" alt="" width="16" height="16" /> Feishu (`feishu`) | 飞书 / Lark，CardKit 流式卡片 | [Feishu](/zh-cn/docs/partners/feishu/) |
| <img src="/channel-icons/dingtalk.svg" alt="" width="16" height="16" /> DingTalk (`dingtalk`) | 钉钉企业机器人，Stream Mode | [DingTalk](/zh-cn/docs/partners/dingtalk/) |
| <img src="/channel-icons/matrix.svg" alt="" width="16" height="16" /> Matrix (`matrix`) | 去中心化房间，可选 E2EE | [Matrix](/zh-cn/docs/partners/matrix/) |
| <img src="/channel-icons/zulip.svg" alt="" width="16" height="16" /> Zulip (`zulip`) | stream + topic 结构化团队聊天 | [Zulip](/zh-cn/docs/partners/zulip/) |
| <img src="/channel-icons/whatsapp.svg" alt="" width="16" height="16" /> WhatsApp (`whatsapp`) | 通过 bridge 运行时接 WhatsApp | [WhatsApp](/zh-cn/docs/partners/whatsapp/) |
| <img src="/channel-icons/email.svg" alt="" width="16" height="16" /> Email (`email`) | IMAP/SMTP 异步收发件箱工作流 | [Email](/zh-cn/docs/partners/email/) |
| <img src="/channel-icons/mochat.svg" alt="" width="16" height="16" /> Mochat (`mochat`) | 客服式聊天面板 | [Mochat](/zh-cn/docs/partners/mochat/) |
| <img src="/channel-icons/msteams.svg" alt="" width="16" height="16" /> Microsoft Teams (`msteams`) | Teams，Bot Framework webhook 监听 | [Microsoft Teams](/zh-cn/docs/partners/msteams/) |

各渠道的连接模型、必填字段和投递开关对照，请看 [渠道矩阵](/zh-cn/docs/partners/channels/)。

## 运行时状态

```text
data/partners/<partner_id>/
├── config.yaml                  # Partner identity, model, channels, tools
├── sessions.db                  # Partner conversation store
├── workspace/
│   ├── knowledge_bases/         # 复制过来的 assigned KBs
│   └── user/
│       ├── workspace/SOUL.md
│       ├── workspace/skills/<name>/SKILL.md
│       ├── workspace/notebook/
│       └── workspace/memory/
└── runtime/
    └── <channel>/...            # QR tokens, cursors, conversation refs
```

分配资源会复制进 Partner workspace，这是刻意设计：即使原用户 workspace 后续变化，Partner 仍保留稳定 library。

## Web UI vs CLI

配置 channel 推荐用 Web UI，因为它会从 `/api/v1/partners/channels/schema` 渲染实时 schema，并自动 mask secret 字段。CLI 更适合 lifecycle 检查：

```bash
deeptutor partner list
deeptutor partner start math-tutor
deeptutor partner stop math-tutor
```
