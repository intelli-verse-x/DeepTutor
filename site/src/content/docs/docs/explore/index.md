---
title: Overview
description: A map of the Explore section — Chat, Partners, Co-Writer, Book, Knowledge, Space, Memory, and Settings.
---

DeepTutor is organized around connected learning surfaces that share one agent-native runtime. This section starts with the surfaces users touch every day, then explains the library, memory, and control layers underneath them.

![Chat workspace](/screenshots/chat.png)

## Product map

| # | Surface | One-liner | Page |
|---|---------|-----------|------|
| 1 | **Chat** | Default agent loop: tools, RAG, attachments, notebook writes, and deeper capabilities in one thread | [**Chat Workspace**](/docs/explore/chat-workspace/) |
| 2 | **Partners** | Persistent IM-connected companions with their own soul, library, and channels | [**Partners**](/docs/explore/partners/) |
| 3 | **Co-Writer** | Selection-aware Markdown editor where AI edits can use KB or web context | [**Co-Writer**](/docs/explore/co-writer/) |
| 4 | **Book** | Compile your materials into interactive living books | [**Book Engine**](/docs/explore/book/) |
| 5 | **Knowledge** | LlamaIndex-backed, versioned RAG libraries | [**Knowledge Bases**](/docs/explore/knowledge/) |
| 6 | **Space** | Skills, personas, notebooks, history, and reusable context assets | [**Space**](/docs/explore/space/) |
| 7 | **Memory** | L1 trace, L2 per-surface facts, L3 cross-surface synthesis, and graph audit | [**Memory**](/docs/explore/memory/) |
| 8 | **Settings** | Models, embeddings, search, tools, MCP, network, memory, and runtime control | [**Settings**](/docs/explore/settings/) |

## How they fit together

- **Chat is the default loop.** `chat`, `deep_solve`, `deep_question`, `deep_research`, `visualize`, `math_animator`, `auto`, and `mastery_path` run through the same orchestrated runtime.
- **Partners reuse Chat, not a separate bot engine.** A partner message becomes a scoped chat turn inside `data/partners/<id>/workspace/`.
- **Tools are mounted by context.** User-toggleable tools are `brainstorm`, `web_search`, `paper_search`, and `reason`; contextual tools include RAG, source reading, memory, skills, notebooks, URL fetch, GitHub, ask-user, and sandboxed execution.
- **Memory is inspectable.** The workbench and graph let you trace synthesized facts back to L2 summaries and raw L1 events.

## Next

Start with [**Chat Workspace**](/docs/explore/chat-workspace/) for the core interaction model, then read [**Partners**](/docs/explore/partners/) if you want DeepTutor inside IM channels.
