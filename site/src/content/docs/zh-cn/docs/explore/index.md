---
title: 概览
description: 探索章节的地图 —— 五大核心界面、三层记忆系统、统一的设置中心。
---

DeepTutor 围绕 **五大核心界面**、贯穿底层的 **三层记忆系统**，以及统一的 **设置中心** 组织。本章节会逐个介绍；下表是地图。

![DeepTutor 主页](/screenshots/dt-current-home.png)

## 五大核心界面

| # | 界面 | 一句话 | 页面 |
|---|------|--------|------|
| 1 | **Chat** | 一个对话线程，五种模式（Chat / Solve / Quiz / Research / Visualize），任意工具组合 | [**聊天工作台**](/zh-cn/docs/explore/chat-workspace/) |
| 2 | **Co-Writer** | 双栏 Markdown 工作台，AI 作为一等公民协作者 | [**Co-Writer**](/zh-cn/docs/explore/co-writer/) |
| 3 | **Book** | 多 agent 流水线把你的材料编成可交互的「活书」 | [**Book Engine**](/zh-cn/docs/explore/book/) |
| 4 | **Knowledge** | 带版本管理的、可直接被 RAG 使用的文档库（端到端 LlamaIndex 实现） | [**知识库**](/zh-cn/docs/explore/knowledge/) |
| 5 | **Space** | 阅读 / 回顾 中心：Chat History、Notebook、Question Bank、Skills | [**Space**](/zh-cn/docs/explore/space/) |

## 此外

| 界面 | 一句话 | 页面 |
|------|--------|------|
| **Memory** | 三层流水线（L1 trace / L2 per-surface / L3 cross-surface）+ Memory Graph | [**记忆系统**](/zh-cn/docs/explore/memory/) |
| **Settings** | 统一控制台 —— 模型、Embedding、搜索、Capability、工具、记忆、MCP、外观、状态 | [**设置**](/zh-cn/docs/explore/settings/) |

## 它们如何组合

- **能力住在 Chat 里**：Solve / Quiz / Research / Visualize 不是单独的顶层 Tab，而是你在 Chat 里随时切换的「模式」，共享同一个 session、知识库、附件和引用历史。
- **工具与流程解耦**：内置工具（RAG、网页搜索、代码执行、reason、brainstorm、paper 搜索、`ask_user`、`web_fetch`、`write_note`、`list_notebook`、`github_query`）可以叠加在任何模式之上。在设置里加 MCP server 还能继续扩展。
- **Memory 是底层 Substrate**：每个界面都读写同一份三层记忆，所以你在 Chat 里学到的东西也会出现在 Co-Writer、TutorBot 对话、Book 阅读里。
- **Session 横跨界面**：Web 启动的 session 在 CLI 里看得到（反之亦然）；一段聊天可以存到 Notebook、挂在 Book 页面下，或者被 Co-Writer 引用。

## 下一步

从 [**聊天工作台**](/zh-cn/docs/explore/chat-workspace/) 开始 —— 多数用户大约 80% 的时间花在这里。从命令行角度，看 [**CLI 概览**](/zh-cn/docs/cli/)。
