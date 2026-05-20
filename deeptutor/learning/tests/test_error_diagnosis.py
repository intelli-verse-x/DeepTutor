"""Tests for error diagnosis fallback behavior."""

import asyncio
from contextlib import asynccontextmanager
from unittest.mock import AsyncMock

import pytest

from deeptutor.capabilities.guided_learning import GuidedLearningCapability
from deeptutor.learning.models import (
    ErrorRecord,
    ErrorType,
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

    @asynccontextmanager
    async def stage(self, name, source="", metadata=None):
        self.events.append(("stage", name))
        yield

    async def content(self, text, source="", stage="", metadata=None):
        self.events.append(("content", text))


def _make_capability() -> GuidedLearningCapability:
    cap = GuidedLearningCapability.__new__(GuidedLearningCapability)
    cap._store = LearningStore.__new__(LearningStore)
    cap._store._root = None
    cap._service = LearningService(cap._store)
    cap._scheduler = None
    cap._kb_name = None
    cap._kb_base_dir = None
    cap._call_llm = AsyncMock(side_effect=RuntimeError("LLM unavailable"))
    return cap


def _make_progress() -> LearningProgress:
    progress = LearningProgress(book_id="book1")
    progress.current_stage = LearningStage.ERROR_DIAGNOSIS
    progress.current_module_id = "m1"
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
    progress.error_records.append(
        ErrorRecord(
            id="er1",
            question_id="q1",
            knowledge_point_id="kp1",
            module_id="m1",
            error_type=ErrorType.APPLICATION_ERROR,
            status="active",
        )
    )
    return progress


@pytest.mark.asyncio
async def test_error_diagnosis_llm_failure_advances_to_module_test():
    cap = _make_capability()
    progress = _make_progress()
    stream = FakeStream()

    await cap._run_error_diagnosis(progress, None, stream)

    assert progress.current_stage == LearningStage.MODULE_TEST
    assert progress.error_records[0].error_type == ErrorType.APPLICATION_ERROR
    assert progress.error_records[0].ai_confirmation.startswith("error_diagnosis_unavailable:")
    assert any("错因诊断暂时不可用" in text for kind, text in stream.events if kind == "content")


@pytest.mark.asyncio
async def test_error_diagnosis_llm_timeout_advances_to_module_test():
    cap = _make_capability()
    cap._ERROR_DIAGNOSIS_TIMEOUT_SECONDS = 0.01

    async def _slow_llm(*args, **kwargs):
        await asyncio.sleep(1)
        return '{"diagnoses": []}'

    cap._call_llm = AsyncMock(side_effect=_slow_llm)
    progress = _make_progress()
    stream = FakeStream()

    await cap._run_error_diagnosis(progress, None, stream)

    assert progress.current_stage == LearningStage.MODULE_TEST
    assert progress.error_records[0].ai_confirmation.startswith("error_diagnosis_unavailable:")


@pytest.mark.asyncio
async def test_call_llm_returns_response_text_not_rag_tuple():
    cap = GuidedLearningCapability.__new__(GuidedLearningCapability)
    cap._call_llm_impl = AsyncMock(return_value=("payload", "rag warning"))

    response = await cap._call_llm("system", "user")

    assert response == "payload"
