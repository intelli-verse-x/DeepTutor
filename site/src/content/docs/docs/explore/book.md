---
title: Book Engine
description: A multi-agent pipeline that compiles your materials into interactive "living books" with 13 block types.
---

Give DeepTutor a topic, point it at your knowledge base, and **Book Engine** produces a structured, interactive book — not a static export, but a living document you can read, quiz yourself on, and discuss in context.

## How it works

Behind the scenes, a multi-agent pipeline handles the heavy lifting:

1. **Outline proposal** — given your topic + KB, propose chapter structure
2. **Source retrieval** — pull relevant passages from the KB
3. **Chapter tree synthesis** — assemble a hierarchical chapter outline
4. **Page planning** — for each page, plan which blocks go where
5. **Block compilation** — generate each block (text, quiz, code, figure, …)

You stay in control: review the proposal, reorder chapters, and chat alongside any page.

## The 13 block types

Pages are assembled from 13 block types, each rendered with its own interactive component:

| Block | What it is |
|-------|-----------|
| **Text** | Standard prose paragraphs |
| **Callout** | Tip / Warning / Note / Important — colored sidebar boxes |
| **Quiz** | Inline interactive question; answers checked against an expected response |
| **Flash cards** | Front / back flipping cards for spaced repetition |
| **Code** | Syntax-highlighted snippet with optional executable runtime |
| **Figure** | Image with caption + alt text |
| **Deep dive** | Collapsible section for advanced / optional material |
| **Animation** | Manim-rendered video |
| **Interactive demo** | Embedded interactive HTML (including a **GeoGebra viewer** for math) |
| **Timeline** | Vertical event timeline |
| **Concept graph** | Mini knowledge graph showing relationships between concepts |
| **Section** | A grouping container for nested blocks |
| **User note** | Editable rich-text area for the reader's own notes |

## KB fingerprinting and drift detection

Book pages are **fingerprinted against their source KB**. When source documents change:

- `deeptutor book health <book_id>` reports drift (which pages are stale)
- `deeptutor book refresh-fingerprints <book_id>` clears stale-page flags when you've acknowledged the changes

This makes it safe to use Book Engine on KBs that evolve — you'll know when a page is no longer in sync.

## Working with a book

In the Web UI:

1. Navigate to **Book** in the left sidebar
2. **+ New book** → pick a topic, attach a KB
3. Review and edit the proposed outline
4. Confirm — the pipeline compiles each page
5. Open a page to read, quiz yourself, or chat alongside

## From the CLI

```bash
deeptutor book list                                   # all books in the workspace
deeptutor book health <book_id>                       # KB drift report
deeptutor book refresh-fingerprints <book_id>         # mark stale pages as acknowledged
```

JSON output for health:

```json
{
  "kb_drift": {
    "kb_name": "physics",
    "stale_pages": ["page_abc", "page_def"],
    "drift_ratio": 0.12
  },
  "log_health": {
    "last_compile": "2026-05-20T14:23:01Z",
    "errors": []
  }
}
```

## Pairs well with

- **Knowledge** — A book is only as good as its KB. Start there.
- **Chat alongside the page** — Each page has its own chat composer pinned to it; ask follow-ups grounded in the page content.
- **Notebooks** — Save chat takeaways from book reading into a notebook for later review.

## See also

- [**Knowledge**](/docs/explore/knowledge/) — build the KB that backs a book
- [**Space → Notebooks**](/docs/explore/space/) — save book discussions
- [**CLI → book commands**](/docs/cli/commands/)
