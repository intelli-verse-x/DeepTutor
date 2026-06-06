---
title: CLI-Only Install
description: Option 4 — the lightweight install for headless servers, agent harnesses, and Claude Code / Codex / Hermes setups.
---

When you don't need the Web UI. The CLI-only package is installed from a **source checkout**, not from PyPI.

## Install

```bash
git clone https://github.com/HKUDS/DeepTutor.git
cd DeepTutor

# Create a venv (macOS / Linux)
# Windows PowerShell:
#   py -3.11 -m venv .venv-cli ; .\.venv-cli\Scripts\Activate.ps1
python3 -m venv .venv-cli && source .venv-cli/bin/activate
python -m pip install --upgrade pip

python -m pip install -e ./packaging/deeptutor-cli
deeptutor init --cli
deeptutor chat
```

`deeptutor init --cli` shares the same `data/user/settings/` layout as the full app but:

- **Skips** the backend / frontend port prompts
- **Defaults embeddings to off** (choose `Yes` if you plan to use `deeptutor kb …` or RAG tools)
- Still writes the complete runtime layout (`system.json`, `auth.json`, `integrations.json`, `model_catalog.json`, `main.yaml`, `agents.yaml`)
- Still prompts for the active LLM provider and model

## When to use this

- You're running DeepTutor as a tool inside another agent's harness (Claude Code, Codex, OpenCode, etc.)
- Headless server / VM with no browser
- You want a fast install with no Node.js toolchain

## Common commands

```bash
deeptutor chat                                          # interactive REPL
deeptutor chat --capability deep_solve --tool rag --kb my-kb
deeptutor run chat "Explain Fourier transform"
deeptutor run deep_solve "Solve x^2 = 4" --tool rag --kb my-kb
deeptutor kb create my-kb --doc textbook.pdf
deeptutor memory show
deeptutor config show
```

Full surface: [**DeepTutor CLI**](/docs/cli/).

## What's available and what isn't

The local `deeptutor-cli` install ships **no Web assets or server dependencies**. Keep the source checkout around — the editable install points to it.

| Surface | CLI-Only | Full install |
|---------|----------|--------------|
| `deeptutor chat` interactive REPL | ✅ | ✅ |
| `deeptutor run` capabilities | ✅ | ✅ |
| `deeptutor kb` (Knowledge Bases) | ✅ *(opt in during init)* | ✅ |
| `deeptutor notebook` | ✅ | ✅ |
| `deeptutor memory` | ✅ | ✅ |
| `deeptutor bot` (TutorBot) | ✅ *(if `[tutorbot]` extra installed)* | ✅ |
| `deeptutor config show` | ✅ | ✅ |
| `deeptutor provider login` | ✅ | ✅ |
| `deeptutor serve` (FastAPI) | ❌ | ✅ |
| `deeptutor start` (Web UI) | ❌ | ✅ |
| Co-Writer UI | ❌ | ✅ |
| Memory Workbench UI | ❌ | ✅ |
| Book Engine UI | ❌ | ✅ |

To add the Web app later, install the PyPI package (Option 1) and run `deeptutor init` + `deeptutor start` from the same workspace.

## Use it from another agent

The CLI is **agent-native**. `deeptutor run --format json` emits one JSON event per line, and data-inspection commands such as `kb list`, `kb search`, `session show`, and `notebook show` expose JSON where implemented — useful for piping into another agent's harness.

Hand the [`SKILL.md`](https://github.com/HKUDS/DeepTutor/blob/main/SKILL.md) at the project root to any tool-using LLM and it can drive DeepTutor on its own. See [**Agent handoff**](/docs/cli/agent-handoff/) for the patterns.

## Updating

```bash
cd DeepTutor
git pull
pip install -e ./packaging/deeptutor-cli --upgrade
```

## Common errors

### `deeptutor: command not found` after install

The console script wasn't placed on PATH. Verify the venv is activated, or call it directly:

```bash
python -m deeptutor_cli.main chat
```

### `ModuleNotFoundError: No module named 'fastapi'` when running `deeptutor serve`

`deeptutor serve` is **unavailable** in the CLI-only install. Use [**PyPI**](/docs/get-started/pypi/) or [**From Source**](/docs/get-started/from-source/) instead.

### TutorBot commands say SDK missing

Channel SDKs (python-telegram-bot, slack-sdk, etc.) are only included with the `[tutorbot]` extra:

```bash
pip install -e "./packaging/deeptutor-cli[tutorbot]"
```

More: [**Troubleshooting**](/docs/get-started/troubleshooting/).

## Next

- [**DeepTutor CLI**](/docs/cli/) — full CLI reference
- [**Agent handoff**](/docs/cli/agent-handoff/) — let your agent drive
- [**Explore TutorBot**](/docs/tutorbot/) — run a bot from CLI
