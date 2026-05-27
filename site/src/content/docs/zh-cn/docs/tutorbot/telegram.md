---
title: Telegram
description: 在 Telegram 上跑 TutorBot —— 通过 BotFather 注册、配置项与运维要点。
---

Telegram 是最容易接入的渠道 —— 不用公网 IP、不用 webhook 签名，BotFather 注册大概一分钟搞定。

## 你需要准备

- 一个 Telegram 账号
- 和 [@BotFather](https://t.me/BotFather) 的一段对话

就这些。不用企业认证、不用开发者控制台注册。

## Step 1 —— 在 BotFather 注册一个 bot

打开 Telegram，搜 `@BotFather`，开个聊天。然后：

```text
You> /newbot

BotFather> Alright, a new bot. How are we going to call it?
          Please choose a name for your bot.

You> Math Mentor

BotFather> Good. Now let's choose a username for your bot.
          It must end in 'bot'. Like this, for example: TetrisBot.

You> hku_math_mentor_bot

BotFather> Done! Congratulations on your new bot.
          You will find it at t.me/hku_math_mentor_bot.

          Use this token to access the HTTP API:
          123456789:ABC-DEF1234ghIkl-zyx57W2v1u123ew11
```

**把这个 token 复制下来。** 稍后要粘进 `agents.yaml`。

## Step 2 —— 找到你自己的 Telegram user id

你得把自己的 user id 填到 `allow_from` 里（否则 bot 谁都不会理）。最简单的办法：和 [@userinfobot](https://t.me/userinfobot) 聊一句，它会回你 id。

```text
You> hi

userinfobot> Id: 123456789
             First: Frank
             Last:
             Username: @frank
             Language: zh
```

## Step 3 —— 配置你的 bot

编辑 `data/tutorbot/<bot_id>/agents.yaml`：

```yaml
agent:
  id: my-math-tutor
  name: Math Mentor
  persona: "Socratic math tutor specializing in calculus and linear algebra."
  model: gpt-4o

channels:
  telegram:
    enabled: true
    token: "123456789:ABC-DEF1234ghIkl-zyx57W2v1u123ew11"
    allow_from:
      - "123456789"       # 你的 Telegram user id
      # - "*"             # 取消注释即对所有人开放（谨慎）
```

## Step 4 —— 启动 bot

```bash
deeptutor bot start my-math-tutor
```

```text
[bot:my-math-tutor] starting...
[bot:my-math-tutor] channel:telegram → connecting
[bot:my-math-tutor] channel:telegram → ok (long-polling)
[bot:my-math-tutor] running.
```

然后打开 Telegram，搜 `@hku_math_mentor_bot`，发 `/start` —— 你就在和 bot 对话了。

## 配置参考

| 字段 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `enabled` | bool | 是 | `false` | 启用该渠道 |
| `token` | string | 是 | —— | BotFather 给的 HTTP API token |
| `allow_from` | list[string] | 是 | `[]` *（默认拒所有）* | User id 列表，或 `"*"` 全开 |

## Telegram 上支持的能力

| 特性 | 支持情况 |
|------|----------|
| 私聊 | ✅ |
| 群聊 | ✅ *（bot 要被加进群，并且 `group_policy` 配合）* |
| Markdown 渲染 | ✅ *（走 Telegram 的 markdown_v2 解析器）* |
| LaTeX 数学公式 | ⚠️ 当纯文本渲染 —— Telegram 不识别 `$...$` |
| 文件上传 | ✅ *（在 Telegram 的 20 MB / 2 GB 限制内）* |
| 文件下载 | ✅ *（bot 可以接收 PDF、图片、语音）* |
| 语音转写 | ✅ *（如果全局配置了 `transcription_api_key`）* |
| 线程内回复 | ⚠️ 部分支持 —— Telegram 只有 reply-to-message，没有真正的 thread |

## 群聊

在 Telegram 群里使用 bot：

1. 把 bot 加入群（Add Member → 搜 `@your_bot`）
2. 在 BotFather 里关掉 **Group Privacy**：`/mybots` → 选 bot → **Bot Settings** → **Group Privacy** → **Turn OFF**
3. 在消息里 @ 它来寻址（`@hku_math_mentor_bot question?`）

在配置里设 `group_policy`：

```yaml
channels:
  telegram:
    group_policy: "mention"   # 只在被 @ 时回复
    # group_policy: "open"    # 每条消息都回（很吵！）
```

## 保活机制

Telegram 渠道默认走 **long polling** —— bot 用一个长连接循环从 Telegram 服务器拉更新。对网络抖动很鲁棒：

- 断网就是下一次 `getUpdates` 调用失败
- 渠道层会指数退避重试
- 网络恢复后 polling 继续

不需要公网 IP、webhook 或反向代理。Telegram 的 BotFather 也不要求你这边配置任何 URL。

## 常见问题

### Bot 不回我消息

99% 是 `allow_from` 的问题：

```yaml
allow_from:
  - "123456789"   # 你真实的 id，用引号包起来（这是 string 字段）
```

空的 `allow_from: []` 表示「拒所有人」—— 包括你自己。用 `["*"]` 表示全开。

### Bot 在群里不回复

两件事要检查：

1. BotFather → `/mybots` → 你的 bot → Group Privacy → **Disabled**
2. 配置里 `group_policy: "mention"` 设了，并且你确实在消息里 `@` 了 bot

### "Conflict: terminated by other getUpdates request"

同一个 bot 你启动了两份（比如 `deeptutor bot start` 跑了两次，或者两个 DeepTutor 实例）。Telegram 一个 token 只允许一个 polling 客户端。把多余的停掉。

### 超过 4096 字的消息被截断

Telegram 单条消息上限 4096 字。Bot 会自动把过长的消息拆成多条发。如果回复非常长（比如 Deep Research 报告），更建议发文件：

```yaml
channels:
  telegram:
    send_long_as_file: true   # 回复超 4096 字时自动附 .md
```

## 语音消息

如果你在 `.env` 里配了 `TRANSCRIPTION_API_KEY`（以及 Groq Whisper 之类的转写 provider），bot 会把语音转成文字当成文本输入处理。否则语音会被忽略。

## 文件和图片

用户上传文件或图片时：

- **图片** → 作为视觉输入发给模型
- **PDF / DOCX** → 解析后作为附件（通过 `read_source` 工具可读全文）
- **其他** → 收到但忽略

## 多租户部署

多用户模式下，每个用户都可以有自己的 Telegram bot。Bot id 是按用户隔离的，所以 `alice` 和 `bob` 都可以叫 `my-tutor` 而不冲突。

如果想要组织级共享的 bot（一个 bot 给很多人用），把 bot 挂在管理员账号下，再把 `allow_from` 配一个长名单，或者直接 `["*"]`（小心）。

## 另请参阅

- [**TutorBot 概览**](/zh-cn/docs/tutorbot/) —— 架构和生命周期
- [**CLI → bot 命令**](/zh-cn/docs/cli/commands/#deeptutor-bot--tutorbot-lifecycle)
