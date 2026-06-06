---
title: 知识库
description: 专为驱动 RAG 的文档集合而设的工作区。端到端 LlamaIndex 实现，版本化索引，抗漂移。
---

一个专门管理驱动 RAG 的文档集合的工作区。每个 KB 是一份对你文档的版本化、可检索的索引 —— 可挂到任意聊天回合、Co-Writer 文档或 Book。

![Knowledge Workspace](/screenshots/dt-knowledge.png)

## 每个 KB 四个 tab

| Tab | 内容 |
|-----|------|
| **Files** | 浏览已上传的源、在线预览 PDF、看每个文件的大小 / 状态 |
| **Add documents** | 拖入 PDF、Office 文件（DOCX / XLSX / PPTX）、Markdown、纯文本以及一大票代码 / 数据格式 —— 自动走对应的 extractor |
| **Index versions** | 每次（重新）建索引都是一个被追踪的版本。可以回滚到旧版、对比不同 embedding 模型、查看 chunking 统计 —— 不会丢掉之前的 build |
| **Settings** | 选 embedding provider / 模型、chunking 参数、reranker。默认值从全局 LLM 和 embedding profile 继承 |

## 端到端基于 LlamaIndex

索引部分端到端基于 **LlamaIndex**。之前的双流水线拆分在 v1.4 refactor 中合并掉了。特性：

- **可重试的 re-index** —— 部分失败不会丢进度
- **Embedding 不匹配检测** —— 换了 embedder 时会先警告，避免静默产出坏结果
- **健壮的持久化向量处理** —— 损坏向量会被隔离，而不是整体崩
- **版本化索引** —— 每次重建都是新版本，可对比、可回滚

## 支持的文档类型

| 类型 | 说明 |
|------|------|
| **PDF** | 文本抽取；扫描页尽力 OCR |
| **DOCX** | 原生 Word 文档 |
| **XLSX** | 表格 —— 每个 sheet 作为一个 chunk batch |
| **PPTX** | PowerPoint —— 每张幻灯片作为一个 chunk |
| **TXT / MD / HTML** | 清洗并切片 |
| **代码文件** | Python / JS / TS / Go / Rust 及大量其他语言 |

## 创建一个 KB

在 UI 里：

1. 左侧栏 **Knowledge** → **+ New knowledge base**
2. 起名，选 RAG provider *（默认 LlamaIndex）*
3. 上传文档 —— 拖拽或文件选择器
4. **Create**

DeepTutor 会抽取、切片、对每个 chunk 做 embedding，并存好向量索引。一个 200 页的 PDF 通常 1–3 分钟。

## 默认 KB

打了 ⭐ 的 KB 是 **默认 KB** —— 新建聊天时会自动挂上。点星号可切换默认 KB。

## 索引版本

每次（重新）建索引都会被追踪：

- **回滚** —— 重建后检索质量变差时可以还原旧版
- **对比** —— 对同样的源文档做不同 embedding 模型 / chunking 策略的 A/B
- **检查** —— chunking 统计、embedding 维度、建索引耗时

## 在 UI 里搜索

KB 内部的搜索框跑的是临时 query。三种模式：

| 模式 | 算法 |
|------|------|
| **Hybrid** *（默认）* | 语义 embedding + BM25 关键词重排 |
| **Vector** | 纯 embedding |
| **Keyword** | 纯 BM25 |

## 在聊天里搜索

在 composer 里挂上 KB，自然提问就行 —— 模型自己决定要不要调 `rag`：

```text
You> [KB: physics attached] What's the relationship between kinetic energy and momentum?

Model> [calls rag tool]
  ● rag_search(query="kinetic energy momentum relationship", kb_name="physics")
  │ KE = p²/(2m), where p is momentum and m is mass...
  └ #1 rag

Model> [synthesizes a reply citing the retrieved passages]
```

## 多 KB 工作流

一个回合可以挂多个 KB。模型会并行查询。适合「对比两本教材」「在多篇 paper 里找同一概念」之类的任务。

## CLI 镜像

```bash
deeptutor kb list                                           # 所有 KB
deeptutor kb info physics                                   # KB 详情
deeptutor kb create physics --doc chapter1.pdf              # 创建
deeptutor kb create textbooks --docs-dir ./pdfs/            # 从目录创建
deeptutor kb add physics --doc chapter3.pdf                 # 增量添加
deeptutor kb search physics "What is angular momentum?"     # 临时检索
deeptutor kb set-default physics                            # 设为默认
deeptutor kb delete physics --force                         # 删除
```

完整 flag 参考看 [**Commands**](/zh-cn/docs/cli/commands/)。

## Embedding provider

Embedder 在 **设置 → Embedding** 里全局配置。新 KB 会继承当前值；已有的 KB 会保留它创建时的 embedder，直到被重新索引。

| Provider | 说明 |
|----------|------|
| OpenAI | `text-embedding-3-small`（1536d） / `-large`（3072d） |
| Cohere | `embed-v4.0` |
| Jina | `jina-embeddings-v3` |
| Gemini | `gemini-embedding-001` |
| SiliconFlow | `Qwen/Qwen3-Embedding-8B` |
| Aliyun DashScope | `qwen3-vl-embedding` |
| Ollama | 本地 embedding 模型 |
| vLLM / LM Studio / OpenAI 兼容 | 自定义 embedding endpoint |

完整 provider 矩阵：[**Providers**](/zh-cn/docs/get-started/providers/)。

## 多用户

多用户部署下，KB 按用户隔离。管理员可以在 `/admin/grants` 授予跨用户访问权限（read / read+search / read+search+modify）—— 见 [**多用户部署**](/zh-cn/docs/get-started/multi-user/)。

## 另见

- [**聊天工作台**](/zh-cn/docs/explore/chat-workspace/) —— 把 KB 挂到聊天回合
- [**Book Engine**](/zh-cn/docs/explore/book/) —— 书是从 KB 编译出来的
- [**记忆系统**](/zh-cn/docs/explore/memory/) —— KB 装的是文档，memory 装的是对话
