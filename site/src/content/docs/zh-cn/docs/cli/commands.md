---
title: 命令参考
description: 每个 deeptutor 命令 —— flag、输出 schema、示例。
---

本页列出每个 `deeptutor` 子命令和 flag。交互式 REPL 用法见 [**交互式 REPL**](/zh-cn/docs/cli/chat-repl/)。自动化模式见 [**代理交接**](/zh-cn/docs/cli/agent-handoff/)。

## `deeptutor run` —— 单次 capability 执行

执行一次 capability turn 然后退出。这是 agent 和脚本最基础的 "干活" 命令。

```bash
deeptutor run <capability> "<message>" [options]
```

### Flag

| Flag | 类型 | 默认值 | 作用 |
|------|------|--------|------|
| `--session <id>` | string | *(新建)* | 续上一个已有 session |
| `-t / --tool <name>` | 可重复 | `[]` | 启用某个 tool（如 `rag`、`web_search`、`code_execution`、`reason`） |
| `--kb <name>` | 可重复 | `[]` | 挂载一个知识库 |
| `--notebook-ref <id[:record,...]>` | 可重复 | `[]` | 挂载 notebook 记录 |
| `--history-ref <session_id>` | 可重复 | `[]` | 引用一个历史 session |
| `-l / --language <code>` | string | `en` | 回复语言 |
| `--config <key=value>` | 可重复 | `[]` | 单个 capability 的 config 覆盖 |
| `--config-json <json>` | string | —— | 以 JSON 形式提供 base config；后续 `--config key=value` 会覆盖同名 key |
| `-f / --format <rich\|json>` | enum | `rich` | 输出模式 |

### 示例

```bash
# 简单 chat turn
deeptutor run chat "用大白话解释量子纠缠"

# Deep Solve，带 reasoning + 针对某个 KB 的 RAG
deeptutor run deep_solve "求 d/dx [sin(x²)]" --tool reason --tool rag --kb math

# 生成 5 道测验题
deeptutor run deep_question "线性代数的特征向量" \
  --config num_questions=5 --config difficulty=hard

# Deep Research，JSON 流
deeptutor run deep_research "检索增强生成最近有什么新进展？" \
  --tool web_search --tool rag --kb papers \
  --config mode=report --config depth=standard \
  --format json

# 续上一个 session
deeptutor run chat "接着刚才的继续" --session sess_abc123
```

### 输出 —— `--format rich`（默认）

按 stage 渲染 Markdown 富文本。示例：

```text
▶ retrieving
  ● rag_search(query="chain rule")
  │ Chain rule: d/dx[f(g(x))] = f'(g(x)) · g'(x)
  └ #1 rag — +5 more lines; run /show 1 to expand

▶ reasoning
  [dim]Applying chain rule with u = x², du/dx = 2x[/]
  [dim]d/dx[sin(u)] = cos(u) · du/dx[/]

▶ formulating

The derivative of sin(x²) is:

**2x · cos(x²)**

[dim]session=sess_abc123 turn=turn_xyz789 capability=deep_solve[/]
```

### 输出 —— `--format json`

每行一个 JSON 对象。方便管道给其他工具：

```text
{"type": "stage_start", "stage": "retrieving"}
{"type": "tool_call", "content": "rag_search", "metadata": {"args": {"query": "chain rule"}}}
{"type": "tool_result", "content": "Chain rule: ...", "metadata": {"tool": "rag"}}
{"type": "stage_end", "stage": "retrieving"}
{"type": "stage_start", "stage": "reasoning"}
{"type": "thinking", "content": "Applying chain rule..."}
{"type": "stage_end", "stage": "reasoning"}
{"type": "stage_start", "stage": "formulating"}
{"type": "content", "content": "The derivative of sin(x²) is **2x · cos(x²)**"}
{"type": "stage_end", "stage": "formulating"}
{"type": "done", "metadata": {"session_id": "sess_abc123", "turn_id": "turn_xyz789"}}
```

事件类型：`stage_start`、`stage_end`、`content`、`thinking`、`progress`、`tool_call`、`tool_result`、`error`、`done`。

## `deeptutor chat` —— 交互式 REPL

进入一个交互式 chat session，用 `/slash` 命令在会话内做配置。

```bash
deeptutor chat [options]
```

flag 和 `run` 里塑形 turn 的那一组一样：`--session`、`--tool`、`--capability`、`--kb`、`--notebook-ref`、`--history-ref`、`--language`、`--config`、`--config-json`。完整说明见 [**交互式 REPL**](/zh-cn/docs/cli/chat-repl/)。

## `deeptutor init` —— 引导式初始化向导

```bash
deeptutor init                # 完整配置（询问端口 + LLM + embedding + 搜索）
deeptutor init --cli          # 仅 CLI（跳过端口问题）
deeptutor init --home /path   # 使用非默认工作区
```

完整流程见 [**Get Started**](/zh-cn/docs/get-started/)。

## `deeptutor start` / `deeptutor serve`

```bash
# 同时启动后端 + 前端（阻塞；Ctrl+C 同时停掉）
deeptutor start
deeptutor start --home /path

# 仅后端
deeptutor serve --host 0.0.0.0 --port 8001
deeptutor serve --reload                # 文件变动时热重载（仅开发用）
```

## `deeptutor kb` —— 知识库管理

### `kb list`

```bash
deeptutor kb list                # Rich 表格
deeptutor kb list --format json
```

JSON 输出：

```json
[
  {
    "name": "physics",
    "status": "ready",
    "documents": 12,
    "rag_provider": "llamaindex",
    "is_default": true
  },
  {
    "name": "math",
    "status": "indexing",
    "documents": 4,
    "rag_provider": "llamaindex",
    "is_default": false
  }
]
```

### `kb info <name>`

```bash
deeptutor kb info physics
```

返回这个 KB 的元数据、文档列表、统计信息和索引状态。

### `kb create <name>`

```bash
# 单个文档
deeptutor kb create physics --doc chapter1.pdf

# 多个文档
deeptutor kb create physics --doc chapter1.pdf --doc chapter2.pdf --doc exercises.docx

# 整个目录
deeptutor kb create textbooks --docs-dir ./my-pdfs
```

支持格式：PDF、DOCX、XLSX、PPTX、TXT、MD、HTML。

### `kb add <name>`

往已有 KB 里增量添加文档：

```bash
deeptutor kb add physics --doc chapter3.pdf
```

### `kb delete <name>`

```bash
deeptutor kb delete physics              # 要求确认
deeptutor kb delete physics --force      # 跳过确认
```

### `kb set-default <name>`

```bash
deeptutor kb set-default physics
```

默认 KB 是指当没有显式指定时，`deeptutor chat` 和 Web UI 会自动挂载的那个。

### `kb search <name> <query>`

```bash
deeptutor kb search physics "什么是角动量？"
deeptutor kb search physics "..." --mode hybrid --format json
```

模式：`hybrid`（默认；语义 + 关键词）、`vector`（仅语义）、`keyword`（BM25）。

### 重新索引

重新索引不是一个 CLI 命令 —— 要从 **Web UI**（Knowledge → 选 KB → **Index versions** 标签页 → **Re-index now**）触发。换了 embedding 模型后通常需要这一步。

## `deeptutor skill` —— 技能库与 Hub

```bash
deeptutor skill list                              # 本地技能列表，含 hub 来源信息
deeptutor skill search "git release notes"        # 在 hub 上语义搜索（默认 clawhub）
deeptutor skill install clawhub:gh-release-notes  # 校验 → 下载 → 注册
deeptutor skill install some-skill@1.2.0          # hub 前缀默认 clawhub；@ 钉住版本
deeptutor skill remove gh-release-notes
```

Hub 引用格式为 `<hub>:<slug>[@version]`。所有安装都过同一道导入门：先查 hub 的安全裁定（被标记的包除非显式传 `--allow-unverified` 否则拒装）、压缩包带 zip-slip / zip-bomb 防护解压、支持文件过文本/脚本后缀白名单（二进制永远进不了工作区）、frontmatter 里的 `always:` 会被剥掉 —— 下载来的包不可能把自己注入每条 system prompt。来源信息（hub、版本、裁定）记录在技能旁边的 `.hub-lock.json` 里。

`install` 的 flag：`--name` 换个本地名字安装，`--force` 覆盖同名技能，`--allow-unverified` 无视可疑裁定继续装。

ClawHub 之外的注册表在 `settings/skill_hubs.json` 里声明 —— `type: "clawhub"` 指向任意兼容的 HTTP API，`type: "command"` 包一个把包下载到 `{dest}` 的命令行工具。在多用户部署里，这套 CLI 操作的是管理员工作区：装好的技能在 grant 分配之前对其他用户不可见。

## `deeptutor session` —— session 查看

### `session list`

```bash
deeptutor session list --limit 20
```

### `session show <id>`

```bash
deeptutor session show sess_abc123                 # Rich
deeptutor session show sess_abc123 --format json   # 完整 JSON
```

JSON 输出（截断版）：

```json
{
  "id": "sess_abc123",
  "title": "Chain rule explanation",
  "capability": "chat",
  "status": "completed",
  "messages": [
    {"role": "user", "content": "..."},
    {"role": "assistant", "content": "..."}
  ],
  "preferences": {
    "tools": ["rag", "reason"],
    "knowledge_bases": ["math"],
    "language": "en"
  },
  "created_at": "2026-05-21T14:23:01Z",
  "updated_at": "2026-05-21T14:24:38Z"
}
```

### `session open <id>` / `session delete <id>` / `session rename <id> --title <title>`

```bash
deeptutor session open sess_abc123                    # 在 REPL 里续上
deeptutor session rename sess_abc123 --title "Calculus review"
deeptutor session delete sess_abc123
```

## `deeptutor notebook` —— notebook 记录

```bash
# 创建 notebook
deeptutor notebook create research-notes --description "Daily reading log"

# 添加 markdown 记录
deeptutor notebook add-md research-notes paper-summary.md \
  --title "Attention is all you need" --type research

# 替换某条记录的内容
deeptutor notebook replace-md research-notes rec_abc123 updated-summary.md

# 删除一条记录
deeptutor notebook remove-record research-notes rec_abc123

# 查看
deeptutor notebook list
deeptutor notebook show research-notes
```

记录类型：`chat`、`question`、`research`、`solve`。

## `deeptutor memory` —— 三层记忆

DeepTutor 把用户记忆按三层存（深入说明见 [**Memory**](/zh-cn/docs/explore/memory/)）：

- **L1** —— 每个 surface（chat、notebook、quiz 等）的原始事件轨迹
- **L2** —— 每个 surface 整理过的 markdown 摘要
- **L3** —— 跨 surface 的整体画像（recent、profile、scope、preferences）

### `memory show [target]`

```bash
deeptutor memory show                # 默认：L3 拼接
deeptutor memory show L3
deeptutor memory show L2             # 列出所有 L2 surface
deeptutor memory show profile        # 某个具体的 L3 doc
deeptutor memory show chat           # 某个具体的 L2 surface doc
```

### `memory clear [target]`

```bash
deeptutor memory clear all --force         # ⚠️ 清空 L1+L2+L3
deeptutor memory clear trace               # 仅 L1
deeptutor memory clear chat                # 仅 chat surface 的 L1 轨迹
```

### 强制触发一次整理

手动整理不是一个 CLI 命令 —— 从 Web UI 的 **Memory Workbench**（`/memory` → **Run consolidator**）触发，或者通过 HTTP API：

```bash
curl -X POST http://localhost:8001/api/v1/memory/runs/start
```

## `deeptutor partner` —— Partner 生命周期

```bash
deeptutor partner list

deeptutor partner create math-tutor \
  --name "Math Mentor" \
  --soul "Socratic tutor specializing in algebra and calculus" \
  --model gpt-4o

deeptutor partner stop math-tutor
deeptutor partner start math-tutor
```

子命令：`list`、`create`、`start`、`stop`。`create` 会写入 partner config，并尝试启动该 partner。Web UI 是配置 channel schema、assets、tools 和 secrets 的推荐入口；CLI 适合列表、创建、启动和停止。

Partner 运行在 `data/partners/<partner_id>/workspace/` 作用域里。渠道接入说明见 [**Partners 伙伴与渠道**](/zh-cn/docs/partners/)。

## `deeptutor config show`

```bash
deeptutor config show
```

示例输出：

```json
{
  "ports": {
    "backend": 8001,
    "frontend": 3782
  },
  "llm": {
    "provider": "openai",
    "model": "gpt-4o",
    "base_url": "https://api.openai.com/v1",
    "api_key": "***"
  },
  "embedding": {
    "status": "configured",
    "provider": "openai",
    "model": "text-embedding-3-large",
    "dimension": 3072,
    "api_key": "***"
  },
  "search": {
    "provider": "tavily",
    "status": "enabled",
    "api_key": "***"
  },
  "language": "en",
  "tools": ["rag", "web_search", "code_execution", "reason"]
}
```

密钥用 `***` 打码。

## `deeptutor plugin` —— 注册表查看

```bash
deeptutor plugin list                  # 所有 capability + tool
deeptutor plugin info deep_solve       # 单个 capability
deeptutor plugin info rag              # 单个 tool
```

`plugin info <capability>` 返回：

```json
{
  "name": "deep_solve",
  "description": "Multi-step agentic problem-solving",
  "cli_aliases": ["solve"],
  "stages": ["planning", "reasoning", "writing"],
  "tools_used": ["rag", "web_search", "code_execution", "reason"],
  "config_defaults": {
    "max_steps": 8
  },
  "availability": {
    "available": true,
    "install_hint": ""
  }
}
```

## `deeptutor provider` —— 认证流程

对于走 OAuth 或特殊 token 流程的 provider：

```bash
deeptutor provider login openai-codex       # 走 oauth-cli-kit 的 OAuth
deeptutor provider login github-copilot     # GitHub 认证校验
```

## `deeptutor book` —— Knowledge Books（引导式学习）

```bash
deeptutor book list

# 给一本 book 做健康检查（KB 漂移 + log 过期检测）
deeptutor book health book_abc123

# 重新快照 fingerprint，消除 "stale page" 警告
deeptutor book refresh-fingerprints book_abc123
```

Book 是 **Guided Learning** 学习路径的存储层。详见 [**Book Engine**](/zh-cn/docs/explore/book/)。

## 常见输出 schema

### TurnRequest（`run` 内部发送的对象）

```python
@dataclass(slots=True)
class TurnRequest:
    content: str
    capability: str = "chat"
    session_id: str | None = None
    tools: list[str] = field(default_factory=list)
    knowledge_bases: list[str] = field(default_factory=list)
    language: str = "en"
    config: dict[str, Any] = field(default_factory=dict)
    notebook_references: list[dict[str, Any]] = field(default_factory=list)
    history_references: list[str] = field(default_factory=list)
    attachments: list[dict[str, Any]] = field(default_factory=list)
    skills: list[str] = field(default_factory=list)
```

### 流事件类型

| 事件 | 触发时机 | 字段 |
|------|----------|------|
| `stage_start` | 进入一个 pipeline stage | `stage`、`metadata` |
| `stage_end` | stage 结束 | `stage` |
| `content` | 面向用户的 markdown 片段 | `content` |
| `thinking` | 中间推理 | `content` |
| `progress` | 状态更新 | `content` |
| `tool_call` | 正在调用某个 tool | `content`（tool 名）、`metadata.args` |
| `tool_result` | tool 返回结果 | `content`、`metadata.tool` |
| `error` | 出错 | `content` |
| `done` | turn 完成 | `session_id`、`turn_id`（顶层）、`metadata.status` |

## 另见

- [**交互式 REPL**](/zh-cn/docs/cli/chat-repl/) —— 日常使用 `deeptutor chat`
- [**代理交接**](/zh-cn/docs/cli/agent-handoff/) —— 让 Claude Code / Codex 来驱动 CLI
- [**服务端 API**](/zh-cn/docs/cli/server-api/) —— `deeptutor serve` 暴露的 HTTP / WebSocket 表面
