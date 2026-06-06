---
title: 聊天工作台
description: 一个对话线程，五种模式，任意工具组合。DeepTutor 核心的统一智能工作台。
---

聊天工作台是大多数用户花时间最多的地方。它是单一的对话界面，承载 **五种模式**，共享同一个 session、知识库、附件和引用历史。

可以在对话中途从一个随手问的小问题切到多 agent 解题、切到 quiz、切到完整的研究报告 —— 上下文不会丢。

![Chat Workspace](/screenshots/dt-current-home.png)

## 界面拆解

| 区域 | 作用 |
|------|------|
| **左侧边栏** | 所有界面之间的导航；顶部是聊天历史 |
| **顶部工具栏** | 把当前回合存到 Notebook、导出 Markdown、新建聊天、打开右侧的 Activity / Viewer 面板 |
| **Composer**（中间） | 输入区 —— 模式选择器、附件、知识库选择器、Space 选择器、模型选择器 |
| **Activity 面板** *（右侧，可切换）* | 实时流式展示流水线阶段、工具调用、耗时 |
| **Viewer 面板** *（右侧，可切换）* | 渲染生成产物：SVG、Mermaid、Chart.js、HTML、Manim 视频 |

## 五种模式

能力选择器在 composer 里。随时可以切 —— 对话上下文会保留。

### Chat

任意工具的自由对话。默认模式 —— 大约能覆盖 80% 的问题。

Chat 流水线跑的是 **agentic loop**：LLM 调用 → 解析协议标签（THINK / TOOL / FINISH）→ 并行派发工具调用 → 把结果回喂 → 迭代直到 FINISH 或触发上下文守护。

**Chat 模式下可用的工具**（按当前上下文逐回合组装）：

| 工具 | 挂载时机 |
|------|----------|
| `rag` | 挂载了 KB |
| `read_source` | 有任意非图片类源 |
| `read_memory` / `write_memory` | 始终可用 |
| `web_search` | 在 设置 → 工具 里开启 |
| `web_fetch` | 始终可用 |
| `code_execution` | 在设置里开启 |
| `reason` | 在设置里开启 |
| `brainstorm` | 在设置里开启 |
| `paper_search` | 在设置里开启 |
| `geogebra_analysis` | 挂载了数学图片 |
| `list_notebook` / `write_note` | 至少存在 1 个 notebook |
| `github_query` | 始终可用 |
| `ask_user` | 始终可用 |

### Solve

多步解题：plan → investigate → solve → verify，并附精确的来源引用。基于 `deep_solve` agentic 引擎。

适用场景：需要分步演算的数学题、有多个子问题的物理题、推理过程需要显式展开的算法题。

常开工具：`rag`、`reason`、`code_execution`、`web_search`。

### Quiz

基于 KB 自动校验的出题。会为每道题派生一个聊天 composer，用于讨论 / 提示 / 评分。基于 `deep_question` agentic 引擎。

Quiz 内部三种子模式：

- **Custom** *（默认）* —— 按主题生成
- **Mimic** —— 上传一份历史试卷，按同样风格生成新题
- **Followup** —— 围绕之前的 quiz 题讨论，不生成新题

可配置：`num_questions`、`difficulty`、`question_types`（short_answer / mcq / numerical / code）、`per_type_counts`。

### Research

把一个主题分解成子主题，跨 RAG / web / arXiv **并行派发 agent**，产出一份带引用的报告，并支持增量 append 模式的迭代修订。

流程：

1. **Rephrasing** —— 精确复述你的问题
2. **Decomposing** —— 给出一个 3–7 子主题的提纲 ★（你在这一步确认 / 修改）
3. **Researching** —— 每个子主题跑并行 agentic loop
4. **Reporting** —— 合成结构化、带引用的 Markdown 报告

提纲确认这一步是最关键的 UX 设计：在昂贵的检索 / 推理跑起来之前，你有机会先把方向定准。

### Visualize

统一的可视化能力 —— analyzer 根据意图选 `render_type`：

| Render type | 适用 | 输出 |
|-------------|------|------|
| `svg` | 静态图、图标 | 内嵌 SVG |
| `chartjs` | 柱状 / 折线 / 饼 / 散点 | 可交互 canvas |
| `mermaid` | 流程图、序列图、状态机 | Mermaid SVG |
| `html` | 交互演示、小应用 | 沙箱化 iframe |
| `manim_video` | 数学动画 | MP4（需要 `[math-animator]` extra） |
| `manim_image` | 数学分镜 | PNG |

> Math Animator **不是独立的 capability** —— 它就是 Visualize 六种 render type 里的两种（`manim_video` / `manim_image`）。

## 累积的来源清单

一个 session 会跨回合累积引用。早些回合的 RAG / web 检索结果在同一段对话里后续依然可复用 —— 模型可以按编号引用。

## 附件

点 **Attach** 把文件带进当前回合：

| 类型 | 来源 |
|------|------|
| **PDF、DOCX、XLSX、PPTX** | 直接上传 —— 走对应的 extractor |
| **图片** | 直接上传 —— vision 模型 OCR / 解读 |
| **Notebook 记录** | Space → Notebooks 选择器 |
| **历史 session** | Space → Chat History 选择器 |
| **Question Bank 条目** | Space → Question Bank 选择器 |
| **Book 引用** | Book Engine 页面 |

附件 **不会** 塞进 system prompt —— 它们以 **工具可读的源** 的形式出现。需要时模型用 `read_source` 拉全文。

## 右上角动作

| 按钮 | 作用 |
|------|------|
| **Save to Notebook** | 把当前回合作为一条记录存到某个 notebook |
| **Download Markdown** | 把当前回合导出为 `.md` |
| **New chat** | 新建一个 session |
| **Activity** | 实时流式展示流水线事件（阶段、工具调用、耗时） |
| **Viewer** | 渲染生成产物（SVG、Mermaid、Chart.js、HTML、Manim） |

## 回合中的 `ask_user`

如果模型需要澄清，它会调 `ask_user` 工具，**暂停当前回合**，在聊天里渲染 1–3 个结构化问题。回答后点提交，回合带着你的回答继续。

## Session 连续性

每段对话都有 session id。Session 会跨：

- 浏览器刷新 / 重启
- 同一 session 内的模式切换
- Web UI ↔ CLI 边界

```bash
# 在 CLI 里继续 Web 端的 session
deeptutor chat --session sess_abc123
```

CLI 里起的 session 也会出现在 Web 侧边栏（反之亦然）。

## 记忆感知

模型通过 `read_memory` 工具内置访问你的 L3 记忆。几次 session 之后，它就会知道：

- 你的背景（`profile.md`）
- 你的知识范围（`scope.md`）
- 你明确表达过的偏好（`preferences.md`）
- 最近学了什么（`recent.md`）

完整的三层架构看 [**记忆系统**](/zh-cn/docs/explore/memory/)。

## 另见

- [**记忆系统**](/zh-cn/docs/explore/memory/) —— 三层持久化记忆 + Memory Graph
- [**知识库**](/zh-cn/docs/explore/knowledge/) —— 可直接被 RAG 使用的 Knowledge Base
- [**Space**](/zh-cn/docs/explore/space/) —— 阅读 / 回顾 中心
- [**设置**](/zh-cn/docs/explore/settings/) —— provider、工具、capability
