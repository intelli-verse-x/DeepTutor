---
title: Overview
description: A map of the Explore section — five core surfaces, three-layer Memory, and a unified Settings workbench.
---

DeepTutor is organised around **five core surfaces**, a **three-layer Memory** that sits underneath them, and a unified **Settings** workbench. This section walks each one; the table below is the map.

![DeepTutor home screen](/screenshots/dt-current-home.png)

## The five surfaces

| # | Surface | One-liner | Page |
|---|---------|-----------|------|
| 1 | **Chat** | One thread, five modes (Chat / Solve / Quiz / Research / Visualize), any tool | [**Chat Workspace**](/docs/explore/chat-workspace/) |
| 2 | **Co-Writer** | Split-view Markdown workbench where AI is a first-class collaborator | [**Co-Writer**](/docs/explore/co-writer/) |
| 3 | **Book** | Multi-agent pipeline that compiles your materials into interactive "living books" | [**Book Engine**](/docs/explore/book/) |
| 4 | **Knowledge** | Versioned RAG-ready document libraries (LlamaIndex end-to-end) | [**Knowledge Bases**](/docs/explore/knowledge/) |
| 5 | **Space** | Read / review hub: Chat History, Notebooks, Question Bank, Skills | [**Space**](/docs/explore/space/) |

## Plus

| Surface | One-liner | Page |
|---------|-----------|------|
| **Memory** | Three-layer pipeline (L1 trace / L2 per-surface / L3 cross-surface) + Memory Graph | [**Memory**](/docs/explore/memory/) |
| **Settings** | Unified control center — Models, Embedding, Search, Capabilities, Tools, Memory, MCP, Appearance, Status | [**Settings**](/docs/explore/settings/) |

## How they fit together

- **Capabilities live inside Chat.** Solve / Quiz / Research / Visualize are not separate top-level tabs — they're modes you switch into mid-thread, sharing the session, knowledge base, attachments, and citation history of the surrounding chat.
- **Tools stay decoupled from workflows.** Built-in tools (RAG, web search, code execution, reason, brainstorm, paper search, `ask_user`, `web_fetch`, `write_note`, `list_notebook`, `github_query`) compose freely on top of every mode. Add MCP servers in Settings to extend.
- **Memory is the substrate.** Every surface reads from and writes to the same three-layer Memory store, so what you learn in Chat surfaces in Co-Writer, in a TutorBot conversation, or in a Book reading session.
- **Sessions cross surfaces.** A session started in the Web UI shows up in the CLI (and vice versa); a chat session can be saved into a Notebook, attached to a Book page, or referenced from Co-Writer.

## Next

Start with [**Chat Workspace**](/docs/explore/chat-workspace/) — most users spend ~80% of their time there. From the CLI side, see the [**CLI overview**](/docs/cli/).
