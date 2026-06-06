---
title: Settings
description: The unified control center - Appearance, Status, Network, LLM / Embedding / Search, Capabilities, Memory, MCP, Tools.
---

The settings surface was unified in v1.4 and split by concern, with a **draft / Apply** model so changes are atomic and can be reverted before save.

![Settings overview](/screenshots/dt-settings.png)

## Tabs

In the order they appear in the left navigation:

| Tab | What it controls |
|-----|------------------|
| **Appearance** | UI language and theme (Cream, Snow, Dark, Glass) |
| **Status** | Live health probe across LLM, embedding, search, and storage backends |
| **Network** | Backend/frontend ports, browser API base, CORS origins, and deployment hints |
| **LLM** | Provider catalog, base URLs, API keys, active model selection |
| **Embedding** | Same shape as LLM, but for the embedder |
| **Search** | Web search provider (Tavily / Brave / Jina / Serper / SearXNG / DuckDuckGo / Perplexity) |
| **Capabilities** | Per-capability tunables (chunking, LLM budget, dedup, max iterations) |
| **Memory** | Toggle consolidator runs, configure cadence and budget |
| **MCP servers** | Register external Model Context Protocol servers |
| **Tools** | Inspect every built-in tool, parameters, status, i18n status copy |

A **Tour** launcher walks new users through the page.

## Appearance

| Setting | Options |
|---------|---------|
| Language | English, 简体中文 |
| Theme | Cream *(default)* / Snow / Dark / Glass |
| Sidebar density | Compact / Comfortable |

## Status

A live health probe:

- LLM provider — connection OK / failing / not configured
- Embedding provider — same
- Search provider — same
- Storage backends — connection state, latency
- Last health-check time per provider

Use this to **debug "the model isn't responding"** issues fast.

## Network

Network settings are startup settings stored in
`data/user/settings/system.json`. Use this page for Docker, LAN, and
reverse-proxy deployments:

- **Backend / frontend ports** control what DeepTutor starts on. Docker port
  mappings must match the container-side ports.
- **Public API base** maps to `next_public_api_base_external`. It is the URL the
  browser uses for HTTP and WebSocket API calls.
- **CORS origins** are frontend page origins allowed to call the backend. They
  are only required for authenticated cross-origin deployments.
- `public_api_base` is accepted as a compatibility alias and normalized on save.

With auth disabled, DeepTutor permits normal HTTP/HTTPS browser origins by
default. With auth enabled, set exact frontend origins and use
`auth.json: cookie_secure=true` for HTTPS cross-site cookies.

## LLM / Embedding / Search

All three share the same **profile** model:

- You can configure **multiple profiles** (e.g., `openai-gpt-4o`, `anthropic-sonnet-4`, `local-ollama`)
- Pick **one active model** per service from the catalog
- Per-turn overrides happen in the chat composer's model selector

Test connection with the **Test** button — it issues a small probe call and reports latency.

Full provider matrix: [**Providers**](/docs/get-started/providers/).

## Capabilities

Per-capability tunables for Chat, Solve, Quiz, Research, Visualize, and Co-Writer:

| Setting | What |
|---------|------|
| **Chunking** | How retrieved KB content is chunked into the context window |
| **LLM budget** | Max tokens / max iterations per capability run |
| **Dedup policy** | How duplicate sources are handled |
| **Reference policy** | When to insert citations |
| **Max iterations** | Hard guard on agentic loops |

Backed by a unified `emit_capability_result` envelope and a shared `UsageTracker` that surfaces **per-call cost**.

## Memory

| Setting | Effect |
|---------|--------|
| **Toggle consolidator** | Pause / resume the L1 → L2 → L3 pipeline |
| **Cadence** | How often each consolidation pass runs |
| **Budget** | Token budget per consolidation pass |
| **Jump to workbench** | Opens `/memory` directly |

See [**Memory**](/docs/explore/memory/) for the full three-layer architecture.

## MCP servers

The **Model Context Protocol** integration lets you plug in external MCP servers as additional tools. Add server configs here; their tools surface alongside built-ins.

Example:

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

Inspect every built-in tool:

- Name, description, parameters
- Status (enabled / coming-soon)
- i18n status copy (how the tool's progress messages appear in English / 中文)
- Whether it's user-toggleable

Five tools are user-toggleable globally: `brainstorm`, `web_search`, `paper_search`, `code_execution`, `reason`. Context-mounted tools (`rag`, `read_memory`, `write_memory`, etc.) can't be toggled here — they appear automatically based on what's attached to the turn.

## i18n

Every capability ships a canonical `capabilities/prompts/{en,zh}/<name>.yaml` so status messages stay consistent in both English and 中文.

## CLI mirror

```bash
deeptutor config show           # Print current configuration (secrets masked)
deeptutor init                  # Re-run wizard, re-prompt every value
$EDITOR data/user/settings/model_catalog.json   # direct edit
```

## See also

- [**Providers**](/docs/get-started/providers/) — full LLM / embedding / search provider matrix
- [**Memory**](/docs/explore/memory/) — what the consolidator actually does
- [**Multi-User Deployment**](/docs/get-started/multi-user/) — auth-related settings
