---
title: Install from PyPI
description: Option 1 — the smoothest path. pip install deeptutor, init, start.
---

The PyPI install is the smoothest path. **Full local Web app + CLI, no clone required.** Needs **Python 3.11+** and a **Node.js 20+** runtime on PATH — the packaged Next.js standalone server is spawned by `deeptutor start`.

## Install

```bash
mkdir -p my-deeptutor && cd my-deeptutor
pip install -U deeptutor
deeptutor init     # prompts for ports + LLM provider + optional embedding
deeptutor start    # starts backend + frontend; keep the terminal open
```

`deeptutor init` prompts for:

- **Backend port** (default `8001`)
- **Frontend port** (default `3782`)
- **LLM provider** / base URL / API key / model
- **Optional embedding provider** for Knowledge Base / RAG

After `deeptutor start`, open the frontend URL printed in the terminal — by default <http://127.0.0.1:3782>. Press `Ctrl+C` in that terminal to stop both backend and frontend.

> Skipping `deeptutor init` is fine for a quick trial; the app boots with default ports and empty model settings. Configure them later in **Settings → LLM**.

## Trying the v1.4.0 beta

PyPI normalizes `1.4.0-beta` → `1.4.0b0`, so plain `pip install -U deeptutor` stays on stable. To opt in:

```bash
pip install --pre -U deeptutor
# or pin exactly:
pip install -U deeptutor==1.4.0b0
```

## Where things live

The workspace lives under the directory you launched from (the `data/` folder appears there on first start). Override with:

```bash
DEEPTUTOR_HOME=/opt/deeptutor deeptutor start
# or
deeptutor start --home /opt/deeptutor
```

Layout (created on first init):

```text
my-deeptutor/
└── data/
    └── user/
        ├── settings/
        │   ├── system.json
        │   ├── auth.json
        │   ├── integrations.json
        │   ├── interface.json
        │   ├── model_catalog.json
        │   ├── main.yaml
        │   └── agents.yaml
        ├── memory/
        └── workspace/
```

See [**Configuration Reference**](#config-files-under-datausersettings) below for what each file controls.

## What `deeptutor` can do once installed

Pop into the CLI any time without leaving the workspace:

```bash
deeptutor chat                                          # interactive REPL
deeptutor run chat "Explain the Fourier transform"      # one-shot
deeptutor kb create my-kb --doc textbook.pdf            # build a KB
deeptutor memory show                                   # inspect memory
deeptutor config show                                   # current config
```

Full surface: [**DeepTutor CLI**](/docs/cli/).

## Updating

```bash
pip install --upgrade deeptutor
deeptutor start
```

Workspace is preserved across upgrades.

## Config files under `data/user/settings/`

Everything under `data/user/settings/` is plain JSON / YAML. The **Settings** page in the browser is the recommended editor.

| File | Purpose |
|------|---------|
| `model_catalog.json` | LLM, embedding, and search provider profiles; API keys; active models |
| `system.json` | Backend / frontend ports, public API base, CORS, SSL verification, attachment directory |
| `auth.json` | Optional auth toggle, username, password hash, token / cookie settings |
| `integrations.json` | Optional PocketBase and sidecar integration settings |
| `interface.json` | UI language / theme / sidebar preferences |
| `main.yaml` | Runtime behavior defaults and path injection |
| `agents.yaml` | Capability / tool temperature and token settings |

> Project-root `.env` is **not** read as an application config file. Configure providers from **Settings → LLM** in the browser, or by editing `model_catalog.json` directly.

## Common errors

### `python: command not found` on macOS

```bash
python3 -m pip install -U deeptutor
python3 -m deeptutor init   # or just `deeptutor init` if entry point is on PATH
```

### Node.js not on PATH

`deeptutor start` spawns the packaged Next.js server, which needs `node` on PATH. Install Node 20+ from <https://nodejs.org> or via `brew install node@22`.

### Port `3782` (or `8001`) already in use

```bash
lsof -i :3782          # macOS
ss -ltnp | grep :3782  # Linux
```

Kill it or change the port via `deeptutor init` re-run.

### LLM provider 401 Unauthorized

API key was rejected. Re-enter it in **Settings → LLM**, or:

```bash
deeptutor init   # re-runs the wizard, preserves the workspace
```

For more, see [**Troubleshooting**](/docs/get-started/troubleshooting/).

## Next

- [**Explore DeepTutor**](/docs/explore/) — tour the running app
- [**Multi-User Deployment**](/docs/get-started/multi-user/) — turn it into a team server
