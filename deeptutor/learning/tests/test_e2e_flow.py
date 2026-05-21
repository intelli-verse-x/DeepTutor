"""End-to-end flow test: PRETEST → EXPLAIN → FEYNMAN_CHECK → PRACTICE_QUIZ → ERROR_DIAGNOSIS → MODULE_TEST → REVIEW → COMPLETED."""

from contextlib import asynccontextmanager
import json
from unittest.mock import AsyncMock

import pytest

from deeptutor.capabilities.guided_learning import GuidedLearningCapability
from deeptutor.learning.models import (
    KnowledgePoint,
    KnowledgeType,
    LearningModule,
    LearningProgress,
    LearningStage,
)
from deeptutor.learning.service import LearningService
from deeptutor.learning.storage import LearningStore


class FakeStream:
    def __init__(self) -> None:
        self.events: list[tuple[str, str]] = []
        self.inputs: list[str] = []
        self._input_idx = 0

    @asynccontextmanager
    async def stage(self, name, source="", metadata=None):
        self.events.append(("stage", name))
        yield

    async def content(self, text, source="", stage="", metadata=None):
        self.events.append(("content", text))

    async def wait_for_input(self, prompt, source="", timeout=None):
        if self._input_idx < len(self.inputs):
            val = self.inputs[self._input_idx]
            self._input_idx += 1
            return val
        return ""


@pytest.mark.asyncio
async def test_e2e_pretest_to_completed(tmp_path):
    """Full flow from PRETEST through COMPLETED with 1 module, 1 KP."""
    # ── Setup ────────────────────────────────────────────────────────────
    store = LearningStore(root=tmp_path)
    service = LearningService(store)

    cap = GuidedLearningCapability.__new__(GuidedLearningCapability)
    cap._store = store
    cap._service = service
    cap._scheduler = type("S", (), {
        "get_initial_state": lambda self, kt: None,
        "build_review_queue": lambda self, p: [],
        "schedule_next": lambda self, state, kt, correct: None,
    })()
    cap._kb_name = None
    cap._kb_base_dir = None

    kp = KnowledgePoint(id="kp1", name="Photosynthesis", type=KnowledgeType.CONCEPT, module_id="m1")
    mod = LearningModule(id="m1", name="Biology", order=0, knowledge_points=[kp])
    progress = LearningProgress(book_id="e2e_book")
    progress.modules = [mod]
    progress.current_module_id = "m1"
    progress.current_kp_index = 0
    progress.current_stage = LearningStage.PRETEST
    progress.knowledge_types["kp1"] = KnowledgeType.CONCEPT

    stream = FakeStream()
    context = type("Ctx", (), {"book_id": "e2e_book"})()

    # ── Mock LLM responses (in call order) ──────────────────────────────
    quiz_data = json.dumps({
        "questions": [
            {"id": "pq1", "question": "What is photosynthesis?", "answer": "photosynthesis", "type": "short"}
        ],
    })
    module_test_data = json.dumps({
        "questions": [
            {"id": "mt1", "question": "Explain photosynthesis.", "answer": "photosynthesis", "type": "short"}
        ],
    })

    cap._call_llm = AsyncMock(side_effect=[
        "Pretest content",                          # 1. PRETEST
        "Explain content",                          # 2. EXPLAIN
        json.dumps({"passed": True, "feedback": "good", "gap": ""}),  # 3. FEYNMAN_CHECK
        quiz_data,                                  # 4. PRACTICE_QUIZ
        module_test_data,                           # 5. MODULE_TEST
        "Review content",                           # 6. REVIEW
    ])

    # User inputs: feynman explanation + 2 quiz answers
    stream.inputs = ["Plants convert sunlight to energy", "photosynthesis", "photosynthesis"]

    # ── Stage 1: PRETEST → EXPLAIN ──────────────────────────────────────
    assert progress.current_stage == LearningStage.PRETEST
    await cap._run_pretest(progress, context, stream)
    assert progress.current_stage == LearningStage.EXPLAIN

    # ── Stage 2: EXPLAIN → FEYNMAN_CHECK ────────────────────────────────
    await cap._run_explain(progress, context, stream)
    assert progress.current_stage == LearningStage.FEYNMAN_CHECK

    # ── Stage 3: FEYNMAN_CHECK → PRACTICE_QUIZ ──────────────────────────
    await cap._run_feynman_check(progress, context, stream)
    # With 1 KP and passed=True, _advance_after_kp goes to PRACTICE_QUIZ
    assert progress.current_stage == LearningStage.PRACTICE_QUIZ

    # ── Stage 4: PRACTICE_QUIZ → ERROR_DIAGNOSIS ────────────────────────
    await cap._run_practice_quiz(progress, context, stream)
    assert progress.current_stage == LearningStage.ERROR_DIAGNOSIS

    # ── Stage 5: ERROR_DIAGNOSIS → MODULE_TEST (no errors) ──────────────
    await cap._run_error_diagnosis(progress, context, stream)
    assert progress.current_stage == LearningStage.MODULE_TEST

    # ── Stage 6: MODULE_TEST → REVIEW ───────────────────────────────────
    await cap._run_module_test(progress, context, stream)
    assert progress.current_stage == LearningStage.REVIEW

    # ── Stage 7: REVIEW → COMPLETED ─────────────────────────────────────
    await cap._run_review(progress, context, stream)
    assert progress.current_stage == LearningStage.COMPLETED

    # ── Verify LLM was called expected number of times ──────────────────
    assert cap._call_llm.call_count == 6

    # ── Verify practice quiz attempt was recorded ───────────────────────
    # (module_test sends questions to client for later grading via /answer endpoint,
    # so no quiz_attempts are recorded during the flow itself)
    assert len(progress.quiz_attempts) == 1
    assert progress.quiz_attempts[0].question_id == "pq1"
    assert progress.quiz_attempts[0].is_correct is True
