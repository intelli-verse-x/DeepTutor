---
title: Co-Writer
description: 支持选区 AI 编辑的 Markdown 工作台，编辑可基于 KB 或 Web 上下文。
---

Co-Writer 是面向笔记、报告、教程和学习草稿的 Markdown 工作台。它把 source editor 和实时 preview 放在一起，让 agent 只编辑你选中的文本，而不是整篇重写。

## 打开方式

从侧边栏打开 **Co-Writer**，或访问 `/co-writer`。可以新建空白 draft，也可以从 sample template 开始。

## 编辑器模型

![Co-Writer 编辑器：左侧 Markdown 源码，右侧实时预览](/screenshots/co-writer.png)

工作区是双栏视图：左侧写 Markdown 源码，右侧实时渲染 preview，格式工具栏在编辑区上方。在源码区选中文本即可唤出 AI 编辑入口（`rewrite`、`expand`、`shorten`），不需要离开文档。

| 部分 | 作用 |
| --- | --- |
| **Document list** | 创建、打开、重命名、删除 Markdown drafts。 |
| **Source editor** | 写 Markdown、表格、代码、数学公式、Mermaid 风格图和结构化笔记。 |
| **Preview pane** | 实时渲染文档。 |
| **Selection popover** | 选中文本后执行 `rewrite`、`expand`、`shorten`。 |
| **Save to Notebook** | 把完成的 draft 保存为可复用上下文。 |

## AI 编辑

Edit agent 会收到选中文本、你的指令、可选 KB 上下文、可选 Web 上下文和周围文档内容。因此它适合：

- 在不改变章节结构的情况下润色解释，
- 把简短笔记扩成教程段落，
- 把长草稿压缩成 Notebook 可复用摘要，
- 让某个论断基于选定知识库重新表述。

## 推荐流程

1. 先用 Markdown 粗写。
2. 只选中需要帮助的段落。
3. 用 **Rewrite**、**Expand** 或 **Shorten**。
4. 继续写之前先人工检查结果。
5. 定稿后保存到 Notebook，成为长期上下文。

## 存储

Co-Writer 文档位于当前用户 workspace 下；多用户部署里各用户 draft 隔离。Partners 可以使用复制过去的 notebooks/skills，但不会直接编辑用户的 Co-Writer drafts。

## 相关页面

- [聊天工作台](/zh-cn/docs/explore/chat-workspace/) —— 生成素材并保存有用 turn
- [Space](/zh-cn/docs/explore/space/) —— 管理 notebooks、skills 和 personas
- [Knowledge](/zh-cn/docs/explore/knowledge/) —— 为编辑提供 grounded context
