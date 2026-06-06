---
title: Knowledge Bases
description: A dedicated workspace for the document collections that power RAG. LlamaIndex end-to-end, versioned indexes, drift-resistant.
---

A dedicated workspace for the document collections that power RAG. Each knowledge base is a versioned, searchable index over your documents — attach it to any chat turn, Co-Writer document, or Book.

![Knowledge Workspace](/screenshots/dt-knowledge.png)

## Four tabs per KB

| Tab | What |
|-----|------|
| **Files** | Browse uploaded sources, preview PDFs inline, see per-file size / status |
| **Add documents** | Drop in PDFs, Office files (DOCX / XLSX / PPTX), Markdown, plain text, and a wide range of code / data file types — routed through the appropriate extractor automatically |
| **Index versions** | Every (re-)index is a tracked version. Roll back to an earlier index, compare embedding models, or inspect chunking stats without losing the previous build |
| **Settings** | Pick the embedding provider / model, chunking parameters, and reranker. Defaults inherit from your global LLM and embedding profiles |

## Built on LlamaIndex end-to-end

Indexing is built on **LlamaIndex** end-to-end. The previous dual-pipeline split was consolidated in the v1.4 refactor. Features:

- **Retry-safe re-index** — partial failures don't lose progress
- **Embedding-mismatch detection** — if you change embedders, you're warned before silently producing bad results
- **Resilient persisted-vector handling** — corrupt vectors are quarantined, not catastrophic
- **Versioned indexes** — every re-index is a new version, comparable and rollback-able

## Supported document types

| Type | Notes |
|------|-------|
| **PDF** | Text extraction; OCR for scanned pages on a best-effort basis |
| **DOCX** | Native Word documents |
| **XLSX** | Spreadsheets — each sheet as a chunk batch |
| **PPTX** | PowerPoint — each slide as a chunk |
| **TXT / MD / HTML** | Cleaned and chunked |
| **Code files** | Python / JS / TS / Go / Rust / many others |

## Creating a KB

In the UI:

1. **Knowledge** in the left sidebar → **+ New knowledge base**
2. Name it, pick a RAG provider *(defaults to LlamaIndex)*
3. Upload documents — drag-and-drop or file picker
4. **Create**

DeepTutor extracts, chunks, embeds each chunk, and stores the vector index. For a 200-page PDF, this typically takes 1–3 minutes.

## Default KB

The KB with a ⭐ star is the **default** — auto-attached when you start a new chat. Click the star to change it.

## Index versions

Every (re-)index is tracked:

- **Roll back** — restore a prior version if a re-index degraded retrieval quality
- **Compare** — A/B different embedding models / chunking strategies on the same source documents
- **Inspect** — chunking stats, embedding dimension, indexing duration

## Searching from the UI

Inside a KB, the search box runs an ad-hoc query. Three modes:

| Mode | Algorithm |
|------|-----------|
| **Hybrid** *(default)* | Semantic embedding + BM25 keyword reranking |
| **Vector** | Pure embedding |
| **Keyword** | Pure BM25 |

## Searching from chat

Attach the KB in the composer and ask naturally — the model decides when to call `rag`:

```text
You> [KB: physics attached] What's the relationship between kinetic energy and momentum?

Model> [calls rag tool]
  ● rag_search(query="kinetic energy momentum relationship", kb_name="physics")
  │ KE = p²/(2m), where p is momentum and m is mass...
  └ #1 rag

Model> [synthesizes a reply citing the retrieved passages]
```

## Multi-KB workflows

Attach multiple KBs to one turn. The model can query them in parallel. Useful for "compare two textbooks", "find the same concept across papers", etc.

## CLI mirror

```bash
deeptutor kb list                                           # all KBs
deeptutor kb info physics                                   # KB details
deeptutor kb create physics --doc chapter1.pdf              # create
deeptutor kb create textbooks --docs-dir ./pdfs/            # from a directory
deeptutor kb add physics --doc chapter3.pdf                 # incremental add
deeptutor kb search physics "What is angular momentum?"     # ad-hoc search
deeptutor kb set-default physics                            # set as default
deeptutor kb delete physics --force                         # delete
```

See [**Commands**](/docs/cli/commands/) for full flag reference.

## Embedding provider

The embedder is configured globally in **Settings → Embedding**. New KBs inherit it. Existing KBs keep their original embedder until re-indexed.

| Provider | Notes |
|----------|-------|
| OpenAI | `text-embedding-3-small` (1536d) / `-large` (3072d) |
| Cohere | `embed-v4.0` |
| Jina | `jina-embeddings-v3` |
| Gemini | `gemini-embedding-001` |
| SiliconFlow | `Qwen/Qwen3-Embedding-8B` |
| Aliyun DashScope | `qwen3-vl-embedding` |
| Ollama | Local embedding models |
| vLLM / LM Studio / OpenAI-compatible | Custom embedding endpoints |

Full provider matrix: [**Providers**](/docs/get-started/providers/).

## Multi-user

In multi-user deployments, KBs are scoped per user. Admins can grant cross-user access (read / read+search / read+search+modify) at `/admin/grants` — see [**Multi-User Deployment**](/docs/get-started/multi-user/).

## See also

- [**Chat Workspace**](/docs/explore/chat-workspace/) — attaching KBs to chat turns
- [**Book Engine**](/docs/explore/book/) — books compile from a KB
- [**Memory**](/docs/explore/memory/) — KBs are for documents; memory is for conversations
