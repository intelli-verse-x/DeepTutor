---
title: 渠道矩阵
description: 所有内置 Partner channels 的连接模型、关键字段和适用场景。
---

Partner channels 是同一个 Partner brain 外面的投递适配器。它不会创建第二套 agent runtime：一条 IM 入站事件会变成作用域内的 chat turn，最终回复再通过 channel 发回去。

大多数配置建议在 Web UI 完成：**Partners -> 你的 partner -> Channels** 会从 `/api/v1/partners/channels/schema` 渲染实时 schema，自动 mask secret 字段，并允许你 reload channels，而不需要手写 YAML。

![Partner channel 配置卡片](/screenshots/partners-channels.png)

## 内置渠道

| 渠道 | Key | 连接模型 | 适合场景 | 核心字段 |
| --- | --- | --- | --- | --- |
| <img src="/channel-icons/weixin.svg" alt="" width="16" height="16" /> WeChat | `weixin` | HTTP long-poll + 扫码登录 | 个人微信助手 | `allow_from`；可选 `token`、`state_dir`、`route_tag`、`poll_timeout` |
| <img src="/channel-icons/wecom.svg" alt="" width="16" height="16" /> WeCom | `wecom` | 企业微信 AI Bot WebSocket | 企业微信 / WeChat Work | `bot_id`、`secret`、`allow_from` |
| <img src="/channel-icons/qq.svg" alt="" width="16" height="16" /> QQ | `qq` | 腾讯 botpy WebSocket | 官方 QQ Bot 部署 | `app_id`、`secret`、`allow_from`、`msg_format` |
| <img src="/channel-icons/napcat.svg" alt="" width="16" height="16" /> QQ (NapCat) | `napcat` | OneBot v11 WebSocket | 通过 NapCat 接个人 QQ | `ws_url`、可选 `access_token`、`allow_from`、`group_policy` |
| <img src="/channel-icons/telegram.svg" alt="" width="16" height="16" /> Telegram | `telegram` | Bot API polling | 简单个人/群 bot | `token`、`allow_from` |
| <img src="/channel-icons/discord.svg" alt="" width="16" height="16" /> Discord | `discord` | Gateway WebSocket | Discord server 和 DM | `token`、`allow_from`、群策略字段 |
| <img src="/channel-icons/slack.svg" alt="" width="16" height="16" /> Slack | `slack` | Socket Mode | Slack team、DM、threaded channel help | `bot_token`、`app_token`、`allow_from`、`group_policy` |
| <img src="/channel-icons/feishu.svg" alt="" width="16" height="16" /> Feishu / Lark | `feishu` | Lark SDK WebSocket | 飞书 / Lark 企业聊天 | `app_id`、`app_secret`，以及 verification/encryption 字段 |
| <img src="/channel-icons/dingtalk.svg" alt="" width="16" height="16" /> DingTalk | `dingtalk` | Stream Mode | 钉钉企业聊天 | 应用凭证、`allow_from`、群策略字段 |
| <img src="/channel-icons/matrix.svg" alt="" width="16" height="16" /> Matrix | `matrix` | Matrix sync loop | 去中心化房间，可选 E2EE | `homeserver`、用户凭证或 `access_token`、`allow_from`、`group_policy` |
| <img src="/channel-icons/zulip.svg" alt="" width="16" height="16" /> Zulip | `zulip` | Event queue | stream + topic 工作流 | `email`、`api_key`、`site`、`allow_from`、`group_policy` |
| <img src="/channel-icons/whatsapp.svg" alt="" width="16" height="16" /> WhatsApp | `whatsapp` | Bridge WebSocket | 通过桥接运行时接 WhatsApp | bridge URL/token、`allow_from` |
| <img src="/channel-icons/email.svg" alt="" width="16" height="16" /> Email | `email` | IMAP poll + SMTP send | 异步邮件答疑 / helpdesk | IMAP host/user/password、SMTP host/user/password、`allow_from` |
| <img src="/channel-icons/mochat.svg" alt="" width="16" height="16" /> Mochat | `mochat` | Socket.IO 或 HTTP polling | 客服式聊天面板 | `base_url` / socket URL、`claw_token`、`allow_from` |
| <img src="/channel-icons/msteams.svg" alt="" width="16" height="16" /> Microsoft Teams | `msteams` | 内置 HTTP webhook listener | Teams DM-first Bot Framework 集成 | `app_id`、`app_password`、`tenant_id`、host/port/path |

## 安装依赖

除 Matrix 外，所有内置 channel 都包含在 Partners extra 里：

```bash
pip install -e ".[partners]"
# 或发布包支持 extras 时：
pip install "deeptutor[partners]"
```

这一条命令会装齐全部 channel SDK——`python-telegram-bot`、`slack-sdk`、`lark-oapi`、`dingtalk-stream`、`qq-botpy`、`wecom-aibot-sdk`、`python-socketio` 等（完整清单见 `requirements/partners.txt`）。Email 只用 Python 标准库，不需要额外的包。Matrix 单独成 extra，因为加密房间依赖原生 `libolm` 库：普通房间装 `".[matrix]"`，E2EE 加密房间装 `".[matrix-e2e]"`。

如果服务器上缺某个 channel 的依赖，Channels 面板会把该 channel 置灰，并显示 import 错误（例如 `No module named 'lark_oapi'`）。装上缺的包、重启 DeepTutor，卡片就能编辑了。

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

每个内置 channel 都有专属配置页：平台侧申请步骤、对着截图逐字段讲解 channel card、配完后的验证流程和故障排查：

- <img src="/channel-icons/weixin.svg" alt="" width="16" height="16" /> [WeChat](/zh-cn/docs/partners/weixin/) —— 个人微信扫码登录和 long-poll 配置
- <img src="/channel-icons/wecom.svg" alt="" width="16" height="16" /> [WeCom](/zh-cn/docs/partners/wecom/) —— 企业微信 AI Bot 配置
- <img src="/channel-icons/qq.svg" alt="" width="16" height="16" /> [QQ / NapCat](/zh-cn/docs/partners/qq/) —— 官方 QQ bot 和个人 QQ bridge 两条路径
- <img src="/channel-icons/telegram.svg" alt="" width="16" height="16" /> [Telegram](/zh-cn/docs/partners/telegram/) —— BotFather 注册、Bot API 轮询、流式回复
- <img src="/channel-icons/discord.svg" alt="" width="16" height="16" /> [Discord](/zh-cn/docs/partners/discord/) —— Developer Portal 应用、intents、Gateway WebSocket
- <img src="/channel-icons/slack.svg" alt="" width="16" height="16" /> [Slack](/zh-cn/docs/partners/slack/) —— Socket Mode 应用（bot + app 双 token）
- <img src="/channel-icons/feishu.svg" alt="" width="16" height="16" /> [Feishu / Lark](/zh-cn/docs/partners/feishu/) —— 开放平台应用和 CardKit 流式卡片
- <img src="/channel-icons/dingtalk.svg" alt="" width="16" height="16" /> [DingTalk](/zh-cn/docs/partners/dingtalk/) —— Stream Mode 企业机器人
- <img src="/channel-icons/matrix.svg" alt="" width="16" height="16" /> [Matrix](/zh-cn/docs/partners/matrix/) —— homeserver 凭证和可选 E2EE
- <img src="/channel-icons/zulip.svg" alt="" width="16" height="16" /> [Zulip](/zh-cn/docs/partners/zulip/) —— bot 账号和 stream 订阅
- <img src="/channel-icons/whatsapp.svg" alt="" width="16" height="16" /> [WhatsApp](/zh-cn/docs/partners/whatsapp/) —— bridge 运行时配置
- <img src="/channel-icons/email.svg" alt="" width="16" height="16" /> [Email](/zh-cn/docs/partners/email/) —— IMAP 收件轮询和 SMTP 回信
- <img src="/channel-icons/mochat.svg" alt="" width="16" height="16" /> [Mochat](/zh-cn/docs/partners/mochat/) —— Socket.IO 客服面板
- <img src="/channel-icons/msteams.svg" alt="" width="16" height="16" /> [Microsoft Teams](/zh-cn/docs/partners/msteams/) —— Bot Framework webhook 监听
