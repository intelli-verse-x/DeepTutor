"""Tests for Feynman check retry limit."""

import asyncio
from contextlib import asynccontextmanager
import json
from unittest.mock import AsyncMock, patch

import pytest

from deeptutor.capabilities.guided_learning import GuidedLearningCapability
from deeptutor.learning.models import (
    KnowledgePoint,
    LearningModule,
    LearningProgress,
    LearningStage,
)
from deeptutor.learning.service import LearningService
from deeptutor.learning.storage import LearningStore


class FakeStream:
    """Minimal StreamBus mock for capability testing."""

    def __init__(self, user_inputs: list[str] | None = None):
        self._inputs = list(user_inputs or [])
        self._input_idx = 0
        self.events: list[str] = []

    @asynccontextmanager
    async def stage(self, name, source="", metadata=None):
        self.events.append(f"stage:{name}")
        yield

    async def content(self, text, source="", stage="", metadata=None):
        self.events.append(text)

    async def wait_for_input(self, prompt, source="", stage="", timeout=None):
        if self._input_idx < len(self._inputs):
            val = self._inputs[self._input_idx]
            self._input_idx += 1
            return val
        return ""


def _make_progress(kp_id="kp1", kp_name="Test KP") -> LearningProgress:
    progress = LearningProgress(book_id="testbook")
    progress.modules = [
        LearningModule(
            id="m1",
            name="M1",
            order=0,
            knowledge_points=[KnowledgePoint(id=kp_id, name=kp_name, type="concept", module_id="m1")],
        )
    ]
    progress.current_module_id = "m1"
    progress.current_kp_index = 0
    progress.current_stage = LearningStage.FEYNMAN_CHECK
    return progress


def _make_capability(llm_response: str) -> GuidedLearningCapability:
    cap = GuidedLearningCapability.__new__(GuidedLearningCapability)
    cap._store = LearningStore.__new__(LearningStore)
    cap._store._root = None  # not used in these tests
    cap._service = LearningService(cap._store)
    cap._scheduler = None
    cap._kb_name = None
    cap._kb_base_dir = None
    cap._call_llm = AsyncMock(return_value=llm_response)
    return cap


@pytest.mark.asyncio
async def test_feynman_3_failures_skips_to_practice_quiz():
    """After 3 consecutive Feynman failures, stage advances past EXPLAIN."""
    failed_response = json.dumps({"passed": False, "feedback": "not quite", "gap": ""})
    cap = _make_capability(failed_response)
    progress = _make_progress()
    ctx = None  # not used by _run_feynman_check

    # Fail 3 times
    for _ in range(3):
        stream = FakeStream(user_inputs=["my explanation"])
        await cap._run_feynman_check(progress, ctx, stream)

    # After 3 failures, stage should NOT be EXPLAIN — it should be PRACTICE_QUIZ
    # (since there's only 1 KP, _advance_after_kp goes to PRACTICE_QUIZ)
    assert progress.current_stage == LearningStage.PRACTICE_QUIZ
    # Mastery marked as weak
    assert progress.mastery_levels["kp1"] == 0.0
    # Retry counter at 3
    assert progress.feynman_retries["kp1"] == 3


@pytest.mark.asyncio
async def test_feynman_pass_resets_counter():
    """Passing Feynman check resets the retry counter."""
    failed_response = json.dumps({"passed": False, "feedback": "no", "gap": ""})
    passed_response = json.dumps({"passed": True, "feedback": "good", "gap": ""})

    progress = _make_progress()
    ctx = None

    # Fail twice
    for _ in range(2):
        cap = _make_capability(failed_response)
        stream = FakeStream(user_inputs=["my explanation"])
        await cap._run_feynman_check(progress, ctx, stream)

    assert progress.feynman_retries["kp1"] == 2
    assert progress.current_stage == LearningStage.EXPLAIN

    # Pass on 3rd attempt
    cap = _make_capability(passed_response)
    stream = FakeStream(user_inputs=["my explanation"])
    await cap._run_feynman_check(progress, ctx, stream)

    # Counter reset, stage advanced
    assert progress.feynman_retries["kp1"] == 0
    assert progress.current_stage == LearningStage.PRACTICE_QUIZ
