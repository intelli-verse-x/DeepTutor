---
title: Command Reference
description: Every deeptutor command — flags, output schemas, examples.
---

This page documents every `deeptutor` subcommand and flag. For interactive REPL usage, see [**Interactive REPL**](/docs/cli/chat-repl/). For automation patterns, see [**Agent handoff**](/docs/cli/agent-handoff/).

## `deeptutor run` — single-turn capability execution

Run one capability turn and exit. The fundamental "do-something" command for agents and scripting.

```bash
deeptutor run <capability> "<message>" [options]
```

### Flags

| Flag | Type | Default | What it does |
|------|------|---------|--------------|
| `--session <id>` | string | *(new)* | Resume an existing session |
| `-t / --tool <name>` | repeatable | `[]` | Enable a tool (e.g., `rag`, `web_search`, `code_execution`, `reason`) |
| `--kb <name>` | repeatable | `[]` | Attach a Knowledge Base |
| `--notebook-ref <id[:record,...]>` | repeatable | `[]` | Attach notebook records |
| `--history-ref <session_id>` | repeatable | `[]` | Reference a prior session |
| `-l / --language <code>` | string | `en` | Response language |
| `--config <key=value>` | repeatable | `[]` | Per-capability config override |
| `--config-json <json>` | string | — | Base config as JSON; repeated `--config key=value` flags override matching keys |
| `-f / --format <rich\|json>` | enum | `rich` | Output mode |

### Examples

```bash
# Simple chat turn
deeptutor run chat "Explain quantum entanglement in plain English"

# Deep Solve with reasoning + RAG against a KB
deeptutor run deep_solve "Find d/dx [sin(x²)]" --tool reason --tool rag --kb math

# Generate 5 quiz questions
deeptutor run deep_question "Linear algebra eigenvectors" \
  --config num_questions=5 --config difficulty=hard

# Deep Research, JSON stream
deeptutor run deep_research "What's new in retrieval-augmented generation?" \
  --tool web_search --tool rag --kb papers \
  --config mode=report --config depth=standard \
  --format json

# Resume a session
deeptutor run chat "Continue from where we left off" --session sess_abc123
```

### Output — `--format rich` (default)

Rich-formatted Markdown rendering, one stage at a time. Sample:

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

### Output — `--format json`

One JSON object per line. Useful for piping into other tools:

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

Event types: `stage_start`, `stage_end`, `content`, `thinking`, `progress`, `tool_call`, `tool_result`, `error`, `done`.

## `deeptutor chat` — interactive REPL

Drop into an interactive chat session with `/slash` commands for in-session configuration.

```bash
deeptutor chat [options]
```

Options mirror the turn-shaping flags from `run`: `--session`, `--tool`, `--capability`, `--kb`, `--notebook-ref`, `--history-ref`, `--language`, `--config`, and `--config-json`. Full walkthrough at [**Interactive REPL**](/docs/cli/chat-repl/).

## `deeptutor init` — guided setup wizard

```bash
deeptutor init                # Full setup (asks ports + LLM + embedding + search)
deeptutor init --cli          # CLI-only (skips port questions)
deeptutor init --home /path   # Use a non-default workspace
```

See [**Get Started**](/docs/get-started/) for the full walkthrough.

## `deeptutor start` / `deeptutor serve`

```bash
# Launch both backend + frontend (blocking; Ctrl+C stops both)
deeptutor start
deeptutor start --home /path

# Backend only
deeptutor serve --host 0.0.0.0 --port 8001
deeptutor serve --reload                # Hot reload on file changes (dev only)
```

## `deeptutor kb` — Knowledge Base management

### `kb list`

```bash
deeptutor kb list                # Rich table
deeptutor kb list --format json
```

JSON output:

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

Returns the KB's metadata, document list, statistics, and indexing state.

### `kb create <name>`

```bash
# Single document
deeptutor kb create physics --doc chapter1.pdf

# Multiple documents
deeptutor kb create physics --doc chapter1.pdf --doc chapter2.pdf --doc exercises.docx

# Entire directory
deeptutor kb create textbooks --docs-dir ./my-pdfs
```

Supported formats: PDF, DOCX, XLSX, PPTX, TXT, MD, HTML.

### `kb add <name>`

Incrementally add documents to an existing KB:

```bash
deeptutor kb add physics --doc chapter3.pdf
```

### `kb delete <name>`

```bash
deeptutor kb delete physics              # Asks for confirmation
deeptutor kb delete physics --force      # Skip confirmation
```

### `kb set-default <name>`

```bash
deeptutor kb set-default physics
```

The default KB is what `deeptutor chat` and the Web UI attach automatically when none is specified.

### `kb search <name> <query>`

```bash
deeptutor kb search physics "What is angular momentum?"
deeptutor kb search physics "..." --mode hybrid --format json
```

Modes: `hybrid` (default; semantic + keyword), `vector` (semantic only), `keyword` (BM25).

### Re-indexing

Re-indexing isn't a CLI command — it's done from the **Web UI** (Knowledge → pick KB → **Index versions** tab → **Re-index now**). Useful after changing embedding models.

## `deeptutor skill` — skill library & hubs

```bash
deeptutor skill list                              # Local skills, with hub provenance
deeptutor skill search "git release notes"        # Semantic search on a hub (default: clawhub)
deeptutor skill install clawhub:gh-release-notes  # Verify → fetch → register
deeptutor skill install some-skill@1.2.0          # Hub prefix defaults to clawhub; @ pins a version
deeptutor skill remove gh-release-notes
```

Hub references use `<hub>:<slug>[@version]`. Every install runs the same import gate: the hub's security verdict is checked first (flagged packages are refused unless you pass `--allow-unverified`), archives are extracted with zip-slip / zip-bomb guards, support files pass a text/script suffix whitelist so binaries never land in the workspace, and `always:` frontmatter is stripped so a downloaded package can't inject itself into every system prompt. Provenance (hub, version, verdict) is recorded in `.hub-lock.json` beside the skill.

`install` flags: `--name` installs under a different local name, `--force` replaces an existing skill, `--allow-unverified` proceeds past a suspicious verdict.

Registries beyond ClawHub are declared in `settings/skill_hubs.json` — `type: "clawhub"` points at any compatible HTTP API, `type: "command"` wraps a fetch CLI that drops the package into `{dest}`. In a multi-user deployment this CLI operates the admin workspace: an installed skill stays invisible to other users until a grant assigns it.

## `deeptutor session` — session inspection

### `session list`

```bash
deeptutor session list --limit 20
```

### `session show <id>`

```bash
deeptutor session show sess_abc123                 # Rich
deeptutor session show sess_abc123 --format json   # Full JSON
```

JSON output (truncated):

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
deeptutor session open sess_abc123                    # Resume in REPL
deeptutor session rename sess_abc123 --title "Calculus review"
deeptutor session delete sess_abc123
```

## `deeptutor notebook` — notebook records

```bash
# Create a notebook
deeptutor notebook create research-notes --description "Daily reading log"

# Add a markdown record
deeptutor notebook add-md research-notes paper-summary.md \
  --title "Attention is all you need" --type research

# Replace a record's content
deeptutor notebook replace-md research-notes rec_abc123 updated-summary.md

# Remove a record
deeptutor notebook remove-record research-notes rec_abc123

# Inspect
deeptutor notebook list
deeptutor notebook show research-notes
```

Record types: `chat`, `question`, `research`, `solve`.

## `deeptutor memory` — three-layer memory

DeepTutor stores user memory in three layers (see [**Memory**](/docs/explore/memory/) for the deep dive):

- **L1** — raw event trace per surface (chat, notebook, quiz, etc.)
- **L2** — per-surface curated markdown summaries
- **L3** — cross-surface profile (recent, profile, scope, preferences)

### `memory show [target]`

```bash
deeptutor memory show                # Default: L3 concatenated
deeptutor memory show L3
deeptutor memory show L2             # List all L2 surfaces
deeptutor memory show profile        # A specific L3 doc
deeptutor memory show chat           # A specific L2 surface doc
```

### `memory clear [target]`

```bash
deeptutor memory clear all --force         # ⚠️ wipes L1+L2+L3
deeptutor memory clear trace               # Only L1
deeptutor memory clear chat                # Only L1 trace for the chat surface
```

### Forcing a consolidation pass

Manual consolidation isn't a CLI command — fire it from the **Memory Workbench** in the Web UI (`/memory` → **Run consolidator**), or from the HTTP API:

```bash
curl -X POST http://localhost:8001/api/v1/memory/runs/start
```

## `deeptutor partner` — Partner lifecycle

```bash
deeptutor partner list

deeptutor partner create math-tutor \
  --name "Math Mentor" \
  --soul "Socratic tutor specializing in algebra and calculus" \
  --model gpt-4o

deeptutor partner stop math-tutor
deeptutor partner start math-tutor
```

Subcommands: `list`, `create`, `start`, `stop`. `create` writes partner config and attempts to start the partner. The Web UI is the recommended place to configure channel schemas, assets, tools, and secrets; the CLI is best for listing, creating, starting, and stopping.

Partners run inside `data/partners/<partner_id>/workspace/`. See [**Partners & Channels**](/docs/partners/) for channel setup.

## `deeptutor config show`

```bash
deeptutor config show
```

Sample output:

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

Secrets are masked with `***`.

## `deeptutor plugin` — registry inspection

```bash
deeptutor plugin list                  # All capabilities + tools
deeptutor plugin info deep_solve       # Single capability
deeptutor plugin info rag              # Single tool
```

`plugin info <capability>` returns:

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

## `deeptutor provider` — auth flows

For providers that use OAuth or special token flows:

```bash
deeptutor provider login openai-codex       # OAuth via oauth-cli-kit
deeptutor provider login github-copilot     # GitHub auth validation
```

## `deeptutor book` — Knowledge Books (Guided Learning)

```bash
deeptutor book list

# Health-check a book (KB drift + log staleness)
deeptutor book health book_abc123

# Re-snapshot fingerprints to clear "stale page" warnings
deeptutor book refresh-fingerprints book_abc123
```

Books are the storage layer for **Guided Learning** journeys. See [**Book Engine**](/docs/explore/book/).

## Common output schemas

### TurnRequest (what `run` sends internally)

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

### Stream event types

| Event | When | Fields |
|-------|------|--------|
| `stage_start` | A pipeline stage begins | `stage`, `metadata` |
| `stage_end` | Stage finishes | `stage` |
| `content` | User-facing markdown chunk | `content` |
| `thinking` | Intermediate reasoning | `content` |
| `progress` | Status update | `content` |
| `tool_call` | A tool is being invoked | `content` (tool name), `metadata.args` |
| `tool_result` | A tool returned | `content`, `metadata.tool` |
| `error` | Something went wrong | `content` |
| `done` | Turn complete | `metadata.session_id`, `metadata.turn_id` |

## See also

- [**Interactive REPL**](/docs/cli/chat-repl/) — using `deeptutor chat` day-to-day
- [**Agent handoff**](/docs/cli/agent-handoff/) — letting Claude Code / Codex drive the CLI
- [**Server API**](/docs/cli/server-api/) — the HTTP / WebSocket surface from `deeptutor serve`
