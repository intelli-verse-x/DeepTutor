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

[คุณสมบัติ](#-คุณสมบัติหลัก) · [เริ่มต้น](#-เริ่มต้น) · [สำรวจ](#-สำรวจ-deeptutor) · [CLI](#️-deeptutor-cli--อินเทอร์เฟซ-agent-native) · [ระบบนิเวศ](#-ระบบนิเวศ--eduhub--ชุมชน-skills) · [ชุมชน](#-ชุมชน)

</div>

---

> 🤝 **เรายินดีรับการมีส่วนร่วมทุกรูปแบบ!** โหวตรายการ roadmap หรือเสนอรายการใหม่ที่ [`Roadmap`](https://github.com/HKUDS/DeepTutor/issues/498) และดู [คู่มือการมีส่วนร่วม](../../CONTRIBUTING.md) สำหรับกลยุทธ์ branching มาตรฐานการเขียนโค้ด และวิธีเริ่มต้น

### 📦 การเปิดตัว

> **[2026.6.17]** [v1.4.6](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.6) — รวมสี่พื้นผิว: Space → **แดชบอร์ดการเรียนรู้** พร้อม **My Agents** ที่นำเข้าได้และ Memory ระดับบนสุด; **Knowledge Center** เพิ่มเอ็นจิน GraphRAG / PageIndex / LightRAG พร้อม KB ที่เชื่อมโยงและการเมาท์ Obsidian; Settings เปิดการแยกวิเคราะห์เอกสาร / เสียง / รูปภาพ+วิดีโอ; ความสามารถ LLM ถูกควบคุมตามโมเดลที่กำหนด

> **[2026.6.14]** [v1.4.5](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.5) — **การเรียนรู้แบบนำทาง** สร้างใหม่บนลูปแชท agent พร้อมประตูความเชี่ยวชาญแบบ hard per-type และแดชบอร์ด `/learning`; เฟรมเวิร์ก loop-plugin ที่ขยายได้ใหม่; Markdown export / save-to-notebook สำหรับบทสนทนา Partner

> **[2026.6.13]** [v1.4.4](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.4) — ติดตั้ง **ทักษะชุมชนจาก [ClawHub](https://clawhub.ai/)** ด้วย `deeptutor skill install` ผ่านประตูความปลอดภัย; ดูตัวอย่าง DOCX/XLSX จริงในเบราว์เซอร์สำหรับไฟล์ knowledge base

> **[2026.6.12]** [v1.4.3](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.3) — TutorBot กลายเป็น **Partners** บน IM pipeline ระดับ production (15 ช่องทาง, live streaming), Chat ย้ายไปใช้ agent loop เดียว, การแยกส่วนต่อผู้ใช้จริง และ Visualize ที่สร้างใหม่

<details>
<summary><b>การเปิดตัวที่ผ่านมา (มากกว่า 2 สัปดาห์)</b></summary>

> **[2026.5.28]** [v1.4.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.2) — ความเสถียรภาพ + ความเรียบร้อย: Gemini 2.5+ ปลดล็อคใน Visualize และ Chat, การแก้ไข auth-routing (#485), UX การ streaming ที่ราบรื่น, แถบด้านข้าง Recents แบบพับได้ และรองรับ Lemonade local provider

> **[2026.5.27]** [v1.4.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.1) — ความปลอดภัย + ความเสถียรภาพ: ล็อค sandbox เครื่องมือ TutorBot, การแยกส่วนทรัพยากรต่อผู้ใช้, การ fallback ภาพ multimodal, API HTTP/SSE สำหรับ TutorBot และการแก้ไข chat regression ของ v1.4.0

> **[2026.5.22]** [v1.4.0](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.0) — GA cut ของ v1.4: Auto Mode, Memory สามชั้น, Deep Research / Solve / Question แบบ agentic, การ refactor RAG ด้วย LlamaIndex, การรวม Visualize/Animator และ turn runtime ที่ปลอดภัยต่อการรีสตาร์ท

> **[2026.5.21]** [v1.4.0-beta](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.0-beta) — เวิร์กเบนช์ Memory สามชั้น (L1/L2/L3), ความสามารถ chat ทั้งหมดสร้างใหม่บน agentic engine เดียว, RAG เฉพาะ LlamaIndex และพื้นที่ Settings + Capabilities แบบรวม

> **[2026.5.10]** [v1.3.10](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.10) — การกู้คืน CORS ของ Docker ระยะไกล, `DISABLE_SSL_VERIFY` สำหรับ SDK providers, การอ้างอิง code-block ที่ปลอดภัยขึ้น และรองรับ Matrix E2EE add-on แบบเสริม

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

- **2026-05-22** 🌐 เว็บไซต์เอกสารอย่างเป็นทางการเปิดตัวแล้วที่ [**deeptutor.info**](https://deeptutor.info/) — คู่มือ การอ้างอิง และ capability tours ทั้งหมดในที่เดียว
- **2026-04-19** 🎉 ถึง 20k stars ใน 111 วัน! ขอบคุณสำหรับการสนับสนุนที่น่าเหลือเชื่อ — เรามุ่งมั่นพัฒนาต่อเนื่องเพื่อการสอนพิเศษที่เป็นส่วนตัวและชาญฉลาดสำหรับทุกคน
- **2026-04-10** 📄 บทความของเราตอนนี้มีบน arXiv แล้ว! อ่าน [preprint](https://arxiv.org/abs/2604.26962) เพื่อเรียนรู้เพิ่มเติมเกี่ยวกับการออกแบบและแนวคิดที่อยู่เบื้องหลัง DeepTutor
- **2026-02-06** 🚀 ถึง 10k stars ในเพียง 39 วัน! ขอบคุณชุมชนที่น่าเหลือเชื่ออย่างยิ่ง!
- **2026-01-01** 🎊 สวัสดีปีใหม่! เข้าร่วม [Discord](https://discord.gg/eRsjPgMU4t), [WeChat](https://github.com/HKUDS/DeepTutor/issues/78) หรือ [Discussions](https://github.com/HKUDS/DeepTutor/discussions) — มาร่วมกันกำหนดอนาคตของ DeepTutor!
- **2025-12-29** 🎓 DeepTutor ได้รับการเปิดตัวอย่างเป็นทางการแล้ว!

## ✨ คุณสมบัติหลัก

DeepTutor คือ workspace การเรียนรู้แบบ agent-native ที่เชื่อมต่อการสอนพิเศษ, การแก้ปัญหา, การสร้าง quiz, การวิจัย, การสร้างภาพ และการฝึกความเชี่ยวชาญในระบบที่ขยายได้หนึ่งเดียว

- **รันไทม์เดียวสำหรับทุกโหมด** — Chat, Quiz, Research, Visualize, Solve และ Mastery Path บนลูป agent เดียวกัน คุณเปลี่ยนวัตถุประสงค์ ไม่ใช่เอ็นจิน และบริบทเดินทางไปพร้อมกับผู้เรียน
- **บริบทการเรียนรู้ที่เชื่อมต่อกัน** — ฐานความรู้, หนังสือ, ร่าง Co-Writer, สมุดบันทึก, คลังคำถาม, บุคลิกภาพ และ Memory พร้อมใช้งานในทุกเวิร์กโฟลว์ แทนที่จะอยู่ในเครื่องมือที่แยกจากกัน
- **ซับเอเจนต์และ Partners** — ปรึกษา Claude Code, Codex หรือ Partner แบบสดจากทุก turn (หรือนำเข้าบทสนทนาในอดีต) และรันเพื่อนถาวรบน IM ด้วยสมองเดียวกัน
- **ความรู้หลายเอ็นจิน** — ไลบรารี RAG แบบเวอร์ชันผ่าน LlamaIndex, PageIndex, GraphRAG, LightRAG หรือ Obsidian vault ที่เชื่อมโยง พร้อมการแยกวิเคราะห์เอกสารแบบ pluggable
- **เครื่องมือและทักษะที่ขยายได้** — เครื่องมือในตัว, เซิร์ฟเวอร์ MCP, โมเดลสร้างรูปภาพ/วิดีโอ/เสียง และทักษะชุมชนที่ติดตั้งได้จาก EduHub
- **หน่วยความจำที่ตรวจสอบได้** — การติดตาม L1, สรุปพื้นผิว L2 และการสังเคราะห์ L3 ทำให้การปรับแต่งส่วนบุคคลมองเห็นได้และแก้ไขได้ พร้อม Memory Graph ที่ติดตามทุกการอ้างสิทธิ์กลับไปสู่หลักฐาน

---

## 🚀 เริ่มต้น

DeepTutor มีเส้นทางการติดตั้งสี่เส้นทาง ทั้งหมดแชร์ layout workspace เดียว: การตั้งค่าอยู่ใน `data/user/settings/` ภายใต้ไดเร็กทอรีที่คุณเปิดตัว (หรือภายใต้ `DEEPTUTOR_HOME` / `deeptutor start --home` หากคุณตั้งค่าไว้อย่างชัดเจน) สำหรับแอปเต็มรูปแบบ ขั้นตอนที่แนะนำคือ **เลือกไดเร็กทอรี workspace → ติดตั้ง → `deeptutor init` → `deeptutor start`**

> ✨ **v1.4.6 พร้อมใช้งาน** `pip install -U deeptutor` จะดึงเวอร์ชันที่เสถียรล่าสุด Pre-releases (เมื่อพร้อมใช้งาน) เลือกใช้ได้ด้วย `pip install --pre -U deeptutor`

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

### ตัวเลือกที่ 2 — ติดตั้งจากซอร์สโค้ด

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
<summary><b>ส่วนเสริมการติดตั้ง</b> — dev / partners / matrix / math-animator</summary>

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

<details>
<summary><b>Sandbox การรันโค้ด (office skills)</b></summary>

office skills ที่ติดตั้งมา — **docx / pdf / pptx / xlsx** — ทำงานโดยให้ model เขียน Python script สั้น ๆ รันผ่านเครื่องมือ `exec` / `code_execution` และส่งคืน URL ดาวน์โหลด

`sandbox_allow_subprocess` ใน `data/user/settings/system.json` (ค่าเริ่มต้น `true`) ควบคุม sandbox ตั้งเป็น `false` หรือ export `DEEPTUTOR_SANDBOX_ALLOW_SUBPROCESS=0` เพื่อปิด

</details>

<details>
<summary><b>เอกสารอ้างอิงการตั้งค่า</b> — ไฟล์การกำหนดค่าภายใต้ <code>data/user/settings/</code></summary>

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

---

## 📖 สำรวจ DeepTutor

เริ่มต้นด้วยพื้นผิวหลักที่คุณจะใช้ทุกวัน: Chat, Partners, My Agents, Co-Writer, Book, Knowledge Center, Learning Space, Memory และ Settings

<div align="center">
<img src="../../assets/figs/web-1.4.6+/OVERVIEW.png" alt="DeepTutor home — workspace Chat พร้อมทุกพื้นผิวใน sidebar" width="900">
</div>

### 💬 แชท (Chat)

Chat คือความสามารถเริ่มต้นและสถานที่ที่งานส่วนใหญ่เริ่มต้น thread เดียวสามารถพูดคุยตามปกติ, เรียกเครื่องมือ, อ้างอิงใน knowledge bases ที่เลือก, อ่านไฟล์แนบ, สร้างรูปภาพ, ปรึกษา subagents, เขียน notebook records และดำเนินการต่อด้วยบริบทเดียวกันตลอด turns

<div align="center">
<img src="../../assets/figs/web-1.4.6+/home/00-overview.png" alt="DeepTutor workspace chat" width="900">
</div>

ลูปนั้นเรียบง่ายโดยเจตนา: model คิดในรอบ ๆ, เรียกเครื่องมือเมื่อมีประโยชน์, สังเกตผลลัพธ์ และจบด้วยข้อความที่ไม่มีเครื่องมือ `ask_user` เป็นพิเศษ — แทนที่จะเดา agent สามารถหยุด turn, ถามคำถามชี้แจงที่มีโครงสร้าง และดำเนินการต่อเมื่อคุณตอบ

<div align="center">
<img src="../../assets/figs/system/chat-agent-loop.png" alt="DeepTutor chat agent loop" width="900">
</div>

เครื่องมือที่ผู้ใช้สลับได้: `brainstorm`, `web_search`, `paper_search`, `reason`, `geogebra_analysis` รวมถึง `imagegen` และ `videogen` เมื่อคุณกำหนดค่าโมเดลสร้างที่ตรงกัน เครื่องมือตามบริบท: `rag`, `read_source`, `read_memory`, `write_memory`, `read_skill`, `load_tools`, `exec`, `web_fetch`, `ask_user`, `list_notebook`, `write_note`, `github`, `consult_subagent` เมาท์อัตโนมัติเมื่อ turn มีบริบทที่ถูกต้อง

### 🤝 พาร์ทเนอร์ (Partner)

<div align="center">
<img src="../../assets/figs/web-1.4.6+/partners/00-partners overview.png" alt="DeepTutor workspace partners" width="900">
</div>

Partners คือเพื่อนถาวรที่มี soul, นโยบาย model, ห้องสมุด, memory และช่องทางของตัวเอง พวกเขาไม่ใช่เอ็นจิน bot แยกต่างหาก: ทุกข้อความ web หรือ IM ที่เข้ามาจะกลายเป็น turn ปกติของ `ChatOrchestrator` ภายใน workspace ที่มีขอบเขต partner

<div align="center">
<img src="../../assets/figs/system/partners-architecture.png" alt="สถาปัตยกรรม partners DeepTutor" width="900">
</div>

แต่ละ partner มี `SOUL.md`, การเลือก model, ช่องทาง, นโยบายเครื่องมือ และห้องสมุดที่กำหนด Knowledge bases, skills และ notebooks ถูกคัดลอกไปยัง `data/partners/<id>/workspace/` ดังนั้น RAG, skill, notebook และเครื่องมือ memory เดิมทำงานได้โดยไม่มีกรณีพิเศษ partner อ่าน memory ของเจ้าของแต่เขียนเฉพาะของตัวเอง

<div align="center">
<img src="../../assets/figs/web-1.4.6+/partners/02-IM config for each partner.png" alt="การกำหนดค่าช่องทาง IM ต่อ partner" width="900">
</div>

ชั้น channel ที่ขับเคลื่อนด้วย schema สามารถเชื่อมต่อกับแพลตฟอร์ม IM ได้แก่ Feishu, Telegram, Slack, DingTalk, QQ/NapCat, WeCom, WhatsApp, Zulip, Matrix และ Microsoft Teams ขึ้นอยู่กับ extras ที่ติดตั้งและ credentials ที่กำหนดค่า

### 🧑‍🚀 เอเจนต์ของฉัน (My Agents)

<div align="center">
<img src="../../assets/figs/web-1.4.6+/myagents/00-overview.png" alt="DeepTutor workspace My Agents" width="900">
</div>

My Agents เปลี่ยน agent อื่น ๆ ให้กลายเป็นบริบทสำหรับ DeepTutor และทำสองสิ่งที่แตกต่างกัน **เชื่อมต่อ agent แบบสด** — Claude Code หรือ Codex CLI บนเครื่องของคุณ หรือหนึ่งใน Partners ของคุณ — และปรึกษามันจากภายใน chat turn: DeepTutor จริง ๆ *รัน* agent อื่นและ stream งานเข้าสู่แผง Activity ผ่านเครื่องมือ `consult_subagent` เลือกด้วย Agent chip (หรือพิมพ์ `@`) และตั้งค่าจำนวนรอบที่การปรึกษาอาจทำ

<div align="center">
<img src="../../assets/figs/web-1.4.6+/home/08-subagent demo with claude code.png" alt="การปรึกษา subagent Claude Code แบบสด" width="900">
</div>

**นำเข้าบทสนทนาในอดีต** — นำประวัติ Claude Code และ Codex ที่มีอยู่ของคุณมาเป็น agent ที่มีชื่อ, ค้นหาได้ และสามารถดำเนินการต่อได้ เลือกวันที่จะนำเข้า การรีเฟรชจะ re-sync ข้อมูล อ้างอิงบทสนทนาที่นำเข้าจาก chat turn ใด ๆ ผ่าน `+` → My Agents และ DeepTutor จะอ่านมันเป็น transcript ของบุคคลที่สาม

### ✍️ Co-Writer

<div align="center">
<img src="../../assets/figs/web-1.4.6+/co-writer/00-overview.png" alt="DeepTutor workspace Co-Writer" width="900">
</div>

Co-Writer คือ workspace Markdown แบบ split-view สำหรับรายงาน, บทเรียน, บันทึก และ artifacts การเรียนรู้แบบยาว เอกสารบันทึกอัตโนมัติ, แสดงตัวอย่างสด (คณิตศาสตร์ KaTeX, diagram fences) และสามารถบันทึกกลับเข้า notebooks เมื่อร่างกลายเป็นบริบทที่นำมาใช้ซ้ำได้

<div align="center">
<img src="../../assets/figs/web-1.4.6+/co-writer/01-edit panel.png" alt="Co-Writer editor พร้อม live preview" width="900">
</div>

แนวคิดหลักคือ **การแก้ไขแบบผ่าตัด**: เลือกช่วงและขอให้ DeepTutor เขียนใหม่, ขยาย หรือย่อ agent การแก้ไขสามารถอ้างอิงใน knowledge base หรือหลักฐานเว็บ, เก็บ trace ของ tool calls และแสดงทุกการเปลี่ยนแปลงเป็น accept/reject diff — ดังนั้นไม่มีอะไรลงจนกว่าคุณจะอนุมัติ

### 📖 หนังสือ (Book)

<div align="center">
<img src="../../assets/figs/web-1.4.6+/book/00-book_overview.png" alt="DeepTutor book library" width="900">
</div>

Book แปลงแหล่งที่มาที่เลือกให้เป็น **หนังสือมีชีวิต** แบบโต้ตอบ — ไม่ใช่ PDF แบบคงที่ แต่เป็นสภาพแวดล้อมการอ่านที่สร้างจาก typed blocks หนังสือสามารถเริ่มจาก knowledge bases, notebooks, question banks หรือประวัติ chat; ขั้นตอนการสร้างจะเสนอ outline บทก่อนที่จะสร้างเนื้อหา

<p align="center">
<img src="../../assets/figs/web-1.4.6+/book/01-book-demo-quiz card.png" alt="Book quiz block" width="31%">
&nbsp;
<img src="../../assets/figs/web-1.4.6+/book/02-book-demo-manim video.png" alt="Book Manim animation block" width="31%">
&nbsp;
<img src="../../assets/figs/web-1.4.6+/book/03-book-demo interactive module.png" alt="Book interactive widget block" width="31%">
</p>

แต่ละบทคอมไพล์เป็น typed blocks — text, callouts, quizzes, flash cards, timelines, code, figures, interactive HTML, animations, concept graphs, deep dives และ user notes — และทุกหน้ามี Page Chat ของตัวเอง Blocks สามารถแก้ไขได้: แทรก, ย้าย, สร้างใหม่ หรือเปลี่ยนประเภทของ block โดยไม่ต้องเขียนบทใหม่

### 📚 ศูนย์ความรู้ (Knowledge Center)

<div align="center">
<img src="../../assets/figs/web-1.4.6+/knowledge/00-overview.png" alt="DeepTutor Knowledge Center" width="900">
</div>

Knowledge bases คือคอลเลกชันเอกสารที่อยู่เบื้องหลัง RAG — รองรับ Chat turns, Co-Writer edits, Book generation และบทสนทนา Partner สิ่งที่โดดเด่นคือ **การเลือกเอ็นจิน retrieval**: **LlamaIndex** (ค่าเริ่มต้น, local vector + BM25), **PageIndex** (hosted, reasoning retrieval พร้อม page-level citations), **GraphRAG** และ **LightRAG** (knowledge-graph retrieval) หรือ **Obsidian** vault ที่เชื่อมโยง KB แต่ละอันถูก indexed โดยเอ็นจินหนึ่ง

<div align="center">
<img src="../../assets/figs/web-1.4.6+/knowledge/01-create knowledge base.png" alt="สร้าง knowledge base" width="900">
</div>

เมื่อสร้าง KB คุณ **สร้างใหม่** (อัพโหลดเอกสารและสร้าง index ใหม่) หรือ **เชื่อมโยงที่มีอยู่** (นำ index ที่สร้างไว้มาใช้ซ้ำ อ่านในที่โดยไม่ต้อง re-index) การ re-indexing จะเขียน directory `version-N` ใหม่และเก็บอันก่อนหน้าไว้ CLI: `deeptutor kb list`, `info`, `create`, `add`, `search`, `set-default`, `delete`

### 🌐 พื้นที่การเรียนรู้ (Learning Space)

<div align="center">
<img src="../../assets/figs/web-1.4.6+/learning-space/00-overview.png" alt="DeepTutor Learning Space hub" width="900">
</div>

Learning Space คือชั้น library และ personalization — ที่ซึ่งสิ่งที่คงอยู่ถาวรอาศัยอยู่ **Conversations & Materials** เก็บประวัติ chat, notebooks และ question bank (แต่ละคำถามที่บันทึกเก็บคำตอบของคุณ, คำตอบอ้างอิง และคำอธิบาย) **Personalization** เก็บ mastery paths, personas (พฤติกรรมที่ตั้งค่าล่วงหน้าเช่น *peer*, *research-assistant*, *teacher*) และ skills (`SKILL.md` playbooks ที่ model อ่านตามต้องการ)

<div align="center">
<img src="../../assets/figs/web-1.4.6+/learning-space/07- download skills from eduhub.png" alt="นำเข้า skills จาก EduHub" width="900">
</div>

คุณไม่จำเป็นต้องเขียน skill ทุกอันเอง — **นำเข้าจาก EduHub** จะเรียกดู catalog ชุมชนและดาวน์โหลด skill ตรงเข้า library ผ่านประตูความปลอดภัย (ดู [ระบบนิเวศ](#-ระบบนิเวศ--eduhub--ชุมชน-skills))

### 🧠 หน่วยความจำ (Memory)

<div align="center">
<img src="../../assets/figs/web-1.4.6+/memory/00-overview.png" alt="DeepTutor memory overview" width="900">
</div>

Memory คือระบบไฟล์สามชั้นที่คุณอ่าน, จัดการ และตรวจสอบได้ — โดยเจตนาไม่ใช่ vector store ที่ซ่อนอยู่ **L1** คือ workspace mirror พร้อม append-only event trace (`trace/<surface>/<date>.jsonl`); **L2** คือข้อเท็จจริงที่จัดการต่อพื้นผิว (`L2/<surface>.md`); **L3** คือการสังเคราะห์ข้ามพื้นผิว (`L3/<profile|recent|scope>.md`) เนื่องจาก L2 อ้างอิง L1 และ L3 อ้างอิง L2 ไม่มีอะไรในโปรไฟล์ของคุณที่ตรวจสอบไม่ได้

<div align="center">
<img src="../../assets/figs/web-1.4.6+/memory/01-3 layer memory graph.png" alt="DeepTutor memory graph" width="900">
</div>

Memory Graph แสดงพีระมิดทั้งหมด — การสังเคราะห์ L3 ที่ศูนย์กลาง, L2 ในวงกลางกลาง, L1 traces ด้านนอก — เพื่อให้คุณติดตามการอ้างสิทธิ์ที่สังเคราะห์ใด ๆ กลับไปสู่เหตุการณ์ดิบที่แน่นอน Memory ถูกติดตามใน surfaces: `chat`, `notebook`, `quiz`, `kb`, `book`, partner และ `cowriter`; งบประมาณ Update / Audit / Dedup ของ consolidator ปรับได้ใน **Settings → Memory**

### ⚙️ การตั้งค่า (Settings)

<div align="center">
<img src="../../assets/figs/web-1.4.6+/settings/00-setting overview.png" alt="DeepTutor settings hub" width="900">
</div>

Settings คือ control plane การดำเนินงาน พร้อม live status strip (Backend, LLM, Embedding, Search) และหนึ่งการ์ดต่อพื้นที่: **Appearance** (ธีม + ภาษา UI), **Network** (API base, ports, CORS), **Models** (LLM, Embedding, Search, Text-to-Speech, Speech-to-Text, Image Generation, Video Generation), **Knowledge Base** (เอ็นจินการแยกวิเคราะห์เอกสาร), **Chat** (เครื่องมือ, MCP servers, พารามิเตอร์ต่อความสามารถ), **Partners & Agents** (subagents ที่คุณปรึกษาได้จาก turn) และ **Memory** (งบประมาณของ consolidator)

<div align="center">
<img src="../../assets/figs/web-1.4.6+/settings/01-appearance settings.png" alt="DeepTutor appearance settings and themes" width="900">
</div>

ส่วนส่วนใหญ่ใช้ draft-and-apply flow เพื่อให้คุณทดสอบ provider ก่อนยืนยัน ธีมสี่แบบมาในกล่อง — Default, Cream, Dark และ Glass ไฟล์ `.env` ที่ root ของโปรเจกต์ถูกเพิกเฉยโดยเจตนา; การกำหนดค่า runtime อยู่ใน `data/user/settings/*.json`

---

## ⌨️ DeepTutor CLI — อินเทอร์เฟซ Agent-Native

binary `deeptutor` เดียว, สองวิธีเข้า: **REPL** แบบโต้ตอบสำหรับคนที่อยู่ใน terminal และ **JSON** ที่มีโครงสร้างสำหรับ agents อื่น ๆ ที่ขับเคลื่อน DeepTutor เป็นเครื่องมือ ความสามารถ, เครื่องมือ และ knowledge bases เหมือนกันทั้งสองแบบ

```bash
deeptutor chat                                              # interactive REPL
deeptutor chat --capability deep_solve --kb my-kb --tool rag
deeptutor run chat "Explain the Fourier transform" --tool rag --kb textbook
deeptutor run deep_research "Survey 2026 papers on RAG" \
  --config mode=report --config depth=standard
```

<details>
<summary><b>การอ้างอิงคำสั่ง</b></summary>

| คำสั่ง | คำอธิบาย |
|:---|:---|
| `deeptutor init` | สร้างหรืออัพเดต `data/user/settings` สำหรับ workspace ปัจจุบัน |
| `deeptutor start [--home PATH]` | เปิดตัว backend + frontend ด้วยกัน |
| `deeptutor serve [--port PORT]` | เริ่มเฉพาะ FastAPI backend |
| `deeptutor run <capability> <message>` | รัน capability turn เดียว (`chat`, `deep_solve`, `deep_question`, `deep_research`, `visualize`, `math_animator`, `mastery_path`); เพิ่ม `--format json` สำหรับ NDJSON output |
| `deeptutor chat` | Interactive REPL พร้อม capability, tool, KB, notebook และ history controls |
| `deeptutor partner list/create/start/stop` | จัดการ partners ที่เชื่อมต่อผ่าน IM |
| `deeptutor kb list/info/create/add/search/set-default/delete` | จัดการ knowledge bases LlamaIndex |
| `deeptutor skill search/install/list/remove/login/publish/update` | จัดการทักษะ ติดตั้งจากฮับ และเผยแพร่ของคุณเอง (`eduhub:<slug>` โดยค่าเริ่มต้น ดู Ecosystem) |
| `deeptutor memory show/clear` | ตรวจสอบ L2/L3 memory docs หรือล้าง L1/all memory |
| `deeptutor session list/show/open/rename/delete` | จัดการ shared sessions |
| `deeptutor notebook list/create/show/add-md/replace-md/remove-record` | จัดการ notebooks จากไฟล์ Markdown |
| `deeptutor book list/health/refresh-fingerprints` | ตรวจสอบ books และรีเฟรช source fingerprints |
| `deeptutor plugin list/info` | ตรวจสอบเครื่องมือและ capabilities ที่ลงทะเบียน |
| `deeptutor config show` | พิมพ์สรุปการกำหนดค่า |
| `deeptutor provider login <provider>` | Provider auth (OAuth login สำหรับ `openai-codex`; `github-copilot` ตรวจสอบ session auth Copilot ที่มีอยู่) |

</details>

---

## 👥 หลายผู้ใช้ — การปรับใช้แบบแชร์

การยืนยันตัวตนเป็นแบบเสริมและ **ปิดอยู่โดยค่าเริ่มต้น** — DeepTutor ทำงานแบบผู้ใช้คนเดียว เปิดใช้งานและ tree `data/` หนึ่งจะโฮสต์ workspace ของ admin, workspace ต่อผู้ใช้แบบแยกส่วน และ workspace ของ partner ไว้ด้วยกัน:

```text
data/
├── user/                         # Workspace และการตั้งค่าของ Admin
├── users/<uid>/                  # ขอบเขตผู้ใช้: ประวัติ chat, memory, notebooks, KBs
│   ├── user/chat_history.db
│   ├── user/settings/interface.json
│   ├── user/workspace/{chat,co-writer,book,memory,notebook,...}
│   └── knowledge_bases/...
├── partners/<id>/workspace/      # ขอบเขต partner (synthetic-user)
└── system/
    ├── auth/users.json
    ├── grants/<uid>.json
    └── audit/usage.jsonl
```

**ผู้ใช้คนแรกที่ลงทะเบียนจะกลายเป็น admin** และเป็นเจ้าของ model catalogs, provider credentials, shared knowledge bases, skills และ per-user grants ลงทะเบียน admin คนแรกที่ `/register` จากนั้นสร้างผู้ใช้จาก `/admin/users`

---

## 🧩 ระบบนิเวศ — EduHub และชุมชน Skills

DeepTutor skills ใช้รูปแบบ **Agent-Skills** แบบเปิด — โฟลเดอร์ที่มี `SKILL.md` playbook (YAML frontmatter + Markdown) และไฟล์อ้างอิงแบบเสริม DeepTutor มาพร้อมกับ **[EduHub](https://eduhub.deeptutor.info/)** — registry ทักษะที่เน้นการศึกษาของเรา — เชื่อมต่อเป็นฮับเริ่มต้น

<details>
<summary><b>EduHub — ระบบนิเวศทักษะของ DeepTutor</b></summary>

[**EduHub**](https://eduhub.deeptutor.info/) คือ community hub ที่ DeepTutor เปิดตัวสำหรับแชร์ agent skills เชิงสอน — Socratic tutors, flashcard builders, essay feedback, exam blueprints, concept explainers และอื่น ๆ อีกมาก มันถูกสร้างเข้า DeepTutor ดังนั้นไม่มีอะไรต้องกำหนดค่า: slug เปล่าหรือ prefix `eduhub:` จะ resolve ไปยังมัน

**ค้นหาและติดตั้ง** — ในเบราว์เซอร์ เปิด **Learning Space → Skills → นำเข้าจาก EduHub** เพื่อเรียกดู catalog และดาวน์โหลด skill ตรงเข้า library จาก terminal:

```bash
deeptutor skill search "socratic tutor"               # ค้นหา EduHub (ฮับเริ่มต้น)
deeptutor skill install socratic-tutor                # fetch → verify → register
deeptutor skill install eduhub:socratic-tutor@1.2.0   # ระบุ hub และเวอร์ชัน
deeptutor skill list                                  # skills ในเครื่องพร้อม hub provenance
```

**เผยแพร่ของคุณเอง** — แพ็ค `SKILL.md` และแชร์กลับสู่ชุมชน:

```bash
deeptutor skill login                                 # browser sign-in ไปยัง EduHub
deeptutor skill publish ./my-skill                    # interactive: เลือก track + tags แล้วอัพโหลด
deeptutor skill update                                # rollback หรือ release เวอร์ชันใหม่
```

EduHub ยังเป็น registry แบบ standalone ที่เข้ากันได้กับ ClawHub ดังนั้น agents ที่ไม่ใช่ DeepTutor (Claude Code, Codex, …) สามารถใช้มันโดยตรงผ่าน CLI `eduhub` — `npx eduhub install socratic-tutor`

</details>

<details>
<summary><b>ประตูความปลอดภัยในการนำเข้า</b></summary>

ไม่ว่าแหล่งที่มาจะเป็นอะไร ทุกการนำเข้าจะผ่าน **ประตูความปลอดภัยเดียวกัน** ก่อนที่อะไรจะแตะ workspace ของคุณ:

- **security verdict** ของ registry จะถูกตรวจสอบก่อน — แพ็คเกจที่ถูกตั้งค่าสถานะจะถูกปฏิเสธเว้นแต่คุณจะส่ง `--allow-unverified`
- archives จะถูก extract อย่างระมัดระวัง (ป้องกัน zip-slip / zip-bomb) หลัง **suffix whitelist** แบบ text/script ดังนั้น binaries จะไม่ลงใน workspace เลย
- frontmatter จะถูก normalize เป็น schema ของ DeepTutor และ `always:` จะถูก **ลบออก** ดังนั้น skill ที่ดาวน์โหลดมาไม่สามารถบังคับตัวเองเข้าสู่ system prompt ทุกอัน
- provenance — hub, version, verdict และเวลาติดตั้ง — จะถูกเขียนลง `.hub-lock.json` สำหรับการตรวจสอบและอัพเดต

</details>

<details>
<summary><b>รองรับ ClawHub ด้วย (--hub clawhub)</b></summary>

เนื่องจาก DeepTutor พูดรูปแบบ Agent-Skills แบบเปิด **[ClawHub](https://clawhub.ai/)** ทำงานเป็นแหล่งระดับ first-class ด้วย — มันถูกสร้างเข้าพร้อมกับ EduHub เลือกด้วย hub prefix:

```bash
deeptutor skill search "git release notes" --hub clawhub
deeptutor skill install clawhub:git-release-notes@1.0.1
```

เพิ่ม registries เพิ่มเติมใน `settings/skill_hubs.json`: entry `type: "clawhub"` ชี้ไปที่ HTTP API ที่เข้ากันได้ใด ๆ, `type: "command"` ห่อ CLI ที่ registry ส่งมา และ `"default"` เลือกฮับที่ใช้สำหรับ slugs เปล่า ทั้งหมดนี้ป้อนข้อมูลผ่านประตูนำเข้าเดียวกัน

</details>

---

## 🌐 ชุมชน

### 📮 ติดต่อ

DeepTutor คือโปรเจกต์โอเพนซอร์สที่นำโดย [Bingxi Zhao](https://github.com/pancacake) ภายในกลุ่ม [HKUDS](https://github.com/HKUDS) และพัฒนาใน **รูปแบบโอเพนซอร์สอย่างสมบูรณ์** สร้างร่วมกับชุมชน จนถึงปัจจุบัน เรา **ไม่มี** ผลิตภัณฑ์ออนไลน์แบบชำระเงินในรูปแบบใด ๆ ติดต่อได้ที่ **bingxizhao39@gmail.com** สำหรับการสนทนา, ไอเดีย หรือการร่วมมือ

### 🙏 ขอบคุณ

ขอบคุณอย่างจริงใจถึง [**Chao Huang**](https://sites.google.com/view/chaoh), ผู้อำนวยการ Data Intelligence Lab @ HKU และเพื่อน ๆ ใน HKUDS lab สำหรับการสนับสนุนอย่างอบอุ่น — โดยเฉพาะ [**Jiahao Zhang**](https://github.com/zzhtx258), [**Zirui Guo**](https://github.com/LarFii) และ [**Xubin Ren**](https://github.com/Re-bin) เรายังขอบคุณอย่างสุดซึ้งถึง **ชุมชนโอเพนซอร์ส**: stars, issues, pull requests และ discussions ของคุณกำหนดรูปร่าง DeepTutor ทุกวัน

DeepTutor ยังยืนอยู่บนไหล่ของโปรเจกต์โอเพนซอร์สที่โดดเด่นที่ให้ทั้งเครื่องมือและแรงบันดาลใจแก่เรา:

| โปรเจกต์ | บทบาท / แรงบันดาลใจ |
|:---|:---|
| [**LlamaIndex**](https://github.com/run-llama/llama_index) | กระดูกสันหลังของ RAG pipeline และการ indexing เอกสาร |
| [**nanobot**](https://github.com/HKUDS/nanobot) | Ultra-lightweight agent engine ที่ขับเคลื่อน TutorBot ดั้งเดิม *(HKUDS)* |
| [**LightRAG**](https://github.com/HKUDS/LightRAG) | RAG ที่ง่ายและเร็ว *(HKUDS)* |
| [**AutoAgent**](https://github.com/HKUDS/AutoAgent) | Zero-code agent framework *(HKUDS)* |
| [**AI-Researcher**](https://github.com/HKUDS/AI-Researcher) | Pipeline การวิจัยอัตโนมัติ *(HKUDS)* |
| [**OpenClaw**](https://github.com/openclaw/openclaw) | Open agent gateway และ skill ecosystem เบื้องหลัง ClawHub |
| [**Codex**](https://github.com/openai/codex) | Agent-native coding CLI ที่เป็นแรงบันดาลใจให้ CLI workflow ของเรา |
| [**Claude Code**](https://github.com/anthropics/claude-code) | Agentic coding CLI ที่เป็นแรงบันดาลใจให้ DeepTutor agent loop |
| [**ManimCat**](https://github.com/Wing900/ManimCat) | การสร้าง animation คณิตศาสตร์ที่ขับเคลื่อนด้วย AI สำหรับ Math Animator |

### 🗺️ Roadmap และการมีส่วนร่วม

เราต้องการให้ DeepTutor พัฒนาและปรับปรุงต่อเนื่อง — และสุดท้ายกลายเป็นของขวัญที่เรามอบคืนสู่ชุมชนโอเพนซอร์ส [**roadmap**](https://github.com/HKUDS/DeepTutor/issues/498) ของเราอัพเดตต่อเนื่อง โหวตรายการที่นั่นหรือเสนอรายการใหม่ หากต้องการมีส่วนร่วม ดู [**คู่มือการมีส่วนร่วม**](../../CONTRIBUTING.md) สำหรับกลยุทธ์ branching มาตรฐานโค้ด และวิธีเริ่มต้น

<div align="center">

เราหวังว่า DeepTutor จะกลายเป็นของขวัญสำหรับชุมชน 🎁

<a href="https://github.com/HKUDS/DeepTutor/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=HKUDS/DeepTutor&max=999" alt="ผู้มีส่วนร่วม" />
</a>

</div>

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
