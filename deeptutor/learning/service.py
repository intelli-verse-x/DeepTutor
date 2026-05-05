from __future__ import annotations

import time
import uuid

from deeptutor.learning.models import (
    ErrorRecord,
    LearningModule,
    LearningProgress,
    LearningStage,
    QuizAttempt,
)
from deeptutor.learning.storage import LearningStore


class LearningService:
    def __init__(self, store: LearningStore | None = None) -> None:
        self._store = store or LearningStore()

    def get_or_create(self, book_id: str) -> LearningProgress:
        existing = self._store.load(book_id)
        if existing is not None:
            return existing
        return LearningProgress(book_id=book_id)

    def init_modules(
        self, progress: LearningProgress, modules: list[LearningModule]
    ) -> None:
        progress.modules = modules
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
        progress.updated_at = time.time()

    def update_mastery(
        self, progress: LearningProgress, kp_id: str, level: float
    ) -> None:
        progress.mastery_levels[kp_id] = level
        progress.updated_at = time.time()

    def save(self, progress: LearningProgress) -> None:
        self._store.save(progress)


__all__ = ["LearningService"]
