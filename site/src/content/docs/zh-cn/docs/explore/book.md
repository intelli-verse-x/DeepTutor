---
title: Book Engine
description: 从知识库、Notebook、Question Bank 和 Chat history 生成可交互 living books。
---

Book 会把你的材料变成可交互学习内容。一本书可以从 topic 和选定 sources 开始，生成解释、quiz、视觉 blocks 和读者笔记。

<p align="center">
  <img src="/screenshots/book01.png" alt="Book 阅读视图" width="31%" />
  <img src="/screenshots/book02.png" alt="Book 交互 block 视图" width="31%" />
  <img src="/screenshots/book03.png" alt="Book 创建视图" width="31%" />
</p>

## 创建流程

1. 打开 **Book -> New book**。
2. 选择 topic 和 sources：Knowledge Bases、Notebooks、Question Bank 或 Chat history。
3. 编译前先 review 生成的 proposal。
4. 让 BookEngine 生成 page plans 和 blocks。
5. 阅读、批注、做题，或在页面旁边继续 chat。

## Block 类型

Book pages 由 typed blocks 组成：text、sections、callouts、quiz、flash cards、timeline、code、figure、interactive HTML、animation、concept graph、deep dive、user note。目标不是生成 PDF 式内容堆砌，而是一个可继续学习的环境。

## Source drift

Books 会记录 source fingerprints。如果知识库在编译后发生变化，可以用维护命令检查 drift：

```bash
deeptutor book list
deeptutor book health <book_id>
deeptutor book refresh-fingerprints <book_id>
```

## Source 怎么选

| Source | 适用场景 |
| --- | --- |
| Knowledge Base | 需要基于教材/论文的 grounded 内容。 |
| Notebook | 已经有人工整理过的笔记或总结。 |
| Question Bank | 想以练习题为中心组织页面。 |
| Chat History | 想把一次辅导对话变成学习材料。 |

## 相关页面

- [Knowledge](/zh-cn/docs/explore/knowledge/) —— 先构建文档库
- [聊天工作台](/zh-cn/docs/explore/chat-workspace/) —— 围绕 book page 继续讨论
- [CLI 命令](/zh-cn/docs/cli/commands/) —— book 维护命令
