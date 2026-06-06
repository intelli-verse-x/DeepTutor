---
title: Server API
description: The HTTP and WebSocket surface exposed by deeptutor serve -- for custom frontends and integrations.
---

`deeptutor serve` exposes a FastAPI backend at `http://localhost:8001/` unless you configured a different backend port. This page gives the high-signal map for custom frontends, mobile apps, and service-to-service integrations.

For the exhaustive, always-current schema, start the server and open:

```text
GET /openapi.json     # Full OpenAPI 3.1 spec
GET /docs             # Interactive Swagger UI
GET /redoc            # Alternative ReDoc UI
```

## Starting the server

```bash
# Backend only. Port comes from data/user/settings/system.json, default 8001.
deeptutor serve

# Custom host/port for this process
deeptutor serve --host 127.0.0.1 --port 18001

# Development: hot reload on Python file changes
deeptutor serve --reload
```

## Authentication

If auth is enabled in `data/user/settings/auth.json`, every endpoint except `/api/v1/auth/*` requires a valid JWT in the `Authorization: Bearer <token>` header or a session cookie.

```bash
# Login
curl -X POST http://localhost:8001/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username":"alice","password":"..."}'

# Response includes an access_token.

# Use the token
curl http://localhost:8001/api/v1/sessions \
  -H "Authorization: Bearer eyJ..."
```

If auth is disabled, auth dependencies are no-ops and local single-user requests do not need a token.

## Turn execution WebSocket

```text
WS /api/v1/ws
```

This is the unified turn WebSocket used by the Web UI. It supports every capability uniformly and streams the same event family that `deeptutor run --format json` prints.

Start a turn by sending a `type: "start_turn"` or `type: "message"` payload:

```json
{
  "type": "start_turn",
  "content": "Find d/dx [sin(x^2)]",
  "capability": "deep_solve",
  "session_id": null,
  "tools": ["rag", "reason"],
  "knowledge_bases": ["math"],
  "language": "en",
  "config": {"max_steps": 6},
  "notebook_references": [],
  "history_references": [],
  "attachments": [],
  "skills": []
}
```

Other supported client message types include `subscribe_turn`, `subscribe_session`, `resume_from`, `unsubscribe`, `cancel_turn`, `submit_user_reply`, `regenerate`, and `ping`.

Typical received events:

```json
{"type":"stage_start","stage":"retrieving"}
{"type":"tool_call","content":"rag_search","metadata":{"args":{"query":"chain rule"}}}
{"type":"tool_result","content":"...","metadata":{"tool":"rag"}}
{"type":"stage_end","stage":"retrieving"}
{"type":"content","content":"## Solution\n\nThe derivative..."}
{"type":"done","metadata":{"session_id":"sess_abc123","turn_id":"turn_xyz789"}}
```

## Legacy chat WebSocket

```text
WS /api/v1/chat
```

This legacy endpoint is still present for simple chat clients. Prefer `/api/v1/ws` for new integrations because it supports all capabilities, replay, cancellation, regeneration, and `ask_user` replies.

## Sessions

```text
GET    /api/v1/sessions                              List sessions
GET    /api/v1/sessions/{session_id}                 Get a session + messages
PATCH  /api/v1/sessions/{session_id}                 Rename (body: {"title":"..."})
DELETE /api/v1/sessions/{session_id}                 Delete
PUT    /api/v1/sessions/{session_id}/branch-selection
DELETE /api/v1/sessions/{session_id}/messages/{message_id}
POST   /api/v1/sessions/{session_id}/quiz-results
```

Legacy chat-session aliases also exist:

```text
GET    /api/v1/chat/sessions
GET    /api/v1/chat/sessions/{session_id}
DELETE /api/v1/chat/sessions/{session_id}
```

## Knowledge Bases

```text
GET    /api/v1/knowledge/list                         List KBs
GET    /api/v1/knowledge/{kb_name}                    KB info
DELETE /api/v1/knowledge/{kb_name}                    Delete
POST   /api/v1/knowledge/create                       Create a KB
POST   /api/v1/knowledge/{kb_name}/upload             Add documents
POST   /api/v1/knowledge/{kb_name}/reindex            Re-embed docs
GET    /api/v1/knowledge/default                      Get default KB
PUT    /api/v1/knowledge/default/{kb_name}            Set default KB
GET    /api/v1/knowledge/supported-file-types         Supported uploads
GET    /api/v1/knowledge/{kb_name}/files              List source files
GET    /api/v1/knowledge/{kb_name}/progress           Indexing progress
WS     /api/v1/knowledge/{kb_name}/progress/ws        Progress stream
```

Ad-hoc KB search is exposed through the RAG runtime/tool path rather than a dedicated `POST /knowledge/{name}/search` route in the current API. From CLI, use `deeptutor kb search <name> <query>`.

## Notebook

```text
GET    /api/v1/notebook/list
GET    /api/v1/notebook/statistics
POST   /api/v1/notebook/create
GET    /api/v1/notebook/{notebook_id}
PUT    /api/v1/notebook/{notebook_id}
DELETE /api/v1/notebook/{notebook_id}
POST   /api/v1/notebook/add_record
POST   /api/v1/notebook/add_record_with_summary
DELETE /api/v1/notebook/{notebook_id}/records/{record_id}
PUT    /api/v1/notebook/{notebook_id}/records/{record_id}
```

## Memory

```text
GET    /api/v1/memory/overview
GET    /api/v1/memory/doc/{layer}/{key}
PUT    /api/v1/memory/doc/{layer}/{key}
POST   /api/v1/memory/doc/{layer}/{key}/reset
POST   /api/v1/memory/doc/{layer}/{key}/update
POST   /api/v1/memory/doc/{layer}/{key}/audit
POST   /api/v1/memory/doc/{layer}/{key}/dedup
POST   /api/v1/memory/runs/start
GET    /api/v1/memory/runs
GET    /api/v1/memory/runs/{run_id}
GET    /api/v1/memory/runs/{run_id}/events
POST   /api/v1/memory/runs/{run_id}/cancel
POST   /api/v1/memory/runs/{run_id}/undo
GET    /api/v1/memory/trace/{surface}
DELETE /api/v1/memory/trace/{surface}
GET    /api/v1/memory/settings
PUT    /api/v1/memory/settings
```

Layers are `L2` and `L3`; examples: `/api/v1/memory/doc/L3/profile` and `/api/v1/memory/doc/L2/chat`.

## Settings, tools, plugins, and system

```text
GET  /api/v1/settings
GET  /api/v1/settings/catalog
PUT  /api/v1/settings/catalog
POST /api/v1/settings/apply
PUT  /api/v1/settings/enabled-tools
GET  /api/v1/tools
GET  /api/v1/plugins/list
POST /api/v1/plugins/tools/{tool_name}/execute
POST /api/v1/plugins/tools/{tool_name}/execute-stream
POST /api/v1/plugins/capabilities/{capability_name}/execute-stream
GET  /api/v1/system/status
GET  /api/v1/system/runtime-topology
POST /api/v1/system/test/llm
POST /api/v1/system/test/embeddings
POST /api/v1/system/test/search
```

Provider profiles are edited through the catalog endpoints; there are not separate `/settings/llm` or `/settings/embedding` routes in the current API.

## TutorBot Manager

```text
GET    /api/v1/tutorbot
POST   /api/v1/tutorbot
GET    /api/v1/tutorbot/recent
GET    /api/v1/tutorbot/channels/schema
GET    /api/v1/tutorbot/{bot_id}
PATCH  /api/v1/tutorbot/{bot_id}
DELETE /api/v1/tutorbot/{bot_id}
DELETE /api/v1/tutorbot/{bot_id}/destroy
GET    /api/v1/tutorbot/{bot_id}/files
PUT    /api/v1/tutorbot/{bot_id}/files/{filename}
GET    /api/v1/tutorbot/{bot_id}/history
WS     /api/v1/tutorbot/{bot_id}/ws
```

## Book Engine

```text
GET    /api/v1/book/books
POST   /api/v1/book/books
GET    /api/v1/book/books/{book_id}
GET    /api/v1/book/books/{book_id}/spine
GET    /api/v1/book/books/{book_id}/pages/{page_id}
DELETE /api/v1/book/books/{book_id}
POST   /api/v1/book/books/confirm-proposal
POST   /api/v1/book/books/confirm-spine
POST   /api/v1/book/books/compile-page
POST   /api/v1/book/books/{book_id}/refresh-fingerprints
WS     /api/v1/book/ws
```

## Outputs and attachments

User-generated artifacts are served from a read-only static mount:

```text
GET /api/outputs/<path>
```

Only paths whitelisted via `SafeOutputStaticFiles` are accessible; directory traversal is blocked. Original chat attachments are served under:

```text
GET /api/attachments/{session_id}/{attachment_id}/{filename}
```

## Generate a typed client

```bash
curl http://localhost:8001/openapi.json > deeptutor.openapi.json

# TypeScript client
npx openapi-typescript deeptutor.openapi.json -o deeptutor.d.ts

# Python client
pip install openapi-python-client
openapi-python-client generate --path deeptutor.openapi.json
```
