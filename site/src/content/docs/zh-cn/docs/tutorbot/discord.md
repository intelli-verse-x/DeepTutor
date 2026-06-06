---
title: Discord
description: 在 Discord 上跑 TutorBot —— Developer Portal 注册、Gateway WebSocket 连接、群组策略。
---

Discord 走 **Gateway WebSocket**，不是 polling。DeepTutor 直接实现了 gateway 协议（不依赖 `discord.py`），断线自动重连。

## 你需要准备

- 一个 Discord 账号
- 一个你能管理的 server（用来测试 bot）
- 5 分钟在 Discord Developer Portal 上

## Step 1 —— 创建一个 Discord Application

1. 打开 <https://discord.com/developers/applications>
2. 点 **New Application**
3. 起个名字（比如 "Math Mentor"）
4. Save

## Step 2 —— 创建 Bot 用户

1. 应用左侧栏选 **Bot**
2. 点 **Add Bot** → 确认
3. 在 **TOKEN** 下点 **Reset Token**，然后 **Copy** —— 这就是你的 `token`
4. 在 **Privileged Gateway Intents** 下打开：
   - **Message Content Intent** *（必须，才能读消息正文）*
   - **Server Members Intent** *（推荐）*

## Step 3 —— 把 bot 邀请进 server

1. 左侧栏 → **OAuth2** → **URL Generator**
2. Scopes：勾 `bot`
3. Bot Permissions：勾 `Send Messages`、`Read Message History`、`Attach Files`、`Embed Links`、`Add Reactions`
4. 复制生成的 URL，新标签页打开，选一个 server，**Authorize**

## Step 4 —— 配置

编辑 `data/tutorbot/<bot_id>/agents.yaml`：

```yaml
channels:
  discord:
    enabled: true
    token: "YOUR_BOT_TOKEN"
    allow_from:
      - "USER_ID_1"           # 在 Discord 里右键用户 → Copy User ID（需要先开 Dev Mode）
      # - "*"                 # 全开
    group_policy: "mention"   # 或 "open"
    intents: 37377            # 默认 —— 涵盖 messages + guilds
```

> **拿 User ID 的 Dev Mode：** Discord 设置 → **Advanced** → 打开 **Developer Mode**。之后右键任意用户 → Copy User ID。

## Step 5 —— 启动

```bash
deeptutor bot start my-math-tutor
```

```text
[bot:my-math-tutor] channel:discord → connecting (gateway wss://...)
[bot:my-math-tutor] channel:discord → ready (heartbeat 41250ms)
```

## 配置参考

| 字段 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `enabled` | bool | 是 | `false` | |
| `token` | string | 是 | —— | Developer Portal 里的 Bot token |
| `allow_from` | list[string] | 是 | `[]` | User id 列表，或 `"*"` |
| `group_policy` | `"mention" \| "open"` | 可选 | `"mention"` | 群聊行为 |
| `gateway_url` | string | 可选 | `wss://gateway.discord.gg/?v=10&encoding=json` | 只有走代理时才需要改 |
| `intents` | int | 可选 | `37377` | 位字段；默认涵盖 messages + guilds + members |

## Discord 上支持的能力

| 特性 | 支持情况 |
|------|----------|
| DM 私聊 | ✅ |
| Guild 文字频道 | ✅ |
| Thread | ⚠️ 部分支持 —— bot 目前是在父频道回复 |
| 文件上传 | ✅ *（20 MB 以内）* |
| 文件下载 | ✅ |
| Markdown / mention 渲染 | ✅ *（Discord flavored markdown）* |
| 正在输入指示 | ✅ |
| 表情反应 | ⚠️ 只支持发出方向（bot 加 reaction，但不会响应用户的 reaction） |

## 群组策略

| 策略 | 行为 |
|------|------|
| `mention` | Bot 只回复 @ 它的消息 |
| `open` | Bot 回频道里的每条消息 *（很吵 —— 只适合专门的 bot 频道）* |

DM 里不管什么策略 bot 都会回。

## 保活机制

DeepTutor 的 Discord 渠道维护 gateway WebSocket，**每 ~41 秒发一次 heartbeat**（按 Discord 协议）。断线时：

- 5 秒后自动重连
- 先试 session resume（不用重新加入频道）
- resume 失败则走完整重连

你不需要任何外部守护进程 —— 渠道管理器搞定所有重连。

## 常见问题

### `4014: Disallowed intent`

你在配置里申请了一个 intent，但 Developer Portal 没启用。最常见就是 Message Content Intent。

修复：Developer Portal → 你的 app → **Bot** → 启用 **Message Content Intent**。

### Bot 在线但是不回复

检查 `allow_from`。规则和 Telegram 一样：空列表拒所有人。

再确认 Message Content Intent 是开的 —— 不开的话，bot 收到的消息 `content` 是空的。

### 超过 2000 字的消息被截断

Discord 单条消息上限 2000 字。Bot 会自动拆长回复。Deep Research 这类输出建议直接发文件：

```yaml
channels:
  discord:
    send_long_as_file: true   # 超 2000 字时附 .md
```

### 429 限流

Discord 按频道限流。如果你的 bot 短时间发很多消息（比如繁忙频道里跑 `open` 策略），就会撞到 429。渠道层会指数退避重试，但更建议切到 `mention`。

## 另请参阅

- [**Telegram**](/zh-cn/docs/tutorbot/telegram/) —— 更简单的 gateway 模型，可以对比着看
- [**Slack**](/zh-cn/docs/tutorbot/slack/) —— 也是 socket-mode，配置感觉类似
