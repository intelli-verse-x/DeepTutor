"""Regression tests for TutorBot-compatible plugin capability streaming."""

from __future__ import annotations

import importlib
import json
import re
from typing import Any

import pytest

try:
    from fastapi import FastAPI
    from fastapi.testclient import TestClient
except Exception:  # pragma: no cover
    FastAPI = None
    TestClient = None

pytestmark = pytest.mark.skipif(
    FastAPI is None or TestClient is None, reason="fastapi not installed"
)


def _events(text: str) -> list[tuple[str, dict[str, Any]]]:
    events: list[tuple[str, dict[str, Any]]] = []
    for block in text.strip().split("\n\n"):
        event = ""
        data = "{}"
        for line in block.splitlines():
            if line.startswith("event: "):
                event = line[len("event: ") :]
            elif line.startswith("data: "):
                data = line[len("data: ") :]
        if event:
            events.append((event, json.loads(data)))
    return events


def _client_with_fake_tutorbot(monkeypatch):
    from deeptutor.services.tutorbot.manager import BotConfig

    class FakeInstance:
        running = True

    class FakeMgr:
        def __init__(self):
            self.calls: list[dict[str, Any]] = []

        def get_bot(self, bot_id: str):
            return FakeInstance()

        def load_bot_config(self, bot_id: str):
            return BotConfig(name=bot_id)

        async def start_bot(self, bot_id: str, config: BotConfig):
            return FakeInstance()

        async def send_message(self, bot_id: str, content: str, **kwargs):
            self.calls.append({"bot_id": bot_id, "content": content, **kwargs})
            on_progress = kwargs.get("on_progress")
            if on_progress:
                await on_progress("thinking")
            return "streamed answer"

    mgr = FakeMgr()
    tutorbot_router_mod = importlib.import_module("deeptutor.api.routers.tutorbot")
    plugins_router_mod = importlib.import_module("deeptutor.api.routers.plugins_api")
    monkeypatch.setattr(tutorbot_router_mod, "get_tutorbot_manager", lambda: mgr)
    tutorbot_router_mod._start_locks.clear()

    app = FastAPI()
    app.include_router(plugins_router_mod.router, prefix="/api/v1/plugins")
    return TestClient(app), mgr


def test_plugin_chat_stream_routes_to_specified_tutorbot_session(monkeypatch):
    client, mgr = _client_with_fake_tutorbot(monkeypatch)

    response = client.post(
        "/api/v1/plugins/capabilities/chat/execute-stream",
        json={
            "content": "hi",
            "bot_id": "math-bot",
            "session_id": "lesson-1",
            "enabledTools": [],
            "knowledgeBases": [],
            "language": "zh",
            "llmSelection": {"profile_id": "p-alt", "model_id": "m-alt"},
        },
    )

    assert response.status_code == 200
    events = _events(response.text)
    assert ("session", {"bot_id": "math-bot", "session_id": "lesson-1"}) in events
    assert ("thinking", {"content": "thinking"}) in events
    assert ("content", {"content": "streamed answer"}) in events
    assert ("done", {"bot_id": "math-bot", "session_id": "lesson-1"}) in events
    assert len(mgr.calls) == 1
    call = mgr.calls[0]
    assert call["bot_id"] == "math-bot"
    assert call["content"] == "hi"
    assert call["chat_id"] == "lesson-1"
    assert call["session_id"] == "lesson-1"
    assert callable(call["on_progress"])


def test_plugin_chat_stream_creates_session_when_missing(monkeypatch):
    client, mgr = _client_with_fake_tutorbot(monkeypatch)

    response = client.post(
        "/api/v1/plugins/capabilities/chat/execute-stream",
        json={"content": "first message", "bot_id": "math-bot"},
    )

    assert response.status_code == 200
    assert "event: done" in response.text
    match = re.search(r'"session_id": "([^"]+)"', response.text)
    assert match is not None
    session_id = match.group(1)
    assert session_id != "web"
    assert mgr.calls[0]["session_id"] == session_id
    assert mgr.calls[0]["chat_id"] == session_id
