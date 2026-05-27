---
title: Slack
description: 在 Slack 上跑 TutorBot —— Socket Mode 应用、按 thread 分会话、频道与 DM 策略。
---

Slack 是功能最完整的渠道：DM、频道 @、**按 thread 分会话**（每条 thread 就是一个独立的 DeepTutor session）、Slack 风味的 markdown、文件上传、确认 reaction。

连接走 **Socket Mode** —— 不需要公网 IP 或 webhook。

## 你需要准备

- 一个你可以装应用的 Slack workspace（自己的或管理员授权的）
- 5 分钟在 <https://api.slack.com/apps>

## Step 1 —— 创建 Slack app

1. 去 <https://api.slack.com/apps> → **Create New App** → **From scratch**
2. 起名（比如 "Math Mentor"），选 workspace
3. 创建后进 **Socket Mode**（左侧栏）→ **Enable Socket Mode** *（开关打开）*
4. 提示你生成 App-Level Token 时，给 `connections:write` 权限并复制 —— 这就是你的 **`app_token`**（`xapp-` 开头）

## Step 2 —— 配置 OAuth scopes

还在你的 app 里：

1. 左侧栏 → **OAuth & Permissions**
2. **Scopes** → **Bot Token Scopes** 加上：
   - `chat:write` —— 发消息
   - `chat:write.public` —— 不入群也能发到频道
   - `files:write` —— 上传文件
   - `reactions:write` —— 加 reaction（`:eyes:` 确认）
   - `users:read` —— 解析 user id 到名字
   - `app_mentions:read` —— 接收 @
   - `im:history` —— 读 DM 历史
   - `im:read` —— 读 DM 频道信息
   - `channels:history` —— 读公开频道历史
   - `groups:history` —— *（可选）* 私有频道
3. 点 **Install to Workspace** → 授权
4. 复制 **Bot User OAuth Token**（`xoxb-` 开头）—— 这是你的 **`bot_token`**

## Step 3 —— 订阅事件

1. 左侧栏 → **Event Subscriptions**
2. **Subscribe to bot events** 加上：
   - `app_mention`
   - `message.im`
   - `message.channels` *（只在你想监听频道时才加；否则跳过）*

## Step 4 —— 配置

```yaml
channels:
  slack:
    enabled: true
    mode: "socket"                  # 只支持 socket 一种
    bot_token: "xoxb-XXX..."        # 来自 OAuth & Permissions
    app_token: "xapp-XXX..."        # 来自 Socket Mode
    reply_in_thread: true           # 回复留在 thread 内
    react_emoji: "eyes"             # 用来确认收到的 reaction
    allow_from: ["*"]               # User id 列表；"*" = 全开
    group_policy: "mention"         # 频道里只回 @ 消息
    group_allow_from: []            # 限制到特定频道 id（如果用 mention）
    dm:
      enabled: true
      policy: "open"                # DM 全回，或 "allowlist"
      allow_from: []
```

## Step 5 —— 启动

```bash
deeptutor bot start my-math-tutor
```

```text
[bot:my-math-tutor] channel:slack → connecting (socket mode)
[bot:my-math-tutor] channel:slack → ready
```

在 Slack 里 DM bot，或者在频道 @ 它。

## 配置参考

| 字段 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `enabled` | bool | 是 | `false` | |
| `mode` | string | 是 | `"socket"` | 只支持 `socket` |
| `bot_token` | string | 是 | —— | `xoxb-…` |
| `app_token` | string | 是 | —— | `xapp-…`（Socket Mode token） |
| `reply_in_thread` | bool | 可选 | `true` | 在 thread 内回复 vs 发新消息 |
| `react_emoji` | string | 可选 | `"eyes"` | 确认 reaction 用的 emoji 名 |
| `allow_from` | list[string] | 是 | `[]` | User id 列表，或 `"*"` |
| `group_policy` | `"mention" \| "open"` | 可选 | `"mention"` | 频道内 |
| `group_allow_from` | list[string] | 可选 | `[]` | 频道 id 列表（想限定到特定频道时） |
| `dm.enabled` | bool | 可选 | `true` | |
| `dm.policy` | `"open" \| "allowlist"` | 可选 | `"open"` | |
| `dm.allow_from` | list[string] | 可选 | `[]` | `policy=allowlist` 时生效 |

## 按 thread 分会话

这是 Slack 上最爽的一个特性：**每条 Slack thread 都是独立的 DeepTutor session**。当你在频道 @ bot：

1. Bot 回复，开启一条新 thread
2. 在那条 thread 里的后续回复都进同一个 session（带它全部历史、挂载的 KB 等）
3. 不同频道里的 thread 是不同 session
4. DM 自己一个 session（每个用户一个）

这意味着一个团队可以在同一个频道里并行开多个导师对话而不互相串扰。

如果想关掉这个（每次回复都从头开始）：

```yaml
channels:
  slack:
    reply_in_thread: false
    # 附带效果：bot 直接在频道里回，不开 thread
```

## Slack 上支持的能力

| 特性 | 支持情况 |
|------|----------|
| DM | ✅ |
| 频道 @ | ✅ |
| Thread（会话隔离） | ✅ |
| 文件上传 | ✅ |
| 文件下载 | ✅ |
| Markdown → mrkdwn | ✅ *（渠道自动转换）* |
| 代码块 | ✅ |
| LaTeX 数学公式 | ⚠️ 当代码块渲染（Slack 不支持 LaTeX） |
| 发送 reaction | ✅ *（通过 `react_emoji`）* |
| Slash 命令 | ⚠️ 暂不支持 —— 用 DM/@ 寻址 |

## Markdown 到 mrkdwn

Slack 用自己的 markdown 方言（"mrkdwn"）。DeepTutor 的 Slack 渠道会自动转换：

| 标准 markdown | mrkdwn 输出 |
|---------------|-------------|
| `**bold**` | `*bold*` |
| `*italic*` | `_italic_` |
| `# heading` | `*heading*`（加粗） |
| `` `code` `` | `` `code` `` |
| ` ```code``` ` | ` ```code``` ` |
| `[link](url)` | `<url|link>` |
| `- bullet` | `• bullet` |
| `> quote` | `> quote` |

## 常见问题

### Bot 说了 hi 但后面就不回了

检查 `reply_in_thread`：

```yaml
reply_in_thread: true
```

如果是 true，bot 只监听它自己开的 thread（`thread_ts` 要匹配）。如果你在它首次回复之后又在非 thread 消息里发，bot 看不到。

### "Not authorized" / Slack API 401

Token 弄反了 —— 确认 `bot_token` 填的是 `xoxb-` 开头的，`app_token` 填的是 `xapp-` 开头的。很容易顺手填反。

### Bot 在频道里不回复

两个前提：
1. Bot 要被 **邀请到频道**（`/invite @bot`）
2. 如果 `group_policy: mention`，你的消息必须 @ bot（`@math-mentor what is...`）

### 长消息被截断

Slack 单条消息上限 40000 字（比 Telegram/Discord 长得多）。DeepTutor 不会主动拆 —— 但极长的回复（比如 50+ 页的 Deep Research 报告）建议直接发文件。

## 保活机制

Socket Mode 是一条 WebSocket 长连。渠道层：
- 每 30 秒发 ping
- 断线自动指数退避重连
- 不需要任何外部守护

## 另请参阅

- [**Discord**](/zh-cn/docs/tutorbot/discord/) —— 类似的 developer portal 模型
- [**TutorBot 概览**](/zh-cn/docs/tutorbot/) —— 整体架构
