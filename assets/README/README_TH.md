<div align="center">

<p align="center"><img src="../../assets/figs/logo/logo.png" alt="DeepTutor logo" height="56" style="vertical-align: middle;">&nbsp;<img src="../../assets/figs/logo/banner.png" alt="DeepTutor" height="48" style="vertical-align: middle;"></p>

# DeepTutor: การสอนพิเศษส่วนตัวแบบ Agent-Native

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
  <a href="README_HI.md"><img alt="Hindi" height="40" src="https://img.shields.io/badge/Hindi-CDCFD4"></a>&nbsp;
  <a href="README_PT.md"><img alt="Português" height="40" src="https://img.shields.io/badge/Português-CDCFD4"></a>&nbsp;
  <a href="README_TH.md"><img alt="Thai" height="40" src="https://img.shields.io/badge/Thai-BCDCF7"></a>&nbsp;
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

[คุณสมบัติ](#-คุณสมบัติหลัก) · [เริ่มต้น](#-เริ่มต้น) · [สำรวจ](#-สำรวจ-deeptutor) · [CLI](#️-deeptutor-cli--อินเทอร์เฟซ-agent-native) · [หลายผู้ใช้](#-หลายผู้ใช้--การปรับใช้แบบแชร์) · [ชุมชน](#-ชุมชนและระบบนิเวศ)

</div>

---

> 🤝 **เรายินดีรับการมีส่วนร่วมทุกรูปแบบ!** โหวตรายการ roadmap หรือเสนอรายการใหม่ที่ [`Roadmap`](https://github.com/HKUDS/DeepTutor/issues/498) และดู [คู่มือการมีส่วนร่วม](../../CONTRIBUTING.md) สำหรับกลยุทธ์ branching มาตรฐานการเขียนโค้ด และวิธีเริ่มต้น

### 📦 การเปิดตัว

> **[2026.6.12]** [v1.4.3](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.3) — TutorBot กลายเป็น **Partners** บน IM pipeline ระดับ production พร้อมการตอบกลับแบบ live streaming และ 15 ช่องทาง, Chat ย้ายไปใช้ agent loop เดียว, การแยกส่วนต่อผู้ใช้จริงสำหรับการปรับใช้แบบหลายผู้ใช้, Visualize สร้างใหม่พร้อม local validate+repair บวกกับการอัพเกรดใน Co-writer, file viewer, MinerU cloud parsing และ CLI เอกสารได้รับการรีเฟรชอย่างสมบูรณ์ที่ [deeptutor.info](https://deeptutor.info/)

> **[2026.5.28]** [v1.4.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.2) — ความเสถียรภาพ + ความเรียบร้อยใน v1.4.1: Gemini 2.5+ ปลดล็อคใน Visualize และ Chat, การแก้ไข ContextVar auth-routing (#485), โปรโตคอล label ของ reasoning + native-tools แข็งแกร่งขึ้น, UX การ streaming ที่ราบรื่นในทุกพื้นที่ chat, แถบด้านข้าง Recents แบบพับได้ใหม่ และรองรับ local provider Lemonade

> **[2026.5.27]** [v1.4.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.1) — แพตช์ความปลอดภัย + ความเสถียรภาพ: ล็อค sandbox ของเครื่องมือ TutorBot, การแยกส่วนทรัพยากรต่อผู้ใช้, การ fallback ภาพ multimodal สำหรับ provider ที่มีความสามารถ vision, API HTTP/SSE สำหรับคุยกับ TutorBot และการแก้ไข chat regression ของ v1.4.0

> **[2026.5.22]** [v1.4.0](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.0) — GA cut ของ v1.4: Auto Mode, Memory สามชั้น, Deep Research / Solve / Question แบบ agentic, การ refactor RAG ด้วย LlamaIndex, การรวม Visualize/Animator, การทำให้ reasoning-effort เป็นมาตรฐาน, tool-schema fallback และ turn runtime ที่ปลอดภัยต่อการรีสตาร์ท

<details>
<summary><b>การเปิดตัวที่ผ่านมา (มากกว่า 2 สัปดาห์)</b></summary>

> **[2026.5.21]** [v1.4.0-beta](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.0-beta) — เวิร์กเบนช์ Memory สามชั้น (L1/L2/L3), ความสามารถ chat ทั้งหมดสร้างใหม่บน agentic engine เดียว, RAG เฉพาะ LlamaIndex และพื้นที่ Settings + Capabilities แบบรวม

> **[2026.5.10]** [v1.3.10](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.10) — การกู้คืน CORS ของ Docker ระยะไกล, `DISABLE_SSL_VERIFY` สำหรับ SDK providers, การอ้างอิง code-block ที่ปลอดภัยขึ้น และ Matrix E2EE add-on แบบเสริม

> **[2026.5.9]** [v1.3.9](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.9) — รองรับ Zulip และ NVIDIA NIM สำหรับ TutorBot, การ routing ของ thinking-model ที่ปลอดภัยขึ้น, `deeptutor start`, tooltips แถบด้านข้าง และความเท่าเทียมของ session-store

> **[2026.5.8]** [v1.3.8](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.8) — การปรับใช้แบบหลายผู้ใช้แบบเสริมพร้อม workspace ผู้ใช้แบบแยกส่วน, admin grants, auth routes และการเข้าถึง runtime แบบจำกัดขอบเขต

> **[2026.5.4]** [v1.3.7](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.7) — การแก้ไข thinking-model/provider, ประวัติดัชนี Knowledge ที่มองเห็นได้ และการแก้ไข template/การล้าง Co-Writer ที่ปลอดภัยขึ้น

> **[2026.5.3]** [v1.3.6](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.6) — การเลือก model จาก catalog สำหรับ chat และ TutorBot, การ re-indexing RAG ที่ปลอดภัยขึ้น, การแก้ไขขีดจำกัด token ของ OpenAI Responses และการตรวจสอบ Skills editor

> **[2026.5.2]** [v1.3.5](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.5) — การตั้งค่าการเปิดตัว local ที่ราบรื่นขึ้น, RAG queries ที่ปลอดภัยขึ้น, auth การ embedding local ที่ชัดเจนขึ้น และการปรับปรุง dark-mode ของ Settings

> **[2026.5.1]** [v1.3.4](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.4) — การคงอยู่ของ chat ในหน้า Book และขั้นตอนการสร้างใหม่, การอ้างอิงจาก chat ไปยัง Book, การจัดการภาษา/ความคิดที่แข็งแกร่งขึ้น, การดึงเอกสาร RAG ที่แข็งแกร่งขึ้น

> **[2026.4.30]** [v1.3.3](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.3) — รองรับ embedding NVIDIA NIM + Gemini, บริบท Space แบบรวมสำหรับประวัติ chat/skills/memory, session snapshots, ความยืดหยุ่นของการ re-index RAG

> **[2026.4.29]** [v1.3.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.2) — URL endpoint การ embedding แบบโปร่งใส, ความยืดหยุ่นของการ re-index RAG สำหรับ vectors ที่คงอยู่ไม่ถูกต้อง, การล้าง memory สำหรับเอาต์พุต thinking-model, การแก้ไข Deep Solve runtime

> **[2026.4.28]** [v1.3.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.1) — ความเสถียรภาพ: การ routing RAG และการตรวจสอบ embedding ที่ปลอดภัยขึ้น, ความคงอยู่ของ Docker, การป้อนข้อมูลที่ปลอดภัยสำหรับ IME, ความแข็งแกร่งของ Windows/GBK

> **[2026.4.27]** [v1.3.0](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.0) — ดัชนี KB แบบ versioned พร้อมขั้นตอนการ re-index, workspace Knowledge ที่สร้างใหม่, การค้นพบ embedding อัตโนมัติพร้อม adapters ใหม่, Space hub

> **[2026.4.25]** [v1.2.5](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.5) — ไฟล์แนบ chat ที่คงอยู่พร้อม drawer ดูตัวอย่างไฟล์, pipeline ความสามารถที่รับรู้ไฟล์แนบ, การส่งออก Markdown ของ TutorBot

> **[2026.4.25]** [v1.2.4](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.4) — ไฟล์แนบข้อความ/โค้ด/SVG, Setup Tour คำสั่งเดียว, การส่งออก Markdown ของ chat, UI การจัดการ KB แบบกะทัดรัด

> **[2026.4.24]** [v1.2.3](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.3) — ไฟล์แนบเอกสาร (PDF/DOCX/XLSX/PPTX), การแสดงบล็อก thinking ของ reasoning, ตัวแก้ไข template Soul, การบันทึก Co-Writer ลง notebook

> **[2026.4.22]** [v1.2.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.2) — ระบบ Skills ที่ผู้ใช้สร้าง, การปรับปรุงประสิทธิภาพการป้อนข้อมูล chat, การเริ่ม TutorBot อัตโนมัติ, UI Book Library, การดู visualization แบบเต็มหน้าจอ

> **[2026.4.21]** [v1.2.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.1) — ขีดจำกัด token ต่อขั้นตอน, การสร้างการตอบกลับใหม่ในทุกจุดเข้าถึง, การแก้ไขความเข้ากันได้ของ RAG และ Gemma

> **[2026.4.20]** [v1.2.0](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.0) — คอมไพเลอร์ "หนังสือมีชีวิต" Book Engine, Co-Writer หลายเอกสาร, visualization HTML แบบโต้ตอบ, @-mention ของ Question Bank

> **[2026.4.18]** [v1.1.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.1.2) — แท็บ Channels ที่ขับเคลื่อนด้วย schema, การรวม RAG pipeline เดียว, การ externalize prompts ของ chat

> **[2026.4.17]** [v1.1.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.1.1) — "ตอบตอนนี้" สากล, การซิงค์การเลื่อน Co-Writer, แผงการตั้งค่าแบบรวม, ปุ่ม Stop ของ streaming

> **[2026.4.15]** [v1.1.0](https://github.com/HKUDS/DeepTutor/releases/tag/v1.1.0) — การปรับปรุงคณิตศาสตร์บล็อก LaTeX, โพรบการวินิจฉัย LLM, คำแนะนำ Docker + LLM ในเครื่อง

> **[2026.4.14]** [v1.1.0-beta](https://github.com/HKUDS/DeepTutor/releases/tag/v1.1.0-beta) — session ที่บุ๊กมาร์กได้, ธีม Snow, WebSocket heartbeat & auto-reconnect, การปรับปรุง embedding registry

> **[2026.4.13]** [v1.0.3](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.3) — Question Notebook พร้อมบุ๊กมาร์กและหมวดหมู่, Mermaid ใน Visualize, การตรวจจับความไม่ตรงกันของ embedding, ความเข้ากันได้กับ Qwen/vLLM, รองรับ LM Studio & llama.cpp และธีม Glass

> **[2026.4.11]** [v1.0.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.2) — การรวม search พร้อม SearXNG fallback, การแก้ไขการเปลี่ยน provider, การแก้ไขการรั่วไหลของทรัพยากร frontend

> **[2026.4.10]** [v1.0.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.1) — ความสามารถ Visualize (Chart.js/SVG), การป้องกัน quiz ซ้ำ, รองรับ model o4-mini

> **[2026.4.10]** [v1.0.0-beta.4](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.0-beta.4) — การติดตามความคืบหน้าของ embedding พร้อม retry ขีดจำกัด rate, การแก้ไข dependency ข้ามแพลตฟอร์ม, การแก้ไข MIME validation

> **[2026.4.8]** [v1.0.0-beta.3](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.0-beta.3) — SDK OpenAI/Anthropic แบบ native (ลบ litellm), รองรับ Windows Math Animator, การแยกวิเคราะห์ JSON ที่แข็งแกร่ง และ i18n ภาษาจีนแบบสมบูรณ์

> **[2026.4.7]** [v1.0.0-beta.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.0-beta.2) — การโหลดการตั้งค่าใหม่แบบ hot, เอาต์พุต MinerU แบบซ้อน, การแก้ไข WebSocket และขั้นต่ำ Python 3.11+

> **[2026.4.4]** [v1.0.0-beta.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.0-beta.1) — การเขียนสถาปัตยกรรม agent-native ใหม่ (~200k บรรทัด): โมเดล plugin Tools + Capabilities, CLI & SDK, TutorBot, Co-Writer, Guided Learning และ memory ถาวร

> **[2026.1.23]** [v0.6.0](https://github.com/HKUDS/DeepTutor/releases/tag/v0.6.0) — ความคงอยู่ของ session, การอัพโหลดเอกสารแบบ incremental, การนำเข้า RAG pipeline แบบยืดหยุ่น และการแปลภาษาจีนแบบสมบูรณ์

> **[2026.1.18]** [v0.5.2](https://github.com/HKUDS/DeepTutor/releases/tag/v0.5.2) — รองรับ Docling สำหรับ RAG-Anything, การปรับปรุงระบบ log และการแก้ไขบัก

> **[2026.1.15]** [v0.5.0](https://github.com/HKUDS/DeepTutor/releases/tag/v0.5.0) — การกำหนดค่าบริการแบบรวม, การเลือก RAG pipeline ต่อ knowledge base, การปรับปรุงการสร้างคำถาม และการปรับแต่ง sidebar

> **[2026.1.9]** [v0.4.0](https://github.com/HKUDS/DeepTutor/releases/tag/v0.4.0) — รองรับ LLM & embedding หลาย provider, หน้าแรกใหม่, การแยก RAG module และการ refactor ตัวแปรสภาพแวดล้อม

> **[2026.1.5]** [v0.3.0](https://github.com/HKUDS/DeepTutor/releases/tag/v0.3.0) — สถาปัตยกรรม PromptManager แบบรวม, GitHub Actions CI/CD และ images Docker ที่สร้างล่วงหน้าบน GHCR

> **[2026.1.2]** [v0.2.0](https://github.com/HKUDS/DeepTutor/releases/tag/v0.2.0) — การปรับใช้ Docker, การอัพเกรด Next.js 16 & React 19, การเสริมความปลอดภัย WebSocket และการแก้ไขช่องโหว่ที่สำคัญ

</details>

### 📰 ข่าวสาร

> **[2026.5.22]** 🌐 เว็บไซต์เอกสารอย่างเป็นทางการของเราเปิดตัวแล้วที่ [**deeptutor.info**](https://deeptutor.info/) — คู่มือ การอ้างอิง และ capability tours ทั้งหมดในที่เดียว

> **[2026.4.19]** 🎉 เราถึง 20k stars ใน 111 วัน! ขอบคุณสำหรับการสนับสนุนที่น่าเหลือเชื่อ — เรามุ่งมั่นที่จะพัฒนาต่อเนื่องเพื่อการสอนพิเศษที่เป็นส่วนตัวและชาญฉลาดอย่างแท้จริงสำหรับทุกคน

> **[2026.4.10]** 📄 บทความของเราตอนนี้มีอยู่บน arXiv แล้ว! อ่าน [preprint](https://arxiv.org/abs/2604.26962) เพื่อเรียนรู้เพิ่มเติมเกี่ยวกับการออกแบบและแนวคิดที่อยู่เบื้องหลัง DeepTutor

> **[2026.4.4]** นานมาแล้ว! ✨ DeepTutor v1.0.0 มาถึงแล้ว — การพัฒนาแบบ agent-native ที่มีการเขียนสถาปัตยกรรมจากศูนย์ TutorBot และการสลับ mode แบบยืดหยุ่นภายใต้ใบอนุญาต Apache-2.0 บทใหม่เริ่มต้นแล้ว และเรื่องราวของเรายังคงดำเนินต่อไป!

> **[2026.2.6]** 🚀 เราถึง 10k stars ในเพียง 39 วัน! ขอบคุณชุมชนที่น่าเหลือเชื่อของเราอย่างยิ่ง!

> **[2026.1.1]** สวัสดีปีใหม่! เข้าร่วม [Discord](https://discord.gg/eRsjPgMU4t), [WeChat](https://github.com/HKUDS/DeepTutor/issues/78) หรือ [Discussions](https://github.com/HKUDS/DeepTutor/discussions) ของเรา — มาร่วมกันกำหนดอนาคตของ DeepTutor!

> **[2025.12.29]** DeepTutor ได้รับการเปิดตัวอย่างเป็นทางการแล้ว!

## ✨ คุณสมบัติหลัก

DeepTutor ถูกจัดระเบียบรอบ runtime แบบ agent-native: ChatOrchestrator ที่แชร์กันจะ route ทุก turn ไปยัง capabilities, ToolRegistry จะเปิดเผยเครื่องมือแบบ single-shot เมื่อ model ต้องการ และ CapabilityRegistry จะให้ workflow ที่ลึกกว่าเข้าควบคุม turn เมื่องานต้องการโครงสร้าง

<div align="center">
<img src="../../assets/figs/system/system%20architecture.png" alt="สถาปัตยกรรมระบบ DeepTutor" width="900">
</div>

**พื้นที่การเรียนรู้เดียว**

- **Chat เป็น loop เริ่มต้น** — การสอนพิเศษทั่วไป, Q&A ที่อ้างอิงแหล่งที่มา, Deep Solve, Deep Question, Deep Research, Visualize และ Auto Mode ทั้งหมดแชร์บริบท session และ inventory แหล่งที่มาเดียวกัน
- **พื้นที่การเรียนรู้ที่เชื่อมต่อกัน** — ร่าง Co-Writer, หน้า Book, Knowledge Bases, assets ใน Space และ Memory เป็น workspace แยกกัน แต่ทั้งหมดป้อนข้อมูลให้ agent runtime เดียวกันแทนที่จะกลายเป็นแอปที่แยกจากกัน
- **Partners สำหรับความเป็นเพื่อนถาวร** — เพื่อนที่เชื่อมต่อผ่าน IM ตอนนี้ทำงานบน chat agent loop เดียวกับผลิตภัณฑ์หลัก พร้อม workspace สังเคราะห์และห้องสมุดที่กำหนดเองของตัวเอง

**เครื่องมือ memory และการควบคุม**

- **เครื่องมือที่ประกอบได้** — RAG, การอ่านแหล่งที่มา, การอ่าน/เขียน memory, notebooks, การดึง URL, การค้นหา GitHub, การหยุดถามผู้ใช้, การรันแบบ sandbox และเครื่องมือ brainstorm/web/paper/reason แบบเสริมสามารถติดตั้งได้ตามบริบทและการตั้งค่า
- **Memory สามชั้น** — traces L1, สรุปต่อพื้นที่ L2 และการสังเคราะห์ข้ามพื้นที่ L3 ทำให้การ personalization สามารถตรวจสอบได้แทนที่จะซ่อนอยู่หลัง black box
- **การตั้งค่าและ CLI แบบรวม** — catalogs ของ model, embeddings, การค้นหา, เครือข่าย, เซิร์ฟเวอร์ MCP, เครื่องมือ, capabilities และการตั้งค่าการปรับใช้สามารถแก้ไขได้จาก web UI และเขียนสคริปต์ได้จาก `deeptutor`

---

## 🚀 เริ่มต้น

DeepTutor มีเส้นทางการติดตั้งสี่เส้นทาง ทั้งหมดแชร์ layout workspace เดียว: การตั้งค่าอยู่ใน `data/user/settings/` ภายใต้ไดเร็กทอรีที่คุณเปิดตัว (หรือภายใต้ `DEEPTUTOR_HOME` / `deeptutor start --home` หากคุณตั้งค่าไว้อย่างชัดเจน) สำหรับแอปเต็มรูปแบบ ขั้นตอนที่แนะนำคือ **เลือกไดเร็กทอรี workspace → ติดตั้ง → `deeptutor init` → `deeptutor start`**

> ✨ **v1.4.3 พร้อมใช้งาน** `pip install -U deeptutor` จะดึงเวอร์ชันที่เสถียรล่าสุด Pre-releases (เมื่อพร้อมใช้งาน) เลือกใช้ได้ด้วย `pip install --pre -U deeptutor`

### ตัวเลือกที่ 1 — ติดตั้งจาก PyPI

แอป Web local แบบเต็มรูปแบบ + CLI ไม่ต้องโคลน ต้องการ **Python 3.11+** และ runtime **Node.js 20+** บน PATH (เซิร์ฟเวอร์ standalone Next.js ที่แพ็คไว้จะถูกเปิดตัวโดย `deeptutor start`)

```bash
mkdir -p my-deeptutor && cd my-deeptutor
pip install -U deeptutor
deeptutor init     # ขอพอร์ต + LLM provider + embedding แบบเสริม
deeptutor start    # เริ่ม backend + frontend; เปิด terminal ไว้
```

`deeptutor init` จะขอพอร์ต backend (ค่าเริ่มต้น `8001`), พอร์ต frontend (ค่าเริ่มต้น `3782`), LLM provider / base URL / API key / model และ embedding provider แบบเสริมสำหรับ Knowledge Base / RAG

หลังจาก `deeptutor start` ให้เปิด URL ของ frontend ที่พิมพ์ใน terminal — ค่าเริ่มต้น [http://127.0.0.1:3782](http://127.0.0.1:3782) กด `Ctrl+C` ใน terminal นั้นเพื่อหยุดทั้ง backend และ frontend การข้าม `deeptutor init` ก็ใช้ได้สำหรับการทดลองอย่างรวดเร็ว แอปจะบูตด้วยพอร์ตเริ่มต้นและการตั้งค่า model ว่าง กำหนดค่าในภายหลังใน **Settings → Models**

### ตัวเลือกที่ 2 — ติดตั้งจาก Source

สำหรับการพัฒนาจาก checkout ใช้ **Python 3.11+** และ **Node.js 22 LTS** เพื่อให้ตรงกับ CI และ Docker

```bash
git clone https://github.com/HKUDS/DeepTutor.git
cd DeepTutor

# สร้าง venv (macOS/Linux). Windows PowerShell:
#   py -3.11 -m venv .venv ; .\.venv\Scripts\Activate.ps1
python3 -m venv .venv && source .venv/bin/activate
python -m pip install --upgrade pip

# ติดตั้ง backend + frontend deps
python -m pip install -e .
( cd web && npm ci --legacy-peer-deps )

deeptutor init
deeptutor start
```

<details>
<summary><b>สภาพแวดล้อม Conda</b> (แทน <code>venv</code>)</summary>

```bash
conda create -n deeptutor python=3.11
conda activate deeptutor
python -m pip install --upgrade pip
```

</details>

<details>
<summary><b>Extras การติดตั้งแบบเสริม</b> — dev / partners / matrix / math-animator</summary>

```bash
pip install -e ".[dev]"             # เครื่องมือ tests/lint
pip install -e ".[partners]"        # SDKs ช่องทาง IM ของ Partners + MCP client
pip install -e ".[matrix]"          # ช่องทาง Matrix โดยไม่มี E2EE/libolm
pip install -e ".[matrix-e2e]"      # Matrix E2EE; ต้องการ libolm
pip install -e ".[math-animator]"   # Manim addon; ต้องการ LaTeX/ffmpeg/system libs
```

</details>

<details>
<summary><b>การแก้ปัญหาเซิร์ฟเวอร์ dev</b></summary>

```bash
rm -f web/.next/dev/lock web/.next/lock
deeptutor start
```

</details>

### ตัวเลือกที่ 3 — Docker

```bash
docker run --rm --name deeptutor \
  -p 127.0.0.1:3782:3782 \
  -p 127.0.0.1:8001:8001 \
  -v deeptutor-data:/app/data \
  ghcr.io/hkuds/deeptutor:latest
```

> ⚠️ **Map ทั้ง `3782` และ `8001`** `3782` ให้บริการ web UI; `8001` คือ FastAPI backend ที่เบราว์เซอร์ของคุณเรียกโดยตรง — ไม่มี proxy ภายใน container

เปิด [http://127.0.0.1:3782](http://127.0.0.1:3782)

**Remote Docker / reverse proxy:**
```json
{
  "next_public_api_base_external": "https://deeptutor.example.com"
}
```

<details>
<summary><b>การเชื่อมต่อกับ Ollama / LM Studio / llama.cpp / vLLM / Lemonade บน host</b></summary>

```bash
docker run --rm --name deeptutor \
  -p 127.0.0.1:3782:3782 -p 127.0.0.1:8001:8001 \
  --add-host=host.docker.internal:host-gateway \
  -v deeptutor-data:/app/data \
  ghcr.io/hkuds/deeptutor:latest
```

- Ollama LLM: `http://host.docker.internal:11434/v1`
- Ollama embedding: `http://host.docker.internal:11434/api/embed`
- LM Studio: `http://host.docker.internal:1234/v1`
- llama.cpp: `http://host.docker.internal:8080/v1`
- Lemonade: `http://host.docker.internal:13305/api/v1`

</details>

### Sandbox การรันโค้ด (office skills)

office skills ที่ติดตั้งมา — **docx / pdf / pptx / xlsx** — ทำงานโดยให้ model เขียน Python script สั้น ๆ รันผ่านเครื่องมือ `exec` / `code_execution` และส่งคืน URL ดาวน์โหลด

`sandbox_allow_subprocess` ใน `data/user/settings/system.json` (ค่าเริ่มต้น `true`) ควบคุม sandbox ตั้งเป็น `false` หรือ export `DEEPTUTOR_SANDBOX_ALLOW_SUBPROCESS=0` เพื่อปิด

### ตัวเลือกที่ 4 — CLI เท่านั้น

```bash
git clone https://github.com/HKUDS/DeepTutor.git
cd DeepTutor
python3 -m venv .venv-cli && source .venv-cli/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ./packaging/deeptutor-cli
deeptutor init --cli
deeptutor chat
```

<details>
<summary><b>คำสั่งทั่วไป</b></summary>

```bash
deeptutor chat
deeptutor chat --capability deep_solve --tool rag --kb my-kb
deeptutor run chat "Explain Fourier transform"
deeptutor run deep_solve "Solve x^2 = 4" --tool rag --kb my-kb
deeptutor kb create my-kb --doc textbook.pdf
deeptutor memory show
deeptutor config show
```

</details>

### การอ้างอิงการกำหนดค่า

<details>
<summary><b>ไฟล์การกำหนดค่าภายใต้ <code>data/user/settings/</code></b></summary>

| ไฟล์ | วัตถุประสงค์ |
|:---|:---|
| `model_catalog.json` | โปรไฟล์ provider LLM, embedding และ search; API keys; models ที่ใช้งานอยู่ |
| `system.json` | พอร์ต backend/frontend, public API base, CORS, SSL, ไดเร็กทอรีไฟล์แนบ |
| `auth.json` | สวิตช์ auth แบบเสริม, ชื่อผู้ใช้, password hash, การตั้งค่า token/cookie |
| `integrations.json` | การตั้งค่า PocketBase แบบเสริมและการรวม sidecar |
| `interface.json` | ความชอบภาษา / ธีม / แถบด้านข้างของ UI |
| `main.yaml` | ค่าเริ่มต้นพฤติกรรม runtime และการ inject path |
| `agents.yaml` | การตั้งค่า temperature และ token ของ capability/tool |

</details>

## 📖 สำรวจ DeepTutor

### 💬 Chat — Agent Loop ที่คุณใช้จริง

<div align="center">
<img src="../../assets/figs/webui/chat.png" alt="Workspace chat DeepTutor" width="900">
</div>

Chat คือ capability เริ่มต้นและสถานที่ที่งานส่วนใหญ่เริ่มต้น thread เดียวสามารถพูดคุยตามปกติ, เรียกเครื่องมือ, อ้างอิงใน knowledge bases ที่เลือก, อ่านไฟล์แนบ, เขียน notebook records และดำเนินการต่อด้วย inventory แหล่งที่มาเดียวกันตลอด turns

<div align="center">
<img src="../../assets/figs/system/chat-agent-loop.png" alt="Chat agent loop DeepTutor" width="900">
</div>

เครื่องมือที่ผู้ใช้สลับได้: `brainstorm`, `web_search`, `paper_search`, `reason` เครื่องมือตามบริบท: `rag`, `read_source`, `read_memory`, `write_memory`, `read_skill`, `load_tools`, `exec`, `web_fetch`, `ask_user`, `list_notebook`, `write_note`, `github`

### 🤝 Partner — เพื่อนถาวรบน Brain เดียวกัน

<div align="center">
<img src="../../assets/figs/webui/partners.png" alt="Workspace partners DeepTutor" width="900">
</div>

Partners แทนที่ engine TutorBot เก่าด้วยโมเดลที่สะอาดขึ้น: ทุกข้อความ web หรือ IM ที่เข้ามาจะกลายเป็น turn ปกติของ ChatOrchestrator ภายใน workspace ที่มีขอบเขต partner

<div align="center">
<img src="../../assets/figs/system/partners-architecture.png" alt="สถาปัตยกรรม partners DeepTutor" width="900">
</div>

แต่ละ partner มี `SOUL.md`, การเลือก model, ช่องทาง, นโยบายเครื่องมือ และห้องสมุดที่กำหนด Knowledge bases, skills และ notebooks ถูกคัดลอกไปยัง `data/partners/<id>/workspace/`

<div align="center">
<img src="../../assets/figs/webui/partners02.png" alt="มุมมองรายละเอียด partner DeepTutor" width="900">
</div>

ชั้น channel รองรับ Feishu, Telegram, Slack, DingTalk, QQ/Napcat, WeCom, WhatsApp, Zulip, Matrix และ Microsoft Teams

### ✍️ Co-Writer — การเขียนร่าง Markdown ที่รับรู้การเลือก

Co-Writer เป็น workspace Markdown แบบ split-view สำหรับรายงาน, บทเรียน, บันทึก เอกสารจะบันทึกอัตโนมัติ, แสดงตัวอย่างสด และสามารถบันทึกกลับเข้า notebooks

### 📖 Book — หนังสือมีชีวิตจากวัสดุของคุณ

<p align="center">
<img src="../../assets/figs/webui/book01.png" alt="มุมมองการอ่านหนังสือ DeepTutor" width="31%">
&nbsp;
<img src="../../assets/figs/webui/book02.png" alt="มุมมองบล็อกโต้ตอบหนังสือ DeepTutor" width="31%">
&nbsp;
<img src="../../assets/figs/webui/book03.png" alt="มุมมองการสร้างหนังสือ DeepTutor" width="31%">
</p>

Book แปลงแหล่งที่มาที่เลือกเป็นวัสดุการเรียนรู้แบบโต้ตอบ BookEngine คอมไพล์หน้าเป็น typed blocks: text, sections, callouts, quizzes, flash cards, timelines, code, figures, interactive HTML, animations, concept graphs, deep dives และ user notes

### 📚 Knowledge — ไลบรารี RAG ที่มีเวอร์ชัน

<div align="center">
<img src="../../assets/figs/webui/knowledge.png" alt="Workspace knowledge base DeepTutor" width="900">
</div>

Knowledge Bases คือคอลเลกชันเอกสารเบื้องหลัง RAG สแตกปัจจุบันคือ LlamaIndex เท่านั้น การ re-indexing จะเก็บเวอร์ชันก่อนหน้า CLI: `deeptutor kb list`, `info`, `create`, `add`, `search`, `set-default`, `delete`

### 🌐 Space — Skills, Personas และบริบทที่ใช้ซ้ำได้

<div align="center">
<img src="../../assets/figs/webui/space.png" alt="Workspace Space DeepTutor" width="900">
</div>

Space คือชั้น library สำหรับบริบทที่ใช้ซ้ำได้ รวบรวม skills ที่ผู้ใช้สร้าง, personas, notebooks, ประวัติ chat Skills เก็บเป็นไฟล์ `SKILL.md`

### 🧠 Memory — การปรับแต่งส่วนบุคคลที่ตรวจสอบได้

<div align="center">
<img src="../../assets/figs/webui/memory01.png" alt="Workbench memory DeepTutor" width="900">
</div>

Memory คือระบบสามชั้น: `trace/<surface>/<date>.jsonl` (L1), `L2/<surface>.md` (L2), `L3/<recent|profile|scope|preferences>.md` (L3)

<div align="center">
<img src="../../assets/figs/webui/memory02.png" alt="กราฟ memory DeepTutor" width="900">
</div>

Surfaces: `chat`, `notebook`, `quiz`, `kb`, `book`, `tutorbot`, `cowriter`

### ⚙️ Settings — แผงควบคุมเดียว

<div align="center">
<img src="../../assets/figs/webui/settings.png" alt="Workspace settings DeepTutor" width="900">
</div>

Settings ครอบคลุมรูปลักษณ์, พอร์ตเครือข่าย, catalogs LLM และ embedding, search providers, MinerU, memory, MCP servers, เครื่องมือ

---

## ⌨️ DeepTutor CLI — อินเทอร์เฟซ Agent-Native

```bash
deeptutor run chat "Explain Fourier transform" --tool rag --kb textbook
deeptutor run deep_solve "Solve x^2 = 4" --tool reason
deeptutor chat --capability deep_research --kb papers
deeptutor partner create math-tutor --soul "Socratic math tutor"
deeptutor kb create calculus --doc textbook.pdf
```

<details>
<summary><b>การอ้างอิงคำสั่ง</b></summary>

| คำสั่ง | คำอธิบาย |
|:---|:---|
| `deeptutor init` | สร้างหรืออัพเดต `data/user/settings` สำหรับ workspace ปัจจุบัน |
| `deeptutor start [--home PATH]` | เปิดตัว backend + frontend ด้วยกัน |
| `deeptutor serve [--port PORT]` | เริ่มเฉพาะ FastAPI backend |
| `deeptutor run <capability> <message>` | รัน capability turn เดียว (`chat`, `deep_solve`, `deep_question`, `deep_research`, `visualize`, `math_animator`, `auto`, `mastery_path`) |
| `deeptutor chat` | Interactive REPL พร้อม capability, tool, KB, notebook และ history controls |
| `deeptutor partner list/create/start/stop` | จัดการ partners ที่เชื่อมต่อผ่าน IM |
| `deeptutor kb list/info/create/add/search/set-default/delete` | จัดการ knowledge bases LlamaIndex |
| `deeptutor memory show/clear` | ตรวจสอบ L2/L3 memory docs หรือล้าง L1/all memory |
| `deeptutor session list/show/open/rename/delete` | จัดการ shared sessions |
| `deeptutor notebook list/create/show/add-md/replace-md/remove-record` | จัดการ notebooks จากไฟล์ Markdown |
| `deeptutor book list/health/refresh-fingerprints` | ตรวจสอบ books และรีเฟรช source fingerprints |
| `deeptutor plugin list/info` | ตรวจสอบเครื่องมือและ capabilities ที่ลงทะเบียน |
| `deeptutor config show` | พิมพ์สรุปการกำหนดค่า |
| `deeptutor provider login <provider>` | จัดการ provider OAuth login ตามที่รองรับ |

</details>

---

## 👥 หลายผู้ใช้ — การปรับใช้แบบแชร์

<div align="center">
<img src="../../assets/figs/webui/multi-user.png" alt="Workspace admin หลายผู้ใช้ DeepTutor" width="900">
</div>

การยืนยันตัวตนเป็นแบบเสริมและปิดอยู่โดยค่าเริ่มต้น เมื่อเปิดใช้งาน DeepTutor จะกลายเป็นการปรับใช้แบบแชร์

```text
data/
├── user/                         # Workspace และการตั้งค่าของ Admin
├── users/<uid>/                  # ขอบเขตผู้ใช้ที่ไม่ใช่ admin
│   ├── user/chat_history.db
│   ├── user/settings/interface.json
│   ├── user/workspace/{chat,co-writer,book,memory,notebook,...}
│   └── knowledge_bases/...
├── partners/<id>/workspace/      # ขอบเขตผู้ใช้สังเคราะห์ของ partner
└── system/
    ├── auth/users.json
    ├── grants/<uid>.json
    └── audit/usage.jsonl
```

ผู้ใช้คนแรกที่ลงทะเบียนจะกลายเป็น admin ลงทะเบียน admin คนแรกที่ `/register` จากนั้นสร้างผู้ใช้จาก `/admin/users`

---

## 🌐 ชุมชนและระบบนิเวศ

| โปรเจค | บทบาทใน DeepTutor |
|:---|:---|
| [**nanobot**](https://github.com/HKUDS/nanobot) | agent engine น้ำหนักเบาพิเศษที่ขับเคลื่อน TutorBot ดั้งเดิม (Partners ตอนนี้ทำงานบน DeepTutor's chat agent loop) |
| [**LlamaIndex**](https://github.com/run-llama/llama_index) | กระดูกสันหลังของ RAG pipeline และการ indexing เอกสาร |
| [**ManimCat**](https://github.com/Wing900/ManimCat) | การสร้าง animation คณิตศาสตร์ขับเคลื่อนด้วย AI สำหรับ Math Animator |

**จากระบบนิเวศ HKUDS:**

| [⚡ LightRAG](https://github.com/HKUDS/LightRAG) | [🤖 AutoAgent](https://github.com/HKUDS/AutoAgent) | [🔬 AI-Researcher](https://github.com/HKUDS/AI-Researcher) | [🧬 nanobot](https://github.com/HKUDS/nanobot) |
|:---:|:---:|:---:|:---:|
| RAG ง่ายและเร็ว | Framework Agent แบบ Zero-Code | การวิจัยอัตโนมัติ | AI Agent น้ำหนักเบาพิเศษ |


## 🤝 การมีส่วนร่วม

<div align="center">

เราหวังว่า DeepTutor จะกลายเป็นของขวัญสำหรับชุมชน 🎁

<a href="https://github.com/HKUDS/DeepTutor/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=HKUDS/DeepTutor&max=999" alt="ผู้มีส่วนร่วม" />
</a>

</div>

ดู [CONTRIBUTING.md](../../CONTRIBUTING.md) สำหรับแนวทางการตั้งค่าสภาพแวดล้อมการพัฒนา มาตรฐานโค้ด และขั้นตอนการทำ pull request

## ⭐ ประวัติดาว

<div align="center">

<a href="https://www.star-history.com/#HKUDS/DeepTutor&type=timeline&legend=top-left">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=HKUDS/DeepTutor&type=timeline&theme=dark&legend=top-left" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=HKUDS/DeepTutor&type=timeline&legend=top-left" />
    <img alt="กราฟประวัติดาว" src="https://api.star-history.com/svg?repos=HKUDS/DeepTutor&type=timeline&legend=top-left" />
  </picture>
</a>

</div>

<p align="center">
 <a href="https://www.star-history.com/hkuds/deeptutor">
  <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/badge?repo=HKUDS/DeepTutor&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/badge?repo=HKUDS/DeepTutor" />
   <img alt="อันดับประวัติดาว" src="https://api.star-history.com/badge?repo=HKUDS/DeepTutor" />
  </picture>
 </a>
</p>

<div align="center">

**[Data Intelligence Lab @ HKU](https://github.com/HKUDS)**

[⭐ ให้ดาวเรา](https://github.com/HKUDS/DeepTutor/stargazers) · [🐛 รายงานบัก](https://github.com/HKUDS/DeepTutor/issues) · [💬 การสนทนา](https://github.com/HKUDS/DeepTutor/discussions)

---

ได้รับอนุญาตภายใต้ [Apache License 2.0](../../LICENSE)

<p>
  <img src="https://visitor-badge.laobi.icu/badge?page_id=HKUDS.DeepTutor&style=for-the-badge&color=00d4ff" alt="จำนวนผู้เข้าชม">
</p>

</div>
