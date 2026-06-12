---
title: Co-Writer
description: A selection-aware Markdown workspace where AI edits can be grounded in your KB or the web.
---

Co-Writer is a Markdown workspace for notes, reports, tutorials, and product/learning drafts. It pairs a source editor with live preview and lets the agent edit selected text instead of replacing your whole document.

## Opening Co-Writer

Open **Co-Writer** from the sidebar or visit `/co-writer`. Create a blank draft or start from the sample template.

## Editor model

![Co-Writer editor with Markdown source on the left and live preview on the right](/screenshots/co-writer.png)

The workspace is a split view: Markdown source on the left, rendered preview on the right, with the formatting toolbar above the editor. Selecting text in the source pane surfaces the AI edit entry (`rewrite`, `expand`, `shorten`) without leaving the document.

| Part | What it does |
| --- | --- |
| **Document list** | Create, open, rename, and delete Markdown drafts. |
| **Source editor** | Write Markdown, tables, code, math, Mermaid-style diagrams, and structured notes. |
| **Preview pane** | Render the document while you write. |
| **Selection popover** | Select text and run `rewrite`, `expand`, or `shorten`. |
| **Save to Notebook** | Preserve a finished draft as reusable context. |

## AI edits

The edit agent receives the selected text, your instruction, optional KB context, optional web context, and the surrounding document. This makes it useful for:

- tightening an explanation without changing the section structure,
- expanding terse notes into a tutorial paragraph,
- shortening a long draft before moving it to a notebook,
- grounding a claim against a selected knowledge base.

## Recommended workflow

1. Draft roughly in Markdown.
2. Select only the paragraph that needs help.
3. Use **Rewrite**, **Expand**, or **Shorten**.
4. Review the diff mentally before continuing.
5. Save polished notes into a Notebook when they should become durable context.

## Storage

Co-Writer documents live under the active user workspace, so multi-user deployments keep each user's drafts isolated. Partners can use notebook/skill resources copied from a user's library, but they do not edit the user's Co-Writer drafts directly.

## See also

- [Chat Workspace](/docs/explore/chat-workspace/) — generate source material and save useful turns
- [Space](/docs/explore/space/) — manage notebooks, skills, and personas
- [Knowledge](/docs/explore/knowledge/) — provide grounded context for edits
