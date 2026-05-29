"""Tests for replace_modules, merge_modules, and CAS save."""

from pathlib import Path

from deeptutor.learning.models import (
    ErrorRecord,
    ErrorType,
    KnowledgePoint,
    KnowledgeType,
    LearningModule,
    LearningProgress,
    LearningStage,
    RepetitionState,
    ReviewTask,
)
from deeptutor.learning.service import LearningService
from deeptutor.learning.storage import LearningStore


def _make_kp(kp_id: str, module_id: str = "m1") -> KnowledgePoint:
    return KnowledgePoint(id=kp_id, name=f"KP {kp_id}", type=KnowledgeType.CONCEPT, module_id=module_id)


def _make_module(mod_id: str, kp_ids: list[str]) -> LearningModule:
    return LearningModule(
        id=mod_id,
        name=f"Module {mod_id}",
        order=0,
        knowledge_points=[_make_kp(kid, mod_id) for kid in kp_ids],
    )


# ── merge_modules ────────────────────────────────────────────────────────


class TestMergeModules:
    def test_merge_adds_new_modules(self, tmp_path: Path):
        store = LearningStore(root=tmp_path)
        service = LearningService(store)
        progress = LearningProgress(book_id="test")

        service.merge_modules(progress, [_make_module("m1", ["kp1"])])
        assert len(progress.modules) == 1
        assert progress.modules[0].id == "m1"

        service.merge_modules(progress, [_make_module("m2", ["kp2"])])
        assert len(progress.modules) == 2

    def test_merge_updates_existing_module(self, tmp_path: Path):
        store = LearningStore(root=tmp_path)
        service = LearningService(store)
        progress = LearningProgress(book_id="test")

        service.merge_modules(progress, [_make_module("m1", ["kp1"])])
        # Update m1 with different KPs
        service.merge_modules(progress, [_make_module("m1", ["kp1", "kp1b"])])
        assert len(progress.modules) == 1
        assert len(progress.modules[0].knowledge_points) == 2

    def test_init_modules_replaces_existing_modules(self, tmp_path: Path):
        store = LearningStore(root=tmp_path)
        service = LearningService(store)
        progress = LearningProgress(book_id="test")

        service.init_modules(progress, [_make_module("m1", ["kp1"])])
        assert len(progress.modules) == 1
        service.init_modules(progress, [_make_module("m2", ["kp2"])])
        assert [m.id for m in progress.modules] == ["m2"]
        assert "kp1" not in progress.knowledge_types
        assert "kp2" in progress.knowledge_types


# ── replace_modules ──────────────────────────────────────────────────────


class TestReplaceModules:
    def test_replace_removes_old_modules(self, tmp_path: Path):
        store = LearningStore(root=tmp_path)
        service = LearningService(store)
        progress = LearningProgress(book_id="test")

        service.merge_modules(progress, [_make_module("m1", ["kp1"]), _make_module("m2", ["kp2"])])
        assert len(progress.modules) == 2

        service.replace_modules(progress, [_make_module("m3", ["kp3"])])
        assert len(progress.modules) == 1
        assert progress.modules[0].id == "m3"

    def test_replace_cleans_stale_mastery(self, tmp_path: Path):
        store = LearningStore(root=tmp_path)
        service = LearningService(store)
        progress = LearningProgress(book_id="test")

        service.merge_modules(progress, [_make_module("m1", ["kp1"])])
        progress.mastery_levels["kp1"] = 0.8

        service.replace_modules(progress, [_make_module("m2", ["kp2"])])
        assert "kp1" not in progress.mastery_levels

    def test_replace_cleans_stale_knowledge_types(self, tmp_path: Path):
        store = LearningStore(root=tmp_path)
        service = LearningService(store)
        progress = LearningProgress(book_id="test")

        service.merge_modules(progress, [_make_module("m1", ["kp1"])])
        assert "kp1" in progress.knowledge_types

        service.replace_modules(progress, [_make_module("m2", ["kp2"])])
        assert "kp1" not in progress.knowledge_types
        assert "kp2" in progress.knowledge_types

    def test_replace_cleans_stale_repetition_states(self, tmp_path: Path):
        store = LearningStore(root=tmp_path)
        service = LearningService(store)
        progress = LearningProgress(book_id="test")

        service.merge_modules(progress, [_make_module("m1", ["kp1"])])
        progress.repetition_states["kp1"] = RepetitionState(
            interval_index=0, consecutive_correct=0, consecutive_wrong=0, next_review_at=0
        )

        service.replace_modules(progress, [_make_module("m2", ["kp2"])])
        assert "kp1" not in progress.repetition_states

    def test_replace_cleans_stale_error_records(self, tmp_path: Path):
        store = LearningStore(root=tmp_path)
        service = LearningService(store)
        progress = LearningProgress(book_id="test")

        service.merge_modules(progress, [_make_module("m1", ["kp1"])])
        progress.error_records.append(
            ErrorRecord(
                id="er1",
                question_id="q1",
                knowledge_point_id="kp1",
                module_id="m1",
                error_type=ErrorType.APPLICATION_ERROR,
            )
        )

        service.replace_modules(progress, [_make_module("m2", ["kp2"])])
        assert len(progress.error_records) == 0

    def test_replace_cleans_stale_feynman_retries(self, tmp_path: Path):
        store = LearningStore(root=tmp_path)
        service = LearningService(store)
        progress = LearningProgress(book_id="test")

        service.merge_modules(progress, [_make_module("m1", ["kp1"])])
        progress.feynman_retries["kp1"] = 2

        service.replace_modules(progress, [_make_module("m2", ["kp2"])])
        assert "kp1" not in progress.feynman_retries

    def test_replace_cleans_stale_review_queue(self, tmp_path: Path):
        store = LearningStore(root=tmp_path)
        service = LearningService(store)
        progress = LearningProgress(book_id="test")

        service.merge_modules(progress, [_make_module("m1", ["kp1"])])
        progress.review_queue.append(
            ReviewTask(
                id="rt1",
                knowledge_point_id="kp1",
                knowledge_type=KnowledgeType.CONCEPT,
                due_at=0,
                priority=1,
                state=RepetitionState(
                    interval_index=0, consecutive_correct=0, consecutive_wrong=0, next_review_at=0
                ),
            )
        )

        service.replace_modules(progress, [_make_module("m2", ["kp2"])])
        assert len(progress.review_queue) == 0

    def test_replace_preserves_new_module_kps(self, tmp_path: Path):
        store = LearningStore(root=tmp_path)
        service = LearningService(store)
        progress = LearningProgress(book_id="test")

        service.replace_modules(progress, [_make_module("m1", ["kp1"])])
        assert "kp1" in progress.knowledge_types
        assert progress.modules[0].knowledge_points[0].id == "kp1"

    def test_replace_cleans_stale_feynman_explanations(self, tmp_path: Path):
        store = LearningStore(root=tmp_path)
        service = LearningService(store)
        progress = LearningProgress(book_id="test")

        service.merge_modules(progress, [_make_module("m1", ["kp1"])])
        progress.feynman_explanations["kp1"] = "user explanation text"

        service.replace_modules(progress, [_make_module("m2", ["kp2"])])
        assert "kp1" not in progress.feynman_explanations

    def test_replace_clears_stage_failure_records(self, tmp_path: Path):
        store = LearningStore(root=tmp_path)
        service = LearningService(store)
        progress = LearningProgress(book_id="test")

        service.merge_modules(progress, [_make_module("m1", ["kp1"])])
        progress.stage_failure_counts["explain"] = 4
        progress.stage_failure_notes["explain"] = "timeout"

        service.replace_modules(progress, [_make_module("m2", ["kp2"])])
        assert progress.stage_failure_counts == {}
        assert progress.stage_failure_notes == {}


# ── CAS save ─────────────────────────────────────────────────────────────


class TestCASSave:
    def test_cas_save_succeeds_on_matching_version(self, tmp_path: Path):
        store = LearningStore(root=tmp_path)
        progress = LearningProgress(book_id="test")
        store.save(progress)  # version becomes 1

        progress.current_stage = LearningStage.PLAN
        assert store.save_cas(progress, expected_version=1) is True
        loaded = store.load("test")
        assert loaded.version == 2
        assert loaded.current_stage == LearningStage.PLAN

    def test_cas_save_fails_on_mismatched_version(self, tmp_path: Path):
        store = LearningStore(root=tmp_path)
        progress = LearningProgress(book_id="test")
        store.save(progress)  # version becomes 1

        # Someone else saves between our load and save_cas
        other = store.load("test")
        other.current_stage = LearningStage.PLAN
        store.save(other)  # version becomes 2

        # Our save_cas with stale version should fail
        progress.current_stage = LearningStage.EXPLAIN
        assert store.save_cas(progress, expected_version=1) is False

        # Disk should have the other save's value
        loaded = store.load("test")
        assert loaded.current_stage == LearningStage.PLAN
        assert loaded.version == 2

    def test_save_increments_version(self, tmp_path: Path):
        store = LearningStore(root=tmp_path)
        progress = LearningProgress(book_id="test")
        assert progress.version == 0

        store.save(progress)
        assert store.load("test").version == 1

        store.save(progress)
        assert store.load("test").version == 2

    def test_cas_save_fails_when_progress_does_not_exist(self, tmp_path: Path):
        store = LearningStore(root=tmp_path)
        progress = LearningProgress(book_id="nonexistent")
        assert store.save_cas(progress, expected_version=0) is False
