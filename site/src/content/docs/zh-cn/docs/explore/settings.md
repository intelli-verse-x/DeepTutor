---
title: 设置
description: 统一控制中心 —— 外观、状态、LLM / Embedding / Search、Capabilities、记忆、MCP、工具。
---

设置界面在 v1.4 里被统一并按关注点拆分，采用 **草稿 / Apply** 模型 —— 改动是原子的，存之前可以回退。

![Settings overview](/screenshots/dt-settings.png)

## Tab 列表

按左侧导航的顺序：

| Tab | 控制什么 |
|-----|----------|
| **Appearance** | UI 语言和主题（Cream、Snow、Dark、Glass） |
| **Status** | LLM、embedding、search、存储后端的实时健康探测 |
| **LLM** | Provider 目录、base URL、API key、当前激活模型 |
| **Embedding** | 形态同 LLM，但作用于 embedder |
| **Search** | Web 搜索 provider（Tavily / Brave / Jina / Serper / SearXNG / DuckDuckGo / Perplexity） |
| **Capabilities** | 各 capability 可调参数（chunking、LLM 预算、dedup、最大迭代） |
| **Memory** | 开关 consolidator、配置节奏与预算 |
| **MCP servers** | 注册外部 Model Context Protocol server |
| **Tools** | 查看每个内置工具的参数、状态、i18n 状态文案 |

页面顶部有一个 **Tour** 启动器，带新用户走一遍。

## Appearance

| 设置项 | 选项 |
|--------|------|
| 语言 | English、简体中文 |
| 主题 | Cream *（默认）* / Snow / Dark / Glass |
| 侧边栏密度 | Compact / Comfortable |

## Status

一份实时健康探测：

- LLM provider —— 连接 OK / 失败 / 未配置
- Embedding provider —— 同上
- Search provider —— 同上
- 存储后端 —— 连接状态、延迟
- 每个 provider 的上次健康检查时间

排查「模型不回我」类问题时，先看这里。

## LLM / Embedding / Search

三者共享相同的 **profile** 模型：

- 可以配 **多个 profile**（比如 `openai-gpt-4o`、`anthropic-sonnet-4`、`local-ollama`）
- 在每项服务里从目录中选 **一个激活模型**
- 单回合的临时覆盖发生在聊天 composer 的模型选择器里

用 **Test** 按钮测连接 —— 它会发一个小探测请求并报延迟。

完整 provider 矩阵：[**Providers**](/zh-cn/docs/get-started/providers/)。

## Capabilities

针对 Chat、Solve、Quiz、Research、Visualize、Co-Writer 的每 capability 可调参数：

| 设置项 | 含义 |
|--------|------|
| **Chunking** | 检索到的 KB 内容如何切分进上下文窗口 |
| **LLM budget** | 单次 capability 运行的最大 token / 最大迭代 |
| **Dedup policy** | 重复源如何处理 |
| **Reference policy** | 何时插入引用 |
| **Max iterations** | agentic loop 的硬性上限 |

底层是统一的 `emit_capability_result` 信封和共享的 `UsageTracker`，会暴露 **每次调用的成本**。

## Memory

| 设置项 | 效果 |
|--------|------|
| **开关 consolidator** | 暂停 / 恢复 L1 → L2 → L3 流水线 |
| **节奏** | 每个 consolidation pass 的运行频率 |
| **预算** | 每个 consolidation pass 的 token 预算 |
| **跳转到 workbench** | 直接打开 `/memory` |

完整三层架构看 [**记忆系统**](/zh-cn/docs/explore/memory/)。

## MCP servers

**Model Context Protocol** 集成让你可以把外部 MCP server 挂成额外工具。在这里加 server 配置；它们的工具会和内置工具并列出现。

示例：

```yaml
servers:
  filesystem:
    command: npx
    args: ["-y", "@modelcontextprotocol/server-filesystem", "/Users/frank/docs"]
  github:
    command: npx
    args: ["-y", "@modelcontextprotocol/server-github"]
    env:
      GITHUB_PERSONAL_ACCESS_TOKEN: ${GITHUB_TOKEN}
```

## Tools

逐个查看每个内置工具：

- 名称、描述、参数
- 状态（启用 / 即将推出）
- i18n 状态文案（工具的进度消息在英文 / 中文下分别长什么样）
- 是否允许用户切换

五个工具支持用户全局开关：`brainstorm`、`web_search`、`paper_search`、`code_execution`、`reason`。基于上下文挂载的工具（`rag`、`read_memory`、`write_memory` 等）不能在这里切换 —— 它们会根据当前回合挂了什么自动出现。

## i18n

每个 capability 都自带一份标准的 `capabilities/prompts/{en,zh}/<name>.yaml`，保证状态消息在英文和中文下都一致。

## CLI 镜像

```bash
deeptutor config show           # 打印当前配置（secret 已脱敏）
deeptutor init                  # 重跑向导，重新逐项提示
$EDITOR data/user/settings/model_catalog.json   # 直接编辑
```

## 另见

- [**Providers**](/zh-cn/docs/get-started/providers/) —— 完整的 LLM / embedding / search provider 矩阵
- [**记忆系统**](/zh-cn/docs/explore/memory/) —— consolidator 到底干了什么
- [**多用户部署**](/zh-cn/docs/get-started/multi-user/) —— 与认证相关的设置
