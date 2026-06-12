---
title: Chat Workspace
description: "The default DeepTutor agent loop: tools, RAG, attachments, memory, notebooks, and deeper capabilities in one thread."
---

Chat is where most work begins. It is not just a message box: it is the default agent loop that can call tools, read sources, search knowledge bases, write notes, ask for clarification, and switch into deeper capabilities without losing the session.

![Chat workspace](/screenshots/chat.png)

## What you see

| Region | What it does |
| --- | --- |
| **Left sidebar** | Main surfaces: Chat, Partners, Co-Writer, Book, Knowledge, Space, Memory, Settings. Recents show resumable sessions. |
| **Composer** | Message box, capability selector, file/context attachment, persona, model selector, and send button. |
| **Activity panel** | Tool calls, intermediate progress, source previews, and generated artifacts. |
| **Notebook / Markdown actions** | Save useful turns to notebooks or export a session as Markdown. |

## The agent loop

![Chat agent loop](/screenshots/chat-agent-loop.png)

A turn can take several rounds:

1. The model drafts a response or tool plan.
2. If tools are needed, DeepTutor dispatches them and appends the observations.
3. The model continues with better evidence.
4. A final tool-free answer ends the turn.

`ask_user` is special: it pauses the turn, asks structured clarification questions, and resumes after you answer.

## Capabilities launched from Chat

| Capability | Use it for |
| --- | --- |
| `chat` | Normal tutoring, open-ended Q&A, lightweight tool use. |
| `deep_solve` | Worked solutions, multi-step reasoning, verification. |
| `deep_question` | Question generation, quiz-style practice, mimic-source workflows. |
| `deep_research` | Subtopic decomposition, RAG/web/arXiv research, cited reports. |
| `visualize` | SVG, Chart.js, Mermaid, HTML, and routed animation outputs. |
| `math_animator` | Manim-heavy math animation workflows. |
| `auto` | Let DeepTutor choose the right capability. |
| `mastery_path` | Learning-path and mastery planning flows. |

## Tools

User-toggleable tools in Settings are `brainstorm`, `web_search`, `paper_search`, and `reason`. Contextual tools mount automatically when useful: `rag`, `read_source`, `read_memory`, `write_memory`, `read_skill`, `load_tools`, `exec`, `web_fetch`, `ask_user`, `list_notebook`, `write_note`, and `github`.

## Practical examples

```text
Attach a KB + ask: "Explain chapter 4 and quiz me on the weak spots."
```

```text
Attach a PDF + ask: "Extract the assumptions and save the final summary to my notebook."
```

```bash
deeptutor run chat "Explain Fourier transform" --tool rag --kb signals
deeptutor chat --capability deep_research --kb papers
```

## See also

- [Partners](/docs/explore/partners/) — the same loop inside IM companions
- [Knowledge](/docs/explore/knowledge/) — RAG libraries for chat grounding
- [Memory](/docs/explore/memory/) — inspectable personalization
- [CLI](/docs/cli/) — run the same turns from terminal
