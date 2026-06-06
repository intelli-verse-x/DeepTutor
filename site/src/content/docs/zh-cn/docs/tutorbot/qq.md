---
title: QQ
description: 在 QQ 上跑 TutorBot —— 腾讯的国民即时通讯，走官方 botpy SDK。
---

QQ 是腾讯的旗舰国民即时通讯。DeepTutor 通过腾讯官方的 **botpy** SDK 走 WebSocket 连接。

## 你需要准备

- 一个 [**QQ 开放平台**](https://bot.q.qq.com/) 账号
- 腾讯云账号（某些进阶能力需要）

## Step 1 —— 注册 QQ bot

1. 登录 <https://bot.q.qq.com/>
2. **新建机器人** → 填名字和描述
3. 复制 **App ID** 和 **Secret**
4. 启用你需要的消息类型：C2C（私信）和群消息

## Step 2 —— 配置

```yaml
channels:
  qq:
    enabled: true
    app_id: "YOUR_APP_ID"
    secret: "YOUR_SECRET"
    allow_from: []
    msg_format: "plain"      # 或 "markdown"
```

## Step 3 —— 启动

```bash
deeptutor bot start my-math-tutor
```

## 配置参考

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `enabled` | bool | 是 | |
| `app_id` | string | 是 | 来自 bot 平台 |
| `secret` | string | 是 | 来自 bot 平台 |
| `allow_from` | list[string] | 可选 | QQ user id |
| `msg_format` | `"plain" \| "markdown"` | 可选 | 回复格式 |

## QQ 上支持的能力

| 特性 | 支持情况 |
|------|----------|
| C2C（私信） | ✅ |
| 群消息 | ✅ |
| Markdown | ✅ *（要 `msg_format: "markdown"`）* |
| 文件 / 图片附件 | ✅ |
| 回复里的图片生成 | ✅ |
| @ 寻址 | ✅ |

## 常见问题

### 重复消息

QQ 的 gateway 偶尔会重发消息。渠道层维护一个最近 1000 条 message id 的 deque，静默丢弃重复消息。如果你仍然看到重复，可能 deque 已经回绕 —— 重启 bot。

### 连接时报 "Auth failed"

`app_id` / `secret` 错了，或者你的 bot 没有被审核通过相应的消息类型。去 QQ Bot 平台检查。

### Markdown 不渲染

QQ 各客户端版本对 markdown 的渲染参差不齐。有些客户端识别 `**bold**`，有些要 `<b>bold</b>`。如果用户反馈渲染异常，试试 `msg_format: "plain"`。

## 另请参阅

- [**TutorBot 概览**](/zh-cn/docs/tutorbot/) —— 整体架构
