---
title: Memory
description: Inspectable personalization through L1 traces, L2 surface summaries, L3 synthesis, and the Memory Graph.
---

Memory is DeepTutor's inspectable personalization system. It is not a hidden vector store; it is a file-backed three-layer pipeline that you can inspect, edit, and audit.

![Memory workbench](/screenshots/memory-workbench.png)

## Three layers

![Memory overview with L1, L2, and L3 layer cards](/screenshots/memory.png)

The Memory overview shows all three layers at a glance — live L1 traces, curated L2 facts per surface, synthesized L3 knowledge — plus the entry into the Memory graph. Click any layer card to inspect or curate it.

| Layer | Storage | Role |
| --- | --- | --- |
| **L1 trace** | `trace/<surface>/<YYYY-MM-DD>.jsonl` | Append-only raw events. |
| **L2 surface facts** | `L2/<surface>.md` | Curated facts per surface, with citations back to L1. |
| **L3 synthesis** | `L3/<recent|profile|scope|preferences>.md` | Cross-surface summaries used for personalization. |

Supported surfaces are `chat`, `notebook`, `quiz`, `kb`, `book`, `tutorbot`, and `cowriter`. The `tutorbot` surface name is retained for compatibility with earlier memory data, even though the product-facing companion model is now Partners.

The overview presents L1 as a **workspace mirror**: alongside the raw trace, DeepTutor keeps a per-surface snapshot of your live workspace, and refreshing it records changes into L1.

## Memory Graph

![Memory graph](/screenshots/memory-graph.png)

The graph view lets you trace a high-level L3 claim back to L2 supporting facts and then to L1 events. Use it when you want to answer: "Why does DeepTutor think it knows this about me?"

## CLI

```bash
deeptutor memory show L3
deeptutor memory show L2
deeptutor memory show profile
deeptutor memory show chat
deeptutor memory clear trace --force
```

## Good practice

- Keep memory on for long-running learning workflows.
- Review L3 preferences when DeepTutor's tone or assumptions feel off.
- Clear only L1 trace for a surface if you want to remove raw history while keeping curated summaries.
- In multi-user mode, each user gets scoped memory under their own workspace.
