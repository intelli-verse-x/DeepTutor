---
type: ["api", "ux"]
skills: []
negative_tests: 2
---

# Block 22: Display module name instead of raw book_id on /learning cards

## Problem

`GET /api/v1/learning/progress` returns `ProgressSummary` without a human-readable name field. The `/learning` page card heading shows `card.book_id` directly, resulting in auto-generated IDs like `unified_1778812096729_f4d265d6` displayed to users. Only manually-named books (e.g., "default", "init3") look readable.

## Root cause

`list_progress()` in `deeptutor/learning/service.py:139-146` builds a summary dict with 6 fields but no `name`. The `LearningProgress.modules[]` each have a `.name`, but the summary never surfaces it. The frontend `ProgressSummary` interface mirrors the backend exactly — no name field.

## Files to modify (3)

| File | Change |
|------|--------|
| `deeptutor/learning/service.py:139-146` | Add `"name"` to summaries dict |
| `web/lib/learning-api.ts:45-52` | Add `name: string` to `ProgressSummary` |
| `web/app/(workspace)/learning/page.tsx:132` | Change `{card.book_id}` to `{card.name \|\| card.book_id}` |

## Implementation details

### 1. Backend (`service.py`)

In `list_progress()`, derive display name from modules:
```python
display_name = ""
if progress.modules:
    display_name = progress.modules[0].name
summaries.append({
    ...
    "name": display_name or progress.book_id,  # fallback to book_id
    ...
})
```

### 2. Frontend type (`learning-api.ts`)

Add to `ProgressSummary`:
```typescript
name: string;
```

### 3. Frontend card (`page.tsx:132`)

Change line 132 from:
```tsx
{card.book_id}
```
to:
```tsx
{card.name || card.book_id}
```

## Acceptance criteria

1. `list_progress()` returns `"name"` field for all books
2. Empty-module books show `name` = book_id (fallback)
3. Non-empty books show `name` = first module name
4. Frontend card heading uses `card.name` when available
5. All existing tests pass (no breakage)
6. Book IDs in URLs (router.push, delete/redo params, card keys) remain unchanged

## Negative tests (2 required)

1. Book with 0 modules — verify `name` falls back to `book_id`, card shows book_id text
2. Book with modules but empty name in first module — verify no crash, graceful fallback

## Verification

```bash
# Backend test
python -m pytest deeptutor/learning/tests/ -v

# Frontend: visit /learning, verify module cards show readable names
```
