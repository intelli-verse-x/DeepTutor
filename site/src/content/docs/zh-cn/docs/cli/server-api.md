---
title: 服务端 API
description: deeptutor serve 暴露的 HTTP 和 WebSocket 表面 —— 用于自定义前端和集成。
---

`deeptutor serve` 在 `http://localhost:8001/` 上启动 FastAPI 后端（除非你改了后端端口）。本页是给自定义前端、移动 App 和服务间集成准备的高密度地图。

要看穷尽且永远最新的 schema，启动服务后打开：

```text
GET /openapi.json     # 完整 OpenAPI 3.1 spec
GET /docs             # 交互式 Swagger UI
GET /redoc            # 备选的 ReDoc UI
```

## 启动服务

```bash
# 仅后端。端口取自 data/user/settings/system.json，默认 8001。
deeptutor serve

# 给本次进程指定自定义 host/port
deeptutor serve --host 127.0.0.1 --port 18001

# 开发模式：Python 文件变动时热重载
deeptutor serve --reload
```

## 鉴权

如果 `data/user/settings/auth.json` 里开启了鉴权，除 `/api/v1/auth/*` 之外的每个 endpoint 都要求 `Authorization: Bearer <token>` header 携带有效 JWT，或者带 session cookie。

```bash
# 登录
curl -X POST http://localhost:8001/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username":"alice","password":"..."}'

# 响应里包含 access_token。

# 用 token 调用
curl http://localhost:8001/api/v1/sessions \
  -H "Authorization: Bearer eyJ..."
```

如果鉴权没开，认证依赖就是 no-op，本地单用户请求不需要带 token。

## Turn 执行 WebSocket

```text
WS /api/v1/ws
```

这是 Web UI 在用的统一 turn WebSocket。它对所有 capability 一视同仁，输出的事件和 `deeptutor run --format json` 打印的是同一族。

发一个 `type: "start_turn"` 或 `type: "message"` 载荷启动 turn：

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

其他支持的 client 消息类型包括 `subscribe_turn`、`subscribe_session`、`resume_from`、`unsubscribe`、`cancel_turn`、`submit_user_reply`、`regenerate`、`ping`。

典型收到的事件：

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

这个旧 endpoint 还留着，给简单 chat 客户端用。新集成建议直接走 `/api/v1/ws`，因为它支持所有 capability、replay、cancel、regenerate 和 `ask_user` 回复。

## Session

```text
GET    /api/v1/sessions                              列 session
GET    /api/v1/sessions/{session_id}                 拿到一个 session + 消息
PATCH  /api/v1/sessions/{session_id}                 重命名（body: {"title":"..."}）
DELETE /api/v1/sessions/{session_id}                 删除
PUT    /api/v1/sessions/{session_id}/branch-selection
DELETE /api/v1/sessions/{session_id}/messages/{message_id}
POST   /api/v1/sessions/{session_id}/quiz-results
```

旧版 chat-session 别名也仍然存在：

```text
GET    /api/v1/chat/sessions
GET    /api/v1/chat/sessions/{session_id}
DELETE /api/v1/chat/sessions/{session_id}
```

## 知识库

```text
GET    /api/v1/knowledge/list                         列 KB
GET    /api/v1/knowledge/{kb_name}                    KB 信息
DELETE /api/v1/knowledge/{kb_name}                    删除
POST   /api/v1/knowledge/create                       创建 KB
POST   /api/v1/knowledge/{kb_name}/upload             添加文档
POST   /api/v1/knowledge/{kb_name}/reindex            重新 embed 文档
GET    /api/v1/knowledge/default                      获取默认 KB
PUT    /api/v1/knowledge/default/{kb_name}            设置默认 KB
GET    /api/v1/knowledge/supported-file-types         支持的上传格式
GET    /api/v1/knowledge/{kb_name}/files              列源文件
GET    /api/v1/knowledge/{kb_name}/progress           索引进度
WS     /api/v1/knowledge/{kb_name}/progress/ws        进度流
```

临时的 KB 搜索目前是通过 RAG 运行时 / tool 路径暴露的，当前 API 里没有专门的 `POST /knowledge/{name}/search` 路由。从 CLI 走，用 `deeptutor kb search <name> <query>`。

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

层级是 `L2` 和 `L3`；例：`/api/v1/memory/doc/L3/profile` 和 `/api/v1/memory/doc/L2/chat`。

## Settings、tools、plugins 和 system

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

Provider profile 通过 catalog endpoint 编辑；当前 API 里没有单独的 `/settings/llm` 或 `/settings/embedding` 路由。

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

## 输出和附件

用户生成的产物通过一个只读静态挂载提供：

```text
GET /api/outputs/<path>
```

只有通过 `SafeOutputStaticFiles` 白名单的路径才能访问；目录穿越被拦掉了。原始 chat 附件挂在：

```text
GET /api/attachments/{session_id}/{attachment_id}/{filename}
```

## 生成 typed client

```bash
curl http://localhost:8001/openapi.json > deeptutor.openapi.json

# TypeScript client
npx openapi-typescript deeptutor.openapi.json -o deeptutor.d.ts

# Python client
pip install openapi-python-client
openapi-python-client generate --path deeptutor.openapi.json
```
