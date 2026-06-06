"""Pre-merge boot smoke test for PR #14.

Boots the FastAPI app via TestClient (runs the real lifespan: PG/LLM/EventBus/
memory migration — all degrade gracefully without DB/LLM) and exercises core
endpoints, with focus on the QuizVerse /memory compat contract.

Run: ./venv/bin/python smoke_test.py
"""
import os
import sys

os.environ.setdefault("AUTH_ENABLED", "false")

from fastapi.testclient import TestClient  # noqa: E402

from deeptutor.api.main import app  # noqa: E402

H = {"x-user-id": "smoke_user_123"}
PASS, FAIL = "PASS", "FAIL"
rows = []


def check(name, ok, detail=""):
    rows.append((PASS if ok else FAIL, name, detail))


with TestClient(app, raise_server_exceptions=False) as c:
    # 1. OpenAPI / routing
    r = c.get("/openapi.json")
    paths = list(r.json().get("paths", {})) if r.status_code == 200 else []
    check("GET /openapi.json", r.status_code == 200, f"{r.status_code}, {len(paths)} paths")

    # 2. Health endpoints (discover from openapi)
    for hp in [p for p in paths if p.endswith("/health")][:4]:
        r = c.get(hp)
        check(f"GET {hp}", r.status_code == 200, str(r.status_code))

    # 3. QuizVerse /memory compat — snapshot
    r = c.get("/api/v1/memory", headers=H)
    body = r.json() if r.headers.get("content-type", "").startswith("application/json") else {}
    has_shape = isinstance(body, dict) and "summary" in body and "profile" in body
    check("GET /api/v1/memory (compat snapshot)", r.status_code == 200 and has_shape,
          f"{r.status_code}, keys={sorted(body)[:6]}")

    # 4. QuizVerse /memory compat — refresh (L1->L2->L3 'recent' consolidation; session_id advisory)
    r = c.post("/api/v1/memory/refresh", headers=H, json={"session_id": "sess_advisory", "language": "en"})
    body = r.json() if r.headers.get("content-type", "").startswith("application/json") else {}
    ok = r.status_code == 200 and isinstance(body, dict) and "changed" in body and "summary" in body
    check("POST /api/v1/memory/refresh (compat)", ok,
          f"{r.status_code}, changed={body.get('changed')}, keys={sorted(body)[:6]}")

    # 5. QuizVerse /memory compat — update + clear round trip
    r = c.put("/api/v1/memory", headers=H, json={"file": "summary", "content": "smoke note"})
    check("PUT /api/v1/memory (compat update)", r.status_code == 200, str(r.status_code))
    r = c.post("/api/v1/memory/clear", headers=H, json={"file": "summary"})
    check("POST /api/v1/memory/clear (compat)", r.status_code == 200, str(r.status_code))

    # 6. Upstream v3 memory workbench still mounted (no route collision with compat)
    wb = [p for p in paths if p.startswith("/api/v1/memory") and p not in
          ("/api/v1/memory", "/api/v1/memory/refresh", "/api/v1/memory/clear")]
    check("v3 memory workbench routes present", len(wb) > 0, f"{len(wb)} extra memory routes")

    # 7. A representative fork router is mounted
    check("fork exams router mounted", any(p.startswith("/api/v1/exams") for p in paths),
          f"exams paths={sum(p.startswith('/api/v1/exams') for p in paths)}")

print("\n=== SMOKE TEST RESULTS ===")
fails = 0
for status, name, detail in rows:
    if status == FAIL:
        fails += 1
    print(f"[{status}] {name}  ({detail})")
print(f"\n{len(rows)-fails}/{len(rows)} passed; {fails} failed")
sys.exit(1 if fails else 0)
