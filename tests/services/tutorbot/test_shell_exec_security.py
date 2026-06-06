"""TutorBot shell execution security defaults."""

from __future__ import annotations

import asyncio
from pathlib import Path
from types import SimpleNamespace

import pytest

from deeptutor.services.tutorbot.manager import BotConfig, TutorBotManager


@pytest.fixture
def manager(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> TutorBotManager:
    path_service = SimpleNamespace(
        project_root=tmp_path,
        workspace_root=tmp_path,
        get_memory_dir=lambda: tmp_path / "memory",
    )
    monkeypatch.setattr(
        "deeptutor.services.tutorbot.manager.get_path_service",
        lambda: path_service,
    )
    return TutorBotManager()


def _patch_start_bot_dependencies(
    monkeypatch: pytest.MonkeyPatch,
    captured: dict[str, object],
) -> None:
    class FakeAgentLoop:
        def __init__(self, *args, **kwargs) -> None:
            captured["exec_enabled"] = kwargs["exec_config"].enabled
            captured["restrict_to_workspace"] = kwargs.get("restrict_to_workspace")
            self.model = kwargs.get("model") or "fake-model"
            self.context_window_tokens = kwargs.get("context_window_tokens") or 65_536

        async def run(self) -> None:
            return None

        async def stop(self) -> None:
            return None

    class FakeHeartbeat:
        def __init__(self, *args, **kwargs) -> None:
            pass

        async def start(self) -> None:
            return None

        def stop(self) -> None:
            return None

    async def _done() -> None:
        return None

    monkeypatch.setattr("deeptutor.tutorbot.agent.loop.AgentLoop", FakeAgentLoop)
    monkeypatch.setattr(
        "deeptutor.tutorbot.providers.deeptutor_adapter.create_deeptutor_provider",
        lambda *_args, **_kwargs: object(),
    )
    monkeypatch.setattr(
        "deeptutor.services.tutorbot.model_runtime.resolve_tutorbot_llm_config",
        lambda _cfg: SimpleNamespace(model="selected-model", context_window=123456),
    )
    monkeypatch.setattr(
        "deeptutor.services.tutorbot.manager.TutorBotManager._build_channel_manager",
        lambda *_args, **_kwargs: None,
    )
    monkeypatch.setattr(
        "deeptutor.services.tutorbot.manager.TutorBotManager._outbound_router",
        lambda *_args, **_kwargs: _done(),
    )
    monkeypatch.setattr("deeptutor.tutorbot.heartbeat.HeartbeatService", FakeHeartbeat)


def test_bot_config_persists_shell_exec_opt_in(manager: TutorBotManager) -> None:
    cfg = BotConfig(name="bot", allow_shell_exec=True)

    manager.save_bot_config("shell-bot", cfg)

    assert manager.load_bot_config("shell-bot") == cfg


def test_shell_exec_config_uses_strict_bool_parsing(manager: TutorBotManager) -> None:
    bot_dir = manager._bot_dir("strict-bool-bot")
    bot_dir.mkdir(parents=True, exist_ok=True)
    (bot_dir / "config.yaml").write_text(
        "name: strict-bool\nallow_shell_exec: 'false'\n",
        encoding="utf-8",
    )

    cfg = manager.load_bot_config("strict-bool-bot")

    assert cfg is not None
    assert cfg.allow_shell_exec is False


def test_start_bot_disables_shell_exec_by_default(
    manager: TutorBotManager,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    captured: dict[str, object] = {}
    _patch_start_bot_dependencies(monkeypatch, captured)

    async def run_start() -> None:
        instance = await manager.start_bot("safe-default-bot", BotConfig(name="bot"))
        for task in instance.tasks:
            task.cancel()

    asyncio.run(run_start())

    assert captured["exec_enabled"] is False
    assert captured["restrict_to_workspace"] is True


def test_start_bot_shell_exec_requires_explicit_opt_in(
    manager: TutorBotManager,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    captured: dict[str, object] = {}
    _patch_start_bot_dependencies(monkeypatch, captured)

    async def run_start() -> None:
        cfg = BotConfig(name="bot", allow_shell_exec=True)
        instance = await manager.start_bot("shell-opt-in-bot", cfg)
        for task in instance.tasks:
            task.cancel()

    asyncio.run(run_start())

    assert captured["exec_enabled"] is True
    assert captured["restrict_to_workspace"] is True
