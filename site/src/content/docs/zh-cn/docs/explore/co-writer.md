---
title: Co-Writer 协同写作
description: AI 作为一等公民协作者的 Markdown 编辑器 —— Edit Agent、Narrator Agent、文档模板。
---

**Co-Writer** 是 DeepTutor 围绕 AI 协作设计的 Markdown 编辑器。内置两个 AI agent：

- **Edit Agent** —— 改写选中文本（rewrite、扩写、压缩、改风格）
- **Narrator Agent** —— 生成新内容（接着写、把提纲填成正文、解释某个概念）

外加文档模板、版本历史，以及与知识库的集成。

## 打开 Co-Writer

点左侧导航的 **Co-Writer**，或访问 `/co-writer`。第一次进来会看到文档选择器。选 **+ New document** 从零开始，或打开一个最近的。

## 编辑器

标准 Markdown 编辑器，双栏：

| 栏 | 内容 |
|----|------|
| **左** | Markdown 源码 —— 输入、编辑、格式化 |
| **右** | 渲染预览（可关掉以全宽看源码） |

快捷键：

| 键 | 动作 |
|----|------|
| `⌘B` / `Ctrl+B` | 加粗 |
| `⌘I` / `Ctrl+I` | 斜体 |
| `⌘K` / `Ctrl+K` | 插入链接 |
| `⌘S` / `Ctrl+S` | 保存（其实一直在自动保存） |
| `⌘/` / `Ctrl+/` | 切换 AI 侧栏 |

## AI 侧栏

用 `⌘/` 打开。两个 tab：

### Edit（基于选区）

在编辑器里选中文本，挑一个 Edit 动作：

| 动作 | 作用 |
|------|------|
| Rewrite | 同义改写 |
| Expand | 补细节、补背景、补例子 |
| Condense | 压缩，但保留要点 |
| Change tone | 正式 / 口语 / 学术 / 友好 |
| Fix grammar | 仅做轻微润色 |
| Translate | 翻译成另一种语言 |

Edit Agent 会用结果替换选中文本。`⌘Z` 可撤销。

### Narrator（基于光标）

把光标放到你想生成新内容的位置，然后：

| 动作 | 作用 |
|------|------|
| Continue | 从这里接着写 |
| Fill outline | 把你的项目符号提纲展开成正文 |
| Explain | 给上一段加一段解释 |
| Cite from KB | 去挂载的 KB 里查点东西并附引用 |

Narrator Agent 会在光标处插入内容。

## 挂载上下文

和 Chat 一样，Co-Writer 也能挂上下文：

- **知识库** —— Narrator 生成时可以从你的 KB 里取材
- **历史 session** —— 引用之前的 Chat / Research 回合
- **Notebook 记录** —— 从存好的片段里取

点 AI 侧栏的回形针图标。

## 模板

DeepTutor 自带几个示例模板：

| 模板 | 适用 |
|------|------|
| Research memo | 多源综合写作，带引用 |
| Lecture notes | 提纲 + 展开的小节 |
| Problem set solutions | 带代码块的题解 |
| Reading log | 一篇 paper / 一章一条记录 |

新建文档时挑一个。模板会预填好结构，里面的 prompt 提示也是 agent 能上下文理解的。

## 嵌入其他 capability 的产物

可以直接把 DeepTutor 其他 capability 的结果嵌进文档：

- **Deep Solve 结果** → 把解答拖到 Co-Writer
- **Visualize 产物** → 内嵌为 SVG / Mermaid 块
- **Quiz** → 内嵌为可展开的 details 块

## 保存与导出

文档每几秒自动保存。手动导出选项：

- **Download .md** —— 原始 Markdown
- **Download .pdf** —— 通过 Pandoc 渲染
- **Copy to clipboard** —— 粘到其他工具里

## 版本历史

点右上的时钟图标看版本历史。Co-Writer 会保留：

- 最近 24 小时的全部保存
- 最近 7 天的小时级快照
- 永久保留的天级快照

一键回滚到任意历史版本。

## 多用户须知

多用户模式下，每位用户有自己独立的 Co-Writer 文档空间。共享功能在路线图上（关注 [issue #498](https://github.com/HKUDS/DeepTutor/issues/498)）。

## 另见

- [**知识库**](/zh-cn/docs/explore/knowledge/) —— 挂 KB 拿到 ground-truth 引用
- [**聊天工作台**](/zh-cn/docs/explore/chat-workspace/) —— 跑 Visualize / Research，把产物带进文档
- [**Space**](/zh-cn/docs/explore/space/) —— 保存并复用持久化产物
