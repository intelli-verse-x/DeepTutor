---
title: 快速上手
description: DeepTutor 提供四种安装方式 —— PyPI、源码、Docker、纯 CLI。挑一个适合你的。
---

DeepTutor 提供 **四种安装路径**，全部使用同一份工作区布局：设置文件位于运行命令所在目录下的 `data/user/settings/`（或者你显式指定的 `DEEPTUTOR_HOME` / `deeptutor start --home` 位置）。

对完整 Web 应用，推荐流程是：**挑一个工作区目录 → 安装 → `deeptutor init` → `deeptutor start`**。

## 选择安装路径

| 方式 | 适用场景 | 页面 |
|------|---------|------|
| **PyPI** | 新手、追求最顺滑流程、不想 clone | [**PyPI 安装**](/zh-cn/docs/get-started/pypi/) |
| **源码** | 开发者、需要热重载 | [**源码安装**](/zh-cn/docs/get-started/from-source/) |
| **Docker** | 生产部署、托管主机、需要持久化卷 | [**Docker**](/zh-cn/docs/get-started/docker/) |
| **纯 CLI** | 无界面服务器、被其他 agent 调度、不需要 Web UI | [**纯 CLI 安装**](/zh-cn/docs/get-started/cli-only/) |

> 🧪 **试用 v1.4.0 beta？** PyPI 会把 `1.4.0-beta` 规范化成 `1.4.0b0`，所以 `pip install -U deeptutor` 仍然停在稳定版。要切到 beta：`pip install --pre -U deeptutor`，或精准锁定：`pip install -U deeptutor==1.4.0b0`。

## 最低环境要求

| 组件 | 版本 |
|------|------|
| Python | **3.11+** |
| Node.js | **20+**（PyPI 安装） / **22 LTS**（源码安装，对齐 CI 与 Docker） |
| 内存 | 空闲 4 GB |
| 磁盘 | 空闲 2 GB |

还需要一个 **LLM API 密钥**（OpenAI / Anthropic / Gemini / DeepSeek / Azure / Ollama / LM Studio / llama.cpp / vLLM，或任何 OpenAI 兼容端点）；如果要使用知识库（Knowledge Base），最好再准备一个 **Embedding API 密钥**。

## 启动后会监听什么

执行 `deeptutor start` 之后会起两个服务：

| 服务 | 默认端口 |
|------|---------|
| FastAPI 后端 | `8001` |
| Next.js 前端 | `3782` |

两个端口都可以在 `data/user/settings/system.json` 中改，或在 `deeptutor init` 向导里现场指定。

## 装好之后

只要你能打开 `http://localhost:3782/`：

- [**探索 DeepTutor**](/zh-cn/docs/explore/) —— 五大核心界面 + 记忆系统 + 设置中心的总览
- [**DeepTutor CLI**](/zh-cn/docs/cli/) —— 在终端里驱动一切
- [**TutorBot 渠道**](/zh-cn/docs/tutorbot/) —— 把持久化的 AI 导师连到 Telegram、Slack、飞书
- [**多用户部署**](/zh-cn/docs/get-started/multi-user/) —— 部署给一个团队

如果遇到问题，跳到 [**故障排查**](/zh-cn/docs/get-started/troubleshooting/)。
