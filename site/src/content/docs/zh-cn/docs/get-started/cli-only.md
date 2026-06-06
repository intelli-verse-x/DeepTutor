---
title: 仅 CLI 安装
description: 选项 4 —— 给 headless 服务器、agent harness 以及 Claude Code / Codex / Hermes 用的轻量安装方式。
---

不需要 Web UI 时用这个。仅 CLI 的包从**源码 checkout** 安装，不走 PyPI。

## 安装

```bash
git clone https://github.com/HKUDS/DeepTutor.git
cd DeepTutor

# 创建 venv（macOS / Linux）
# Windows PowerShell：
#   py -3.11 -m venv .venv-cli ; .\.venv-cli\Scripts\Activate.ps1
python3 -m venv .venv-cli && source .venv-cli/bin/activate
python -m pip install --upgrade pip

python -m pip install -e ./packaging/deeptutor-cli
deeptutor init --cli
deeptutor chat
```

`deeptutor init --cli` 和完整版应用共享同一份 `data/user/settings/` 目录结构，但是：

- **跳过**后端 / 前端端口的询问
- **embeddings 默认关闭**（如果打算用 `deeptutor kb …` 或 RAG 工具，选 `Yes`）
- 仍然会写完整的运行时布局（`system.json`、`auth.json`、`integrations.json`、`model_catalog.json`、`main.yaml`、`agents.yaml`）
- 仍然会询问当前激活的 LLM 提供商和模型

## 什么场景用它

- 把 DeepTutor 当作工具，挂在另一个 agent 的 harness 里跑（Claude Code、Codex、OpenCode 等）
- 没有浏览器的 headless 服务器 / VM
- 想要不带 Node.js toolchain 的快速安装

## 常用命令

```bash
deeptutor chat                                          # 交互式 REPL
deeptutor chat --capability deep_solve --tool rag --kb my-kb
deeptutor run chat "解释一下傅里叶变换"
deeptutor run deep_solve "解 x^2 = 4" --tool rag --kb my-kb
deeptutor kb create my-kb --doc textbook.pdf
deeptutor memory show
deeptutor config show
```

完整命令面：[**DeepTutor CLI**](/zh-cn/docs/cli/)。

## 哪些能用、哪些不能

本地 `deeptutor-cli` 安装**不含任何 Web 资源或服务器依赖**。保留源码 checkout —— editable 安装是指向它的。

| 功能 | 仅 CLI | 完整安装 |
|------|--------|----------|
| `deeptutor chat` 交互式 REPL | ✅ | ✅ |
| `deeptutor run` capabilities | ✅ | ✅ |
| `deeptutor kb`（知识库） | ✅ *（init 时选择启用）* | ✅ |
| `deeptutor notebook` | ✅ | ✅ |
| `deeptutor memory` | ✅ | ✅ |
| `deeptutor bot`（TutorBot） | ✅ *（装了 `[tutorbot]` extra 时）* | ✅ |
| `deeptutor config show` | ✅ | ✅ |
| `deeptutor provider login` | ✅ | ✅ |
| `deeptutor serve`（FastAPI） | ❌ | ✅ |
| `deeptutor start`（Web UI） | ❌ | ✅ |
| Co-Writer UI | ❌ | ✅ |
| Memory Workbench UI | ❌ | ✅ |
| Book Engine UI | ❌ | ✅ |

后续要加 Web 应用，装 PyPI 包（选项 1），然后在同一工作区跑 `deeptutor init` + `deeptutor start`。

## 让另一个 agent 来调用

CLI 是 **agent-native** 的。`deeptutor run --format json` 每行输出一个 JSON 事件，`kb list`、`kb search`、`session show`、`notebook show` 等数据查询命令在已实现的地方都暴露 JSON —— 方便接到另一个 agent 的 harness 里。

把项目根目录的 [`SKILL.md`](https://github.com/HKUDS/DeepTutor/blob/main/SKILL.md) 丢给任何会调工具的 LLM，它就能自己驱动 DeepTutor。具体模式见 [**Agent handoff**](/zh-cn/docs/cli/agent-handoff/)。

## 升级

```bash
cd DeepTutor
git pull
pip install -e ./packaging/deeptutor-cli --upgrade
```

## 常见错误

### 装完之后 `deeptutor: command not found`

console script 没装到 PATH 上。确认 venv 已激活，或直接调用：

```bash
python -m deeptutor_cli.main chat
```

### 跑 `deeptutor serve` 时报 `ModuleNotFoundError: No module named 'fastapi'`

`deeptutor serve` 在仅 CLI 安装里**不可用**。请用 [**PyPI**](/zh-cn/docs/get-started/pypi/) 或 [**从源码安装**](/zh-cn/docs/get-started/from-source/)。

### TutorBot 命令提示 SDK 缺失

Channel SDKs（python-telegram-bot、slack-sdk 等）只在 `[tutorbot]` extra 里：

```bash
pip install -e "./packaging/deeptutor-cli[tutorbot]"
```

更多：[**故障排查**](/zh-cn/docs/get-started/troubleshooting/)。

## 下一步

- [**DeepTutor CLI**](/zh-cn/docs/cli/) —— 完整 CLI 参考
- [**Agent handoff**](/zh-cn/docs/cli/agent-handoff/) —— 让你的 agent 来驱动
- [**探索 TutorBot**](/zh-cn/docs/tutorbot/) —— 从 CLI 跑一个 bot
