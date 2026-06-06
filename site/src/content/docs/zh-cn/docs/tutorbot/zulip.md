---
title: Zulip
description: 在 Zulip 上跑 TutorBot —— stream + topic 寻址、KaTeX 数学渲染，自 v1.3.9 起支持。
---

Zulip 在 **v1.3.9**（2026-05-09）加入。它用 Zulip 的 event-queue 长轮询，并支持 Zulip 独有的 **stream + topic** 寻址方式。

## 你需要准备

- 一个 Zulip 服务器（任意版本 —— Zulip Cloud 或自建）
- 在你的组织里创建 bot 的管理员权限

## Step 1 —— 创建 bot

1. 在 Zulip 里点 ⚙️ 图标（右上角）→ **Organization** → **Bots & integrations**
2. 点 **Add a new bot**
3. Bot 类型：**Generic bot**
4. 名字："Math Mentor"
5. Bot 邮箱：自动生成，比如 `math-mentor-bot@your-zulip.example.com`
6. 点 **Create bot**
7. **Download API key** 或 **Show API key** 然后复制

## Step 2 —— 把 bot 订阅到 stream

默认情况下，generic bot 能收到私信，但不会看到公开 stream，除非你订阅它。在 bot 设置里：**Streams subscribed** → 添加你希望 bot 关注的 stream。

也可以通过配置完成（`subscribe_streams` 字段）。

## Step 3 —— 配置

```yaml
channels:
  zulip:
    enabled: true
    site: "https://your-zulip.example.com"
    email: "math-mentor-bot@your-zulip.example.com"
    api_key: "YOUR_API_KEY"
    allow_from: ["*"]
    group_policy: "mention"        # 订阅的 stream 内：mention vs open
    subscribe_streams:
      - "study-help"
      - "homework"
    timeout: 60.0                  # 事件队列 poll 超时，秒
```

## Step 4 —— 启动

```bash
deeptutor bot start my-math-tutor
```

```text
[bot:my-math-tutor] channel:zulip → register event queue
[bot:my-math-tutor] channel:zulip → subscribed: [study-help, homework]
[bot:my-math-tutor] channel:zulip → ready (queue_id=q_abc)
```

## 配置参考

| 字段 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `enabled` | bool | 是 | `false` | |
| `site` | url | 是 | —— | 你的 Zulip 服务器 |
| `email` | string | 是 | —— | Zulip 给的 bot 邮箱 |
| `api_key` | string | 是 | —— | 来自 bot 创建页 |
| `allow_from` | list[string] | 可选 | `[]` | User id 或 email；`["*"]` 全开 |
| `group_policy` | `"mention" \| "open"` | 可选 | `"mention"` | stream 内 |
| `subscribe_streams` | list[string] | 可选 | `[]` | 要自动订阅的 stream |
| `timeout` | float | 可选 | `60.0` | 事件队列 poll 超时（秒） |

## Stream + topic 寻址（Zulip 特色）

Zulip 把消息按 **stream**（像频道）和 **topic**（stream 内的话题）切分。DeepTutor 按 **(stream, topic)** 对来划分 session：

- 新 topic = 新的 DeepTutor session
- 同一 topic 跨天 = 同一 session，记忆持久化
- 同 stream 里不同 topic = 不同 session

这对课堂使用非常合适：每道作业题一个独立 topic，bot 各自独立跟踪。

## Zulip 上支持的能力

| 特性 | 支持情况 |
|------|----------|
| 私信 | ✅ |
| Stream 消息 + topic | ✅ *（按 topic 隔离 session）* |
| Markdown | ✅ |
| **LaTeX / KaTeX 数学公式** | ✅ *（Zulip 原生渲染 `$$...$$`）* |
| 文件上传/下载 | ✅ |
| Mention 或 open 模式 | ✅ |
| 表情反应 | ⚠️ 只支持发出方向 |

## 保活机制

Zulip 的 **event-queue API** 是带自动恢复的长轮询：

- Bot 用 `timeout=60s` 调 `/api/v1/events?queue_id=...`
- 新事件以 JSON 返回；超时后返回空响应
- 如果 `queue_id` 过期（服务器重启、闲置太久），bot 自动注册一个新的

后台线程跑监听器，把事件桥接到 DeepTutor 的 async 总线。线程一直跑直到 bot 被停掉。

## 常见问题

### "Bad event queue id"

队列过期了（服务器重启或闲置 > 10 分钟）。渠道会自动恢复 —— 不用处理。如果反复发生，可能是 Zulip 服务器状态不太对。

### Bot 看不到 stream 消息

订阅了吗？要么在 Zulip UI（bot 设置 → Streams）做，要么通过 `subscribe_streams` 配置。

### 数学公式不渲染

Bot 输出的数学要符合 Zulip 期望的格式：

```text
行内：$x^2$

块级：
```math
\int_0^\infty e^{-x^2} dx = \frac{\sqrt{\pi}}{2}
```
```

DeepTutor 的 Zulip 渠道会自动把标准 `$...$` 和 `$$...$$` 转成 Zulip 格式。

## 另请参阅

- [**TutorBot 概览**](/zh-cn/docs/tutorbot/) —— 整体架构
- [Zulip Bot API 文档](https://zulip.com/api/) —— 参考资料
