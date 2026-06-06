---
title: DeepTutor CLI
description: Drive every DeepTutor capability from the terminal — interactive REPL, single-turn execution, agent handoff.
---

DeepTutor is built around an **agent-native CLI**: core runtime surfaces have terminal mirrors, turn execution can stream JSON for machine consumers, and the supported automation surface is documented in a single skill file that AI agents can read and drive autonomously. Some browser-first workflows (for example rich Co-Writer editing and Memory Workbench review) still live in the Web UI or HTTP API.

This section covers:

- [**Commands**](/docs/cli/commands/) — every top-level command and subcommand group with flags, schemas, and examples
- [**Interactive REPL**](/docs/cli/chat-repl/) — drive a long chat session with `/slash` commands inline
- [**Agent handoff**](/docs/cli/agent-handoff/) — let Claude Code, Codex, OpenCode, or Hermes drive `deeptutor` for you
- [**Server API**](/docs/cli/server-api/) — the HTTP / WebSocket surface that `deeptutor serve` exposes

## Quick tour

```bash
# Install (one of the paths from Get Started)
pip install deeptutor

# Configure
deeptutor init

# Interactive chat
deeptutor chat

# Single-turn, agent-style
deeptutor run deep_solve "Find the derivative of sin(x²)" --tool reason --format json

# Manage knowledge bases
deeptutor kb create physics --doc chapter1.pdf
deeptutor kb search physics "What is angular momentum?"

# Run a TutorBot
deeptutor bot create my-bot --persona "Socratic math tutor"

# Inspect three-layer memory
deeptutor memory show L3
```

## Why CLI-first?

The terminal experience is **the same experience an AI agent gets**. When you write a turn in `deeptutor chat`, the underlying turn schema (`TurnRequest`) is identical to what Claude Code or Codex would send if you handed them `SKILL.md`.

This means:

- Core learning flows can be driven from the terminal; browser-only editing and admin screens expose their state through the Web UI / API
- `deeptutor run --format json` emits one JSON event per line; data-inspection commands such as `kb list`, `kb search`, `session show`, and `notebook show` also expose JSON where implemented
- Sessions persist across turns — you can switch between Web, REPL, and one-shot `run` calls and resume where you left off
- The CLI is the best automation entry point for turns, KBs, sessions, notebooks, memory, TutorBots, config inspection, plugins, providers, and Books

## Top-level command map

| Group | What it does | Most-used |
|-------|--------------|-----------|
| `deeptutor init` | Guided setup wizard | `deeptutor init --cli` |
| `deeptutor start` | Launch backend + frontend together | `deeptutor start` |
| `deeptutor serve` | Backend only (FastAPI on `:8001`) | `deeptutor serve --host 0.0.0.0` |
| `deeptutor chat` | Interactive REPL | `deeptutor chat --kb physics` |
| `deeptutor run` | One-shot capability turn | `deeptutor run deep_solve "..."` |
| `deeptutor kb` | Knowledge Base management | `deeptutor kb create / list / search` |
| `deeptutor session` | Session inspection | `deeptutor session list / show <id>` |
| `deeptutor notebook` | Notebook records | `deeptutor notebook create / add-md` |
| `deeptutor memory` | Three-layer memory store | `deeptutor memory show L3` |
| `deeptutor bot` | TutorBot lifecycle | `deeptutor bot create / start / stop` (`create` starts the bot immediately) |
| `deeptutor config` | View runtime configuration | `deeptutor config show` |
| `deeptutor plugin` | Capability / tool registry | `deeptutor plugin list` |
| `deeptutor provider` | Provider auth flows | `deeptutor provider login openai-codex` |
| `deeptutor book` | Knowledge Books (Guided Learning) | `deeptutor book list / health` |

See [**Commands**](/docs/cli/commands/) for the full reference.

## Two modes of use

### Mode 1 — Interactive

For exploratory, multi-turn work, drop into the REPL:

```text
$ deeptutor chat --kb physics
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ DeepTutor CLI                                                  ┃
┃ Type a message. /quit /tool /cap /kb /history /show /refs     ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
[dim]session=(new) capability=chat tools=[] kb=[physics] history=[] notebook_refs=[] language=en config={}[/]
You> Explain the chain rule with a worked example
```

Full guide: [**Interactive REPL**](/docs/cli/chat-repl/).

### Mode 2 — Agent-style one-shot

For automation, CI, or AI-agent harnesses, use `deeptutor run`:

```bash
deeptutor run deep_solve "Find the eigenvalues of [[4,1],[2,3]]" \
  --tool reason --tool code_execution \
  --format json | jq -r '.content // empty'
```

Each JSON line is one event — `stage_start`, `content`, `tool_call`, `tool_result`, `thinking`, `done`. You can pipe these into a downstream agent or extract the final answer with `jq`.

Full guide: [**Agent handoff**](/docs/cli/agent-handoff/).

## Where state lives

Every CLI command operates against the same workspace as the Web UI. By default, runtime data lives under `data/` in the directory where you launch DeepTutor. Override the workspace root with `DEEPTUTOR_HOME=/path`, `deeptutor init --home /path`, or `deeptutor start --home /path`.

## Help is always one flag away

Every command supports `--help`:

```text
$ deeptutor --help

 Usage: deeptutor [OPTIONS] COMMAND [ARGS]...  

 DeepTutor — agent-native, open-source personalized tutoring.  

╭─ Commands ───────────────────────────────────────────────────────────────────╮
│ init          Guided setup wizard.                                            │
│ start         Launch backend + frontend together.                             │
│ serve         Backend only.                                                   │
│ chat          Interactive REPL.                                               │
│ run           One-shot capability turn.                                       │
│ kb            Knowledge base management.                                      │
│ session       Session inspection.                                             │
│ notebook      Notebook records.                                               │
│ memory        Three-layer memory store.                                       │
│ bot           TutorBot lifecycle.                                             │
│ config        View runtime configuration.                                     │
│ plugin        Capability / tool registry.                                     │
│ provider      Provider auth flows.                                            │
│ book          Knowledge Books (Guided Learning).                              │
╰──────────────────────────────────────────────────────────────────────────────╯
```

And every subcommand:

```text
$ deeptutor run --help
$ deeptutor kb create --help
$ deeptutor bot start --help
```
