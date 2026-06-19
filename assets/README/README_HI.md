<div align="center">

<p align="center"><img src="../../assets/figs/logo/logo.png" alt="DeepTutor logo" height="56" style="vertical-align: middle;">&nbsp;<img src="../../assets/figs/logo/banner.png" alt="DeepTutor" height="48" style="vertical-align: middle;"></p>

# DeepTutor: एजेंट-नेटिव व्यक्तिगत ट्यूटरिंग

<p align="center">
  <a href="https://deeptutor.info" target="_blank"><img alt="Docs — deeptutor.info" src="https://img.shields.io/badge/Docs-deeptutor.info%20%E2%86%97-0A0A0A?style=for-the-badge&labelColor=F5F5F4" height="36"></a>
</p>

<a href="https://trendshift.io/repositories/17099" target="_blank"><img src="https://trendshift.io/api/badge/repositories/17099" alt="HKUDS%2FDeepTutor | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>

<p align="center">
  <a href="../../README.md"><img alt="English" height="40" src="https://img.shields.io/badge/English-CDCFD4"></a>&nbsp;
  <a href="README_CN.md"><img alt="简体中文" height="40" src="https://img.shields.io/badge/简体中文-CDCFD4"></a>&nbsp;
  <a href="README_JA.md"><img alt="日本語" height="40" src="https://img.shields.io/badge/日本語-CDCFD4"></a>&nbsp;
  <a href="README_ES.md"><img alt="Español" height="40" src="https://img.shields.io/badge/Español-CDCFD4"></a>&nbsp;
  <a href="README_FR.md"><img alt="Français" height="40" src="https://img.shields.io/badge/Français-CDCFD4"></a>&nbsp;
  <a href="README_AR.md"><img alt="Arabic" height="40" src="https://img.shields.io/badge/Arabic-CDCFD4"></a>&nbsp;
  <a href="README_RU.md"><img alt="Русский" height="40" src="https://img.shields.io/badge/Русский-CDCFD4"></a>&nbsp;
  <a href="README_HI.md"><img alt="Hindi" height="40" src="https://img.shields.io/badge/Hindi-BCDCF7"></a>&nbsp;
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

[विशेषताएं](#-मुख्य-विशेषताएं) · [शुरू करें](#-शुरू-करें) · [एक्सप्लोर करें](#-deeptutor-को-एक्सप्लोर-करें) · [CLI](#️-deeptutor-cli--एजेंट-नेटिव-इंटरफेस) · [मल्टी-यूजर](#-मल्टी-यूजर--साझा-deployments) · [इकोसिस्टम](#-इकोसिस्टम--eduhub-और-skills-community) · [समुदाय](#-समुदाय)

</div>

---

> 🤝 **हम किसी भी प्रकार के योगदान का स्वागत करते हैं!** [`Roadmap`](https://github.com/HKUDS/DeepTutor/issues/498) पर roadmap items के लिए वोट करें या नए प्रस्तावित करें, और branching strategy, coding standards और शुरू करने के तरीके के लिए हमारी [Contributing Guide](../../CONTRIBUTING.md) देखें।

### 📦 रिलीज़

> **[2026.6.17]** [v1.4.6](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.6) — Space → My Agents के साथ लर्निंग डैशबोर्ड बन गया और शीर्ष-स्तरीय Memory जुड़ी; Knowledge Center में GraphRAG / PageIndex / LightRAG engines और लिंक्ड KB व Obsidian mounts शामिल हुए; Settings में document parsing / आवाज / इमेज+वीडियो खुला; और LLM क्षमताएं assigned model के अनुसार गेटेड हुईं।

> **[2026.6.14]** [v1.4.5](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.5) — गाइडेड लर्निंग को chat agent loop पर पुनर्निर्मित किया गया, हर type के लिए hard मास्टरी गेट्स और `/learning` dashboard के साथ; एक नया extensible लूप-प्लगइन फ्रेमवर्क; और Partner conversations के लिए Markdown एक्सपोर्ट / save-to-notebook।

> **[2026.6.13]** [v1.4.4](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.4) — एक security gate के पीछे `deeptutor skill install` से [ClawHub](https://clawhub.ai/) से कम्युनिटी स्किल्स install करें; और knowledge-base files के लिए browser में real DOCX/XLSX ब्राउज़र प्रीव्यू।

> **[2026.6.12]** [v1.4.3](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.3) — TutorBot **Partners** बन गया है एक production-grade IM pipeline (15 channels, live streaming) पर, Chat single agent loop पर चला गया, वास्तविक per-user isolation, और Visualize को फिर से बनाया गया।

<details>
<summary><b>पिछली रिलीज़ (2 सप्ताह से अधिक पुरानी)</b></summary>

> **[2026.5.28]** [v1.4.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.2) — v1.4.1 पर stability + polish: Gemini 2.5+ Visualize और Chat में unblocked, ContextVar auth-routing fix (#485), reasoning + native-tools label protocol मजबूत, हर chat surface पर smooth-streaming UX, नया collapsible Recents sidebar, और Lemonade local-provider support।

> **[2026.5.27]** [v1.4.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.1) — Security + stability patch: TutorBot tool sandbox locked down, per-user resource isolation, vision-capable providers के लिए multimodal image fallback, TutorBot से बात करने के लिए HTTP/SSE API, और v1.4.0 chat regression fix।

> **[2026.5.22]** [v1.4.0](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.0) — v1.4 का GA cut: Auto Mode, three-layer Memory, agentic Deep Research / Solve / Question, LlamaIndex RAG refactor, Visualize/Animator merge, reasoning-effort normalization, tool-schema fallback, और restart-safe turn runtime।

> **[2026.5.21]** [v1.4.0-beta](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.0-beta) — Three-layer Memory workbench (L1/L2/L3), हर chat capability एक ही agentic engine पर पुनर्निर्मित, LlamaIndex-only RAG, और unified Settings + Capabilities surface।

> **[2026.5.10]** [v1.3.10](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.10) — Remote Docker CORS recovery, SDK providers में `DISABLE_SSL_VERIFY`, सुरक्षित code-block citations, और optional Matrix E2EE add-on।

> **[2026.5.9]** [v1.3.9](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.9) — TutorBot Zulip और NVIDIA NIM support, सुरक्षित thinking-model routing, `deeptutor start`, sidebar tooltips, और session-store parity।

> **[2026.5.8]** [v1.3.8](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.8) — isolated user workspaces, admin grants, auth routes, और scoped runtime access के साथ optional multi-user deployments।

> **[2026.5.4]** [v1.3.7](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.7) — Thinking-model/provider fixes, visible Knowledge index history, और सुरक्षित Co-Writer clear/template editing।

> **[2026.5.3]** [v1.3.6](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.6) — chat और TutorBot के लिए Catalog-based model selection, सुरक्षित RAG re-indexing, OpenAI Responses token-limit fixes, और Skills editor validation।

> **[2026.5.2]** [v1.3.5](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.5) — Smoother local launch settings, सुरक्षित RAG queries, cleaner local embedding auth, और Settings dark-mode polish।

> **[2026.5.1]** [v1.3.4](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.4) — Book page chat persistence और rebuild flows, chat-to-book references, मजबूत language/reasoning handling, RAG document extraction hardening।

> **[2026.4.30]** [v1.3.3](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.3) — NVIDIA NIM + Gemini embedding support, chat history/skills/memory के लिए unified Space context, session snapshots, RAG re-index resilience।

> **[2026.4.29]** [v1.3.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.2) — Transparent embedding endpoint URLs, invalid persisted vectors के लिए RAG re-index resilience, thinking-model output के लिए memory cleanup, Deep Solve runtime fix।

> **[2026.4.28]** [v1.3.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.1) — Stability: सुरक्षित RAG routing & embedding validation, Docker persistence, IME-safe input, Windows/GBK robustness।

> **[2026.4.27]** [v1.3.0](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.0) — Versioned KB indexes re-index workflow के साथ, rebuilt Knowledge workspace, नए adapters के साथ embedding auto-discovery, Space hub।

> **[2026.4.25]** [v1.2.5](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.5) — file-preview drawer के साथ persistent chat attachments, attachment-aware capability pipelines, TutorBot Markdown export।

> **[2026.4.25]** [v1.2.4](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.4) — Text/code/SVG attachments, one-command Setup Tour, Markdown chat export, compact KB management UI।

> **[2026.4.24]** [v1.2.3](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.3) — Document attachments (PDF/DOCX/XLSX/PPTX), reasoning thinking-block display, Soul template editor, Co-Writer save-to-notebook।

> **[2026.4.22]** [v1.2.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.2) — User-authored Skills system, chat input performance overhaul, TutorBot auto-start, Book Library UI, visualization fullscreen।

> **[2026.4.21]** [v1.2.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.1) — Per-stage token limits, सभी entry points पर Regenerate response, RAG & Gemma compatibility fixes।

> **[2026.4.20]** [v1.2.0](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.0) — Book Engine "living book" compiler, multi-document Co-Writer, interactive HTML visualizations, Question Bank @-mention।

> **[2026.4.18]** [v1.1.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.1.2) — Schema-driven Channels tab, RAG single-pipeline consolidation, externalized chat prompts।

> **[2026.4.17]** [v1.1.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.1.1) — Universal "Answer now", Co-Writer scroll sync, unified settings panel, streaming Stop button।

> **[2026.4.15]** [v1.1.0](https://github.com/HKUDS/DeepTutor/releases/tag/v1.1.0) — LaTeX block math overhaul, LLM diagnostic probe, Docker + local LLM guidance।

> **[2026.4.14]** [v1.1.0-beta](https://github.com/HKUDS/DeepTutor/releases/tag/v1.1.0-beta) — Bookmarkable sessions, Snow theme, WebSocket heartbeat & auto-reconnect, embedding registry overhaul।

> **[2026.4.13]** [v1.0.3](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.3) — bookmarks & categories के साथ Question Notebook, Visualize में Mermaid, embedding mismatch detection, Qwen/vLLM compatibility, LM Studio & llama.cpp support, और Glass theme।

> **[2026.4.11]** [v1.0.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.2) — SearXNG fallback के साथ Search consolidation, provider switch fix, और frontend resource leak fixes।

> **[2026.4.10]** [v1.0.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.1) — Visualize capability (Chart.js/SVG), quiz duplicate prevention, और o4-mini model support।

> **[2026.4.10]** [v1.0.0-beta.4](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.0-beta.4) — rate-limit retry के साथ Embedding progress tracking, cross-platform dependency fixes, और MIME validation fix।

> **[2026.4.8]** [v1.0.0-beta.3](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.0-beta.3) — Native OpenAI/Anthropic SDK (litellm हटाया), Windows Math Animator support, robust JSON parsing, और full Chinese i18n।

> **[2026.4.7]** [v1.0.0-beta.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.0-beta.2) — Hot settings reload, MinerU nested output, WebSocket fix, और Python 3.11+ minimum।

> **[2026.4.4]** [v1.0.0-beta.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.0-beta.1) — Agent-native architecture rewrite (~200k lines): Tools + Capabilities plugin model, CLI & SDK, TutorBot, Co-Writer, Guided Learning, और persistent memory।

> **[2026.1.23]** [v0.6.0](https://github.com/HKUDS/DeepTutor/releases/tag/v0.6.0) — Session persistence, incremental document upload, flexible RAG pipeline import, और full Chinese localization।

> **[2026.1.18]** [v0.5.2](https://github.com/HKUDS/DeepTutor/releases/tag/v0.5.2) — RAG-Anything के लिए Docling support, logging system optimization, और bug fixes।

> **[2026.1.15]** [v0.5.0](https://github.com/HKUDS/DeepTutor/releases/tag/v0.5.0) — Unified service configuration, प्रति knowledge base RAG pipeline selection, question generation overhaul, और sidebar customization।

> **[2026.1.9]** [v0.4.0](https://github.com/HKUDS/DeepTutor/releases/tag/v0.4.0) — Multi-provider LLM & embedding support, नया home page, RAG module decoupling, और environment variable refactor।

> **[2026.1.5]** [v0.3.0](https://github.com/HKUDS/DeepTutor/releases/tag/v0.3.0) — Unified PromptManager architecture, GitHub Actions CI/CD, और GHCR पर pre-built Docker images।

> **[2026.1.2]** [v0.2.0](https://github.com/HKUDS/DeepTutor/releases/tag/v0.2.0) — Docker deployment, Next.js 16 & React 19 upgrade, WebSocket security hardening, और critical vulnerability fixes।

</details>

### 📰 समाचार

> **[2026.5.22]** 🌐 deeptutor.info पर आधिकारिक डॉक्स साइट लाइव — guides, references, और capability tours सब एक ही जगह।

> **[2026.4.19]** 🎉 111 दिनों में 20k स्टार्स! आपके अविश्वसनीय समर्थन के लिए धन्यवाद — हम सभी के लिए सच्ची व्यक्तिगत, बुद्धिमान ट्यूटरिंग की दिशा में निरंतर iteration के प्रति प्रतिबद्ध हैं।

> **[2026.4.10]** 📄 हमारा paper अब arXiv पर live है! DeepTutor के design और विचारों के बारे में अधिक जानने के लिए [preprint](https://arxiv.org/abs/2604.26962) पढ़ें।

> **[2026.2.6]** 🚀 39 दिनों में 10k स्टार्स! हमारे अविश्वसनीय community के समर्थन के लिए बहुत धन्यवाद!

> **[2026.1.1]** नया साल मुबारक! हमारे [Discord](https://discord.gg/eRsjPgMU4t), [WeChat](https://github.com/HKUDS/DeepTutor/issues/78), या [Discussions](https://github.com/HKUDS/DeepTutor/discussions) से जुड़ें — आइए मिलकर DeepTutor का भविष्य बनाएं!

> **[2025.12.29]** DeepTutor आधिकारिक रूप से जारी हुआ!

## ✨ मुख्य विशेषताएं

DeepTutor एक agent-native runtime के इर्द-गिर्द बनाया गया है: एक shared ChatOrchestrator हर turn को capabilities में route करता है, एक ToolRegistry single-shot tools को expose करता है जब model को उनकी जरूरत हो, और एक CapabilityRegistry गहरे workflows को turn संभालने देता है जब task को structure की जरूरत हो।

<div align="center">
<img src="../../assets/figs/system/system%20architecture.png" alt="DeepTutor system architecture" width="900">
</div>

- **हर मोड के लिए एक रनटाइम** — Chat, Quiz, Research, Visualize, Solve और Mastery Path एक ही एजेंट लूप पर चलते हैं, इसलिए आप objective बदलते हैं, engine नहीं, और context learner के साथ बना रहता है।
- **जुड़ा हुआ लर्निंग कॉन्टेक्स्ट** — नॉलेज बेस, किताबें, Co-Writer ड्राफ्ट, नोटबुक, प्रश्न बैंक, पर्सोना और Memory सभी वर्कफ्लो में उपलब्ध रहते हैं, isolated tools में बंद रहने की बजाय।
- **सब-एजेंट और Partners** — किसी भी टर्न से live Claude Code, Codex, या Partner से सलाह लें (या उनकी पिछली conversations import करें); same brain पर स्थायी IM कम्पेनियन चलाएं।
- **मल्टी-इंजन नॉलेज** — LlamaIndex, PageIndex, GraphRAG, LightRAG या लिंक्ड Obsidian वॉल्ट के साथ versioned RAG लाइब्रेरी, pluggable document parsing के साथ।
- **एक्सटेंसिबल टूल्स और स्किल्स** — बिल्ट-इन टूल्स, MCP सर्वर, इमेज/वीडियो/वॉइस जेनरेशन मॉडल, और EduHub से installable कम्युनिटी स्किल्स।
- **इंस्पेक्टेबल मेमोरी** — L1 ट्रेस, L2 surface summaries, और L3 synthesis personalization को visible और editable बनाते हैं, एक Memory Graph के साथ जो हर दावे को उसके साक्ष्य तक ट्रेस करता है।

---

## 🚀 शुरू करें

DeepTutor चार installation paths के साथ आता है। वे सभी एक workspace layout साझा करते हैं: settings `data/user/settings/` में उस directory के नीचे रहती हैं जहां से आप launch करते हैं (या `DEEPTUTOR_HOME` / `deeptutor start --home` के नीचे अगर आप explicitly set करते हैं)। पूरे app के लिए, recommended flow है **workspace directory चुनें → install करें → `deeptutor init` → `deeptutor start`**।

> ✨ **v1.4.6 live है।** `pip install -U deeptutor` latest stable को pick up करता है। Pre-releases (जब उपलब्ध हों) `pip install --pre -U deeptutor` से opt in होते हैं।

### Option 1 — PyPI से Install करें

पूरा local Web app + CLI, clone की जरूरत नहीं। **Python 3.11+** और PATH पर **Node.js 20+** runtime चाहिए (`deeptutor start` packaged Next.js standalone server को spawn करता है)।

```bash
mkdir -p my-deeptutor && cd my-deeptutor
pip install -U deeptutor
deeptutor init     # ports + LLM provider + optional embedding के लिए prompt करता है
deeptutor start    # backend + frontend शुरू करता है; terminal खुला रखें
```

`deeptutor init` backend port (default `8001`), frontend port (default `3782`), LLM provider / base URL / API key / model, और Knowledge Base / RAG के लिए optional embedding provider के लिए prompt करता है।

`deeptutor start` के बाद, terminal में print किया गया frontend URL खोलें — default रूप से [http://127.0.0.1:3782](http://127.0.0.1:3782)। backend और frontend दोनों को रोकने के लिए उस terminal में `Ctrl+C` दबाएं। Quick trial के लिए `deeptutor init` छोड़ना ठीक है; app default ports और empty model settings के साथ boot होगा, उन्हें बाद में **Settings → Models** में configure करें।

### Option 2 — Source से Install करें

Checkout के विरुद्ध development के लिए। CI और Docker से match करने के लिए **Python 3.11+** और **Node.js 22 LTS** उपयोग करें।

```bash
git clone https://github.com/HKUDS/DeepTutor.git
cd DeepTutor

# एक venv बनाएं (macOS/Linux). Windows PowerShell:
#   py -3.11 -m venv .venv ; .\.venv\Scripts\Activate.ps1
python3 -m venv .venv && source .venv/bin/activate
python -m pip install --upgrade pip

# Backend + frontend deps install करें
python -m pip install -e .
( cd web && npm ci --legacy-peer-deps )

deeptutor init
deeptutor start
```

Source installs local `web/` directory के विरुद्ध Next.js को dev mode में run करते हैं; बाकी सब (config layout, ports, `Ctrl+C` से stop) Option 1 से match करता है।

<details>
<summary><b>Conda environment</b> (<code>venv</code> की बजाय)</summary>

```bash
conda create -n deeptutor python=3.11
conda activate deeptutor
python -m pip install --upgrade pip
```

</details>

<details>
<summary><b>वैकल्पिक install extras</b> — dev / partners / matrix / math-animator</summary>

```bash
pip install -e ".[dev]"             # tests/lint tools
pip install -e ".[partners]"        # Partner IM channel SDKs + MCP client
pip install -e ".[matrix]"          # E2EE/libolm के बिना Matrix channel
pip install -e ".[matrix-e2e]"      # Matrix E2EE; libolm चाहिए
pip install -e ".[math-animator]"   # Manim addon; LaTeX/ffmpeg/system libs चाहिए
```

</details>

<details>
<summary><b>Frontend dependency tweaks और dev-server troubleshooting</b></summary>

**Frontend dependencies बदलना:** `web/package-lock.json` refresh करने के लिए `npm install --legacy-peer-deps` run करें, फिर `web/package.json` और `web/package-lock.json` दोनों को commit करें।

**Stuck dev server:** अगर `deeptutor start` एक existing frontend report करता है जो respond नहीं कर रहा, तो उस PID को stop करें जो वह print करता है। अगर कोई Next.js process actually नहीं चल रही, तो lock files stale हैं — उन्हें remove करें और retry करें:

```bash
rm -f web/.next/dev/lock web/.next/lock
deeptutor start
```

</details>

### Option 3 — Docker

पूरे Web app के लिए एक container। GitHub Container Registry पर images:

- `ghcr.io/hkuds/deeptutor:latest` — stable release
- `ghcr.io/hkuds/deeptutor:pre` — pre-release, जब उपलब्ध हो

```bash
docker run --rm --name deeptutor \
  -p 127.0.0.1:3782:3782 \
  -p 127.0.0.1:8001:8001 \
  -v deeptutor-data:/app/data \
  ghcr.io/hkuds/deeptutor:latest
```

> ⚠️ **`3782` और `8001` दोनों map करें।** `3782` web UI serve करता है; `8001` FastAPI backend है जिसे आपका browser directly call करता है — container के अंदर कोई proxy नहीं है। `8001` mapping skip करने पर page लोड तो होगा, लेकिन **Settings** "Backend unreachable" दिखाएगा और unusable रहेगा।

[http://127.0.0.1:3782](http://127.0.0.1:3782) खोलें। Container पहले boot पर `/app/data/user/settings/*.json` बनाता है; Web Settings page से model providers configure करें। Config, API keys, logs, workspace files, memory, और knowledge bases `deeptutor-data` volume में persist करते हैं।

- **अलग host ports:** प्रत्येक `-p host:container` mapping के left side को बदलें (जैसे `-p 127.0.0.1:8088:3782`)। अगर आप `/app/data/user/settings/system.json` में container-side ports बदलते हैं, तो restart करें और match करने के लिए प्रत्येक mapping के right side को update करें।
- **Detached:** `-d` add करें, फिर follow करने के लिए `docker logs -f deeptutor`, stop करने के लिए `docker stop deeptutor`, नाम reuse करने से पहले `docker rm deeptutor`। `deeptutor-data` volume आपकी settings और workspace को restarts के पार रखता है।

**Remote Docker / reverse proxy:** Web UI browser में चलता है, इसलिए browser को एक backend URL चाहिए जिस तक वह पहुंच सके। Remote servers के लिए, **Settings -> Network** खोलें या `data/user/settings/system.json` edit करें:

```json
{
  "next_public_api_base_external": "https://deeptutor.example.com"
}
```

`public_api_base` compatibility alias के रूप में accept किया जाता है और save पर `next_public_api_base_external` में normalize होता है। CORS frontend **origins** उपयोग करता है, API URLs नहीं। Auth disabled होने पर, DeepTutor default रूप से normal HTTP/HTTPS browser origins permit करता है। Auth enabled होने पर, exact frontend origins add करें:

```json
{
  "cors_origins": ["https://deeptutor.example.com"]
}
```

<details>
<summary><b>Host पर Ollama / LM Studio / llama.cpp / vLLM / Lemonade से Connect करना</b></summary>

Docker के अंदर, `localhost` container itself है, आपका host machine नहीं। Host पर चल रहे model service तक पहुंचने के लिए, host gateway उपयोग करें (recommended):

```bash
docker run --rm --name deeptutor \
  -p 127.0.0.1:3782:3782 -p 127.0.0.1:8001:8001 \
  --add-host=host.docker.internal:host-gateway \
  -v deeptutor-data:/app/data \
  ghcr.io/hkuds/deeptutor:latest
```

फिर **Settings → Models** में, provider Base URL को `host.docker.internal` पर point करें:

- Ollama LLM: `http://host.docker.internal:11434/v1`
- Ollama embedding: `http://host.docker.internal:11434/api/embed`
- LM Studio: `http://host.docker.internal:1234/v1`
- llama.cpp: `http://host.docker.internal:8080/v1`
- Lemonade: `http://host.docker.internal:13305/api/v1`

Docker Desktop (macOS/Windows) आमतौर पर `--add-host` के बिना `host.docker.internal` resolve करता है। Linux पर, यह flag modern Docker Engine पर वह hostname बनाने का portable तरीका है।

**Linux alternative — host networking:** `--network=host` add करें और `-p` flags हटाएं। Container host network directly share करता है, इसलिए [http://127.0.0.1:3782](http://127.0.0.1:3782) (या `system.json` में `frontend_port`) खोलें, और host services को normal localhost URLs जैसे `http://127.0.0.1:11434/v1` से reach किया जा सकता है। ध्यान दें कि host networking container ports को host पर directly expose करता है और existing services से conflict हो सकता है।

</details>

### Code Execution Sandbox (office skills)

Built-in office skills — **docx / pdf / pptx / xlsx** — model द्वारा एक short Python script (`python-docx`, `reportlab`, `openpyxl`, …) लिखकर, इसे `exec` / `code_execution` tools के जरिए run करके, और download URL वापस करके काम करती हैं। वे tools तब mount होते हैं जब एक sandbox backend active होता है, जो **default रूप से** हर deployment shape में होता है:

- **Local (Option 1 / 2) और Docker (Option 3, single container):** एक restricted subprocess sandbox model का code run करता है (locally host पर, या Docker के नीचे container के अंदर — container itself एक isolation boundary है)।
- **docker-compose:** इसके बजाय `DEEPTUTOR_SANDBOX_RUNNER_URL` के जरिए एक hardened, least-privileged **runner sidecar** (`Dockerfile.runner`) पर route किया जाता है — सबसे मजबूत posture, और automatically preferred जब present हो।

Subprocess sandbox `data/user/settings/system.json` में `sandbox_allow_subprocess` setting द्वारा controlled होता है (default `true`)। अपने host पर model-generated code run करना एक real trust decision है — host-side execution को disable करने के लिए इसे `false` set करें (या `DEEPTUTOR_SANDBOX_ALLOW_SUBPROCESS=0` export करें), office skills की files produce करने की क्षमता खोने की कीमत पर।

### Option 4 — केवल CLI

जब आपको Web UI की जरूरत न हो। CLI-only package PyPI से नहीं, source checkout से install होता है।

```bash
git clone https://github.com/HKUDS/DeepTutor.git
cd DeepTutor

# एक venv बनाएं (macOS/Linux). Windows PowerShell:
#   py -3.11 -m venv .venv-cli ; .\.venv-cli\Scripts\Activate.ps1
python3 -m venv .venv-cli && source .venv-cli/bin/activate
python -m pip install --upgrade pip

python -m pip install -e ./packaging/deeptutor-cli
deeptutor init --cli
deeptutor chat
```

`deeptutor init --cli` पूरे app के समान `data/user/settings/` layout share करता है लेकिन backend/frontend port prompts skip करता है और embeddings को **off** default करता है (अगर आप `deeptutor kb …` या RAG tools उपयोग करने की योजना रखते हैं तो `Yes` चुनें)। यह फिर भी एक complete runtime layout (`system.json`, `auth.json`, `integrations.json`, `model_catalog.json`, `main.yaml`, `agents.yaml`) लिखता है और active LLM provider और model के लिए prompt करता है।

<details>
<summary><b>सामान्य commands</b></summary>

```bash
deeptutor chat                                          # interactive REPL
deeptutor chat --capability deep_solve --tool rag --kb my-kb
deeptutor run chat "Explain Fourier transform"
deeptutor run deep_solve "Solve x^2 = 4" --tool rag --kb my-kb
deeptutor kb create my-kb --doc textbook.pdf
deeptutor memory show
deeptutor config show
```

</details>

Local `deeptutor-cli` install में कोई Web assets या server dependencies नहीं हैं। Source checkout को आसपास रखें — editable install उस पर point करता है। बाद में Web app add करने के लिए, PyPI package (Option 1) install करें और same workspace से `deeptutor init` + `deeptutor start` run करें।

### कॉन्फ़िगरेशन संदर्भ

<details>
<summary><b><code>data/user/settings/</code> के नीचे Config files</b> — JSON/YAML reference</summary>

`data/user/settings/` के नीचे सब कुछ plain JSON/YAML है। Browser में **Settings** page recommended editor है।

| File | उद्देश्य |
|:---|:---|
| `model_catalog.json` | LLM, embedding, और search provider profiles; API keys; active models |
| `system.json` | Backend/frontend ports, public API base, CORS, SSL verification, attachment directory |
| `auth.json` | Optional auth toggle, username, password hash, token/cookie settings |
| `integrations.json` | Optional PocketBase और sidecar integration settings |
| `interface.json` | UI language / theme / sidebar preferences |
| `main.yaml` | Runtime behavior defaults और path injection |
| `agents.yaml` | Capability/tool temperature और token settings |

Project-root `.env` application config file के रूप में **नहीं** पढ़ा जाता। Minimal model setup के लिए, **Settings → Models** खोलें, एक LLM profile (Base URL / API key / model name) add करें, और save करें। Embedding profile केवल तभी add करें जब आप Knowledge Base / RAG features उपयोग करने की योजना रखते हों।

</details>

## 📖 DeepTutor को एक्सप्लोर करें

README tour product surfaces को उस क्रम में follow करता है जिसमें आप उनसे सबसे अधिक मिलेंगे। नीचे दिए गए screenshots v1.4.6 के हैं।

<div align="center">
<img src="../../assets/figs/web-1.4.6+/OVERVIEW.png" alt="DeepTutor overview" width="900">
</div>

### 💬 Chat

<div align="center">
<img src="../../assets/figs/web-1.4.6+/home/00-overview.png" alt="DeepTutor chat workspace" width="900">
</div>

Chat डिफ़ॉल्ट एजेंट लूप है और वह जगह है जहां से अधिकांश काम शुरू होता है। एक single thread normally बात कर सकता है, tools call कर सकता है, selected knowledge bases में खुद को ground कर सकता है, attachments पढ़ सकता है, images generate कर सकता है, subagents से consult कर सकता है, notebook records लिख सकता है, और turns के पार same context के साथ जारी रह सकता है।

Loop जानबूझकर simple है: model rounds में सोचता है, जब उपयोगी हो tools call करता है, tool results observe करता है, और tool-free message के साथ finish करता है। `ask_user` special है — guess करने की बजाय, agent टर्न पॉज़ कर सकता है, एक structured स्पष्टीकरण प्रश्न पूछ सकता है, और आपके जवाब देने के बाद resume कर सकता है।

User-toggleable tools हैं `brainstorm`, `web_search`, `paper_search`, `reason`, और `geogebra_analysis` — साथ ही `imagegen` और `videogen` जब आप matching generation model configure करें। Contextual tools जैसे `rag`, `read_source`, `read_memory`, `write_memory`, `read_skill`, `load_tools`, `exec`, `web_fetch`, `ask_user`, `list_notebook`, `write_note`, `github`, और `consult_subagent` तब automatically mount होते हैं जब turn के पास सही context हो।

Context दो प्रकार की होती है: **स्टिकी कॉन्टेक्स्ट** (सब-एजेंट, KB, पर्सोना, मॉडल, आवाज) composer toolbar पर रहती है और turns के पार persist करती है; **एक-बार रेफरेंस** (फ़ाइलें, chat इतिहास, किताबें, नोटबुक, प्रश्न बैंक, imported agents) + menu से आते हैं एक single turn के लिए।

Chat deeper capabilities के लिए launch point भी है: Quiz question generation के लिए, Research cited reports के लिए, Visualize charts/diagrams/animations के लिए, और More Capabilities के नीचे Solve worked reasoning के लिए और Mastery Path learning-plan flows के लिए।

<div align="center">
<img src="../../assets/figs/system/chat-agent-loop.png" alt="DeepTutor chat agent loop" width="900">
</div>

### 🤝 Partner

<div align="center">
<img src="../../assets/figs/web-1.4.6+/partners/00-partners%20overview.png" alt="DeepTutor partners overview" width="900">
</div>

Partners स्थायी कम्पेनियन हैं जिनकी अपनी soul, model policy, library, memory, और channels हैं। वे एक अलग bot engine नहीं हैं: हर inbound web या IM message partner-scoped workspace के अंदर एक normal ChatOrchestrator turn बन जाता है। एक partner "एक chat है जिसकी personality और phone number है।"

हर partner के पास एक `SOUL.md`, model selection, channels, tool policy, और assigned library है। Knowledge bases, skills, और notebooks `data/partners/<id>/workspace/` में copy होते हैं, इसलिए same RAG, skill, notebook, और memory tools special cases के बिना काम करते हैं। एक partner अपने owner की memory पढ़ता है लेकिन केवल अपनी memory में लिखता है।

<div align="center">
<img src="../../assets/figs/system/partners-architecture.png" alt="DeepTutor partners architecture" width="900">
</div>

Channel layer schema-driven है और Feishu, Telegram, Slack, DingTalk, QQ/NapCat, WeCom, WhatsApp, Zulip, Matrix, और Microsoft Teams से connect हो सकती है। एक partner को subagent के रूप में भी connect किया जा सकता है और normal chat turn से consult किया जा सकता है — नीचे My Agents देखें।

<div align="center">
<img src="../../assets/figs/web-1.4.6+/partners/02-IM%20config%20for%20each%20partner.png" alt="IM config for each partner" width="900">
</div>

### 🧑‍🚀 मेरे एजेंट

<div align="center">
<img src="../../assets/figs/web-1.4.6+/myagents/00-overview.png" alt="DeepTutor My Agents overview" width="900">
</div>

My Agents दूसरे agents को DeepTutor के लिए context बनाता है, और दो अलग काम करता है। **लाइव एजेंट कनेक्ट करें** — आपकी machine पर Claude Code या Codex CLI, या आपके Partners में से एक — और इसे chat turn के अंदर से consult करें: DeepTutor actually दूसरे agent को run करता है और इसके काम को `consult_subagent` tool के जरिए Activity panel में stream करता है। इसे Agent chip से select करें (या @ type करें), और set करें कि consult कितने rounds ले सकता है।

**पिछली बातचीत इम्पोर्ट करें** — अपनी existing Claude Code और Codex history को named, searchable, resumable agents के रूप में bring in करें। Import करने के लिए कौन से days लेने हैं चुनें; refreshing उन्हें re-sync करता है। किसी भी chat turn से imported conversation को + → My Agents के जरिए reference करें, और DeepTutor इसे एक third-party transcript के रूप में पढ़ता है — यह उनकी conversation रहती है, DeepTutor की अपनी आवाज नहीं।

<div align="center">
<img src="../../assets/figs/web-1.4.6+/home/08-subagent%20demo%20with%20claude%20code.png" alt="Subagent demo with Claude Code" width="900">
</div>

### ✍️ Co-Writer

<div align="center">
<img src="../../assets/figs/web-1.4.6+/co-writer/00-overview.png" alt="DeepTutor Co-Writer overview" width="900">
</div>

Co-Writer reports, tutorials, notes, और long-form learning artifacts के लिए एक स्प्लिट-व्यू Markdown workspace है। Documents autosave होते हैं और live preview render करते हैं (KaTeX math, diagram fences), और जब draft reusable context बन जाए तो notebooks में save किए जा सकते हैं।

इसका defining idea सर्जिकल एडिटिंग है: एक span select करें और DeepTutor से rewrite, expand, या shorten करने के लिए कहें। Edit agent change को एक knowledge base या web evidence में ground कर सकता है, अपने tool calls का trace रखता है, और हर change को accept/reject diff दिखाएं के रूप में present करता है — इसलिए कुछ भी land नहीं होता जब तक आप approve नहीं करते।

<div align="center">
<img src="../../assets/figs/web-1.4.6+/co-writer/01-edit%20panel.png" alt="Co-Writer edit panel" width="900">
</div>

### 📖 बुक

<div align="center">
<img src="../../assets/figs/web-1.4.6+/book/00-book_overview.png" alt="DeepTutor book overview" width="900">
</div>

<p align="center">
<img src="../../assets/figs/web-1.4.6+/book/01-book-demo-quiz%20card.png" alt="Book quiz card" width="31%">
&nbsp;
<img src="../../assets/figs/web-1.4.6+/book/02-book-demo-manim%20video.png" alt="Book manim video" width="31%">
&nbsp;
<img src="../../assets/figs/web-1.4.6+/book/03-book-demo%20interactive%20module.png" alt="Book interactive module" width="31%">
</p>

Book selected sources को एक interactive living book में बदलता है — एक static PDF नहीं, बल्कि typed blocks से बना एक reading environment। एक book knowledge bases, notebooks, question banks, या chat history से शुरू हो सकती है; creation flow content generate होने से पहले एक chapter outline propose करता है, इसलिए आप blind one-shot output accept करने की बजाय shape review करते हैं।

हर chapter typed blocks में compile होती है — text, callouts, quizzes, flash cards, timelines, code, figures, interactive HTML, animations, concept graphs, deep dives, और user notes — और हर page का अपना Page Chat है। Blocks editable हैं: chapter rewrite किए बिना किसी block को insert, move, regenerate, या उसका type switch करें।

### 📚 नॉलेज सेंटर

<div align="center">
<img src="../../assets/figs/web-1.4.6+/knowledge/00-overview.png" alt="DeepTutor Knowledge Center overview" width="900">
</div>

Knowledge bases RAG के पीछे document collections हैं — वे Chat turns, Co-Writer edits, Book generation, और Partner conversations को ground करते हैं। जो distinctive है वह है retrieval engines का choice: LlamaIndex (default, local vector + BM25), PageIndex (hosted, reasoning retrieval with page-level citations), GraphRAG और LightRAG (knowledge-graph retrieval), या एक linked Obsidian vault जिसे tutor in-place पढ़ता और लिखता है। हर KB को एक engine द्वारा index किया जाता है।

KB बनाते समय, आप either new create करते हैं (documents upload करें और fresh index build करें) या existing link करते हैं (कहीं और बना index reuse करें, re-index के बिना in-place पढ़ें)। Re-indexing एक नई flat version-N directory लिखता है और prior ones रखता है, इसलिए एक working index rebuild के दौरान कभी destroy नहीं होता। Document parsing — Text-only, MinerU, Docling, या markitdown — Settings → Knowledge Base में choose किया जाता है, local model downloads default रूप से off हैं।

<div align="center">
<img src="../../assets/figs/web-1.4.6+/knowledge/01-create%20knowledge%20base.png" alt="Create knowledge base" width="900">
</div>

### 🌐 लर्निंग स्पेस

<div align="center">
<img src="../../assets/figs/web-1.4.6+/learning-space/00-overview.png" alt="DeepTutor Learning Space overview" width="900">
</div>

Learning Space library और personalization layer है — वह जगह जहां persist होने वाली चीजें रहती हैं। Conversations & Materials में आपका chat history, notebooks, और एक question bank है (हर saved question आपका जवाब, reference answer, और एक explanation रखता है)। Personalization में mastery paths, personas (behavior presets जैसे peer, research-assistant, teacher), और skills (SKILL.md playbooks जिन्हें model on-demand पढ़ता है) हैं। यहां सब कुछ Chat, Partners, Co-Writer, और Book से reuse किया जा सकता है।

आपको हर skill खुद नहीं लिखनी है — Import from EduHub community catalog browse करता है और एक security gate के जरिए directly आपकी library में skill download करता है।

<div align="center">
<img src="../../assets/figs/web-1.4.6+/learning-space/07-%20download%20skills%20from%20eduhub.png" alt="Download skills from EduHub" width="900">
</div>

### 🧠 मेमोरी

<div align="center">
<img src="../../assets/figs/web-1.4.6+/memory/00-overview.png" alt="DeepTutor Memory overview" width="900">
</div>

Memory एक file-backed, three-layer system है जिसे आप पढ़, curate, और audit कर सकते हैं — जानबूझकर एक hidden vector store नहीं। L1 workspace mirror plus एक append-only event trace (`trace/<surface>/<date>.jsonl`) है; L2 per-surface curated facts (`L2/<surface>.md`) है; L3 cross-surface synthesis (`L3/<profile|recent|scope>.md`) है। क्योंकि L2 L1 cite करता है और L3 L2 cite करता है, आपके profile में कुछ भी unaccountable नहीं है।

Memory Graph पूरा pyramid दिखाता है — L3 synthesis centre में, L2 middle ring में, L1 traces outside में — इसलिए आप किसी भी synthesized claim को उसके पीछे exact raw event तक trace कर सकते हैं। Memory chat, notebook, quiz, kb, book, partner, और cowriter surfaces पर track किया जाता है; consolidator के Update / Audit / Dedup budgets Settings → Memory में tune किए जाते हैं।

<div align="center">
<img src="../../assets/figs/web-1.4.6+/memory/01-3%20layer%20memory%20graph.png" alt="3-layer memory graph" width="900">
</div>

### ⚙️ सेटिंग्स

<div align="center">
<img src="../../assets/figs/web-1.4.6+/settings/00-setting%20overview.png" alt="DeepTutor Settings overview" width="900">
</div>

Settings operational control plane है, एक live status strip (Backend, LLM, Embedding, Search) और प्रत्येक area के लिए एक card के साथ: Appearance (theme + UI language), Network (API base, ports, CORS), Models (LLM, Embedding, Search, Text-to-Speech, Speech-to-Text, Image Generation, Video Generation), Knowledge Base (document parsing engine), Chat (tools, MCP servers, per-capability parameters), Partners & Agents (वे subagents जिन्हें आप turn से consult कर सकते हैं), और Memory (consolidator के budgets)।

अधिकांश sections एक draft-and-apply flow उपयोग करते हैं, इसलिए आप provider को commit करने से पहले test कर सकते हैं। चार themes box में आते हैं — Default, Cream, Dark, और Glass। Project-root `.env` files जानबूझकर ignored हैं; runtime configuration `data/user/settings/*.json` के नीचे रहती है जब तक कि `DEEPTUTOR_HOME` या `deeptutor start --home` app को कहीं और point न करे।

<div align="center">
<img src="../../assets/figs/web-1.4.6+/settings/01-appearance%20settings.png" alt="Appearance settings" width="900">
</div>

---

## ⌨️ DeepTutor CLI — एजेंट-नेटिव इंटरफेस

DeepTutor CLI-native है: same `deeptutor` entry point workspace initialize कर सकता है, web app start कर सकता है, one-shot capability run कर सकता है, interactive REPL खोल सकता है, knowledge bases manage कर सकता है, sessions inspect कर सकता है, books maintain कर सकता है, और partners operate कर सकता है।

```bash
deeptutor run chat "Explain Fourier transform" --tool rag --kb textbook
deeptutor run deep_solve "Solve x^2 = 4" --tool reason
deeptutor chat --capability deep_research --kb papers
deeptutor partner create math-tutor --soul "Socratic math tutor"
deeptutor kb create calculus --doc textbook.pdf
```

<details>
<summary><b>Command reference</b></summary>

| Command | विवरण |
|:---|:---|
| `deeptutor init` | Current workspace के लिए `data/user/settings` create या update करें |
| `deeptutor start [--home PATH]` | Backend + frontend को एक साथ launch करें |
| `deeptutor serve [--port PORT]` | केवल FastAPI backend start करें |
| `deeptutor run <capability> <message>` | एक single capability turn run करें (`chat`, `deep_solve`, `deep_question`, `deep_research`, `visualize`, `math_animator`, `auto`, `mastery_path`) |
| `deeptutor chat` | capability, tool, KB, notebook, और history controls के साथ Interactive REPL |
| `deeptutor partner list/create/start/stop` | IM-connected partners manage करें |
| `deeptutor kb list/info/create/add/search/set-default/delete` | LlamaIndex knowledge bases manage करें |
| `deeptutor memory show/clear` | L2/L3 memory docs inspect करें या L1/all memory clear करें |
| `deeptutor session list/show/open/rename/delete` | Shared sessions manage करें |
| `deeptutor notebook list/create/show/add-md/replace-md/remove-record` | Markdown files से notebooks manage करें |
| `deeptutor book list/health/refresh-fingerprints` | Books inspect करें और source fingerprints refresh करें |
| `deeptutor skill search/install/list/remove/login/publish/update` | स्किल्स प्रबंधित करें, हब से इंस्टॉल करें, और अपनी स्किल्स पब्लिश करें (डिफ़ॉल्ट `eduhub:<slug>`) |
| `deeptutor plugin list/info` | Registered tools और capabilities inspect करें |
| `deeptutor config show` | Configuration summary print करें |
| `deeptutor provider login <provider>` | जहां supported हो provider OAuth login manage करें |

</details>

CLI-only distribution `packaging/deeptutor-cli` में present है; इस checkout में इसे `python -m pip install -e ./packaging/deeptutor-cli` से source से install किया जाना चाहिए। Public `deeptutor-cli` package currently PyPI पर उपलब्ध नहीं है, इसलिए main Get Started section source-install path रखता है।

---

## 👥 मल्टी-यूजर — साझा Deployments

प्रमाणीकरण default रूप से बंद है — DeepTutor single-user चलता है। इसे on करें और एक `data/` tree एक admin workspace, isolated per-user workspaces, और partner workspaces को side by side host करती है:

```text
data/
├── user/                    # Admin workspace + global settings
├── users/<uid>/             # Per-user scope: chat history, memory, notebooks, KBs
├── partners/<id>/workspace/ # Partner (synthetic-user) scope
└── system/                  # auth/users.json · grants/<uid>.json · audit/usage.jsonl
```

पहला पंजीकृत user admin बनता है और model catalogs, provider credentials, shared knowledge bases, skills, और per-user grants own करता है। बाकी सभी को isolated workspace और redacted Settings page मिलती है — admin-assigned models, KBs, और skills scoped, read-only options के रूप में दिखाई देते हैं, कभी raw API keys के रूप में नहीं।

इसे enable करें: `data/user/settings/auth.json` में auth on करें, `deeptutor start` restart करें, `/register` पर पहला admin register करें, फिर `/admin/users` से users add करें और grants के जरिए models, KBs, skills, tool/MCP policy, और code-execution access assign करें।

---

## 🧩 इकोसिस्टम — EduHub और Skills Community

DeepTutor skills open Agent-Skills format उपयोग करती हैं — एक `SKILL.md` playbook (YAML frontmatter + Markdown) और optional reference files के साथ एक folder। DeepTutor में EduHub (https://eduhub.deeptutor.info/) डिफ़ॉल्ट हब के रूप में बिल्ट-इन है — हमारी अपनी education-focused skill registry — configure करने की कोई जरूरत नहीं।

<details>
<summary><b>EduHub — DeepTutor का स्किल इकोसिस्टम</b></summary>

EduHub community hub है जिसे DeepTutor ने teaching-oriented agent skills share करने के लिए launch किया — Socratic tutors, flashcard builders, essay feedback, exam blueprints, concept explainers, और बहुत कुछ। यह DeepTutor में built in है, इसलिए configure करने की कोई जरूरत नहीं: एक bare slug या `eduhub:` prefix इसे resolve करता है।

**सर्च करें और इंस्टॉल करें** — browser में, Learning Space → Skills → Import from EduHub खोलें catalog browse करने और directly आपकी library में skill download करने के लिए। Terminal से:

```bash
deeptutor skill search "socratic tutor"               # EduHub खोजें (default hub)
deeptutor skill install socratic-tutor                # fetch → verify → register
deeptutor skill install eduhub:socratic-tutor@1.2.0   # hub और version pin करें
deeptutor skill list                                  # अपने hub provenance के साथ local skills
```

**अपनी स्किल्स पब्लिश करें** — एक `SKILL.md` package करें और community के साथ share करें:

```bash
deeptutor skill login                                 # EduHub पर browser sign-in
deeptutor skill publish ./my-skill                    # interactive: track + tags चुनें, फिर upload
deeptutor skill update                                # roll back या नया version release करें
```

EduHub एक standalone, ClawHub-compatible registry भी है, इसलिए agents जो DeepTutor नहीं हैं (Claude Code, Codex, …) इसे eduhub CLI के जरिए directly use कर सकते हैं — `npx eduhub install socratic-tutor`।

</details>

<details>
<summary><b>इम्पोर्ट सेफ्टी गेट</b></summary>

Source चाहे जो भी हो, हर import आपके workspace को touch करने से पहले same safety gate से गुजरता है:

- Registry का security verdict पहले check होता है — flagged packages refuse किए जाते हैं जब तक आप `--allow-unverified` pass नहीं करते;
- Archives defensively extract होते हैं (zip-slip / zip-bomb guards) text/script suffix whitelist के पीछे, इसलिए binaries workspace में कभी नहीं आते;
- Frontmatter normalize होता है और `always:` strip होता है, इसलिए एक downloaded skill खुद को हर system prompt में force नहीं कर सकती;
- Provenance — hub, version, verdict, और install time — `.hub-lock.json` में लिखा जाता है audits और updates के लिए।

Multi-user deployments में, installing admin-only है।

</details>

<details>
<summary><b>ClawHub के साथ भी संगत (--hub clawhub)</b></summary>

क्योंकि DeepTutor open Agent-Skills format बोलता है, ClawHub (https://clawhub.ai/) भी एक first-class source है। इसे hub prefix से चुनें:

```bash
deeptutor skill search "git release notes" --hub clawhub
deeptutor skill install clawhub:git-release-notes@1.0.1
```

`settings/skill_hubs.json` में और registries add करें।

</details>

---

## 🌐 समुदाय

DeepTutor [Bingxi Zhao](https://github.com/pancacake) द्वारा HKUDS ग्रुप में lead किया जाता है, open-source है, कोई paid products नहीं हैं। संपर्क: bingxizhao39@gmail.com

**आभार:** Chao Huang, HKUDS labmates (Jiahao Zhang, Zirui Guo, Xubin Ren), और open-source community का विशेष आभार।

DeepTutor outstanding open-source projects के कंधों पर खड़ा है:

| Project | DeepTutor में भूमिका |
|:---|:---|
| [**LlamaIndex**](https://github.com/run-llama/llama_index) | RAG pipeline और document indexing backbone |
| [**nanobot**](https://github.com/HKUDS/nanobot) | मूल TutorBot को चलाने वाला अति-हल्का agent engine (HKUDS) |
| [**LightRAG**](https://github.com/HKUDS/LightRAG) | Knowledge-graph RAG engine (HKUDS) |
| [**AutoAgent**](https://github.com/HKUDS/AutoAgent) | Zero-code agent framework (HKUDS) |
| [**AI-Researcher**](https://github.com/HKUDS/AI-Researcher) | Automated research (HKUDS) |
| [**OpenClaw**](https://clawhub.ai/) | ClawHub — open skill registry |
| [**ManimCat**](https://github.com/Wing900/ManimCat) | Math Animator के लिए AI-driven math animation generation |
| Codex | Inspired CLI design |
| Claude Code | Inspired agent loop design |

**HKUDS ecosystem से:**

| [⚡ LightRAG](https://github.com/HKUDS/LightRAG) | [🤖 AutoAgent](https://github.com/HKUDS/AutoAgent) | [🔬 AI-Researcher](https://github.com/HKUDS/AI-Researcher) | [🧬 nanobot](https://github.com/HKUDS/nanobot) |
|:---:|:---:|:---:|:---:|
| Simple & Fast RAG | Zero-Code Agent Framework | Automated Research | Ultra-Lightweight AI Agent |

### Roadmap और योगदान

[`Roadmap issue #498`](https://github.com/HKUDS/DeepTutor/issues/498) पर roadmap items के लिए vote करें या नए propose करें। Development environment setup, code standards, और pull request workflow के लिए [CONTRIBUTING.md](../../CONTRIBUTING.md) देखें।

<div align="center">

हम आशा करते हैं कि DeepTutor community के लिए एक उपहार बने। 🎁

<a href="https://github.com/HKUDS/DeepTutor/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=HKUDS/DeepTutor&max=999" alt="Contributors" />
</a>

</div>

## ⭐ Star History

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

[⭐ हमें Star करें](https://github.com/HKUDS/DeepTutor/stargazers) · [🐛 Bug report करें](https://github.com/HKUDS/DeepTutor/issues) · [💬 Discussions](https://github.com/HKUDS/DeepTutor/discussions)

---

[Apache License 2.0](../../LICENSE) के तहत licensed।

<p>
  <img src="https://visitor-badge.laobi.icu/badge?page_id=HKUDS.DeepTutor&style=for-the-badge&color=00d4ff" alt="Views">
</p>

</div>
