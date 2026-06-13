"""Tests for capability-based access: has_capability_access + require_llm_access.

As of the multi-user release only the LLM capability is grantable per user, so
gating is LLM-only; embedding/search are shared admin infrastructure.
"""

import asyncio

from fastapi import HTTPException
import pytest

from deeptutor.multi_user import access_guards, model_access
from deeptutor.multi_user.context import reset_current_user, set_current_user
from deeptutor.multi_user.models import CurrentUser, UserScope


def make_user(tmp_path, role="user"):
    uid = "u_admin" if role == "admin" else "u_alice"
    return CurrentUser(
        id=uid,
        username="admin" if role == "admin" else "alice",
        role=role,
        scope=UserScope(
            kind="admin" if role == "admin" else "user",
            user_id=uid,
            root=tmp_path / uid,
        ),
    )


def _fake_access(llm=None):
    """Build a redacted_model_access return value with the given llm bucket."""
    return lambda _user_id=None: {"llm": list(llm or [])}


# ── has_capability_access ────────────────────────────────────────────────


def test_admin_always_has_access(tmp_path, monkeypatch):
    # Admins are never gated and must not even consult the grant view.
    def _boom(_user_id=None):
        raise AssertionError("redacted_model_access should not be called for admins")

    monkeypatch.setattr(model_access, "redacted_model_access", _boom)
    token = set_current_user(make_user(tmp_path, role="admin"))
    try:
        assert model_access.has_capability_access("llm") is True
    finally:
        reset_current_user(token)


def test_user_with_available_model_has_access(tmp_path, monkeypatch):
    monkeypatch.setattr(
        model_access,
        "redacted_model_access",
        _fake_access(llm=[{"profile_id": "p", "model_id": "m", "available": True}]),
    )
    token = set_current_user(make_user(tmp_path, role="user"))
    try:
        assert model_access.has_capability_access("llm") is True
    finally:
        reset_current_user(token)


def test_user_with_unavailable_model_has_no_access(tmp_path, monkeypatch):
    # A granted profile that no longer resolves in the catalog is available=False.
    monkeypatch.setattr(
        model_access,
        "redacted_model_access",
        _fake_access(llm=[{"profile_id": "p", "available": False}]),
    )
    token = set_current_user(make_user(tmp_path, role="user"))
    try:
        assert model_access.has_capability_access("llm") is False
    finally:
        reset_current_user(token)


def test_user_with_empty_grant_has_no_access(tmp_path, monkeypatch):
    monkeypatch.setattr(model_access, "redacted_model_access", _fake_access())
    token = set_current_user(make_user(tmp_path, role="user"))
    try:
        assert model_access.has_capability_access("llm") is False
    finally:
        reset_current_user(token)


# ── require_llm_access guard ─────────────────────────────────────────────


def test_guard_raises_typed_403_when_missing(tmp_path, monkeypatch):
    monkeypatch.setattr(model_access, "redacted_model_access", _fake_access())
    token = set_current_user(make_user(tmp_path, role="user"))
    try:
        with pytest.raises(HTTPException) as exc:
            asyncio.run(access_guards.require_llm_access(None))
        assert exc.value.status_code == 403
        assert exc.value.detail["code"] == "NO_MODEL_ACCESS"
        assert exc.value.detail["capability"] == "llm"
    finally:
        reset_current_user(token)


def test_guard_passes_when_capability_available(tmp_path, monkeypatch):
    monkeypatch.setattr(
        model_access,
        "redacted_model_access",
        _fake_access(llm=[{"profile_id": "p", "model_id": "m", "available": True}]),
    )
    token = set_current_user(make_user(tmp_path, role="user"))
    try:
        # Should not raise.
        assert asyncio.run(access_guards.require_llm_access(None)) is None
    finally:
        reset_current_user(token)


def test_guard_passes_for_admin(tmp_path, monkeypatch):
    monkeypatch.setattr(model_access, "redacted_model_access", _fake_access())
    token = set_current_user(make_user(tmp_path, role="admin"))
    try:
        assert asyncio.run(access_guards.require_llm_access(None)) is None
    finally:
        reset_current_user(token)
