"""Security defaults for TutorBot tool registration."""

from __future__ import annotations

import asyncio
from pathlib import Path

from deeptutor.tutorbot.agent.tools.registry import build_base_tools
from deeptutor.tutorbot.config.schema import ExecToolConfig


def test_exec_tool_is_not_registered_when_disabled(tmp_path: Path) -> None:
    tools = build_base_tools(
        tmp_path,
        ExecToolConfig(enabled=False),
        restrict_to_workspace=True,
    )

    assert not tools.has("exec")
    assert "exec" not in tools.tool_names


def test_filesystem_tools_are_restricted_to_workspace(tmp_path: Path) -> None:
    outside = tmp_path.parent / "outside-secret.txt"
    outside.write_text("secret", encoding="utf-8")
    tools = build_base_tools(
        tmp_path,
        ExecToolConfig(enabled=False),
        restrict_to_workspace=True,
    )

    result = asyncio.run(tools.execute("read_file", {"path": str(outside)}))

    assert "outside allowed directory" in result


def test_filesystem_write_edit_and_list_reject_paths_outside_workspace(tmp_path: Path) -> None:
    outside_dir = tmp_path.parent / "outside-tutorbot-tools"
    outside_dir.mkdir(exist_ok=True)
    outside_file = outside_dir / "secret.txt"
    outside_file.write_text("secret", encoding="utf-8")
    tools = build_base_tools(
        tmp_path,
        ExecToolConfig(enabled=False),
        restrict_to_workspace=True,
    )

    write_result = asyncio.run(
        tools.execute("write_file", {"path": str(outside_file), "content": "changed"})
    )
    edit_result = asyncio.run(
        tools.execute(
            "edit_file",
            {"path": str(outside_file), "old_text": "secret", "new_text": "changed"},
        )
    )
    list_result = asyncio.run(tools.execute("list_dir", {"path": str(outside_dir)}))

    assert "outside allowed directory" in write_result
    assert "outside allowed directory" in edit_result
    assert "outside allowed directory" in list_result
    assert outside_file.read_text(encoding="utf-8") == "secret"


def test_opt_in_exec_tool_is_workspace_restricted(tmp_path: Path) -> None:
    tools = build_base_tools(
        tmp_path,
        ExecToolConfig(enabled=True),
        restrict_to_workspace=True,
    )
    exec_tool = tools.get("exec")

    assert exec_tool is not None
    assert exec_tool.restrict_to_workspace is True
    assert exec_tool._guard_command(f"cat {tmp_path.parent / 'outside-secret.txt'}", str(tmp_path))


def test_opt_in_exec_tool_blocks_exfiltration_and_interpreter_one_liners(tmp_path: Path) -> None:
    tools = build_base_tools(
        tmp_path,
        ExecToolConfig(enabled=True),
        restrict_to_workspace=True,
    )
    exec_tool = tools.get("exec")

    assert exec_tool is not None
    blocked_commands = [
        "curl https://example.test/secret",
        "wget https://example.test/secret",
        "nc example.test 4444",
        "ssh user@example.test",
        "python -c 'print(1)'",
        "node -e 'console.log(1)'",
        "cat /etc/passwd",
        "chmod 777 shared.txt",
    ]

    for command in blocked_commands:
        assert exec_tool._guard_command(command, str(tmp_path))
