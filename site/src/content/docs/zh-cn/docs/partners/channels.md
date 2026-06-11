---
title: 渠道矩阵
description: 所有内置 Partner channels 的连接模型、关键字段和适用场景。
---

Partner channels 是同一个 Partner brain 外面的投递适配器。它不会创建第二套 agent runtime：一条 IM 入站事件会变成作用域内的 chat turn，最终回复再通过 channel 发回去。

大多数配置建议在 Web UI 完成：**Partners -> 你的 partner -> Channels** 会从 `/api/v1/partners/channels/schema` 渲染实时 schema，自动 mask secret 字段，并允许你 reload channels，而不需要手写 YAML。

## 内置渠道

| 渠道 | Key | 连接模型 | 适合场景 | 核心字段 |
| --- | --- | --- | --- | --- |
| WeChat | `weixin` | HTTP long-poll + 扫码登录 | 个人微信助手 | `allow_from`；可选 `token`、`state_dir`、`route_tag`、`poll_timeout` |
| WeCom | `wecom` | 企业微信 AI Bot WebSocket | 企业微信 / WeChat Work | `bot_id`、`secret`、`allow_from` |
| QQ | `qq` | 腾讯 botpy WebSocket | 官方 QQ Bot 部署 | `app_id`、`secret`、`allow_from`、`msg_format` |
| QQ (NapCat) | `napcat` | OneBot v11 WebSocket | 通过 NapCat 接个人 QQ | `ws_url`、可选 `access_token`、`allow_from`、`group_policy` |
| Telegram | `telegram` | Bot API polling | 简单个人/群 bot | `token`、`allow_from` |
| Discord | `discord` | Gateway WebSocket | Discord server 和 DM | `token`、`allow_from`、群策略字段 |
| Slack | `slack` | Socket Mode | Slack team、DM、threaded channel help | `bot_token`、`app_token`、`allow_from`、`group_policy` |
| Feishu / Lark | `feishu` | Lark SDK WebSocket | 飞书 / Lark 企业聊天 | `app_id`、`app_secret`，以及 verification/encryption 字段 |
| DingTalk | `dingtalk` | Stream Mode | 钉钉企业聊天 | 应用凭证、`allow_from`、群策略字段 |
| Matrix | `matrix` | Matrix sync loop | 去中心化房间，可选 E2EE | `homeserver`、用户凭证或 `access_token`、`allow_from`、`group_policy` |
| Zulip | `zulip` | Event queue | stream + topic 工作流 | `email`、`api_key`、`site`、`allow_from`、`group_policy` |
| WhatsApp | `whatsapp` | Bridge WebSocket | 通过桥接运行时接 WhatsApp | bridge URL/token、`allow_from` |
| Email | `email` | IMAP poll + SMTP send | 异步邮件答疑 / helpdesk | IMAP host/user/password、SMTP host/user/password、`allow_from` |
| Mochat | `mochat` | Socket.IO 或 HTTP polling | 客服式聊天面板 | `base_url` / socket URL、`claw_token`、`allow_from` |
| Microsoft Teams | `msteams` | 内置 HTTP webhook listener | Teams DM-first Bot Framework 集成 | `app_id`、`app_password`、`tenant_id`、host/port/path |

## 共享投递开关

大多数 channels 都继承同一组 delivery controls：

| 字段 | 含义 |
| --- | --- |
| `enabled` | Partner 是否启动这个 channel。 |
| `send_progress` | 长 turn 期间是否投递 narration/progress。 |
| `send_tool_hints` | 是否投递一行工具调用提示。调试时有用，生产环境可能太吵。 |
| `streaming` | 仅 Telegram、Discord、Feishu：回复实时流式输出，靠原地编辑消息逐步长出（Feishu 走 CardKit 流式卡片）。需要 `send_progress` 开启。默认关闭。 |
| `allow_from` | 用户/会话 allowlist。`*` 适合测试；部署时更建议明确 id。 |

## 配置流程

1. 先在 Web UI 创建并测试 Partner，不要一开始就开 IM channel。
2. 第一次只启用一个 channel。
3. 调试阶段保持 `send_progress` 和 `send_tool_hints` 开启。
4. `allow_from: ["*"]` 只用于本地/私有测试。
5. 发一条短消息，检查日志，再把 `*` 换成真实 sender ids。
6. 第一个 channel 稳定后，再添加其它 channels。

## 怎么选

- 个人微信用 **WeChat**，需要人工扫码和持久化 state。
- 企业/团队部署用 **WeCom**、**Feishu**、**DingTalk**、**Slack** 或 **Teams**。
- 官方 QQ Bot 用 **QQ**；只有在明确操作个人 QQ bridge 时才用 **NapCat**。
- 异步 inbox 工作流用 **Email**。
- 需要 room/topic 结构时，用 **Matrix** 或 **Zulip**。

## 状态存在哪里

Channel runtime state 存在 Partner runtime 目录下，例如：

```text
data/partners/<partner_id>/runtime/weixin/account.json
data/partners/<partner_id>/runtime/msteams/msteams_conversations.json
```

Docker 或生产部署要持久化整个 `data/partners/`。丢失 runtime state 可能导致重新扫码，或重新收集 conversation reference。

## 详细页面

- [WeChat](/zh-cn/docs/partners/weixin/) —— 个人微信扫码登录和 long-poll 配置
- [WeCom](/zh-cn/docs/partners/wecom/) —— 企业微信 AI Bot 配置
- [QQ / NapCat](/zh-cn/docs/partners/qq/) —— 官方 QQ bot 和个人 QQ bridge 两条路径
