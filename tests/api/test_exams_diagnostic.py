"""Diagnostic adaptive-ladder unit tests.

Closes the "ladder direction only verifies against a live backend" gap: these
exercise the *actual* decision functions the `/diagnostic/answer` endpoint uses
(`_next_difficulty`, `_difficulty_fallback_order`, `_score_pct`) so the adaptive
trajectory (correct → harder, wrong → easier) and the accuracy computation are
verified deterministically, with no database or live deployment.
"""

from __future__ import annotations

import pytest

# Importing the router module is enough to reach the pure helpers; skip cleanly
# if the FastAPI/SQLAlchemy stack isn't installed in this environment.
pytest.importorskip("fastapi")
pytest.importorskip("sqlalchemy")

from deeptutor.api.routers import exams  # noqa: E402


class TestNextDifficulty:
    """Correct → step up; wrong → step down; clamped at easy/hard bounds."""

    def test_correct_steps_up(self):
        assert exams._next_difficulty("easy", True) == "medium"
        assert exams._next_difficulty("medium", True) == "hard"

    def test_correct_clamped_at_hard(self):
        assert exams._next_difficulty("hard", True) == "hard"

    def test_wrong_steps_down(self):
        assert exams._next_difficulty("hard", False) == "medium"
        assert exams._next_difficulty("medium", False) == "easy"

    def test_wrong_clamped_at_easy(self):
        assert exams._next_difficulty("easy", False) == "easy"

    def test_unexpected_value_defaults_to_medium_trajectory(self):
        # Unknown stored difficulty is treated as medium, then stepped.
        assert exams._next_difficulty("expert", True) == "hard"
        assert exams._next_difficulty("expert", False) == "easy"

    def test_full_ascending_then_descending_ladder(self):
        # Simulate a real session trajectory and assert it never inverts.
        d = "medium"
        for is_correct, expected in [
            (True, "hard"),   # medium → hard
            (True, "hard"),   # capped
            (False, "medium"),
            (False, "easy"),
            (False, "easy"),  # capped
            (True, "medium"),
        ]:
            d = exams._next_difficulty(d, is_correct)
            assert d == expected


class TestDifficultyFallbackOrder:
    """When the exact difficulty is missing, degrade to the *nearest* level,
    biased in the adaptive direction on a tie (medium)."""

    def test_prefer_harder_on_medium_tie(self):
        # Last answer correct → ascending learner → harder side first.
        assert exams._difficulty_fallback_order("medium", prefer_harder=True) == [
            "hard",
            "easy",
        ]

    def test_prefer_easier_on_medium_tie(self):
        assert exams._difficulty_fallback_order("medium", prefer_harder=False) == [
            "easy",
            "hard",
        ]

    def test_nearest_first_from_hard(self):
        # From hard, medium is nearer than easy regardless of the tie bias.
        assert exams._difficulty_fallback_order("hard", prefer_harder=True)[0] == "medium"

    def test_unknown_target_returns_full_ladder(self):
        assert exams._difficulty_fallback_order("expert") == ["easy", "medium", "hard"]


class TestScorePct:
    def test_perfect_run_is_not_zero(self):
        # The 0%-accuracy regression class: a perfect run must be 100, never 0.
        assert exams._score_pct(13, 13) == 100.0

    def test_partial(self):
        assert exams._score_pct(13, 15) == 86.7

    def test_no_answers_is_zero(self):
        assert exams._score_pct(0, 0) == 0


class TestCanonSubject:
    """Localized/variant subject labels must canonicalize so the breakdown never
    shows garbled or wrong-locale rows (e.g. 영어/국어/수학 on an English exam)."""

    def test_localized_labels_map_to_english(self):
        assert exams._canon_subject("수학") == "Mathematics"
        assert exams._canon_subject("영어") == "English"
        assert exams._canon_subject("국어") == "Reading"

    def test_case_insensitive_and_variants(self):
        assert exams._canon_subject("MATHS") == "Mathematics"
        assert exams._canon_subject("verbal") == "Reading"

    def test_leaked_foreign_script_collapses_to_general(self):
        # An unmapped non-Latin label must not surface raw.
        assert exams._canon_subject("العربية") == "General"

    def test_empty_is_general(self):
        assert exams._canon_subject(None) == "General"
        assert exams._canon_subject("   ") == "General"

    def test_unknown_latin_label_is_title_cased(self):
        assert exams._canon_subject("astronomy") == "Astronomy"
