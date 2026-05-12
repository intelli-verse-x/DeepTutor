"""Guided Learning capability — Framework v1.8.2 structured mastery-based learning."""

from __future__ import annotations

import json
import time

from deeptutor.core.capability_protocol import BaseCapability, CapabilityManifest
from deeptutor.core.context import UnifiedContext
from deeptutor.core.stream_bus import StreamBus
from deeptutor.learning.models import (
    DiagnosticResult,
    KnowledgePoint,
    KnowledgeType,
    LearningModule,
    LearningProgress,
    LearningStage,
)
from deeptutor.learning.scheduler import SpacedRepetitionScheduler
from deeptutor.learning.service import LearningService
from deeptutor.learning.storage import LearningStore


class GuidedLearningCapability(BaseCapability):
    manifest = CapabilityManifest(
        name="guided_learning",
        description="Framework v1.8.2: structured mastery-based learning with spaced repetition",
        stages=[
            "diagnostic_phase1",
            "diagnostic_phase2",
            "metacognitive_intro",
            "plan",
            "pretest",
            "explain",
            "feynman_check",
            "practice",
            "error_diagnosis",
            "module_test",
            "review",
            "completed",
        ],
        tools_used=["rag", "code_execution", "web_search"],
    )

    def __init__(
        self,
        service: LearningService | None = None,
        scheduler: SpacedRepetitionScheduler | None = None,
        store: LearningStore | None = None,
    ) -> None:
        if service is not None:
            self._service = service
        else:
            self._store = store or LearningStore()
            self._service = LearningService(self._store)
        self._scheduler = scheduler or SpacedRepetitionScheduler()

    def _resolve_book_id(self, context: UnifiedContext) -> str:
        book_id = getattr(context, "book_id", None)
        if book_id:
            return book_id
        metadata = getattr(context, "metadata", {}) or {}
        refs = metadata.get("book_references", [])
        if refs:
            ref = refs[0]
            if isinstance(ref, str):
                return ref
            return ref.get("book_id") or ref.get("id", "default")
        return getattr(context, "session_id", "default")

    # ── Mock LLM ─────────────────────────────────────────────────────────

    def _mock_llm(self, system_prompt: str, user_message: str) -> str:
        """Return canned responses for testing. Replace with real LLM calls later."""
        lower = (system_prompt + " " + user_message).lower()
        if "diagnostic" in lower:
            return json.dumps({
                "questions": ["Q1: placeholder", "Q2: placeholder"],
                "answers": ["A1", "A2"],
            })
        if "explain" in lower:
            return "这是一个概念型知识点的模拟讲解..."
        if "feynman" in lower:
            return "模拟费曼检验结果：通过"
        if "pretest" in lower:
            return json.dumps({"question": "模拟预习题", "hint": "模拟提示"})
        if "practice" in lower:
            return json.dumps({
                "exercises": [
                    {"question": "练习1", "answer": "答案1"},
                    {"question": "练习2", "answer": "答案2"},
                ]
            })
        if "module_test" in lower:
            return json.dumps({
                "questions": ["测验1", "测验2"],
                "answers": ["答案1", "答案2"],
                "pass": True,
            })
        if "review" in lower:
            return "模拟复习内容"
        return "mock response"

    # ── Safe JSON parse ──────────────────────────────────────────────────

    @staticmethod
    def _safe_json_parse(text: str, default: dict | None = None) -> dict:
        """Parse JSON with graceful fallback on failure."""
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            return default or {}

    # ── State machine entry ──────────────────────────────────────────────

    async def run(self, context: UnifiedContext, stream: StreamBus) -> None:
        book_id = self._resolve_book_id(context)
        progress = self._service.get_or_create(book_id)

        stage = progress.current_stage
        handler = self._STAGE_HANDLERS.get(stage)
        if handler is None:
            if stage == LearningStage.COMPLETED:
                async with stream.stage("completed", source=self.manifest.name):
                    await stream.content("学习流程已完成。进入复习阶段。")
            return

        try:
            await handler(self, progress, context, stream)
        finally:
            self._service.save(progress)

    # ── §2 Diagnostic ────────────────────────────────────────────────────

    async def _run_diagnostic_phase1(
        self, progress: LearningProgress, context: UnifiedContext, stream: StreamBus
    ) -> None:
        async with stream.stage("diagnostic_phase1", source=self.manifest.name):
            response = self._mock_llm(
                "diagnostic", "generate diagnostic phase1 screening questions"
            )
            data = self._safe_json_parse(response, default={"questions": [], "answers": []})
            progress.diagnostic = DiagnosticResult(
                total_questions=len(data.get("questions", [])),
                phase1_result=data,
            )
            await stream.content(json.dumps(data, ensure_ascii=False))
            self._service.advance_stage(progress, LearningStage.DIAGNOSTIC_PHASE2)

    async def _run_diagnostic_phase2(
        self, progress: LearningProgress, context: UnifiedContext, stream: StreamBus
    ) -> None:
        async with stream.stage("diagnostic_phase2", source=self.manifest.name):
            response = self._mock_llm(
                "diagnostic", "generate diagnostic phase2 deep dive"
            )
            data = self._safe_json_parse(response, default={})
            if progress.diagnostic is not None:
                progress.diagnostic.phase2_results = {"phase2": data}
            await stream.content(response)
            self._service.advance_stage(progress, LearningStage.METACOGNITIVE_INTRO)

    async def _run_metacognitive_intro(
        self, progress: LearningProgress, context: UnifiedContext, stream: StreamBus
    ) -> None:
        async with stream.stage("metacognitive_intro", source=self.manifest.name):
            response = self._mock_llm("metacognitive", "introduce learning methods")
            await stream.content(response)
            self._service.advance_stage(progress, LearningStage.PLAN)

    async def _run_plan(
        self, progress: LearningProgress, context: UnifiedContext, stream: StreamBus
    ) -> None:
        async with stream.stage("plan", source=self.manifest.name):
            response = self._mock_llm("plan", "generate study plan from diagnostic results")
            await stream.content(response)
            if not progress.modules:
                mock_module = LearningModule(
                    id="module_1", name="模拟模块", order=1,
                    knowledge_points=[
                        KnowledgePoint(id="kp_1", name="模拟知识点", type=KnowledgeType.CONCEPT, module_id="module_1"),
                    ],
                )
                self._service.init_modules(progress, [mock_module])
                progress.current_module_id = "module_1"
            self._service.advance_stage(progress, LearningStage.PRETEST)

    # ── §5 Per-knowledge-point loop ──────────────────────────────────────

    def _current_knowledge_points(self, progress: LearningProgress) -> list:
        if not progress.modules:
            return []
        # If current_module_id is set, find the matching module
        if progress.current_module_id:
            for mod in progress.modules:
                if mod.id == progress.current_module_id:
                    return mod.knowledge_points
        # Fallback: return first module's knowledge points
        return progress.modules[0].knowledge_points

    async def _run_pretest(
        self, progress: LearningProgress, context: UnifiedContext, stream: StreamBus
    ) -> None:
        async with stream.stage("pretest", source=self.manifest.name):
            response = self._mock_llm("pretest", "generate pretest guess question")
            await stream.content(response)
            self._service.advance_stage(progress, LearningStage.EXPLAIN)

    async def _run_explain(
        self, progress: LearningProgress, context: UnifiedContext, stream: StreamBus
    ) -> None:
        async with stream.stage("explain", source=self.manifest.name):
            response = self._mock_llm("explain", "teach this knowledge point")
            await stream.content(response)
            self._service.advance_stage(progress, LearningStage.FEYNMAN_CHECK)

    async def _run_feynman_check(
        self, progress: LearningProgress, context: UnifiedContext, stream: StreamBus
    ) -> None:
        async with stream.stage("feynman_check", source=self.manifest.name):
            response = self._mock_llm("feynman", "verify understanding via feynman technique")
            await stream.content(response)
            kps = self._current_knowledge_points(progress)
            if progress.current_kp_index + 1 < len(kps):
                self._after_knowledge_point(progress)
                self._service.advance_stage(progress, LearningStage.PRETEST)
            else:
                self._service.advance_stage(progress, LearningStage.PRACTICE)

    def _after_knowledge_point(self, progress: LearningProgress) -> None:
        progress.current_kp_index += 1
        progress.updated_at = time.time()

    # ── §5 Per-module loop ───────────────────────────────────────────────

    async def _run_practice(
        self, progress: LearningProgress, context: UnifiedContext, stream: StreamBus
    ) -> None:
        async with stream.stage("practice", source=self.manifest.name):
            response = self._mock_llm("practice", "generate 3-5 exercises with Bloom + interleaving")
            await stream.content(response)
            self._service.advance_stage(progress, LearningStage.ERROR_DIAGNOSIS)

    async def _run_error_diagnosis(
        self, progress: LearningProgress, context: UnifiedContext, stream: StreamBus
    ) -> None:
        async with stream.stage("error_diagnosis", source=self.manifest.name):
            response = self._mock_llm("error_diagnosis", "self-attribution and AI confirmation")
            await stream.content(response)
            self._service.advance_stage(progress, LearningStage.MODULE_TEST)

    async def _run_module_test(
        self, progress: LearningProgress, context: UnifiedContext, stream: StreamBus
    ) -> None:
        async with stream.stage("module_test", source=self.manifest.name):
            response = self._mock_llm("module_test", "10-question module test with mastery gate")
            await stream.content(response)
            self._init_repetition_states(progress)
            self._service.advance_stage(progress, LearningStage.REVIEW)

    # ── §9 Review ────────────────────────────────────────────────────────

    def _advance_to_next_module(self, progress: LearningProgress) -> bool:
        ids = [m.id for m in progress.modules]
        if not progress.current_module_id or progress.current_module_id not in ids:
            return False
        idx = ids.index(progress.current_module_id)
        if idx + 1 < len(ids):
            progress.current_module_id = ids[idx + 1]
            progress.current_kp_index = 0
            return True
        return False

    def _init_repetition_states(self, progress: LearningProgress) -> None:
        current_kps = set()
        for mod in progress.modules:
            if mod.id == progress.current_module_id:
                for kp in mod.knowledge_points:
                    current_kps.add(kp.id)
        for kp_id in current_kps:
            kp_type = progress.knowledge_types.get(kp_id, KnowledgeType.MEMORY)
            if kp_id not in progress.repetition_states:
                progress.repetition_states[kp_id] = self._scheduler.get_initial_state(kp_type)

    async def _run_review(
        self, progress: LearningProgress, context: UnifiedContext, stream: StreamBus
    ) -> None:
        async with stream.stage("review", source=self.manifest.name):
            self._init_repetition_states(progress)
            self._schedule_reviews(progress)
            response = self._mock_llm("review", "spaced repetition review")
            await stream.content(response)
            if self._advance_to_next_module(progress):
                self._service.advance_stage(progress, LearningStage.PRETEST)
            else:
                self._service.advance_stage(progress, LearningStage.COMPLETED)

    def _schedule_reviews(self, progress: LearningProgress) -> None:
        tasks = self._scheduler.build_review_queue(progress)
        progress.review_queue = tasks

    # ── Stage dispatch table ─────────────────────────────────────────────

    _STAGE_HANDLERS = {
        LearningStage.DIAGNOSTIC_PHASE1: _run_diagnostic_phase1,
        LearningStage.DIAGNOSTIC_PHASE2: _run_diagnostic_phase2,
        LearningStage.METACOGNITIVE_INTRO: _run_metacognitive_intro,
        LearningStage.PLAN: _run_plan,
        LearningStage.PRETEST: _run_pretest,
        LearningStage.EXPLAIN: _run_explain,
        LearningStage.FEYNMAN_CHECK: _run_feynman_check,
        LearningStage.PRACTICE: _run_practice,
        LearningStage.ERROR_DIAGNOSIS: _run_error_diagnosis,
        LearningStage.MODULE_TEST: _run_module_test,
        LearningStage.REVIEW: _run_review,
    }


__all__ = ["GuidedLearningCapability"]
