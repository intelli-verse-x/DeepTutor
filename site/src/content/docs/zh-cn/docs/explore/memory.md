---
title: 记忆系统
description: 三层流水线（L1 / L2 / L3）、一个可审视的 workbench，以及 Memory Graph —— 审计 DeepTutor 「为什么知道它知道的事」。
---

DeepTutor 的记忆是一条 **三层流水线**，在 `/memory` 配套一个可审视的 workbench。v1 的双文件 `SUMMARY.md` / `PROFILE.md` 模型已经退役；所有内容会在首次启动时迁移到新结构。

![Memory Workbench](/images/dt-memory.png)

## 三层

| 层 | 角色 | 存储 |
|----|------|------|
| **L1 · 工作区镜像** *（LIVE）* | 按 surface、按天的 append-only 交互轨迹。真实发生过什么的无损记录。 | `trace/<surface>/<YYYY-MM-DD>.jsonl` |
| **L2 · 按 surface 摘要** *（CURATED）* | 由 consolidator 抽取出的、surface 专属的事实。每条事实都带 footnote 引用回到 L1 trace。支持按文档的 **Update / Audit / Dedup** 操作。 | `L2/<surface>.md` |
| **L3 · 跨 surface 知识** *（SYNTHESIS）* | 跨 surface 合成：你的 `profile`、`recent` 时间线、`scope` 知识范围、`preferences` 偏好。每条带保留态度（hedged）的陈述都有 L2 证据支撑。 | `L3/{recent,profile,scope,preferences}.md` |

## 七个 surface 喂养这条流水线

| Surface | L1 捕获什么 |
|---------|-------------|
| `chat` | 每个聊天回合（输入、工具调用、输出） |
| `notebook` | Notebook 的增 / 改 / 删 |
| `quiz` | Quiz 生成 + 你的答案 + 评分结果 |
| `kb` | KB 的创建 / 查询 / 索引事件 |
| `book` | Book 阅读 session、页面级交互 |
| `tutorbot` | TutorBot 消息（跨所有 channel） |
| `cowriter` | Co-Writer 的文档编辑 |

## Consolidator

Consolidator 是 **LLM 驱动** 的，异步运行（`POST /memory/runs/start` —— 也可从 workbench 触发）。你可以：

- **手动触发** —— 在 workbench 点 "Run consolidator"
- **看着 L1 → L2 → L3 流动** —— 实时进度流
- **手动编辑任意层** —— 你的编辑在下一次运行时会被合并

默认节奏（可在 **设置 → 记忆** 里调）：

| Pass | 触发时机 |
|------|----------|
| L1 → L2（按 surface） | 该 surface 每 N 个回合，或被触发时 |
| L2 → L3 跨 surface | 每天的第一个回合，或按需 |

## Memory Workbench（Web UI）

打开 `/memory`。五个子视图：

| Tab | 路由 | 内容 |
|-----|------|------|
| **L3** | `/memory/l3` *（默认）* | 四份跨 surface 文档 |
| **L2** | `/memory/l2` | 七份按 surface 文档 |
| **L1** | `/memory/l1` | 按 surface、按天的原始事件轨迹 |
| **Graph** | `/memory/graph` | Memory Graph（见下文） |
| **Resolve** | `/memory/resolve` | 通过 footnote id 反查源事件 |

## L3 详解

四份 markdown：

| 文件 | 内容 |
|------|------|
| `recent.md` | 近期学习的滚动摘要（最近几天 / 几周）—— 你在学什么、还有什么悬而未决 |
| `profile.md` | 你是谁：背景、目标、角色、学习风格 |
| `scope.md` | 你接触过的主题以及大致的掌握度 |
| `preferences.md` | 明确偏好：回复用什么语言、深度、格式、先举例还是先讲理论 |

**只有 `preferences.md` 由模型直接写**（通过 `write_memory` 工具）。另外三份由 consolidator agent 维护；你的手动编辑会在下一次 pass 时被合并进来。

## L2 详解

七份文档，每个 surface 一份。每份都是带 **footnote 风格引用** 的结构化 markdown，比如 `[^abc123]`，会链回具体的 L1 事件。

Workbench 中每份文档支持：

- **Update** —— 对该 surface 最近的 L1 事件重跑一次 consolidation
- **Audit** —— LLM 检查 L2 中过期、相互矛盾或没有依据的陈述
- **Dedup** —— 合并近似重复的要点

## L1 详解

按 surface、按天的 JSONL：

```jsonl
{"id":"evt_001","timestamp":"2026-05-21T14:23:01Z","surface":"chat","kind":"turn","content":"User asked about the chain rule"}
{"id":"evt_002","timestamp":"2026-05-21T14:23:18Z","surface":"chat","kind":"tool_call","content":"rag_search"}
{"id":"evt_003","timestamp":"2026-05-21T14:24:38Z","surface":"chat","kind":"turn_complete","content":"Explained with worked example"}
```

L1 直接看通常用处不大 —— 但 L2 的 footnote 会引用这些 id，而 **Resolve** 视图能让你从 footnote 反查到源。

## Memory Graph

![Memory Graph](/images/dt-memgraph.png)

`/memory/graph` 上的 **Memory Graph** 把 **三层一次性渲染** 出来：

- **中心** —— L3 合成节点（`profile`、`recent`、`scope`、`preferences`）
- **中圈** —— 按 surface 的 L2 事实
- **外圈** —— 按 surface 分组的 L1 trace

悬停任意节点会有内联预览。点击 **锁定高亮**，然后沿 L3 → L2 → L1 一路向内追引用 —— 这样你就能审计 DeepTutor「为什么知道」关于你的某件事。

这是杀手特性：**透明可追溯**。DeepTutor 关于你的每一条断言，你都能钻进去看依据。

## 聊天怎么读 memory

每个聊天回合开始时，system prompt 里会拼接 L3 的几份文档：

```text
─── User profile (from memory) ─────────────────────────────────────
[recent.md content]

[profile.md content]

[scope.md content]

[preferences.md content]
─────────────────────────────────────────────────────────────────────
```

模型也有 `read_memory` 工具可在回合中查询，以及 `write_memory` 用于持久化明确偏好（≤240 字符、过内容安全过滤、自动链接到触发的 L1 事件）。

## 文件布局

```text
data/user/memory/
├── trace/
│   ├── chat/2026-05-21.jsonl     ← L1
│   ├── chat/2026-05-22.jsonl
│   ├── notebook/2026-05-22.jsonl
│   ├── quiz/2026-05-22.jsonl
│   ├── kb/2026-05-22.jsonl
│   ├── book/2026-05-22.jsonl
│   ├── tutorbot/2026-05-22.jsonl
│   └── cowriter/2026-05-22.jsonl
├── L2/
│   ├── chat.md
│   ├── notebook.md
│   ├── quiz.md
│   ├── kb.md
│   ├── book.md
│   ├── tutorbot.md
│   └── cowriter.md
└── L3/
    ├── recent.md
    ├── profile.md
    ├── scope.md
    └── preferences.md
```

多用户模式下，这些位于 `multi-user/<uid>/memory/` 下。

## CLI 镜像

```bash
deeptutor memory show               # L3 拼接（默认）
deeptutor memory show chat          # 某个 L2 surface 文档
deeptutor memory show profile       # 某个 L3 文档
deeptutor memory clear all --force  # 清空所有层（破坏性操作）
deeptutor memory clear chat         # 清掉某 surface 的 L1
```

## 多用户记忆

每位用户有自己独立的 memory，位于 `multi-user/<uid>/memory/`。Memory **不会跨用户共享** —— 即便是管理员也读不到别人的 memory。

## 另见

- [**聊天工作台**](/zh-cn/docs/explore/chat-workspace/) —— 聊天怎么消费 / 写入 memory
- [**Space → Notebooks**](/zh-cn/docs/explore/space/) —— notebook 喂养 `notebook` surface
- [**设置 → 记忆**](/zh-cn/docs/explore/settings/) —— 调整 consolidation 节奏
