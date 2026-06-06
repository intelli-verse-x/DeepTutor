---
title: Mochat
description: 在 Mochat 上跑 TutorBot —— 客服式聊天面板，走 Socket.IO 或 HTTP 轮询。
---

[Mochat](https://github.com/microsoft/mochat) 是一个开源的客服 / 聊天面板。DeepTutor 的 Mochat 渠道通过 **Socket.IO**（首选）或 **HTTP 轮询**（fallback）接入。适合把导师 bot 嵌到你已有网站的客服 widget 里。

## 你需要准备

- 一个运行中的 Mochat 实例（自建或托管）
- 一个带 access token（Claw Token）的 bot 账号

## Step 1 —— 在 Mochat 里创建 bot

1. 登录你的 Mochat 管理面板
2. **Bots** → **Create**
3. 复制 bot 的 **Claw Token**

## Step 2 —— 配置

```yaml
channels:
  mochat:
    enabled: true
    service_url: "https://mochat.example.com"
    claw_token: "YOUR_BOT_TOKEN"
    allow_from: []                    # User id 列表；[] = 全开
    use_http_polling: false           # Socket.IO 不可用时的 fallback
    polling_interval_ms: 1000
    delayed_message_timeout_s: 5
```

## Step 3 —— 启动

```bash
deeptutor bot start my-math-tutor
```

```text
[bot:my-math-tutor] channel:mochat → connecting (socket.io to mochat.example.com)
[bot:my-math-tutor] channel:mochat → ready
```

## 配置参考

| 字段 | 类型 | 必填 | 默认值 |
|------|------|------|--------|
| `enabled` | bool | 是 | `false` |
| `service_url` | url | 是 | —— |
| `claw_token` | string | 是 | —— |
| `allow_from` | list[string] | 可选 | `[]`（全开） |
| `use_http_polling` | bool | 可选 | `false` |
| `polling_interval_ms` | int | 可选 | `1000` |
| `delayed_message_timeout_s` | int | 可选 | `5` |

## Mochat 上支持的能力

| 特性 | 支持情况 |
|------|----------|
| 客户聊天面板消息 | ✅ |
| 群 / 房间消息 | ✅ |
| Markdown | ✅ |
| 文件上传 | ✅ |
| 延迟消息打包 | ✅ *（高频输入下提升效率）* |

## 延迟消息打包

Mochat 用户经常会一连发好几条（比如 "Hi!\n快问一下\nbot 在不在线？"）。为了避免每条都触发一次 bot 回复，渠道会把 `delayed_message_timeout_s`（默认 5s）内收到的消息 **打包**：

- 第一条消息到达 → 启动计时器
- 超时内收到更多消息 → 追加，重置计时器
- 计时器到期 → 把所有消息打包成一个用户回合

根据你的用户聊天节奏调整 `delayed_message_timeout_s`。

## 保活机制

Socket.IO 连接断线自动重连。如果 Socket.IO 反复失败，渠道会 fallback 到 HTTP 轮询：

```yaml
use_http_polling: true
polling_interval_ms: 2000     # 每 2 秒 poll 一次
```

这是用延迟换鲁棒性 —— 在挑剔的企业代理后面很有用。

## 常见问题

### "Cannot connect" 但 Mochat 是开着的

Mochat 有时要求 bot 在管理面板里 **被审核通过** 后 token 才生效。检查 bot 状态。

### 回复发出了但用户看不到

Mochat 有频道级可见性设置。确保 bot 被加进了用户聊天的频道。

### Socket.IO 版本不匹配

如果你的 Mochat 用的是较老的 Socket.IO 版本，与其调版本匹配，不如直接走 HTTP 轮询 —— `use_http_polling: true`。

## 另请参阅

- [**TutorBot 概览**](/zh-cn/docs/tutorbot/) —— 整体架构
