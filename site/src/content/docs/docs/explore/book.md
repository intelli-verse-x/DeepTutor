---
title: Book Engine
description: Build interactive living books from knowledge bases, notebooks, question banks, and chat history.
---

Book turns your materials into interactive learning content. A book can start from a topic plus selected sources, then compile into pages with explanations, quizzes, visual blocks, and reader notes.

<p align="center">
  <img src="/screenshots/book01.png" alt="Book reading view" width="31%" />
  <img src="/screenshots/book02.png" alt="Book interactive block view" width="31%" />
  <img src="/screenshots/book03.png" alt="Book creation view" width="31%" />
</p>

## Creation flow

1. Open **Book -> New book**.
2. Choose a topic and sources: Knowledge Bases, Notebooks, Question Bank, or Chat history.
3. Review the generated proposal before compiling.
4. Let BookEngine generate page plans and blocks.
5. Read, annotate, quiz yourself, or chat alongside pages.

## Block types

Book pages are built from typed blocks: text, sections, callouts, quiz, flash cards, timeline, code, figure, interactive HTML, animation, concept graph, deep dive, and user note. The goal is not to produce a PDF-like dump; the page should stay usable as a learning environment.

## Source drift

Books track source fingerprints. If a knowledge base changes after a book is compiled, maintenance commands help you inspect drift:

```bash
deeptutor book list
deeptutor book health <book_id>
deeptutor book refresh-fingerprints <book_id>
```

## Good source choices

| Source | Use when |
| --- | --- |
| Knowledge Base | You want grounded textbook/paper content. |
| Notebook | You have curated notes or prior summaries. |
| Question Bank | You want practice-centered pages. |
| Chat History | You want to turn a tutoring session into study material. |

## See also

- [Knowledge](/docs/explore/knowledge/) — build document libraries first
- [Chat Workspace](/docs/explore/chat-workspace/) — discuss book pages in context
- [CLI commands](/docs/cli/commands/) — book maintenance commands
