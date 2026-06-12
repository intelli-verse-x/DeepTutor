---
title: 概览
description: 探索章节地图 —— Chat、Partners、Co-Writer、Book、Knowledge、Space、Memory、Settings。
---

DeepTutor 由一组彼此连通的学习界面组成，它们共享同一套 agent-native runtime。本章节先介绍用户每天会用到的界面，再解释底层的资源库、记忆和控制面。

![Chat 工作台](/screenshots/chat.png)

## 产品地图

| # | 界面 | 一句话 | 页面 |
|---|------|--------|------|
| 1 | **Chat** | 默认 agent loop：工具、RAG、附件、Notebook 写入和深层 capability 都在同一线程里 | [**聊天工作台**](/zh-cn/docs/explore/chat-workspace/) |
| 2 | **Partners** | 拥有独立 soul、资源库和渠道的 IM 持久伙伴 | [**Partners 伙伴**](/zh-cn/docs/explore/partners/) |
| 3 | **Co-Writer** | 支持选区 AI 编辑的 Markdown 编辑器，可接入 KB 或 Web 上下文 | [**Co-Writer**](/zh-cn/docs/explore/co-writer/) |
| 4 | **Book** | 把你的材料编译成可交互的 living books | [**Book Engine**](/zh-cn/docs/explore/book/) |
| 5 | **Knowledge** | 基于 LlamaIndex 的版本化 RAG 文档库 | [**知识库**](/zh-cn/docs/explore/knowledge/) |
| 6 | **Space** | Skills、personas、notebooks、history 和可复用上下文资产 | [**Space**](/zh-cn/docs/explore/space/) |
| 7 | **Memory** | L1 trace、L2 per-surface facts、L3 cross-surface synthesis 和图谱审计 | [**Memory**](/zh-cn/docs/explore/memory/) |
| 8 | **Settings** | 模型、Embedding、搜索、工具、MCP、网络、记忆和运行时控制 | [**Settings**](/zh-cn/docs/explore/settings/) |

## 它们如何组合

- **Chat 是默认 loop。** `chat`、`deep_solve`、`deep_question`、`deep_research`、`visualize`、`math_animator`、`auto`、`mastery_path` 都运行在同一个 orchestrated runtime 上。
- **Partners 复用 Chat，而不是另一套 bot engine。** 一条 partner 消息会进入 `data/partners/<id>/workspace/` 作用域里的 chat turn。
- **工具按上下文挂载。** 用户可切换工具是 `brainstorm`、`web_search`、`paper_search`、`reason`；上下文工具包括 RAG、source reading、memory、skills、notebooks、URL fetch、GitHub、ask-user 和 sandboxed execution。
- **Memory 可审计。** Workbench 和 graph 可以把综合事实一路追溯到 L2 summaries 和原始 L1 events。

## 下一步

先读 [**聊天工作台**](/zh-cn/docs/explore/chat-workspace/) 理解核心交互模型；如果想把 DeepTutor 接到 IM 渠道，再读 [**Partners 伙伴**](/zh-cn/docs/explore/partners/)。
