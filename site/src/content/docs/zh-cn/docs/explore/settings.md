---
title: Settings 设置
description: DeepTutor 的统一控制面：外观、状态、网络、模型目录、Embedding、搜索、MinerU、Capabilities、Memory、MCP 和工具。
---

Settings 是 DeepTutor 的运行控制面。多数配置采用 draft-and-apply 模型，可以先测试 provider，再正式保存。

![Settings 工作台](/screenshots/settings.png)

## 主要分区

| 分区 | 控制什么 |
| --- | --- |
| **Appearance** | 主题、语言、侧边栏偏好。 |
| **Status** | Backend 和各模型服务当前实际生效状态。 |
| **Network** | Backend/frontend ports、external API base、CORS origins。 |
| **LLM** | 模型目录 profiles、base URL、API key、active models。 |
| **Embedding** | Knowledge / RAG 使用的 embedding provider。 |
| **Search** | Web/search provider 配置。 |
| **MinerU PDF** | 本地或云端 PDF parsing backend。 |
| **Capabilities** | Chat、Solve、Question、Research、Visualize、Co-Writer 等 pipeline 的预算和参数。 |
| **Memory** | Consolidation 控制和 Memory workbench 入口。 |
| **MCP servers**（仅 admin） | 外部 MCP tool 注册。 |
| **Tools** | 内置工具、上下文工具、coming-soon 工具和用户可切换工具。 |

## 分区详解

### Appearance

主题、界面语言、侧边栏偏好。纯客户端展示配置，不涉及 provider 凭证。

### Status

只读面板，显示 backend 以及当前配置实际解析到的 LLM、embedding、search endpoints。Status 反映上次 **Apply** 之后的运行时取值——draft 修改在 Apply 前不会出现在这里。

### Network

Backend/frontend ports、反向代理部署时浏览器客户端使用的 external API base，以及 CORS origins。

### LLM

![LLM 设置：provider profiles、连接字段和模型目录](/screenshots/settings-llm.png)

语言模型 profiles。每个 profile 是一条 provider connection——provider 类型、base URL、API key、可选 extra headers——加上模型目录：每个模型登记 model ID 和 context window。Active model 用于 Chat 和大多数 agent reasoning。

### Embedding

Embedding 模型 profiles，布局与 LLM 一致（provider connection + models），但登记的是 embedding 模型及其 dimensions。供检索和知识库 ingestion 使用。

### Search

`web_search` 工具及任何需要访问开放网络的 agent step 所用的 web search providers。配置 provider、base URL、API key 后，可在 diagnostics 面板跑一次测试查询。

### MinerU PDF

![MinerU PDF 设置：parsing backend 与本地安装检测](/screenshots/settings-mineru.png)

从上传试卷生成题目时使用的 PDF parsing backend。可选本地 MinerU 安装或 mineru.net 云端 API。本地解析时，页面会检测 MinerU CLI、支持手动指定 CLI path，并管理约 1-2 GB 的模型权重下载（HuggingFace 或 ModelScope）。

### Capabilities

![Capabilities 设置：按 capability 的参数](/screenshots/settings-capabilities.png)

按 capability 的 LLM 参数和运行时旋钮：Chat、Solve、Question、Research、Visualize、Co-Writer 等 pipeline 的 temperature、token 预算和循环上限。Chat 还包括 max rounds 和独立的 exploring/responding token 预算。取值持久化到 `data/user/settings/agents.yaml`（LLM 参数）和 `main.yaml`（运行时旋钮）。

### Memory

调节 chunk-based memory consolidator：**Update** 和 **Audit** 在每个 L2 surface、每个 L3 slot 上的 LLM-round 预算，以及 **Dedup** 迭代次数和是否在 Update 后自动跑 dedup。

### MCP servers（仅 admin）

注册外部 MCP（Model Context Protocol）servers，把它们的工具暴露给 chat agent。先测连接再保存。多用户部署中此分区仅 admin 可见。

### Tools

![Tools 设置：用户可切换工具与内置工具](/screenshots/settings-tools.png)

开关用户可切换工具。**Experience enhancement** 工具（`brainstorm`、`web_search`、`paper_search`、`reason`）由你自由切换；**built-in** 工具如 `rag` 和 code execution 是锁定的，chat agent 需要时自动挂载。

## 部署注意点

- 项目根目录 `.env` 不作为应用配置读取。
- 运行时配置在 `data/user/settings/*.json`，除非设置了 `DEEPTUTOR_HOME` 或 `deeptutor start --home`。
- Docker 浏览器客户端必须同时能访问 frontend 和 backend。反向代理部署时，在 **Network** 配置 external API base。
- 用户可切换工具是 `brainstorm`、`web_search`、`paper_search`、`reason`；其它工具按上下文或运行时能力自动挂载。

## Provider 测试

Apply 前先点 **Test**。测试通过只说明 profile 可以完成最小调用，并不代表该模型适合所有 capability。

## 相关页面

- [Providers](/zh-cn/docs/get-started/providers/) —— 模型/搜索配置示例
- [Docker](/zh-cn/docs/get-started/docker/) —— 端口和反向代理说明
- [Memory](/zh-cn/docs/explore/memory/) —— 检查 memory 状态
