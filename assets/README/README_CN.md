<div align="center">

<p align="center"><img src="../../assets/figs/logo/logo.png" alt="DeepTutor logo" height="56" style="vertical-align: middle;">&nbsp;<img src="../../assets/figs/logo/banner.png" alt="DeepTutor" height="48" style="vertical-align: middle;"></p>

# DeepTutor：智能体原生的个性化辅导

<p align="center">
  <a href="https://deeptutor.info" target="_blank"><img alt="Docs — deeptutor.info" src="https://img.shields.io/badge/Docs-deeptutor.info%20%E2%86%97-0A0A0A?style=for-the-badge&labelColor=F5F5F4" height="36"></a>
</p>

<a href="https://trendshift.io/repositories/17099" target="_blank"><img src="https://trendshift.io/api/badge/repositories/17099" alt="HKUDS%2FDeepTutor | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>

<p align="center">
  <a href="../../README.md"><img alt="English" height="40" src="https://img.shields.io/badge/English-CDCFD4"></a>&nbsp;
  <a href="README_CN.md"><img alt="简体中文" height="40" src="https://img.shields.io/badge/简体中文-BCDCF7"></a>&nbsp;
  <a href="README_JA.md"><img alt="日本語" height="40" src="https://img.shields.io/badge/日本語-CDCFD4"></a>&nbsp;
  <a href="README_ES.md"><img alt="Español" height="40" src="https://img.shields.io/badge/Español-CDCFD4"></a>&nbsp;
  <a href="README_FR.md"><img alt="Français" height="40" src="https://img.shields.io/badge/Français-CDCFD4"></a>&nbsp;
  <a href="README_AR.md"><img alt="Arabic" height="40" src="https://img.shields.io/badge/Arabic-CDCFD4"></a>&nbsp;
  <a href="README_RU.md"><img alt="Русский" height="40" src="https://img.shields.io/badge/Русский-CDCFD4"></a>&nbsp;
  <a href="README_HI.md"><img alt="Hindi" height="40" src="https://img.shields.io/badge/Hindi-CDCFD4"></a>&nbsp;
  <a href="README_PT.md"><img alt="Português" height="40" src="https://img.shields.io/badge/Português-CDCFD4"></a>&nbsp;
  <a href="README_TH.md"><img alt="Thai" height="40" src="https://img.shields.io/badge/Thai-CDCFD4"></a>&nbsp;
  <a href="README_PL.md"><img alt="Polski" height="40" src="https://img.shields.io/badge/Polski-CDCFD4"></a>
</p>

[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![Next.js 16](https://img.shields.io/badge/Next.js-16-000000?style=flat-square&logo=next.js&logoColor=white)](https://nextjs.org/)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue?style=flat-square)](../../LICENSE)
[![GitHub release](https://img.shields.io/github/v/release/HKUDS/DeepTutor?style=flat-square&color=brightgreen)](https://github.com/HKUDS/DeepTutor/releases)
[![arXiv](https://img.shields.io/badge/arXiv-2604.26962-b31b1b?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2604.26962)

[![Discord](https://img.shields.io/badge/Discord-Community-5865F2?style=flat-square&logo=discord&logoColor=white)](https://discord.gg/eRsjPgMU4t)
[![Feishu](https://img.shields.io/badge/Feishu-Group-00D4AA?style=flat-square&logo=feishu&logoColor=white)](../../Communication.md)
[![WeChat](https://img.shields.io/badge/WeChat-Group-07C160?style=flat-square&logo=wechat&logoColor=white)](https://github.com/HKUDS/DeepTutor/issues/78)

[核心亮点](#-核心亮点) · [快速开始](#-快速开始) · [探索 DeepTutor](#-探索-deeptutor) · [CLI](#️-deeptutor-cli--智能体原生接口) · [多用户](#-多用户--共享部署) · [社区](#-社区与生态)

</div>

---

> 🤝 **欢迎各种形式的贡献！** 在 [`Roadmap`](https://github.com/HKUDS/DeepTutor/issues/498) 为路线图条目投票或提出新想法，分支策略、编码规范与上手方式见 [贡献指南](../../CONTRIBUTING.md)。

### 📦 版本发布

> **[2026.6.12]** [v1.4.3](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.3) — TutorBot 升级为 **Partners**，基于生产级 IM 流水线，支持实时流式回复与 15 个频道；Chat 迁移至单智能体循环；多用户部署实现真正的按用户隔离；Visualize 重建并加入本地校验与修复；Co-Writer、文件查看器、MinerU 云端解析及 CLI 全面升级。官方文档已在 [deeptutor.info](https://deeptutor.info/) 全面焕新。

> **[2026.5.28]** [v1.4.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.2) — v1.4.1 稳定性与打磨版：Gemini 2.5+ 在 Visualize 和 Chat 中解除阻塞，ContextVar 认证路由修复(#485)，推理与原生工具标签协议加固，所有聊天界面流式输出更顺滑，新增可折叠的最近记录侧边栏，以及 Lemonade 本地提供商支持。

> **[2026.5.27]** [v1.4.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.1) — 安全与稳定性补丁：TutorBot 工具沙箱加固、按用户资源隔离、视觉能力提供商的多模态图片回退、TutorBot 的 HTTP/SSE API，以及 v1.4.0 聊天回归修复。

> **[2026.5.22]** [v1.4.0](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.0) — v1.4 正式版：Auto Mode、三层 Memory、智能体化的 Deep Research / Solve / Question、LlamaIndex RAG 重构、Visualize/Animator 合并，以及推理力度归一化、工具 schema 回退与重启安全的回合运行时。

<details>
<summary><b>更早发布（两周以前）</b></summary>

> **[2026.5.21]** [v1.4.0-beta](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.0-beta) — 三层 Memory 工作台(L1/L2/L3)、所有聊天能力基于单一智能体引擎重建、RAG 全面切换至 LlamaIndex，以及统一的 Settings + Capabilities 入口。

> **[2026.5.10]** [v1.3.10](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.10) — 修复远程 Docker CORS、SDK Provider 的 `DISABLE_SSL_VERIFY`、更安全的代码块引用，并将 Matrix E2EE 改为可选扩展。

> **[2026.5.9]** [v1.3.9](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.9) — TutorBot 支持 Zulip 与 NVIDIA NIM，思考模型路由更安全，新增 `deeptutor start`、侧栏提示与会话存储一致性提升。

> **[2026.5.8]** [v1.3.8](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.8) — 可选多用户部署，具备隔离的用户工作区、管理员授权、认证路由与作用域运行时访问。

> **[2026.5.4]** [v1.3.7](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.7) — 思考模型/提供商修复，知识索引历史可见，Co-Writer 清空与模板编辑更安全。

> **[2026.5.3]** [v1.3.6](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.6) — 聊天与 TutorBot 基于目录的模型选择，更安全的 RAG 重建索引，OpenAI Responses token 上限修复，Skills 编辑器校验。

> **[2026.5.2]** [v1.3.5](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.5) — 本地启动设置更顺滑、RAG 查询更安全、本地嵌入鉴权更清晰，Settings 深色模式打磨。

> **[2026.5.1]** [v1.3.4](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.4) — Book 页对话持久化与重建流程、聊天到 Book 引用、更强的语言/推理处理、RAG 文档抽取加固。

> **[2026.4.30]** [v1.3.3](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.3) — NVIDIA NIM 与 Gemini 嵌入支持，统一 Space 上下文（聊天历史/技能/记忆），会话快照，RAG 重建索引韧性。

> **[2026.4.29]** [v1.3.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.2) — 嵌入端点 URL 透明可读，无效持久化向量时 RAG 重建索引韧性，思考模型输出记忆清理，Deep Solve 运行时修复。

> **[2026.4.28]** [v1.3.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.1) — 稳定性：更安全的 RAG 路由与嵌入校验、Docker 持久化、输入法友好输入、Windows/GBK 健壮性。

> **[2026.4.27]** [v1.3.0](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.0) — 版本化 KB 索引与重建工作流、Knowledge 工作区重构、嵌入自动发现与新适配器、Space 中心。

> **[2026.4.25]** [v1.2.5](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.5) — 聊天附件持久化与文件预览抽屉，感知附件的能力流水线，TutorBot Markdown 导出。

> **[2026.4.25]** [v1.2.4](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.4) — 文本/代码/SVG 附件、一键 Setup Tour、Markdown 聊天导出、紧凑 KB 管理界面。

> **[2026.4.24]** [v1.2.3](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.3) — 文档附件（PDF/DOCX/XLSX/PPTX）、推理思维块展示、Soul 模板编辑器、Co-Writer 保存至笔记本。

> **[2026.4.22]** [v1.2.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.2) — 用户自建 Skills 体系、聊天输入性能重构、TutorBot 自动启动、Book Library UI、可视化全屏。

> **[2026.4.21]** [v1.2.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.1) — 分阶段 token 上限、各入口重新生成回复、RAG 与 Gemma 兼容性修复。

> **[2026.4.20]** [v1.2.0](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.0) — Book Engine「活书」编译器、多文档 Co-Writer、交互式 HTML 可视化、题库 @ 提及。

> **[2026.4.18]** [v1.1.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.1.2) — 基于 Schema 的 Channels 标签页、RAG 单一流水线收敛、聊天提示词外置。

> **[2026.4.17]** [v1.1.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.1.1) — 通用「立即回答」、Co-Writer 滚动同步、统一设置面板、流式停止按钮。

> **[2026.4.15]** [v1.1.0](https://github.com/HKUDS/DeepTutor/releases/tag/v1.1.0) — LaTeX 块级公式重构、LLM 诊断探测、Docker 与本地 LLM 说明。

> **[2026.4.14]** [v1.1.0-beta](https://github.com/HKUDS/DeepTutor/releases/tag/v1.1.0-beta) — 可收藏会话、Snow 主题、WebSocket 心跳与自动重连、嵌入注册表重构。

> **[2026.4.13]** [v1.0.3](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.3) — 题目笔记本（书签与分类）、Visualize 支持 Mermaid、嵌入不匹配检测、Qwen/vLLM 兼容、LM Studio 与 llama.cpp，以及 Glass 主题。

> **[2026.4.11]** [v1.0.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.2) — 搜索整合与 SearXNG 回退、提供商切换修复、前端资源泄漏修复。

> **[2026.4.10]** [v1.0.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.1) — Visualize 能力（Chart.js/SVG）、测验去重、o4-mini 模型支持。

> **[2026.4.10]** [v1.0.0-beta.4](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.0-beta.4) — 嵌入进度跟踪与限流重试、跨平台依赖修复、MIME 校验修复。

> **[2026.4.8]** [v1.0.0-beta.3](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.0-beta.3) — 原生 OpenAI/Anthropic SDK（移除 litellm）、Windows 数学动画、健壮 JSON 解析、完整中文 i18n。

> **[2026.4.7]** [v1.0.0-beta.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.0-beta.2) — 设置热重载、MinerU 嵌套输出、WebSocket 修复、最低 Python 3.11+。

> **[2026.4.4]** [v1.0.0-beta.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.0-beta.1) — 智能体原生架构重写（约 20 万行）：Tools + Capabilities 插件模型、CLI 与 SDK、TutorBot、Co-Writer、引导学习与持久记忆。

> **[2026.1.23]** [v0.6.0](https://github.com/HKUDS/DeepTutor/releases/tag/v0.6.0) — 会话持久化、文档增量上传、灵活 RAG 流水线导入、完整中文本地化。

> **[2026.1.18]** [v0.5.2](https://github.com/HKUDS/DeepTutor/releases/tag/v0.5.2) — RAG-Anything 支持 Docling、日志系统优化与缺陷修复。

> **[2026.1.15]** [v0.5.0](https://github.com/HKUDS/DeepTutor/releases/tag/v0.5.0) — 统一服务配置、按知识库选择 RAG 流水线、出题改版，以及侧栏定制。

> **[2026.1.9]** [v0.4.0](https://github.com/HKUDS/DeepTutor/releases/tag/v0.4.0) — 多提供商 LLM 与嵌入支持、新首页、RAG 模块解耦、环境变量重构。

> **[2026.1.5]** [v0.3.0](https://github.com/HKUDS/DeepTutor/releases/tag/v0.3.0) — 统一 PromptManager 架构、GitHub Actions CI/CD、GHCR 预构建 Docker 镜像。

> **[2026.1.2]** [v0.2.0](https://github.com/HKUDS/DeepTutor/releases/tag/v0.2.0) — Docker 部署、Next.js 16 与 React 19 升级、WebSocket 安全加固、关键漏洞修复。

</details>

### 📰 动态

> **[2026.5.22]** 🌐 官方文档站已在 [**deeptutor.info**](https://deeptutor.info/) 上线 —— 指南、参考文档与功能演示一站收录。

> **[2026.4.19]** 🎉 111 天内突破 20k star！感谢一路以来的支持 —— 我们将持续迭代，致力于为每个人打造真正个性化的智能辅导。

> **[2026.4.10]** 📄 论文已在 arXiv 上线！阅读[预印本](https://arxiv.org/abs/2604.26962)了解 DeepTutor 背后的设计与理念。

> **[2026.4.4]** 好久不见！✨ DeepTutor v1.0.0 终于上线 —— 智能体原生演进，基于 Apache-2.0 许可证完成自下而上的架构重写，带来 TutorBot 与灵活的模式切换。新篇章已经开启，故事仍在继续！

> **[2026.2.6]** 🚀 39 天内突破 10k star！衷心感谢社区的支持！

> **[2026.1.1]** 新年快乐！欢迎加入 [Discord](https://discord.gg/eRsjPgMU4t)、[微信](https://github.com/HKUDS/DeepTutor/issues/78) 或 [Discussions](https://github.com/HKUDS/DeepTutor/discussions)，一起塑造 DeepTutor 的未来！

> **[2025.12.29]** DeepTutor 正式发布！

## ✨ 核心亮点

DeepTutor 围绕智能体原生运行时构建：共享的 ChatOrchestrator 将每个回合路由至各项能力，ToolRegistry 在模型需要时暴露单次调用工具，CapabilityRegistry 在任务需要结构化时让更深层的工作流接管回合。

<div align="center">
<img src="../../assets/figs/system/system%20architecture.png" alt="DeepTutor 系统架构" width="900">
</div>

**统一的学习工作区**

- **Chat 作为默认循环** —— 日常辅导、基于来源的问答、Deep Solve、Deep Question、Deep Research、Visualize 和 Auto Mode 全部共享同一会话上下文与来源库。
- **保持连接的学习界面** —— Co-Writer 草稿、Book 页面、Knowledge Bases、Space 资源与 Memory 是独立的工作区，但它们共同为同一个智能体运行时提供输入，而非变成各自孤立的应用。
- **Partners 提供持续陪伴** —— IM 接入的伴侣现在与主产品运行在同一个聊天智能体循环上，拥有各自的合成工作区与指定资料库。

**工具、记忆与控制**

- **可组合的工具** —— RAG、来源阅读、记忆读写、笔记本、URL 抓取、GitHub 查询、ask-user 暂停、沙箱执行，以及可选的头脑风暴/网络/论文/推理工具，均可按上下文与设置挂载。
- **三层 Memory** —— L1 轨迹、L2 按工作面整理的摘要、L3 跨工作面综合，让个性化变得可审查，而不是隐藏在黑盒之后。
- **统一 Settings 与 CLI** —— 模型目录、嵌入、搜索、网络、MCP 服务器、工具、能力与部署设置均可在 Web UI 中编辑，并可通过 `deeptutor` 脚本化操作。

---

## 🚀 快速开始

DeepTutor 提供四条安装路径。所有方式共享同一份工作区布局：设置保存在启动目录下的 `data/user/settings/`（或当你显式指定时位于 `DEEPTUTOR_HOME` / `deeptutor start --home` 所指目录）。对于完整应用，推荐流程为 **选择工作区目录 → 安装 → `deeptutor init` → `deeptutor start`**。

> ✨ **v1.4.3 已上线。** `pip install -U deeptutor` 即可获取最新稳定版。如需预发布版本（可用时），使用 `pip install --pre -U deeptutor`。

### 方案 1 —— 从 PyPI 安装

完整本地 Web 应用 + CLI，无需克隆仓库。需要 **Python 3.11+** 以及 PATH 中的 **Node.js 20+** 运行时（打包好的 Next.js 独立服务器由 `deeptutor start` 启动）。

```bash
mkdir -p my-deeptutor && cd my-deeptutor
pip install -U deeptutor
deeptutor init     # 提示配置端口 + LLM 提供商 + 可选嵌入
deeptutor start    # 启动后端 + 前端；保持终端窗口打开
```

`deeptutor init` 会询问后端端口（默认 `8001`）、前端端口（默认 `3782`）、LLM 提供商 / Base URL / API Key / 模型，以及用于 Knowledge Base / RAG 的可选嵌入提供商。

`deeptutor start` 完成后，打开终端中输出的前端 URL —— 默认为 [http://127.0.0.1:3782](http://127.0.0.1:3782)。在该终端按 `Ctrl+C` 即可同时停止后端与前端。如需快速试用可跳过 `deeptutor init`；应用会以默认端口与空模型设置启动，之后在 **Settings → Models** 中配置即可。

### 方案 2 —— 从源码安装

适用于基于代码检出进行开发。请使用 **Python 3.11+** 与 **Node.js 22 LTS**，以贴近 CI 与 Docker 环境。

```bash
git clone https://github.com/HKUDS/DeepTutor.git
cd DeepTutor

# 创建 venv（macOS/Linux）。Windows PowerShell：
#   py -3.11 -m venv .venv ; .\.venv\Scripts\Activate.ps1
python3 -m venv .venv && source .venv/bin/activate
python -m pip install --upgrade pip

# 安装后端 + 前端依赖
python -m pip install -e .
( cd web && npm ci --legacy-peer-deps )

deeptutor init
deeptutor start
```

源码安装会以开发模式针对本地 `web/` 目录运行 Next.js；其余所有配置（布局、端口、`Ctrl+C` 停止）与方案 1 一致。

<details>
<summary><b>Conda 环境</b>（替代 <code>venv</code>）</summary>

```bash
conda create -n deeptutor python=3.11
conda activate deeptutor
python -m pip install --upgrade pip
```

</details>

<details>
<summary><b>可选安装扩展</b> —— dev / partners / matrix / math-animator</summary>

```bash
pip install -e ".[dev]"             # 测试/lint 工具
pip install -e ".[partners]"        # Partner IM 频道 SDK + MCP 客户端
pip install -e ".[matrix]"          # Matrix 频道（不含 E2EE/libolm）
pip install -e ".[matrix-e2e]"      # Matrix E2EE；需要 libolm
pip install -e ".[math-animator]"   # Manim 扩展；需要 LaTeX/ffmpeg/系统库
```

</details>

<details>
<summary><b>前端依赖调整与开发服务器排障</b></summary>

**修改前端依赖：** 运行 `npm install --legacy-peer-deps` 刷新 `web/package-lock.json`，然后同时提交 `web/package.json` 与 `web/package-lock.json`。

**开发服务器卡死：** 如果 `deeptutor start` 报告已有但无响应的前端，请停掉提示中打印的 PID。若没有正在运行的 Next.js 进程，锁文件可能是残留的 —— 删除后重试：

```bash
rm -f web/.next/dev/lock web/.next/lock
deeptutor start
```

</details>

### 方案 3 —— Docker

一个容器运行完整 Web 应用。镜像发布在 GitHub Container Registry：

- `ghcr.io/hkuds/deeptutor:latest` —— 稳定版本
- `ghcr.io/hkuds/deeptutor:pre` —— 预发布版本（若可用）

```bash
docker run --rm --name deeptutor \
  -p 127.0.0.1:3782:3782 \
  -p 127.0.0.1:8001:8001 \
  -v deeptutor-data:/app/data \
  ghcr.io/hkuds/deeptutor:latest
```

> ⚠️ **必须同时映射 `3782` 和 `8001`。** `3782` 提供 Web UI；`8001` 是浏览器直接调用的 FastAPI 后端 —— 容器内没有反向代理。不映射 `8001` 则页面可以加载，但 **Settings** 会显示「Backend unreachable」并无法使用。

打开 [http://127.0.0.1:3782](http://127.0.0.1:3782)。容器首次启动时会创建 `/app/data/user/settings/*.json`；在 Web Settings 页面配置模型提供商即可。配置、API Key、日志、工作区文件、记忆与知识库均持久化在 `deeptutor-data` 卷中。

- **不同宿主端口：** 修改每个 `-p 宿主:容器` 映射的左侧（例如 `-p 127.0.0.1:8088:3782`）。如果你在 `/app/data/user/settings/system.json` 中修改了容器侧端口，请重启并相应调整每个映射的右侧。
- **后台运行：** 加上 `-d`，然后用 `docker logs -f deeptutor` 跟踪日志，`docker stop deeptutor` 停止，重用名称前先 `docker rm deeptutor`。`deeptutor-data` 卷会跨重启保留你的设置与工作区。

**远程 Docker / 反向代理：** Web UI 在浏览器中运行，因此浏览器需要能访问的后端 URL。对于远程服务器，打开 **Settings -> Network** 或编辑 `data/user/settings/system.json`：

```json
{
  "next_public_api_base_external": "https://deeptutor.example.com"
}
```

`public_api_base` 作为兼容别名受支持，保存时会被规范化为 `next_public_api_base_external`。CORS 使用前端**来源**，而非 API URL。未启用认证时，DeepTutor 默认允许普通的 HTTP/HTTPS 浏览器来源。启用认证后，请添加精确的前端来源：

```json
{
  "cors_origins": ["https://deeptutor.example.com"]
}
```

<details>
<summary><b>连接到宿主机上的 Ollama / LM Studio / llama.cpp / vLLM / Lemonade</b></summary>

在 Docker 内部，`localhost` 指向容器自身，不是宿主机。要访问宿主机上运行的模型服务，使用宿主机网关（推荐）：

```bash
docker run --rm --name deeptutor \
  -p 127.0.0.1:3782:3782 -p 127.0.0.1:8001:8001 \
  --add-host=host.docker.internal:host-gateway \
  -v deeptutor-data:/app/data \
  ghcr.io/hkuds/deeptutor:latest
```

然后在 **Settings → Models** 中，将提供商 Base URL 指向 `host.docker.internal`：

- Ollama LLM：`http://host.docker.internal:11434/v1`
- Ollama 嵌入：`http://host.docker.internal:11434/api/embed`
- LM Studio：`http://host.docker.internal:1234/v1`
- llama.cpp：`http://host.docker.internal:8080/v1`
- Lemonade：`http://host.docker.internal:13305/api/v1`

Docker Desktop（macOS/Windows）通常无需 `--add-host` 即可解析 `host.docker.internal`。在 Linux 上，该标志是在现代 Docker Engine 上创建该主机名的可移植方式。

**Linux 替代方案 —— host networking：** 添加 `--network=host` 并去掉 `-p` 标志。容器直接共享宿主网络，访问 [http://127.0.0.1:3782](http://127.0.0.1:3782)（或 `system.json` 中的 `frontend_port`），宿主服务可通过普通 localhost URL 访问，例如 `http://127.0.0.1:11434/v1`。注意 host networking 会将容器端口直接暴露在宿主上，可能与已有服务冲突。

</details>

### 代码执行沙箱（office 技能）

内置的 office 技能 —— **docx / pdf / pptx / xlsx** —— 的工作方式是让模型编写一小段 Python 脚本（`python-docx`、`reportlab`、`openpyxl` 等），通过 `exec` / `code_execution` 工具运行，然后返回下载 URL。这些工具在沙箱后端激活时挂载，而在各种部署形态下**默认激活**：

- **本地（方案 1 / 2）与 Docker（方案 3，单容器）：** 受限的子进程沙箱运行模型代码（本地在宿主机上，Docker 在容器内 —— 容器本身即隔离边界）。
- **docker-compose：** 通过 `DEEPTUTOR_SANDBOX_RUNNER_URL` 路由到硬化的、最小权限的 **runner 侧车**（`Dockerfile.runner`） —— 最强安全态势，且在存在时自动优先使用。

子进程沙箱由 `data/user/settings/system.json` 中的 `sandbox_allow_subprocess` 设置控制（默认 `true`）。在宿主机上运行模型生成的代码是一个真实的信任决策 —— 将其设为 `false`（或导出 `DEEPTUTOR_SANDBOX_ALLOW_SUBPROCESS=0`）可禁用宿主侧执行，代价是 office 技能将无法生成文件。

### 方案 4 —— 仅 CLI

不需要 Web UI 时使用。CLI 专用包从源码检出安装，不从 PyPI 安装。

```bash
git clone https://github.com/HKUDS/DeepTutor.git
cd DeepTutor

# 创建 venv（macOS/Linux）。Windows PowerShell：
#   py -3.11 -m venv .venv-cli ; .\.venv-cli\Scripts\Activate.ps1
python3 -m venv .venv-cli && source .venv-cli/bin/activate
python -m pip install --upgrade pip

python -m pip install -e ./packaging/deeptutor-cli
deeptutor init --cli
deeptutor chat
```

`deeptutor init --cli` 与完整应用共享相同的 `data/user/settings/` 布局，但跳过后端/前端端口提示，并默认将嵌入设为**关闭**（如计划使用 `deeptutor kb …` 或 RAG 工具，请选择 `Yes`）。它仍会写入完整的运行时布局（`system.json`、`auth.json`、`integrations.json`、`model_catalog.json`、`main.yaml`、`agents.yaml`），并仍会询问激活的 LLM 提供商与模型。

<details>
<summary><b>常用命令</b></summary>

```bash
deeptutor chat                                          # 交互式 REPL
deeptutor chat --capability deep_solve --tool rag --kb my-kb
deeptutor run chat "Explain Fourier transform"
deeptutor run deep_solve "Solve x^2 = 4" --tool rag --kb my-kb
deeptutor kb create my-kb --doc textbook.pdf
deeptutor memory show
deeptutor config show
```

</details>

本地 `deeptutor-cli` 安装不包含 Web 资源或服务器依赖。请保留源码检出目录 —— 可编辑安装指向它。如需之后添加 Web 应用，可安装 PyPI 包（方案 1），并在同一工作区运行 `deeptutor init` + `deeptutor start`。

### 配置参考

<details>
<summary><b><code>data/user/settings/</code> 下的配置文件</b> —— JSON/YAML 参考</summary>

`data/user/settings/` 下的所有内容均为普通 JSON/YAML。推荐使用浏览器中的 **Settings** 页面编辑。

| 文件 | 用途 |
|:---|:---|
| `model_catalog.json` | LLM、嵌入与搜索提供商档案；API Key；激活模型 |
| `system.json` | 后端/前端端口、公共 API base、CORS、SSL 校验、附件目录 |
| `auth.json` | 可选认证开关、用户名、密码哈希、token/cookie 设置 |
| `integrations.json` | 可选的 PocketBase 与侧车集成设置 |
| `interface.json` | UI 语言/主题/侧栏偏好 |
| `main.yaml` | 运行时行为默认值与路径注入 |
| `agents.yaml` | 能力/工具的 temperature 与 token 设置 |

项目根目录的 `.env` **不**作为应用配置文件读取。最简模型配置：打开 **Settings → Models**，添加一个 LLM 档案（Base URL / API Key / 模型名），保存即可。仅在计划使用 Knowledge Base / RAG 功能时再添加嵌入档案。

</details>

## 📖 探索 DeepTutor

README 的功能介绍按你最常接触的产品界面顺序展开：Chat、Partner、Co-Writer、Book、Knowledge、Space、Memory 与 Settings。以下截图均来自重新整理后的 `assets/figs` 目录树；旧版归档图片不在此使用。

### 💬 Chat —— 你真正在用的智能体循环

<div align="center">
<img src="../../assets/figs/webui/chat.png" alt="DeepTutor 聊天工作区" width="900">
</div>

Chat 是默认能力，也是大多数工作的起点。一个线程可以正常对话、调用工具、基于选定的知识库检索、读取附件、写入笔记本记录，并在回合间维护同一份来源库。

<div align="center">
<img src="../../assets/figs/system/chat-agent-loop.png" alt="DeepTutor 聊天智能体循环" width="900">
</div>

当前循环刻意保持简洁：模型按轮次思考，在有用时调用工具，观察工具结果，在获得足够证据后结束。用户可切换的工具为 `brainstorm`、`web_search`、`paper_search` 和 `reason`；上下文工具如 `rag`、`read_source`、`read_memory`、`write_memory`、`read_skill`、`load_tools`、`exec`、`web_fetch`、`ask_user`、`list_notebook`、`write_note` 和 `github` 则在回合具备相应上下文时自动挂载。

Chat 也是进入更深层能力的入口：`deep_solve` 用于推理解题，`deep_question` 用于出题，`deep_research` 用于生成带引用的报告，`visualize` 和 `math_animator` 用于视觉化输出，`auto` 用于路由，`mastery_path` 用于学习计划流程。

### 🤝 Partner —— 运行在同一大脑上的持久伴侣

<div align="center">
<img src="../../assets/figs/webui/partners.png" alt="DeepTutor Partners 工作区" width="900">
</div>

Partners 以更简洁的模型取代了旧版 TutorBot 引擎：每条来自 Web 或 IM 的消息都成为 Partner 作用域工作区内的一个普通 ChatOrchestrator 回合。无需维护独立的 bot 大脑保持同步。

<div align="center">
<img src="../../assets/figs/system/partners-architecture.png" alt="DeepTutor Partners 架构" width="900">
</div>

每个 Partner 拥有 `SOUL.md`、模型选择、频道配置、工具策略与指定资料库。Knowledge Bases、Skills 和笔记本会被复制到 `data/partners/<id>/workspace/`，因此相同的 RAG、skill、笔记本和记忆工具无需特殊处理即可正常运行。

<div align="center">
<img src="../../assets/figs/webui/partners02.png" alt="DeepTutor Partner 详情视图" width="900">
</div>

频道层基于 Schema 驱动，可根据已安装的扩展与配置的凭证连接到飞书、Telegram、Slack、钉钉、QQ/Napcat、企业微信、WhatsApp、Zulip、Matrix 和 Microsoft Teams 等 IM 平台。

### ✍️ Co-Writer —— 感知选区的 Markdown 起草工具

Co-Writer 是一个分栏 Markdown 工作区，适合撰写报告、教程、笔记与长篇学习内容。文档自动保存、实时渲染预览，并可在草稿变为可复用上下文时保存回笔记本。

选中文本，让 DeepTutor 改写、扩展或缩短它。编辑智能体会追踪工具调用轨迹，并可基于知识库或网络证据进行编辑，因此 Co-Writer 的行为更像一个具备检索能力的编辑器，而非独立的文本框。

### 📖 Book —— 从你的材料生成活书

<p align="center">
<img src="../../assets/figs/webui/book01.png" alt="DeepTutor Book 阅读视图" width="31%">
&nbsp;
<img src="../../assets/figs/webui/book02.png" alt="DeepTutor Book 交互块视图" width="31%">
&nbsp;
<img src="../../assets/figs/webui/book03.png" alt="DeepTutor Book 创建视图" width="31%">
</p>

Book 将选定的来源转化为交互式学习材料。一本书可以从知识库、笔记本、题库或聊天历史出发；创建流程会在内容生成前提出结构建议，让用户可以审阅框架，而非接受一个盲目的一次性输出。

BookEngine 将页面编译为类型化块：文本、章节、callout、测验、闪卡、时间线、代码、图形、交互式 HTML、动画、概念图、深度剖析与用户笔记。维护命令如 `deeptutor book health` 和 `deeptutor book refresh-fingerprints` 帮助检测来源知识与已编译页面之间的漂移。

### 📚 Knowledge —— 版本化的 RAG 资料库

<div align="center">
<img src="../../assets/figs/webui/knowledge.png" alt="DeepTutor 知识库工作区" width="900">
</div>

Knowledge Bases 是 RAG 背后的文档集合。当前技术栈仅使用 LlamaIndex，采用以嵌入签名为键的扁平 `version-N` 存储布局。重建索引会保留旧版本，避免在处理新文档时覆盖可用索引。

Web 工作区暴露文件、上传、索引版本与设置。CLI 通过 `deeptutor kb list`、`info`、`create`、`add`、`search`、`set-default` 和 `delete` 镜像相同的生命周期。

### 🌐 Space —— 技能、人格与可复用上下文

<div align="center">
<img src="../../assets/figs/webui/space.png" alt="DeepTutor Space 工作区" width="900">
</div>

Space 是可复用上下文的资料层。它汇聚了用户自建的 Skills、人格、笔记本、聊天历史与题库风格资源，让智能体可以用刻意选取的上下文来引导，而非依赖临时提示。

Skills 以 `SKILL.md` 文件形式存储在用户工作区下，可打标签、编辑或在内置时保持只读。人格遵循同样的思路用于角色与语气。这些资源可指定给 Partners、在聊天中引用，并跨学习工作流复用。

### 🧠 Memory —— 可审查的个性化

<div align="center">
<img src="../../assets/figs/webui/memory01.png" alt="DeepTutor Memory 工作台" width="900">
</div>

Memory 是根植于活跃用户工作区的三层系统：`trace/<surface>/<date>.jsonl` 用于 L1 事件轨迹，`L2/<surface>.md` 用于按工作面整理的事实，`L3/<recent|profile|scope|preferences>.md` 用于跨工作面综合。

<div align="center">
<img src="../../assets/figs/webui/memory02.png" alt="DeepTutor Memory 图谱" width="900">
</div>

支持的 Memory 工作面为 `chat`、`notebook`、`quiz`、`kb`、`book`、`tutorbot` 和 `cowriter`。即便产品层面的伴侣模型已升级为 Partners，Memory 层中的旧版 `tutorbot` 工作面名称仍为兼容性保留。工作台支持审查、编辑、运行整合，并可通过图谱将综合论断追溯回其支撑事实与原始事件。

### ⚙️ Settings —— 统一控制平面

<div align="center">
<img src="../../assets/figs/webui/settings.png" alt="DeepTutor 设置工作区" width="900">
</div>

Settings 是操作控制平面。涵盖外观、网络端口与外部 API base、LLM 与嵌入目录、搜索提供商、MinerU 解析、能力预算、记忆节奏、MCP 服务器、内置工具，以及已启用的可选工具列表。

大多数设置采用草稿 / Apply 流程，便于用户在提交前测试提供商。项目根目录的 `.env` 文件刻意被忽略；运行时配置位于 `data/user/settings/*.json` 下，除非 `DEEPTUTOR_HOME` 或 `deeptutor start --home` 将应用指向别处。

---

## ⌨️ DeepTutor CLI —— 智能体原生接口

DeepTutor 天生为 CLI 设计：同一个 `deeptutor` 入口可以初始化工作区、启动 Web 应用、运行单次能力、打开交互式 REPL、管理知识库、查看会话、维护书籍，以及操作 Partners。

```bash
deeptutor run chat "Explain Fourier transform" --tool rag --kb textbook
deeptutor run deep_solve "Solve x^2 = 4" --tool reason
deeptutor chat --capability deep_research --kb papers
deeptutor partner create math-tutor --soul "Socratic math tutor"
deeptutor kb create calculus --doc textbook.pdf
```

<details>
<summary><b>命令参考</b></summary>

| 命令 | 说明 |
|:---|:---|
| `deeptutor init` | 为当前工作区创建或更新 `data/user/settings` |
| `deeptutor start [--home PATH]` | 同时启动后端 + 前端 |
| `deeptutor serve [--port PORT]` | 仅启动 FastAPI 后端 |
| `deeptutor run <capability> <message>` | 运行单个能力回合（`chat`、`deep_solve`、`deep_question`、`deep_research`、`visualize`、`math_animator`、`auto`、`mastery_path`） |
| `deeptutor chat` | 交互式 REPL，支持能力、工具、KB、笔记本与历史记录控制 |
| `deeptutor partner list/create/start/stop` | 管理 IM 接入的 Partners |
| `deeptutor kb list/info/create/add/search/set-default/delete` | 管理 LlamaIndex 知识库 |
| `deeptutor memory show/clear` | 查看 L2/L3 记忆文档或清空 L1/全部记忆 |
| `deeptutor session list/show/open/rename/delete` | 管理共享会话 |
| `deeptutor notebook list/create/show/add-md/replace-md/remove-record` | 从 Markdown 文件管理笔记本 |
| `deeptutor book list/health/refresh-fingerprints` | 查看书籍并刷新来源指纹 |
| `deeptutor plugin list/info` | 查看已注册的工具与能力 |
| `deeptutor config show` | 打印配置摘要 |
| `deeptutor provider login <provider>` | 管理支持的提供商 OAuth 登录 |

</details>

CLI 专用发行版位于 `packaging/deeptutor-cli`；在本检出中应通过源码安装：`python -m pip install -e ./packaging/deeptutor-cli`。公开的 `deeptutor-cli` 包目前不在 PyPI 上提供，因此快速开始部分保留了源码安装路径。

---

## 👥 多用户 —— 共享部署

<div align="center">
<img src="../../assets/figs/webui/multi-user.png" alt="DeepTutor 多用户管理工作区" width="900">
</div>

认证功能默认关闭。启用后，DeepTutor 成为一个共享部署，具备一个管理员工作区、按用户的工作区、Partner 工作区，以及同一个 `data/` 目录树下的系统状态。

```text
data/
├── user/                         # 管理员工作区与设置
├── users/<uid>/                  # 非管理员用户作用域
│   ├── user/chat_history.db
│   ├── user/settings/interface.json
│   ├── user/workspace/{chat,co-writer,book,memory,notebook,...}
│   └── knowledge_bases/...
├── partners/<id>/workspace/      # Partner 合成用户作用域
└── system/
    ├── auth/users.json
    ├── grants/<uid>.json
    └── audit/usage.jsonl
```

首位注册用户成为管理员，可配置模型目录、提供商凭证、知识库、Skills 与用户授权。非管理员用户拥有隔离的聊天历史、记忆、笔记本、个人知识库，以及一个脱敏的 Settings 页面；管理员分配的资源以作用域只读选项的形式出现，不暴露 API Key 或提供商内部信息。

如需本地试用，将 `data/user/settings/auth.json` 设为启用认证，重启 `deeptutor start`，在 `/register` 注册首位管理员，然后从 `/admin/users` 创建用户，并通过授权分配模型、KB、Skills、工具策略、MCP 策略与代码执行权限。

PocketBase 模式在此目录树中仍为单用户集成；多用户部署应将 `integrations.pocketbase_url` 留空，使用默认的 JSON/SQLite 认证与会话存储，除非已为部署显式设计了外部用户存储。

---
## 🌐 社区与生态

DeepTutor 立足于一系列出色的开源项目：

| 项目 | 在 DeepTutor 中的角色 |
|:---|:---|
| [**nanobot**](https://github.com/HKUDS/nanobot) | 驱动原版 TutorBot 的超轻量智能体引擎（Partners 现已运行于 DeepTutor 的聊天智能体循环上） |
| [**LlamaIndex**](https://github.com/run-llama/llama_index) | RAG 流水线与文档索引主干 |
| [**ManimCat**](https://github.com/Wing900/ManimCat) | Math Animator 的 AI 驱动数学动画生成 |

**来自 HKUDS 生态：**

| [⚡ LightRAG](https://github.com/HKUDS/LightRAG) | [🤖 AutoAgent](https://github.com/HKUDS/AutoAgent) | [🔬 AI-Researcher](https://github.com/HKUDS/AI-Researcher) | [🧬 nanobot](https://github.com/HKUDS/nanobot) |
|:---:|:---:|:---:|:---:|
| 简洁高速的 RAG | 零代码智能体框架 | 自动化研究 | 超轻量 AI 智能体 |


## 🤝 贡献

<div align="center">

希望 DeepTutor 能成为送给社区的一份礼物。 🎁

<a href="https://github.com/HKUDS/DeepTutor/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=HKUDS/DeepTutor&max=999" alt="Contributors" />
</a>

</div>

开发环境搭建、代码规范与 PR 流程见 [CONTRIBUTING.md](../../CONTRIBUTING.md)。

## ⭐ Star 历史

<div align="center">

<a href="https://www.star-history.com/#HKUDS/DeepTutor&type=timeline&legend=top-left">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=HKUDS/DeepTutor&type=timeline&theme=dark&legend=top-left" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=HKUDS/DeepTutor&type=timeline&legend=top-left" />
    <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=HKUDS/DeepTutor&type=timeline&legend=top-left" />
  </picture>
</a>

</div>

<p align="center">
 <a href="https://www.star-history.com/hkuds/deeptutor">
  <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/badge?repo=HKUDS/DeepTutor&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/badge?repo=HKUDS/DeepTutor" />
   <img alt="Star History Rank" src="https://api.star-history.com/badge?repo=HKUDS/DeepTutor" />
  </picture>
 </a>
</p>

<div align="center">

**[Data Intelligence Lab @ HKU](https://github.com/HKUDS)**

[⭐ Star 我们](https://github.com/HKUDS/DeepTutor/stargazers) · [🐛 报告 bug](https://github.com/HKUDS/DeepTutor/issues) · [💬 Discussions](https://github.com/HKUDS/DeepTutor/discussions)

---

基于 [Apache License 2.0](../../LICENSE) 开源。

<p>
  <img src="https://visitor-badge.laobi.icu/badge?page_id=HKUDS.DeepTutor&style=for-the-badge&color=00d4ff" alt="Views">
</p>

</div>
