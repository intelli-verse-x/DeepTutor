#!/usr/bin/env bash
# ── End-to-End Test: External Notes Proxy ──────────────────────────
#
# Usage:
#   ./tools/test_external_notes_e2e.sh <USER_UUID>
#   ./tools/test_external_notes_e2e.sh <USER_UUID> <BASE_URL>
#
# Example (prod):
#   ./tools/test_external_notes_e2e.sh 550e8400-e29b-41d4-a716-446655440000
#
# Example (local):
#   ./tools/test_external_notes_e2e.sh 550e8400-e29b-41d4-a716-446655440000 http://localhost:8001
#
# The user_id must be a UUID v4 from the Intelliverse-X-AI users table.
# To find one, query:  SELECT id FROM users WHERE ... LIMIT 5;

set -euo pipefail

USER_ID="${1:?Usage: $0 <USER_UUID> [BASE_URL]}"
BASE="${2:-https://tutor.intelli-verse-x.ai}"

GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

pass() { echo -e "${GREEN}✅ PASS${NC}: $1"; }
fail() { echo -e "${RED}❌ FAIL${NC}: $1"; }
warn() { echo -e "${YELLOW}⚠️  WARN${NC}: $1"; }
info() { echo -e "   ℹ️  $1"; }

echo "═══════════════════════════════════════════════════════════"
echo " External Notes E2E Test"
echo " Base URL: $BASE"
echo " User ID:  $USER_ID"
echo "═══════════════════════════════════════════════════════════"
echo ""

TOTAL=0
PASSED=0
FAILED=0

# ── Test 1: Health check ───────────────────────────────────────────
TOTAL=$((TOTAL + 1))
echo "── Test 1: DeepTutor is reachable ──"
HTTP=$(curl -s -o /dev/null -w "%{http_code}" "$BASE/")
if [[ "$HTTP" == "200" ]]; then
  pass "DeepTutor root returns 200"
  PASSED=$((PASSED + 1))
else
  fail "DeepTutor root returned $HTTP (expected 200)"
  FAILED=$((FAILED + 1))
  echo "Aborting — server not reachable."
  exit 1
fi
echo ""

# ── Test 2: Proxy endpoint exists ──────────────────────────────────
TOTAL=$((TOTAL + 1))
echo "── Test 2: /api/v1/external/notes endpoint exists ──"
RESP=$(curl -s -o /tmp/_e2e_body.json -w "%{http_code}" "$BASE/api/v1/external/notes" \
  -H "x-user-id: $USER_ID")
HTTP="$RESP"
BODY=$(cat /tmp/_e2e_body.json 2>/dev/null || echo "{}")

if [[ "$HTTP" == "200" ]]; then
  pass "Endpoint returns 200"
  PASSED=$((PASSED + 1))
elif [[ "$HTTP" == "404" ]]; then
  fail "Endpoint returns 404 — proxy not deployed yet"
  FAILED=$((FAILED + 1))
  info "Deploy latest DeepTutor code first."
  echo ""
  echo "═══ Results: $PASSED/$TOTAL passed, $FAILED failed ═══"
  exit 1
else
  warn "Endpoint returned $HTTP"
  FAILED=$((FAILED + 1))
fi
echo ""

# ── Test 3: Response shape ─────────────────────────────────────────
TOTAL=$((TOTAL + 1))
echo "── Test 3: Response has correct shape ──"
info "Response body: $(echo "$BODY" | head -c 300)..."

HAS_NOTES=$(echo "$BODY" | python3 -c "import sys,json; d=json.load(sys.stdin); print('yes' if 'notes' in d else 'no')" 2>/dev/null || echo "parse_error")
HAS_SOURCE=$(echo "$BODY" | python3 -c "import sys,json; d=json.load(sys.stdin); print('yes' if d.get('source')=='intelliverse-x' else 'no')" 2>/dev/null || echo "parse_error")

if [[ "$HAS_NOTES" == "yes" && "$HAS_SOURCE" == "yes" ]]; then
  pass "Response contains 'notes' array and 'source: intelliverse-x'"
  PASSED=$((PASSED + 1))
elif [[ "$HAS_NOTES" == "yes" ]]; then
  warn "Has 'notes' but missing source tag"
  PASSED=$((PASSED + 1))
else
  fail "Response shape invalid — missing 'notes' key"
  FAILED=$((FAILED + 1))
fi
echo ""

# ── Test 4: Notes content ──────────────────────────────────────────
TOTAL=$((TOTAL + 1))
echo "── Test 4: User has notes ──"
NOTE_COUNT=$(echo "$BODY" | python3 -c "import sys,json; d=json.load(sys.stdin); print(len(d.get('notes',[])))" 2>/dev/null || echo "0")
TOTAL_COUNT=$(echo "$BODY" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('total',0))" 2>/dev/null || echo "0")
HAS_ERROR=$(echo "$BODY" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('error',''))" 2>/dev/null || echo "")

if [[ -n "$HAS_ERROR" && "$HAS_ERROR" != "" && "$HAS_ERROR" != "None" ]]; then
  warn "Proxy returned error: $HAS_ERROR"
  info "This may mean Cognito S2S auth is not configured yet."
  FAILED=$((FAILED + 1))
elif [[ "$NOTE_COUNT" -gt 0 ]]; then
  pass "Found $NOTE_COUNT notes (total: $TOTAL_COUNT) for user $USER_ID"
  PASSED=$((PASSED + 1))
  
  FIRST_TITLE=$(echo "$BODY" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d['notes'][0].get('title','?')[:60])" 2>/dev/null || echo "?")
  FIRST_TYPE=$(echo "$BODY" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d['notes'][0].get('noteType','?'))" 2>/dev/null || echo "?")
  FIRST_ID=$(echo "$BODY" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d['notes'][0].get('id','?'))" 2>/dev/null || echo "?")
  info "First note: \"$FIRST_TITLE\" (type=$FIRST_TYPE, id=$FIRST_ID)"
else
  warn "No notes found for user $USER_ID (total=$TOTAL_COUNT)"
  info "This user may not have created any notes in the Unity app."
  PASSED=$((PASSED + 1))
fi
echo ""

# ── Test 5: Note detail (if notes exist) ───────────────────────────
if [[ "$NOTE_COUNT" -gt 0 && "$FIRST_ID" != "?" ]]; then
  TOTAL=$((TOTAL + 1))
  echo "── Test 5: Note detail endpoint ──"
  DETAIL_RESP=$(curl -s -o /tmp/_e2e_detail.json -w "%{http_code}" "$BASE/api/v1/external/notes/$FIRST_ID" \
    -H "x-user-id: $USER_ID")
  DETAIL_HTTP="$DETAIL_RESP"
  DETAIL_BODY=$(cat /tmp/_e2e_detail.json 2>/dev/null || echo "{}")
  
  if [[ "$DETAIL_HTTP" == "200" ]]; then
    HAS_CONTENT=$(echo "$DETAIL_BODY" | python3 -c "
import sys,json
d=json.load(sys.stdin)
note=d.get('note',d)
has=bool(note.get('content') or note.get('studyNote') or note.get('summary'))
print('yes' if has else 'no')
" 2>/dev/null || echo "parse_error")
    
    if [[ "$HAS_CONTENT" == "yes" ]]; then
      pass "Note detail has text content (importable to KB)"
    else
      warn "Note detail returned but no text content found (may be media-only)"
    fi
    PASSED=$((PASSED + 1))
  else
    fail "Note detail returned $DETAIL_HTTP"
    FAILED=$((FAILED + 1))
  fi
  echo ""
fi

# ── Test 6: Folders endpoint ───────────────────────────────────────
TOTAL=$((TOTAL + 1))
echo "── Test 6: Folders endpoint ──"
FOLDER_RESP=$(curl -s -o /tmp/_e2e_folders.json -w "%{http_code}" "$BASE/api/v1/external/folders" \
  -H "x-user-id: $USER_ID")
FOLDER_HTTP="$FOLDER_RESP"
FOLDER_BODY=$(cat /tmp/_e2e_folders.json 2>/dev/null || echo "{}")

if [[ "$FOLDER_HTTP" == "200" ]]; then
  FOLDER_COUNT=$(echo "$FOLDER_BODY" | python3 -c "import sys,json; d=json.load(sys.stdin); print(len(d.get('folders',[])))" 2>/dev/null || echo "0")
  pass "Folders endpoint works ($FOLDER_COUNT folders)"
  PASSED=$((PASSED + 1))
else
  fail "Folders endpoint returned $FOLDER_HTTP"
  FAILED=$((FAILED + 1))
fi
echo ""

# ── Test 7: KB list (for import flow) ─────────────────────────────
TOTAL=$((TOTAL + 1))
echo "── Test 7: KB list for import target ──"
KB_RESP=$(curl -s -o /tmp/_e2e_kb.json -w "%{http_code}" "$BASE/api/v1/knowledge/list" \
  -H "x-user-id: $USER_ID")
KB_HTTP="$KB_RESP"
KB_BODY=$(cat /tmp/_e2e_kb.json 2>/dev/null || echo "[]")

if [[ "$KB_HTTP" == "200" ]]; then
  KB_COUNT=$(echo "$KB_BODY" | python3 -c "import sys,json; d=json.load(sys.stdin); print(len(d) if isinstance(d,list) else 0)" 2>/dev/null || echo "0")
  if [[ "$KB_COUNT" -gt 0 ]]; then
    KB_NAME=$(echo "$KB_BODY" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d[0].get('name','?'))" 2>/dev/null || echo "?")
    pass "Found $KB_COUNT knowledge bases (first: '$KB_NAME')"
    info "Import-to-KB flow can be tested with: POST /api/v1/external/notes/import-to-kb"
  else
    warn "No KBs found — import-to-KB cannot be tested without creating one first"
  fi
  PASSED=$((PASSED + 1))
else
  fail "KB list returned $KB_HTTP"
  FAILED=$((FAILED + 1))
fi
echo ""

# ── Summary ────────────────────────────────────────────────────────
echo "═══════════════════════════════════════════════════════════"
if [[ $FAILED -eq 0 ]]; then
  echo -e " ${GREEN}All $TOTAL tests passed!${NC}"
else
  echo -e " ${RED}$FAILED/$TOTAL tests failed${NC}, $PASSED passed"
fi
echo "═══════════════════════════════════════════════════════════"
echo ""
echo "Deployment checklist:"
echo "  1. Set COGNITO_OAUTH2_URL, COGNITO_S2S_CLIENT_ID, COGNITO_S2S_CLIENT_SECRET"
echo "     in deeptutor-secrets (for Cognito client_credentials S2S auth)"
echo "  2. Optionally set INTELLIVERSE_API_URL for internal k8s URL"
echo "     (e.g. http://intelliverse-x-ai-svc.aicart.svc.cluster.local:5001)"
echo "  3. Deploy latest DeepTutor image"
echo "  4. Re-run: $0 $USER_ID"

exit $FAILED
