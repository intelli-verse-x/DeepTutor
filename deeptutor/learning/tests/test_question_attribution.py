"""Tests for per-question knowledge point attribution."""

from deeptutor.capabilities.guided_learning import GuidedLearningCapability
from deeptutor.learning.models import KnowledgePoint, KnowledgeType


def _kp(kp_id: str, name: str) -> KnowledgePoint:
    return KnowledgePoint(id=kp_id, name=name, type=KnowledgeType.CONCEPT, module_id="m1")


def test_resolve_kp_id_map_accepts_ids_and_names():
    kps = [_kp("kp1", "Limits"), _kp("kp2", "Derivatives")]
    data = {
        "questions": [
            {"knowledge_point_id": "kp2"},
            {"knowledge_point": "Limits"},
        ]
    }
    answers = {"q1": "a1", "q2": "a2"}

    result = GuidedLearningCapability._resolve_kp_id_map(data, kps, answers, "quiz")

    assert result == {"q1": "kp2", "q2": "kp1"}


def test_resolve_kp_id_map_round_robins_missing_attribution():
    kps = [_kp("kp1", "Limits"), _kp("kp2", "Derivatives")]
    data = {"questions": [{}, {}, {}]}
    answers = {"q1": "a1", "q2": "a2", "q3": "a3"}

    result = GuidedLearningCapability._resolve_kp_id_map(data, kps, answers, "quiz")

    assert result == {"q1": "kp1", "q2": "kp2", "q3": "kp1"}
