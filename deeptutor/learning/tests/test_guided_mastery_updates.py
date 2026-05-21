"""Tests for Guided Learning mastery updates from in-turn answers."""

from deeptutor.capabilities.guided_learning import GuidedLearningCapability
from deeptutor.learning.models import (
    KnowledgePoint,
    KnowledgeType,
    LearningModule,
    LearningProgress,
    QuizAttempt,
)
from deeptutor.learning.service import LearningService
from deeptutor.learning.storage import LearningStore


def test_record_attempt_updates_mastery_level(tmp_path):
    cap = GuidedLearningCapability.__new__(GuidedLearningCapability)
    cap._store = LearningStore(root=tmp_path)
    cap._service = LearningService(cap._store)
    cap._scheduler = None

    progress = LearningProgress(book_id="book1")
    progress.modules = [
        LearningModule(
            id="m1",
            name="Module 1",
            order=0,
            knowledge_points=[
                KnowledgePoint(id="kp1", name="KP1", type=KnowledgeType.CONCEPT, module_id="m1")
            ],
        )
    ]
    progress.knowledge_types["kp1"] = KnowledgeType.CONCEPT

    cap._record_attempt_and_update_mastery(
        progress,
        QuizAttempt(
            question_id="q1",
            knowledge_point_id="kp1",
            module_id="m1",
            is_correct=True,
            user_answer="answer",
        ),
    )

    assert progress.mastery_levels["kp1"] == 1.0
    loaded = cap._store.load("book1")
    assert loaded is not None
    assert len(loaded.quiz_attempts) == 1
    assert loaded.mastery_levels["kp1"] == 1.0
