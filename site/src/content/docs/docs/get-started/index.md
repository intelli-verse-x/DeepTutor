---
title: Get Started
description: DeepTutor ships four install paths — PyPI, From Source, Docker, and CLI-Only. Pick the one that fits.
---

DeepTutor ships **four installation paths**. They all share one workspace layout: settings live in `data/user/settings/` under the directory you launch from (or under `DEEPTUTOR_HOME` / `deeptutor start --home` if you set one explicitly). Knowledge bases, memory, Partner runtime state, multi-user accounts, and audit logs also live under the same `data/` tree, so deployments only need to persist that tree.

For the full app, the recommended flow is **pick a workspace directory → install → `deeptutor init` → `deeptutor start`**.

## Pick a path

| Option | When to use | Page |
|--------|-------------|------|
| **PyPI** | First-time users, want the smoothest path, no clone | [**Install from PyPI**](/docs/get-started/pypi/) |
| **From Source** | Hacking on the codebase, want hot reload | [**Install from Source**](/docs/get-started/from-source/) |
| **Docker** | Production deployments, hosted hosts, persistent volumes | [**Docker**](/docs/get-started/docker/) |
| **CLI Only** | Headless server, agent harness, no Web UI needed | [**CLI-Only Install**](/docs/get-started/cli-only/) |

> 🧪 **Trying a pre-release?** Plain `pip install -U deeptutor` stays on stable — PyPI skips pre-release versions. Opt in with `pip install --pre -U deeptutor`, or pin an exact version with `pip install -U "deeptutor==<version>"`.

## Minimum requirements

| Component | Version |
|-----------|---------|
| Python | **3.11+** |
| Node.js | **20+** (PyPI) / **22 LTS** (from source, matches CI + Docker) |
| RAM | 4 GB free |
| Disk | 2 GB free |

You'll also need an **LLM API key** (OpenAI, Anthropic, Gemini, DeepSeek, Azure, Ollama, LM Studio, llama.cpp, vLLM, or any OpenAI-compatible endpoint) and ideally an **embedding API key** if you plan to use Knowledge Bases.

## What gets bound

After `deeptutor start`, two services come up:

| Service | Default port |
|---------|--------------|
| FastAPI backend | `8001` |
| Next.js frontend | `3782` |

Both are overridable via `data/user/settings/system.json` or during `deeptutor init`.

## After install

Once you can reach `http://localhost:3782/`:

- [**Explore DeepTutor**](/docs/explore/) — a tour of the Chat, Partners, Co-Writer, Book, Knowledge, Space, Memory, and Settings
- [**DeepTutor CLI**](/docs/cli/) — drive everything from the terminal
- [**Partners & Channels**](/docs/partners/) — connect autonomous tutors to WeChat, WeCom, QQ, Telegram, Slack, Feishu, and more
- [**Multi-User Deployment**](/docs/get-started/multi-user/) — host DeepTutor for a team

If something breaks, jump to [**Troubleshooting**](/docs/get-started/troubleshooting/).
