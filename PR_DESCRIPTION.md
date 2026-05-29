# feat: Guided Learning — structured mastery-based tutoring system

## Summary

This PR introduces **Guided Learning**, a structured, mastery-based tutoring subsystem that transforms DeepTutor from a free-form chat tool into a pedagogical learning system with persistent progress tracking, spaced repetition, and adaptive stage progression.

**Upstream status**: This is a complete new subsystem. `upstream/dev` has no `deeptutor/learning/`, no `guided_learning.py` capability, and no learning-related frontend pages or components.

**Scope**: 71 files changed, +7,284 / -99 lines across 114 commits. All changes are additive except for minor hook points in existing chat/stream infrastructure. The branch was merged with `upstream/dev` (a merge commit at the tip) so it applies cleanly on top of the current dev base.

---

## What's included

### Backend

| Component | Files | Description |
|-----------|-------|-------------|
| **Models** | `deeptutor/learning/models.py` | 4 enums + 9 Pydantic models: `LearningProgress`, `LearningModule`, `KnowledgePoint`, `QuizAttempt`, `ErrorRecord`, etc. |
| **Storage** | `deeptutor/learning/storage.py` | JSON persistence with CAS (compare-and-swap) semantics and path-traversal guards |
| **Service** | `deeptutor/learning/service.py` | Business logic: module lifecycle, mastery calculation (weighted recent accuracy), quiz attempt recording, error tracking |
| **Scheduler** | `deeptutor/learning/scheduler.py` | Spaced repetition scheduler with per-knowledge-type initial states |
| **Grading** | `deeptutor/learning/grading.py` | Server-side answer evaluation with normalization and stripping |
| **Capability** | `deeptutor/capabilities/guided_learning.py` | 12-stage state machine: diagnostic → plan → pretest → explain → Feynman check → practice → error diagnosis → module test → review → completed |
| **API Router** | `deeptutor/api/routers/guided_learning.py` | 10 REST endpoints: progress CRUD, module generation, notebook import, `/redo`, `/answer`, etc. |
| **Tests** | `deeptutor/learning/tests/` (13 files) | 164 tests covering models, storage, scheduler, service, API endpoints, LLM integration, timeout degradation, error diagnosis, E2E flow |

### Frontend

| Component | Files | Description |
|-----------|-------|-------------|
| **Learning Pages** | `web/app/(workspace)/learning/` | Module list, book-based learning session, WebSocket-driven stage streaming |
| **Learning Components** | `web/components/learning/` | `ModuleTree` (sidebar + mastery indicator), `CreateModuleDialog` (4-tab module creation), `StructuredStageContent` (JSON content rendering) |
| **API Client** | `web/lib/learning-api.ts` | Typed API client for all learning endpoints |
| **i18n** | `web/locales/en/app.json`, `zh/app.json` | Full English + Chinese localization |

### Infrastructure hooks

- `deeptutor/core/stream_bus.py`: added `wait_for_input()` for interactive stage turns
- `deeptutor/api/routers/unified_ws.py`: wired Guided Learning into WebSocket routing
- `deeptutor/api/main.py`: registered learning router
- `deeptutor/runtime/bootstrap/builtin_capabilities.py`: registered `guided_learning` capability

---

## Key design decisions

1. **Fail-closed + degradation**: Every LLM call has bounded retry + timeout. If a stage fails repeatedly, it degrades gracefully (skips with user-visible notice) rather than blocking the learner.
2. **Cross-turn persistence**: `LearningProgress` is saved after every interactive step, so reconnects, cancellations, and backend restarts never lose student attempts.
3. **Server-side grading**: All answer evaluation happens server-side with stripped comparisons, preventing client-side manipulation.
4. **Prompt injection hardening**: Notebook-to-module generation uses XML tag boundaries (`<notebook_records>`), system-prompt constraints, input escaping (`html.escape` on user fields), and output validation (type whitelist + length truncation).

---

## Testing

```bash
pytest deeptutor/learning/tests/ -q
# 164 passed
```

Test categories:
- Unit: models, storage, scheduler, grading
- Integration: service replace/merge, mastery updates, timeout degradation
- API: all 10 endpoints with success + error paths
- E2E: complete `PRETEST → EXPLAIN → FEYNMAN_CHECK → PRACTICE_QUIZ → ERROR_DIAGNOSIS → MODULE_TEST → REVIEW → COMPLETED` flow

Frontend type check:

```bash
cd web && npx tsc --noEmit
# clean
```

---

## Checklist

- [x] 164 backend tests pass
- [x] Frontend `tsc --noEmit` clean
- [x] No breaking changes to existing chat / solve / research capabilities
- [x] i18n parity verified (`npm run i18n:parity`)
- [x] No secrets or local configs committed
- [x] All user-facing strings localized
- [x] Branch merged with `upstream/dev` at HEAD (clean three-way merge)

---

## Related

Closes the gap identified in community discussions around structured learning workflows (see Discord #feature-requests, Feishu group).
