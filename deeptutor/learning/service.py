from __future__ import annotations

import time
import uuid

from deeptutor.learning.models import (
    ErrorRecord,
    LearningModule,
    LearningProgress,
    LearningStage,
    QuizAttempt,
    RetryAttempt,
)
from deeptutor.learning.storage import LearningStore


class LearningService:
    def __init__(self, store: LearningStore | None = None) -> None:
        self._store = store or LearningStore()

    def get_or_create(self, book_id: str) -> LearningProgress:
        existing = self._store.load(book_id)
        if existing is not None:
            return existing
        progress = LearningProgress(book_id=book_id)
        self._store.save(progress)  # persist immediately to prevent race
        return progress

    def merge_modules(
        self, progress: LearningProgress, modules: list[LearningModule]
    ) -> None:
        """Incremental merge: keep existing modules, add/update by id."""
        existing_by_id = {m.id: m for m in progress.modules}
        for mod in modules:
            existing_by_id[mod.id] = mod  # add new or replace with updated
            for kp in mod.knowledge_points:
                progress.knowledge_types[kp.id] = kp.type
        progress.modules = list(existing_by_id.values())

    # Backward compat alias
    init_modules = merge_modules

    def replace_modules(
        self, progress: LearningProgress, modules: list[LearningModule]
    ) -> None:
        """Replace all modules and clean stale KP state."""
        new_kp_ids = {kp.id for m in modules for kp in m.knowledge_points}

        # Clean stale KP state
        for key in list(progress.mastery_levels.keys()):
            if key not in new_kp_ids:
                del progress.mastery_levels[key]
        for key in list(progress.knowledge_types.keys()):
            if key not in new_kp_ids:
                del progress.knowledge_types[key]
        for key in list(progress.repetition_states.keys()):
            if key not in new_kp_ids:
                del progress.repetition_states[key]
        progress.error_records = [
            r for r in progress.error_records
            if r.knowledge_point_id in new_kp_ids
        ]
        progress.feynman_retries = {
            k: v for k, v in progress.feynman_retries.items()
            if k in new_kp_ids
        }
        progress.review_queue = [
            t for t in progress.review_queue
            if t.knowledge_point_id in new_kp_ids
        ]

        # Set new modules
        progress.modules = list(modules)
        for mod in modules:
            for kp in mod.knowledge_points:
                progress.knowledge_types[kp.id] = kp.type

    def advance_stage(
        self, progress: LearningProgress, next_stage: LearningStage
    ) -> None:
        progress.current_stage = next_stage
        progress.updated_at = time.time()

    def record_quiz_attempt(
        self, progress: LearningProgress, attempt: QuizAttempt
    ) -> None:
        if not attempt.is_correct and attempt.error_type is not None:
            # Find existing error record for this question + knowledge point.
            existing = None
            for rec in progress.error_records:
                if rec.question_id == attempt.question_id and rec.knowledge_point_id == attempt.knowledge_point_id:
                    existing = rec
                    break

            if existing is not None:
                existing.retry_history.append(
                    RetryAttempt(
                        timestamp=time.time(),
                        is_correct=False,
                        attempt_number=len(existing.retry_history) + 1,
                    )
                )
                existing.status = "retrying"
            else:
                record = ErrorRecord(
                    id=uuid.uuid4().hex,
                    question_id=attempt.question_id,
                    knowledge_point_id=attempt.knowledge_point_id,
                    module_id=attempt.module_id,
                    error_type=attempt.error_type,
                    self_attribution=attempt.self_attribution,
                    status="active",
                )
                progress.error_records.append(record)

        elif attempt.is_correct:
            # Graduate any active error record for this question + knowledge point.
            for rec in progress.error_records:
                if (
                    rec.question_id == attempt.question_id
                    and rec.knowledge_point_id == attempt.knowledge_point_id
                    and rec.status in ("active", "retrying")
                ):
                    rec.retry_history.append(
                        RetryAttempt(
                            timestamp=time.time(),
                            is_correct=True,
                            attempt_number=len(rec.retry_history) + 1,
                        )
                    )
                    rec.status = "graduated"
                    break

        progress.quiz_attempts.append(attempt)
        progress.updated_at = time.time()

    def calculate_mastery(self, progress: LearningProgress, kp_id: str) -> float:
        """Weighted recent accuracy for *kp_id* (last 5 attempts)."""
        attempts = [a for a in progress.quiz_attempts if a.knowledge_point_id == kp_id]
        if not attempts:
            return 0.0
        recent = attempts[-5:]
        weights = [0.5, 0.7, 0.85, 0.95, 1.0]
        w = weights[-len(recent):]
        score = sum((1.0 if a.is_correct else 0.0) * weight for a, weight in zip(recent, w))
        return score / sum(w)

    def update_mastery(
        self, progress: LearningProgress, kp_id: str, level: float
    ) -> None:
        progress.mastery_levels[kp_id] = level
        progress.updated_at = time.time()

    def list_progress(self) -> dict:
        """Return summary of all book progress with per-book error info."""
        import logging
        logger = logging.getLogger(__name__)

        book_ids = self._store.list_all()
        summaries = []
        errors = []
        for bid in book_ids:
            try:
                progress = self._store.load(bid)
                if progress is None:
                    continue
                # Only count KPs from current modules (exclude stale IDs)
                current_kp_ids = {
                    kp.id
                    for m in progress.modules
                    for kp in m.knowledge_points
                }
                total_kps = len(current_kp_ids)
                mastered = sum(
                    1 for kp_id in current_kp_ids
                    if progress.mastery_levels.get(kp_id, 0) >= 0.7
                )
                # Derive display name from first module, fall back to book_id
                display_name = ""
                if progress.modules:
                    display_name = progress.modules[0].name or ""
                summaries.append({
                    "book_id": progress.book_id,
                    "name": display_name or progress.book_id,
                    "modules_count": len(progress.modules),
                    "kp_count": total_kps,
                    "current_stage": progress.current_stage.value if progress.current_stage else "",
                    "mastered_pct": round(mastered / total_kps * 100) if total_kps else 0,
                    "updated_at": progress.updated_at,
                })
            except Exception:
                logger.warning("Failed to load progress for book %s, skipping", bid, exc_info=True)
                errors.append({"book_id": bid, "error": "Failed to load"})
                continue
        return {"summaries": summaries, "errors": errors}

    def save(self, progress: LearningProgress) -> None:
        self._store.save(progress)


__all__ = ["LearningService"]
