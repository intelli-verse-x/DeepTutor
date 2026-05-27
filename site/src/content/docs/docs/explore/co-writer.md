---
title: Co-Writer
description: A Markdown editor where AI is a first-class collaborator — Edit Agent, Narrator Agent, document templates.
---

**Co-Writer** is DeepTutor's Markdown editor designed around AI collaboration. It has two integrated AI agents:

- **Edit Agent** — refines selected text (rewrite, expand, condense, change tone)
- **Narrator Agent** — generates new content (continue writing, fill outline, explain concept)

Plus document templates, version history, and integration with Knowledge Bases.

## Opening Co-Writer

Click **Co-Writer** in the left navigation, or open `/co-writer`. The first time you visit, you'll see the document picker. Pick **+ New document** to start fresh, or open a recent one.

## The editor

A standard Markdown editor with two panes:

| Pane | What |
|------|------|
| **Left** | Source Markdown — type, edit, format |
| **Right** | Rendered preview (toggle off if you want full-width source) |

Keyboard shortcuts:

| Key | Action |
|-----|--------|
| `⌘B` / `Ctrl+B` | Bold |
| `⌘I` / `Ctrl+I` | Italic |
| `⌘K` / `Ctrl+K` | Insert link |
| `⌘S` / `Ctrl+S` | Save (autosaves anyway) |
| `⌘/` / `Ctrl+/` | Toggle AI sidebar |

## The AI sidebar

Open with `⌘/`. Two tabs:

### Edit (selection-based)

Select text in the editor, then pick an Edit action:

| Action | What it does |
|--------|--------------|
| Rewrite | Same meaning, different words |
| Expand | Add detail, context, examples |
| Condense | Shorten while keeping the key points |
| Change tone | Formal / casual / academic / friendly |
| Fix grammar | Light edits only |
| Translate | To another language |

The Edit Agent replaces the selected text with the result. Undo with `⌘Z`.

### Narrator (cursor-based)

Place your cursor where you want new content, then:

| Action | What it does |
|--------|--------------|
| Continue | Continue writing from this point |
| Fill outline | Convert your bullet outline into prose |
| Explain | Add an explanation of the previous paragraph |
| Cite from KB | Look up something in an attached KB and add a citation |

The Narrator Agent inserts at the cursor.

## Attaching context

Just like Chat, you can attach context to Co-Writer:

- **Knowledge Base** — Narrator can pull from your KB when generating
- **History session** — Reference a prior Chat / Research turn
- **Notebook records** — Pull from saved snippets

Click the paperclip icon in the AI sidebar.

## Templates

DeepTutor ships sample templates:

| Template | Good for |
|----------|---------|
| Research memo | Multi-source synthesis with citations |
| Lecture notes | Outline + filled sections |
| Problem set solutions | Worked solutions with code blocks |
| Reading log | One entry per paper / chapter |

Pick one when creating a new document. Templates pre-fill structure and prompts the agents understand contextually.

## Embedding capability outputs

You can embed results from other DeepTutor capabilities directly into a document:

- **Deep Solve output** → drag the solution into Co-Writer
- **Visualize artifact** → embedded as an inline SVG / Mermaid block
- **Quiz** → embedded as expandable details block

## Saving and exporting

Documents are auto-saved every few seconds. Manual export options:

- **Download .md** — raw Markdown
- **Download .pdf** — rendered via Pandoc
- **Copy to clipboard** — for pasting into other tools

## Version history

Click the clock icon in the top-right to see version history. Co-Writer keeps:

- All saves from the last 24 hours
- Hourly snapshots for the last 7 days
- Daily snapshots indefinitely

Revert to a prior version with one click.

## Multi-user notes

In multi-user mode, each user has their own Co-Writer document space. Sharing is on the roadmap (track [issue #498](https://github.com/HKUDS/DeepTutor/issues/498)).

## See also

- [**Knowledge Bases**](/docs/explore/knowledge/) — attach KBs for ground-truth citations
- [**Chat Workspace**](/docs/explore/chat-workspace/) — run Visualize / Research and bring outputs into documents
- [**Space**](/docs/explore/space/) — save and reuse durable outputs
