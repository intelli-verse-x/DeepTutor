"""Exam-pack slug seeding + backfill tests.

Covers the fix that lets the web SPA's geo→exam preferences resolve for
non-Latin-named packs:

* ``stable_exam_slug`` — pure slug derivation (Latin-led → ``None`` so the SPA
  keeps its own derivation; non-Latin-led → clean ASCII slug).
* ``backfill_exam_pack_slugs`` — idempotently stamps ``metadata.slug`` onto rows
  seeded *before* the fix (the deploy path for already-seeded environments).

The backfill test stubs the async session so it runs with **no database**.
"""

from __future__ import annotations

import asyncio

import pytest

# seed.py imports sqlalchemy at module scope; skip cleanly when the stack isn't
# installed (CI has it).
pytest.importorskip("sqlalchemy")

from deeptutor.services.exam import seed  # noqa: E402


class TestStableExamSlug:
    """Latin-led names are left to the SPA; non-Latin names get a clean slug."""

    @pytest.mark.parametrize(
        "name",
        [
            "JEE Main",
            "SAT",
            "GATE (CS)",
            "Abitur",
            "Mittlere Reife (Realschulabschluss)",
            "Saber 11 (ICFES)",
            "EXANI-II (CENEVAL)",
            "Baccalauréat",
            "ENEM",
        ],
    )
    def test_latin_led_names_return_none(self, name):
        # None → no metadata.slug override → SPA's existing derivation is unchanged
        # (no regression for gate_cs, sat, …).
        assert seed.stable_exam_slug(name) is None

    @pytest.mark.parametrize(
        "name,expected",
        [
            ("高考 (Gaokao)", "gaokao"),
            ("中考 (Zhongkao)", "zhongkao"),
            ("اختبار القدرات (Qudurat)", "qudurat"),
            ("اختبار التحصيلي (Tahsili)", "tahsili"),
            ("الثانوية العامة (Thanawiya Amma)", "thanawiya_amma"),
            ("共通テスト (Kyōtsū Test)", "kyotsu_test"),
            ("高校入試 (Kōkō Nyūshi)", "koko_nyushi"),
            ("수능 (CSAT / Suneung)", "csat"),
        ],
    )
    def test_non_latin_names_get_clean_slug(self, name, expected):
        assert seed.stable_exam_slug(name) == expected

    def test_cyrillic_only_name_has_no_ascii_slug(self):
        # Both the lead and the paren content are Cyrillic → no ASCII slug; the
        # SPA falls back to its derivation (no RU geo-pref depends on this).
        assert seed.stable_exam_slug("ЕГЭ (Единый государственный экзамен)") is None

    def test_empty_name(self):
        assert seed.stable_exam_slug("") is None


# ── Backfill (no-DB stub) ────────────────────────────────────────────────────


class _FakeRow:
    def __init__(self, name, metadata_):
        self.name = name
        self.metadata_ = metadata_


class _FakeScalars:
    def __init__(self, rows):
        self._rows = rows

    def all(self):
        return self._rows


class _FakeResult:
    def __init__(self, rows):
        self._rows = rows

    def scalars(self):
        return _FakeScalars(self._rows)


class _FakeSession:
    def __init__(self, rows):
        self._rows = rows
        self.commits = 0

    async def execute(self, *_args, **_kwargs):
        return _FakeResult(self._rows)

    async def commit(self):
        self.commits += 1


def _patch_session(monkeypatch, session):
    """Stub the async session generator AND ``flag_modified``.

    ``flag_modified`` expects a real SQLAlchemy-instrumented instance, so against
    the plain ``_FakeRow`` stubs we record the calls instead — which doubles as an
    assertion that the JSONB dirty-mark fires once per updated row.

    Returns the recorded ``(obj, attr)`` calls.
    """
    async def _gen():
        yield session

    monkeypatch.setattr(seed, "get_session", _gen)
    flag_calls: list[tuple[object, str]] = []
    monkeypatch.setattr(
        seed, "flag_modified", lambda obj, attr: flag_calls.append((obj, attr))
    )
    return flag_calls


class TestBackfillExamPackSlugs:
    def test_backfills_only_non_latin_and_preserves_other_keys(self, monkeypatch):
        rows = [
            _FakeRow("SAT", {"foo": 1}),  # Latin → untouched
            _FakeRow("GATE (CS)", {}),  # Latin → untouched
            _FakeRow("高考 (Gaokao)", {}),  # → gaokao
            _FakeRow("اختبار القدرات (Qudurat)", {"x": 2}),  # → qudurat, keep x
        ]
        session = _FakeSession(rows)
        flag_calls = _patch_session(monkeypatch, session)

        updated = asyncio.run(seed.backfill_exam_pack_slugs())

        assert updated == 2
        assert "slug" not in rows[0].metadata_  # SAT
        assert "slug" not in rows[1].metadata_  # GATE (CS)
        assert rows[2].metadata_["slug"] == "gaokao"
        assert rows[3].metadata_["slug"] == "qudurat"
        assert rows[3].metadata_["x"] == 2  # existing key preserved
        assert session.commits == 1
        # JSONB dirty-mark fired exactly for the two updated rows.
        assert flag_calls == [(rows[2], "metadata_"), (rows[3], "metadata_")]

    def test_idempotent_second_run_is_noop(self, monkeypatch):
        rows = [
            _FakeRow("高考 (Gaokao)", {}),
            _FakeRow("اختبار القدرات (Qudurat)", {}),
        ]
        session = _FakeSession(rows)
        flag_calls = _patch_session(monkeypatch, session)

        first = asyncio.run(seed.backfill_exam_pack_slugs())
        assert first == 2
        assert len(flag_calls) == 2

        # Second pass over the now-stamped rows must not update, commit, or re-mark.
        session.commits = 0
        flag_calls.clear()
        second = asyncio.run(seed.backfill_exam_pack_slugs())
        assert second == 0
        assert session.commits == 0
        assert flag_calls == []

    def test_existing_correct_slug_skipped(self, monkeypatch):
        rows = [_FakeRow("高考 (Gaokao)", {"slug": "gaokao", "k": 1})]
        session = _FakeSession(rows)
        flag_calls = _patch_session(monkeypatch, session)

        assert asyncio.run(seed.backfill_exam_pack_slugs()) == 0
        assert session.commits == 0
        assert flag_calls == []
        assert rows[0].metadata_ == {"slug": "gaokao", "k": 1}
