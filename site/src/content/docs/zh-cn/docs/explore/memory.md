---
title: Memory 记忆系统
description: 通过 L1 trace、L2 surface summaries、L3 synthesis 和 Memory Graph 实现可审计个性化。
---

Memory 是 DeepTutor 的可审计个性化系统。它不是隐藏的向量库，而是一个文件化的三层 pipeline，可以查看、编辑、审计。

![Memory workbench](/screenshots/memory-workbench.png)

## 三层结构

![Memory 概览页：L1、L2、L3 三层卡片](/screenshots/memory.png)

Memory 概览页一眼看全三层 —— 实时 L1 traces、按 surface 精炼的 L2 facts、跨 surface 综合的 L3 knowledge —— 以及 Memory graph 入口。点击任意层级卡片即可查看或整理。

| 层级 | 存储 | 作用 |
| --- | --- | --- |
| **L1 trace** | `trace/<surface>/<YYYY-MM-DD>.jsonl` | Append-only 原始事件。 |
| **L2 surface facts** | `L2/<surface>.md` | 每个 surface 的精炼事实，并引用回 L1。 |
| **L3 synthesis** | `L3/<recent|profile|scope|preferences>.md` | 跨 surface 综合，用于个性化。 |

支持的 surfaces 是 `chat`、`notebook`、`quiz`、`kb`、`book`、`tutorbot`、`cowriter`。`tutorbot` 这个 surface 名称为兼容旧 memory 数据保留；产品层面的持久伙伴已经是 Partners。

概览页把 L1 呈现为 **workspace mirror**：在原始 trace 之外，DeepTutor 还为每个 surface 保留一份实时工作区 snapshot，点 Refresh 会把变化记录进 L1。

## Memory Graph

![Memory graph](/screenshots/memory-graph.png)

Graph view 可以把一个 L3 高层结论追溯到 L2 支撑事实，再追溯到 L1 原始事件。它适合回答：“DeepTutor 为什么认为它知道这件事？”

## CLI

```bash
deeptutor memory show L3
deeptutor memory show L2
deeptutor memory show profile
deeptutor memory show chat
deeptutor memory clear trace --force
```

## 建议

- 长期学习工作流建议保持 memory 开启。
- 如果 DeepTutor 的语气或假设不对，优先检查 L3 preferences。
- 如果只想删除某个 surface 的原始历史，可以只清 L1 trace，而不是全部 memory。
- 多用户模式下，每个用户都有自己 workspace 作用域里的 memory。
