---
title: Chat Workspace
description: One thread, five modes, any tool. The unified intelligent workspace at the heart of DeepTutor.
---

The Chat Workspace is where most users spend their time. It's a single conversation surface that hosts **five modes** sharing one session, knowledge base, attachments, and references.

Switch mid-thread from a casual question into multi-agent solving, into a quiz, into a full research report — without losing context.

![Chat Workspace](/screenshots/dt-current-home.png)

## Anatomy of the screen

| Region | What it does |
|--------|--------------|
| **Left sidebar** | Navigation across all surfaces; chat history at the top |
| **Top toolbar** | Save current turn to a Notebook, download as Markdown, start a new chat, open Activity / Viewer side panels |
| **Composer** (center) | Where you type — mode selector, attach, Knowledge picker, Space picker, model selector |
| **Activity panel** *(right, toggle)* | Real-time stream of pipeline stages, tool calls, timings |
| **Viewer panel** *(right, toggle)* | Renders generated artifacts: SVG, Mermaid, Chart.js, HTML, Manim video |

## The five modes

The capability picker is in the composer. Switch any time — the conversation context persists.

### Chat

Flexible conversation with any tool. The default mode — covers about 80% of questions.

The chat pipeline runs an **agentic loop**: LLM call → parse protocol labels (THINK / TOOL / FINISH) → dispatch tool calls in parallel → feed results back → iterate until FINISH or context guard.

**Tools available in Chat mode** (composed per-turn based on context):

| Tool | Mounted when… |
|------|---------------|
| `rag` | A KB is attached |
| `read_source` | Any non-image source attached |
| `read_memory` / `write_memory` | Always |
| `web_search` | Toggled in Settings → Tools |
| `web_fetch` | Always |
| `code_execution` | Toggled in Settings |
| `reason` | Toggled in Settings |
| `brainstorm` | Toggled in Settings |
| `paper_search` | Toggled in Settings |
| `geogebra_analysis` | When math image attached |
| `list_notebook` / `write_note` | ≥1 notebook exists |
| `github_query` | Always |
| `ask_user` | Always |

### Solve

Multi-step problem-solving: plan → investigate → solve → verify, with precise source citations. Built on the `deep_solve` agentic engine.

When to use: math problems that need step-by-step work, physics with multiple subproblems, algorithm questions where reasoning should be explicit.

Tools commonly enabled: `rag`, `reason`, `code_execution`, `web_search`.

### Quiz

Auto-validated question generation grounded in your KB. Spawns a follow-up chat composer per question for discussion / hints / grading. Built on the `deep_question` agentic engine.

Three modes inside Quiz:

- **Custom** *(default)* — generate from a topic
- **Mimic** — upload a past exam paper, generate new questions in the same style
- **Followup** — discuss prior quiz questions without generating new ones

Configurable: `num_questions`, `difficulty`, `question_types` (short_answer / mcq / numerical / code), `per_type_counts`.

### Research

Decomposes a topic into subtopics, dispatches **parallel agents** across RAG / web / arXiv, produces a cited report with iterative append-mode revisions.

Flow:

1. **Rephrasing** — restates your question precisely
2. **Decomposing** — proposes a 3–7 sub-topic outline ★ (you confirm / edit here)
3. **Researching** — parallel agentic loops per sub-topic
4. **Reporting** — synthesizes structured Markdown report with citations

The outline confirmation step is the killer UX feature: you steer the research before the expensive work runs.

### Visualize

The unified visualization capability — analyzer picks `render_type` based on intent:

| Render type | Best for | Output |
|-------------|----------|--------|
| `svg` | Static diagrams, icons | Inline SVG |
| `chartjs` | Bar / line / pie / scatter charts | Interactive canvas |
| `mermaid` | Flowcharts, sequence diagrams, state machines | Mermaid SVG |
| `html` | Interactive demos, mini-apps | Sandboxed iframe |
| `manim_video` | Math animations | MP4 (requires `[math-animator]` extra) |
| `manim_image` | Math storyboards | PNG |

> Math Animator is **not a separate capability** — it's just two of Visualize's six render types (`manim_video` / `manim_image`).

## Cumulative source inventory

A session carries citations across turns. RAG / web hits from earlier turns remain reusable later in the same conversation — the model can reference them by index.

## Attachments

Click **Attach** to bring files into the turn:

| Type | Sources |
|------|---------|
| **PDFs, DOCX, XLSX, PPTX** | Direct upload — routed through the appropriate extractor |
| **Images** | Direct upload — vision models OCR / interpret |
| **Notebook records** | Space → Notebooks picker |
| **History sessions** | Space → Chat History picker |
| **Question Bank entries** | Space → Question Bank picker |
| **Book references** | Book Engine pages |

Attachments don't go into the system prompt — they show up as **tool-readable sources**. The model uses `read_source` to load full content when needed.

## Top-right actions

| Button | What it does |
|--------|--------------|
| **Save to Notebook** | Save the current turn as a record in a notebook |
| **Download Markdown** | Export the current turn as `.md` |
| **New chat** | Start a fresh session |
| **Activity** | Real-time stream of pipeline events (stages, tool calls, timings) |
| **Viewer** | Renders generated artifacts (SVG, Mermaid, Chart.js, HTML, Manim) |

## `ask_user` mid-turn

If the model needs clarification, it can call the `ask_user` tool, which **pauses the turn** and renders 1–3 structured questions in the chat. Answer them, click Submit, and the turn resumes with your answers in context.

## Session continuity

Every conversation has a session id. Sessions persist across:

- Browser refreshes / restarts
- Mode switches within the same session
- Web UI ↔ CLI boundary

```bash
# Resume a Web session from CLI
deeptutor chat --session sess_abc123
```

Sessions started in CLI show up in the Web sidebar (and vice versa).

## Memory awareness

The model has built-in access to your L3 memory via the `read_memory` tool. After a few sessions, it knows:

- Your background (`profile.md`)
- Your knowledge scope (`scope.md`)
- Your explicit preferences (`preferences.md`)
- Recent learnings (`recent.md`)

See [**Memory**](/docs/explore/memory/) for the full three-layer architecture.

## See also

- [**Memory**](/docs/explore/memory/) — three-layer persistent memory + Memory Graph
- [**Knowledge**](/docs/explore/knowledge/) — RAG-ready Knowledge Bases
- [**Space**](/docs/explore/space/) — read / review hub
- [**Settings**](/docs/explore/settings/) — providers, tools, capabilities
