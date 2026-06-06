---
title: Memory
description: Three-layer pipeline (L1 / L2 / L3), an inspectable workbench, and the Memory Graph — audit *why* DeepTutor knows what it knows.
---

DeepTutor's memory is a **three-layer pipeline** with an inspectable workbench at `/memory`. The two-file v1 `SUMMARY.md` / `PROFILE.md` model is gone; everything is migrated into the new layout on first boot.

![Memory Workbench](/images/dt-memory.png)

## The three layers

| Layer | Role | Storage |
|-------|------|---------|
| **L1 · Workspace mirror** *(LIVE)* | Append-only trace of every interaction, per surface, per day. The lossless record of what actually happened. | `trace/<surface>/<YYYY-MM-DD>.jsonl` |
| **L2 · Per-surface summaries** *(CURATED)* | Surface-specific facts extracted by the consolidator. Each fact carries footnote citations back to L1 traces. Supports per-doc **Update / Audit / Dedup** runs. | `L2/<surface>.md` |
| **L3 · Cross-surface knowledge** *(SYNTHESIS)* | Cross-surface synthesis: your `profile`, `recent` timeline, `scope` of knowledge, and `preferences`. Hedged claims, each backed by L2 evidence. | `L3/{recent,profile,scope,preferences}.md` |

## Seven surfaces feed the pipeline

| Surface | What L1 captures |
|---------|------------------|
| `chat` | Every chat turn (input, tool calls, output) |
| `notebook` | Notebook creates / edits / deletes |
| `quiz` | Quiz generations + your answers + grading results |
| `kb` | KB creates / queries / indexing events |
| `book` | Book reading sessions, page-level interactions |
| `tutorbot` | TutorBot messages (across all channels) |
| `cowriter` | Co-Writer document edits |

## The consolidator

The consolidator is **LLM-driven** and runs asynchronously (`POST /memory/runs/start` — also reachable from the workbench). You can:

- **Fire it manually** — from the workbench, click "Run consolidator"
- **Watch L1 → L2 → L3 propagate** — live progress stream
- **Edit any layer by hand** — your edits are merged on the next run

Default cadence (tunable in **Settings → Memory**):

| Pass | When |
|------|------|
| L1 → L2 (per surface) | Every N turns on that surface, or when triggered |
| L2 → L3 cross-surface | First turn each day, or on demand |

## The Memory Workbench (Web UI)

Open `/memory`. Five sub-views:

| Tab | Route | What |
|-----|-------|------|
| **L3** | `/memory/l3` *(default)* | The four cross-surface docs |
| **L2** | `/memory/l2` | Seven per-surface docs |
| **L1** | `/memory/l1` | Raw event traces per surface, per day |
| **Graph** | `/memory/graph` | The Memory Graph (see below) |
| **Resolve** | `/memory/resolve` | Look up a footnote id → originating event |

## L3 in detail

Four markdown files:

| File | Contents |
|------|----------|
| `recent.md` | A rolling summary of recent learning (last few days/weeks) — what you've been studying, what's open |
| `profile.md` | Who you are: background, goals, role, learning style |
| `scope.md` | Topics you've engaged with and a rough mastery indicator |
| `preferences.md` | Explicit preferences: language for replies, depth, format, examples-first vs theory-first |

**Only `preferences.md` is written by the model directly** (via the `write_memory` tool). The other three are managed by the consolidator agent; your manual edits get merged on the next pass.

## L2 in detail

Seven documents, one per surface. Each is a structured markdown file with **footnote-style citations** like `[^abc123]` that link back to specific L1 events.

Per-doc actions in the workbench:

- **Update** — re-run consolidation on this surface's recent L1 events
- **Audit** — LLM checks the L2 for stale, contradictory, or unsupported claims
- **Dedup** — merge near-duplicate bullet points

## L1 in detail

Per-surface daily JSONL:

```jsonl
{"id":"evt_001","timestamp":"2026-05-21T14:23:01Z","surface":"chat","kind":"turn","content":"User asked about the chain rule"}
{"id":"evt_002","timestamp":"2026-05-21T14:23:18Z","surface":"chat","kind":"tool_call","content":"rag_search"}
{"id":"evt_003","timestamp":"2026-05-21T14:24:38Z","surface":"chat","kind":"turn_complete","content":"Explained with worked example"}
```

L1 is rarely useful directly — but L2 footnotes reference these ids, and the **Resolve** view lets you trace a footnote back to its source.

## The Memory Graph

![Memory Graph](/images/dt-memgraph.png)

The **Memory Graph** at `/memory/graph` renders **all three layers at once**:

- **Center** — L3 synthesis nodes (`profile`, `recent`, `scope`, `preferences`)
- **Middle ring** — L2 facts per surface
- **Outer ring** — L1 traces, grouped by surface

Hover any node for an inline preview. Click to **lock the highlight** and trace the L3 → L2 → L1 references inward — so you can audit *why* DeepTutor "knows" something about you.

This is the killer feature: **transparent provenance**. Every claim DeepTutor makes about you, you can drill into.

## How chat reads memory

At the start of each chat turn, the system prompt includes concatenated L3 docs:

```text
─── User profile (from memory) ─────────────────────────────────────
[recent.md content]

[profile.md content]

[scope.md content]

[preferences.md content]
─────────────────────────────────────────────────────────────────────
```

The model also has the `read_memory` tool for mid-turn lookups, and `write_memory` for persisting explicit preferences (≤240 chars, content-safety filtered, auto-linked to the triggering L1 event).

## File layout

```text
data/user/memory/
├── trace/
│   ├── chat/2026-05-21.jsonl     ← L1
│   ├── chat/2026-05-22.jsonl
│   ├── notebook/2026-05-22.jsonl
│   ├── quiz/2026-05-22.jsonl
│   ├── kb/2026-05-22.jsonl
│   ├── book/2026-05-22.jsonl
│   ├── tutorbot/2026-05-22.jsonl
│   └── cowriter/2026-05-22.jsonl
├── L2/
│   ├── chat.md
│   ├── notebook.md
│   ├── quiz.md
│   ├── kb.md
│   ├── book.md
│   ├── tutorbot.md
│   └── cowriter.md
└── L3/
    ├── recent.md
    ├── profile.md
    ├── scope.md
    └── preferences.md
```

In multi-user mode this lives under `multi-user/<uid>/memory/`.

## CLI mirror

```bash
deeptutor memory show               # L3 concatenated (default)
deeptutor memory show chat          # an L2 surface doc
deeptutor memory show profile       # an L3 doc
deeptutor memory clear all --force  # wipe all layers (destructive)
deeptutor memory clear chat         # L1 for one surface
```

## Multi-user memory

Each user has their own memory under `multi-user/<uid>/memory/`. Memory is **not shared across users** — even admins can't read another user's memory.

## See also

- [**Chat Workspace**](/docs/explore/chat-workspace/) — how chat consumes / writes memory
- [**Space → Notebooks**](/docs/explore/space/) — notebooks feed the `notebook` surface
- [**Settings → Memory**](/docs/explore/settings/) — tune consolidation cadence
