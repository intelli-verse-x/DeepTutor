---
title: Knowledge Bases 知识库
description: 基于 LlamaIndex 的版本化文档库，用于 RAG、Chat、Co-Writer、Book 和 Partners。
---

Knowledge Bases 是 RAG 背后的文档库，可以为 Chat turn、Co-Writer 编辑、Book 生成和 Partner 对话提供 grounding。

![Knowledge 工作台](/screenshots/knowledge.png)

## KB 包含什么

| 区域 | 作用 |
| --- | --- |
| **Files** | 源文档与解析状态。 |
| **Add documents** | 上传 PDF、Office 文件、Markdown、文本、代码和数据文件。 |
| **Index versions** | 基于 embedding signature 的 flat `version-N` LlamaIndex storage。 |
| **Settings** | Embedding model、chunking 和检索相关参数。 |

## 版本模型

Re-index 会写入新的 `version-N` 目录，并保留旧版本。这样 rebuild 时不会覆盖当前可用 index。旧版本应理解为保留历史和 fallback storage；除非你的部署显式暴露相关操作，不要把它描述成完整的用户可见 rollback workflow。

## CLI 对应命令

```bash
deeptutor kb list
deeptutor kb info physics
deeptutor kb create physics --doc chapter1.pdf
deeptutor kb create textbooks --docs-dir ./pdfs
deeptutor kb add physics --doc chapter2.pdf
deeptutor kb search physics "What is angular momentum?"
deeptutor kb set-default physics
deeptutor kb delete physics --force
```

## 建议

- 创建正式 KB 前，先配置 embedding provider。
- 更换 embedding model 后应 re-index，不要混用向量空间。
- 保留一个小 KB 用于 Partner/channel smoke test。
- Docker 部署要持久化整个 `data/`，否则 KB versions 会随容器丢失。

## 相关页面

- [聊天工作台](/zh-cn/docs/explore/chat-workspace/) —— 把 KB 挂到 turn 上
- [Book Engine](/zh-cn/docs/explore/book/) —— 从 KB 编译学习材料
- [Partners](/zh-cn/docs/explore/partners/) —— 把 KB 复制进 partner workspace
