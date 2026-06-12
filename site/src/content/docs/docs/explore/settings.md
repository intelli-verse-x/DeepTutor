---
title: Settings
description: The unified control plane for appearance, status, network, model catalogs, embeddings, search, MinerU, capabilities, memory, MCP, and tools.
---

Settings is the operational control plane for DeepTutor. Most sections use a draft-and-apply model so you can test provider changes before committing them.

![Settings workspace](/screenshots/settings.png)

## Sections

| Section | What it controls |
| --- | --- |
| **Appearance** | Theme, language, sidebar preferences. |
| **Status** | Live state of the backend and the model services your configuration resolves to. |
| **Network** | Backend/frontend ports, external API base, CORS origins. |
| **LLM** | Model catalog profiles, base URLs, API keys, active models. |
| **Embedding** | Embedding providers for Knowledge and RAG. |
| **Search** | Web/search provider configuration. |
| **MinerU PDF** | Local or cloud PDF parsing backend. |
| **Capabilities** | Budgets and knobs for Chat, Solve, Question, Research, Visualize, Co-Writer, and related pipelines. |
| **Memory** | Consolidation controls and links to the Memory workbench. |
| **MCP servers** (admin only) | External MCP tool registration. |
| **Tools** | Built-in, contextual, coming-soon, and optional user-toggleable tools. |

## Section guide

### Appearance

Theme, display language, and sidebar preferences. Purely client-facing; no provider credentials live here.

### Status

A read-only dashboard of the backend plus the LLM, embedding, and search endpoints your configuration currently resolves to. Status reflects runtime values after the last **Apply** — draft changes do not show up here until applied.

### Network

Backend/frontend ports, the external API base that browser clients use behind a reverse proxy, and CORS origins.

### LLM

![LLM settings with provider profiles, connection fields, and model catalog](/screenshots/settings-llm.png)

Language model profiles. Each profile is a provider connection — provider type, base URL, API key, optional extra headers — plus a model catalog entry per model with its model ID and context window. The active model is used for Chat and most agent reasoning.

### Embedding

Embedding model profiles, mirroring the LLM layout (provider connection + models) but registering embedding models with their dimensions. Used by retrieval and knowledge-base ingestion.

### Search

Web search providers used by the `web_search` tool and any agent step that hits the open web. Configure provider, base URL, and API key, then run a test query from the diagnostics panel.

### MinerU PDF

![MinerU PDF settings with parsing backend and local install detection](/screenshots/settings-mineru.png)

The PDF parsing backend used when generating questions from an uploaded exam paper. Choose between a local MinerU install and the hosted mineru.net cloud API. For local parsing, the page detects the MinerU CLI, accepts an explicit CLI path, and manages the ~1-2 GB model-weights download (HuggingFace or ModelScope).

### Capabilities

![Capabilities settings with per-capability parameters](/screenshots/settings-capabilities.png)

Per-capability LLM parameters and runtime knobs: temperature, token budgets, and loop limits for Chat, Solve, Question, Research, Visualize, Co-Writer, and related pipelines. For Chat this includes max rounds and separate exploring/responding token budgets. Values persist to `data/user/settings/agents.yaml` (LLM params) and `main.yaml` (runtime knobs).

### Memory

Tunes the chunk-based memory consolidator: LLM-round budgets per L2 surface and L3 slot for **Update** and **Audit** runs, plus **Dedup** iterations and whether dedup runs automatically after an update.

### MCP servers (admin only)

Register external MCP (Model Context Protocol) servers to expose their tools to the chat agent. Test the connection first, then save. In multi-user deployments this section is restricted to admins.

### Tools

![Tools settings with user-toggleable and built-in tools](/screenshots/settings-tools.png)

Switches user-toggleable tools on or off. **Experience enhancement** tools (`brainstorm`, `web_search`, `paper_search`, `reason`) are yours to toggle; **built-in** tools such as `rag` and code execution are locked and mount automatically when the chat agent needs them.

## Important deployment notes

- Project-root `.env` is intentionally ignored as application config.
- Runtime settings live under `data/user/settings/*.json` unless you set `DEEPTUTOR_HOME` or `deeptutor start --home`.
- Docker browser clients must reach both the frontend and backend. If you reverse proxy, configure the external API base in **Network**.
- Optional user-toggleable tools are `brainstorm`, `web_search`, `paper_search`, and `reason`; other tools are mounted by context or runtime availability.

## Provider testing

Use **Test** buttons before Apply. A green provider test proves only that the profile can make a minimal call; it does not prove your selected model is ideal for every capability.

## See also

- [Providers](/docs/get-started/providers/) — model/search setup recipes
- [Docker](/docs/get-started/docker/) — port and reverse-proxy notes
- [Memory](/docs/explore/memory/) — inspect memory state
