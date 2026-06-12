---
title: Knowledge Bases
description: LlamaIndex-backed, versioned document libraries for RAG, Chat, Co-Writer, Book, and Partners.
---

Knowledge Bases are the document libraries behind RAG. They can ground Chat turns, Co-Writer edits, Book generation, and Partner conversations.

![Knowledge workspace](/screenshots/knowledge.png)

## What a KB contains

| Area | Purpose |
| --- | --- |
| **Files** | Source documents and extraction status. |
| **Add documents** | Upload PDF, Office files, Markdown, text, code, and data files. |
| **Index versions** | Flat `version-N` LlamaIndex storage directories keyed by embedding signature. |
| **Settings** | Embedding model, chunking, and retrieval-related parameters. |

## Versioning model

Re-indexing writes a new `version-N` directory and preserves prior versions. This protects a working index while a rebuild is in progress. Treat older versions as retained history and fallback storage, not as a full user-facing rollback workflow unless your deployment exposes that action.

## CLI mirror

```bash
deeptutor kb list
deeptutor kb info physics
deeptutor kb create physics --doc chapter1.pdf
deeptutor kb create textbooks --docs-dir ./pdfs
deeptutor kb add physics --doc chapter2.pdf
deeptutor kb search physics "What is angular momentum?"
deeptutor kb set-default physics
deeptutor kb delete physics --force
```

## Tips

- Configure an embedding provider before creating serious KBs.
- If you change embedding models, re-index rather than mixing vector spaces.
- Keep small test KBs for Partner/channel smoke tests.
- For Docker, persist the whole `data/` tree so KB versions survive container restarts.

## See also

- [Chat Workspace](/docs/explore/chat-workspace/) — attach KBs to turns
- [Book Engine](/docs/explore/book/) — compile learning material from KBs
- [Partners](/docs/explore/partners/) — copy KBs into partner workspaces
