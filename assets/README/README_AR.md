<div align="center">

<p align="center"><img src="../../assets/figs/logo/logo.png" alt="شعار DeepTutor" height="56" style="vertical-align: middle;">&nbsp;<img src="../../assets/figs/logo/banner.png" alt="DeepTutor" height="48" style="vertical-align: middle;"></p>

# DeepTutor: تدريس شخصي مبني على الوكلاء الذكيين

<p align="center">
  <a href="https://deeptutor.info" target="_blank"><img alt="الوثائق — deeptutor.info" src="https://img.shields.io/badge/Docs-deeptutor.info%20%E2%86%97-0A0A0A?style=for-the-badge&labelColor=F5F5F4" height="36"></a>
</p>

<a href="https://trendshift.io/repositories/17099" target="_blank"><img src="https://trendshift.io/api/badge/repositories/17099" alt="HKUDS%2FDeepTutor | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>

<p align="center">
  <a href="../../README.md"><img alt="English" height="40" src="https://img.shields.io/badge/English-CDCFD4"></a>&nbsp;
  <a href="README_CN.md"><img alt="简体中文" height="40" src="https://img.shields.io/badge/简体中文-CDCFD4"></a>&nbsp;
  <a href="README_JA.md"><img alt="日本語" height="40" src="https://img.shields.io/badge/日本語-CDCFD4"></a>&nbsp;
  <a href="README_ES.md"><img alt="Español" height="40" src="https://img.shields.io/badge/Español-CDCFD4"></a>&nbsp;
  <a href="README_FR.md"><img alt="Français" height="40" src="https://img.shields.io/badge/Français-CDCFD4"></a>&nbsp;
  <a href="README_AR.md"><img alt="Arabic" height="40" src="https://img.shields.io/badge/Arabic-BCDCF7"></a>&nbsp;
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

[المميزات](#-المميزات-الرئيسية) · [البدء](#-البدء) · [الاستكشاف](#-استكشاف-deeptutor) · [واجهة سطر الأوامر](#%EF%B8%8F-واجهة-سطر-أوامر-deeptutor--الواجهة-الأصيلة-للوكلاء) · [متعدد المستخدمين](#-متعدد-المستخدمين--النشر-المشترك) · [المجتمع](#-المجتمع-والنظام-البيئي)

</div>

---

> 🤝 **نرحب بجميع أنواع المساهمات!** صوّت على عناصر خارطة الطريق أو اقترح عناصر جديدة في [`خارطة الطريق`](https://github.com/HKUDS/DeepTutor/issues/498)، وراجع [دليل المساهمة](../../CONTRIBUTING.md) لمعرفة استراتيجية الفروع ومعايير البرمجة وكيفية البدء.

### 📦 الإصدارات

> **[2026.6.12]** [v1.4.3](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.3) — أصبح TutorBot **Partners** على خط أنابيب إنتاجي لتطبيقات المراسلة الفورية مع ردود بث مباشر و15 قناة، وانتقل Chat إلى حلقة وكيل واحدة، وعزل حقيقي لكل مستخدم في بيئات النشر متعددة المستخدمين، وإعادة بناء Visualize مع التحقق والإصلاح المحلي، فضلاً عن ترقيات في Co-writer ومشاهد الملفات وتحليل MinerU السحابي وواجهة سطر الأوامر. تم تحديث الوثائق بالكامل على [deeptutor.info](https://deeptutor.info/).

> **[2026.5.28]** [v1.4.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.2) — استقرار وتحسين على v1.4.1: إلغاء حجب Gemini 2.5+ في Visualize وChat، وإصلاح توجيه المصادقة ContextVar (رقم 485)، وتصليب بروتوكول التفكير والأدوات الأصيلة، وتجربة مستخدم لبث سلس على جميع أسطح المحادثة، وشريط جانبي قابل للطي للزيارات الأخيرة، ودعم مزود Lemonade المحلي.

> **[2026.5.27]** [v1.4.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.1) — تصحيح أمني واستقرار: قفل صندوق أمان أدوات TutorBot، وعزل موارد لكل مستخدم، وبديل صور متعدد الوسائط لمزودي الرؤية، وواجهة برمجة HTTP/SSE للتحدث إلى TutorBot، وإصلاح تراجع محادثة v1.4.0.

> **[2026.5.22]** [v1.4.0](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.0) — إصدار عام من v1.4: الوضع التلقائي، وذاكرة ثلاثية الطبقات، والبحث العميق الوكيل / Solve / Question، وإعادة هيكلة LlamaIndex RAG، ودمج Visualize/Animator، فضلاً عن تطبيع جهد التفكير واحتياطي مخطط الأداة وبيئة التشغيل الآمنة للإعادة التلقائية.

<details>
<summary><b>الإصدارات السابقة (أكثر من أسبوعين)</b></summary>

> **[2026.5.21]** [v1.4.0-beta](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.0-beta) — محطة عمل ذاكرة ثلاثية الطبقات (L1/L2/L3)، وإعادة بناء كل قدرة محادثة على محرك وكيل واحد، وRAG فقط على LlamaIndex، وسطح إعدادات وقدرات موحّد.

> **[2026.5.10]** [v1.3.10](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.10) — استرداد CORS عن بُعد عبر Docker، و`DISABLE_SSL_VERIFY` عبر مزودي SDK، واستشهادات كتلة رمز أكثر أماناً، وإضافة Matrix E2EE اختيارية.

> **[2026.5.9]** [v1.3.9](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.9) — دعم TutorBot لـ Zulip وNVIDIA NIM، وتوجيه أكثر أماناً لنماذج التفكير، و`deeptutor start`، وتلميحات الشريط الجانبي، وتوحيد مخزن الجلسات.

> **[2026.5.8]** [v1.3.8](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.8) — نشر اختياري متعدد المستخدمين مع مساحات عمل معزولة لكل مستخدم، ومنح إدارية، ومسارات مصادقة، ووصول وقت تشغيل محدد النطاق.

> **[2026.5.4]** [v1.3.7](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.7) — إصلاحات نموذج/مزود التفكير، وتاريخ مرئي لفهرس المعرفة، وتحرير أكثر أماناً لقوالب Co-Writer.

> **[2026.5.3]** [v1.3.6](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.6) — اختيار النموذج القائم على الكتالوج للمحادثة وTutorBot، وإعادة فهرسة RAG أكثر أماناً، وإصلاحات حدود رمز OpenAI Responses، والتحقق من صحة محرر المهارات.

> **[2026.5.2]** [v1.3.5](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.5) — إعدادات إطلاق محلي أكثر سلاسة، واستعلامات RAG أكثر أماناً، ومصادقة تضمين محلي أنظف، وتلميع الوضع الداكن في الإعدادات.

> **[2026.5.1]** [v1.3.4](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.4) — استمرارية محادثة صفحة الكتاب وإعادة البناء، ومراجع محادثة إلى كتاب، ومعالجة أقوى للغة والتفكير، وتصليب استخراج وثائق RAG.

> **[2026.4.30]** [v1.3.3](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.3) — دعم تضمين NVIDIA NIM وGemini، وسياق Space موحّد لتاريخ المحادثة/المهارات/الذاكرة، ولقطات الجلسات، ومرونة إعادة الفهرسة في RAG.

> **[2026.4.29]** [v1.3.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.2) — عناوين URL شفافة لنقطة نهاية التضمين، ومرونة إعادة فهرسة RAG للمتجهات المثبتة غير الصالحة، وتنظيف الذاكرة لمخرجات نموذج التفكير، وإصلاح وقت تشغيل Deep Solve.

> **[2026.4.28]** [v1.3.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.1) — الاستقرار: توجيه RAG أكثر أماناً والتحقق من التضمين، واستمرارية Docker، وإدخال آمن من IME، ومتانة Windows/GBK.

> **[2026.4.27]** [v1.3.0](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.0) — فهارس KB ذات إصدارات مع سير عمل إعادة الفهرسة، ومساحة عمل المعرفة المُعادة بناؤها، واكتشاف تلقائي للتضمين مع محولات جديدة، ومحور Space.

> **[2026.4.25]** [v1.2.5](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.5) — مرفقات محادثة دائمة مع درج معاينة الملفات، وخطوط أنابيب قدرات تدرك المرفقات، وتصدير TutorBot بتنسيق Markdown.

> **[2026.4.25]** [v1.2.4](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.4) — مرفقات نص/رمز/SVG، وجولة إعداد بأمر واحد، وتصدير محادثة Markdown، وواجهة مستخدم مضغوطة لإدارة KB.

> **[2026.4.24]** [v1.2.3](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.3) — مرفقات المستندات (PDF/DOCX/XLSX/PPTX)، وعرض كتلة التفكير الاستنتاجي، ومحرر قالب Soul، وحفظ Co-Writer في دفتر الملاحظات.

> **[2026.4.22]** [v1.2.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.2) — نظام المهارات الذي يؤلفه المستخدم، وتحسين أداء إدخال المحادثة، وبدء TutorBot التلقائي، وواجهة مستخدم مكتبة الكتب، والشاشة الكاملة للتصور.

> **[2026.4.21]** [v1.2.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.1) — حدود رمز لكل مرحلة، وإعادة توليد الاستجابة عبر جميع نقاط الدخول، وإصلاحات توافق RAG وGemma.

> **[2026.4.20]** [v1.2.0](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.0) — محرك الكتاب "الكتاب الحي"، وCo-Writer متعدد المستندات، وتصورات HTML تفاعلية، و@-mention في بنك الأسئلة.

> **[2026.4.18]** [v1.1.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.1.2) — تبويب القنوات المدفوع بالمخطط، وتوحيد خط أنابيب RAG، وخارجية موجهات المحادثة.

> **[2026.4.17]** [v1.1.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.1.1) — "أجب الآن" العالمية، ومزامنة تمرير Co-Writer، ولوحة إعدادات موحّدة، وزر إيقاف البث.

> **[2026.4.15]** [v1.1.0](https://github.com/HKUDS/DeepTutor/releases/tag/v1.1.0) — تجديد شامل لرياضيات LaTeX الكتلية، ومسبار تشخيصي للنماذج اللغوية الكبيرة، وإرشادات Docker والنماذج اللغوية المحلية.

> **[2026.4.14]** [v1.1.0-beta](https://github.com/HKUDS/DeepTutor/releases/tag/v1.1.0-beta) — جلسات قابلة للإشارة المرجعية، وثيمة Snow، ونبضات قلب WebSocket وإعادة الاتصال التلقائي، وتجديد سجل التضمين.

> **[2026.4.13]** [v1.0.3](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.3) — دفتر ملاحظات الأسئلة مع الإشارات المرجعية والفئات، وMermaid في Visualize، وكشف عدم تطابق التضمين، وتوافق Qwen/vLLM، ودعم LM Studio وllama.cpp، وثيمة Glass.

> **[2026.4.11]** [v1.0.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.2) — توحيد البحث مع احتياطي SearXNG، وإصلاح تبديل المزود، وإصلاحات تسرب الموارد في الواجهة الأمامية.

> **[2026.4.10]** [v1.0.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.1) — قدرة Visualize (Chart.js/SVG)، ومنع تكرار الاختبارات، ودعم نموذج o4-mini.

> **[2026.4.10]** [v1.0.0-beta.4](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.0-beta.4) — تتبع تقدم التضمين مع إعادة المحاولة عند حد المعدل، وإصلاحات التبعيات عبر المنصات، وإصلاح التحقق من MIME.

> **[2026.4.8]** [v1.0.0-beta.3](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.0-beta.3) — SDK أصيل لـ OpenAI/Anthropic (إسقاط litellm)، ودعم Math Animator على Windows، وتحليل JSON قوي، وi18n صيني كامل.

> **[2026.4.7]** [v1.0.0-beta.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.0-beta.2) — إعادة تحميل الإعدادات الساخنة، وإخراج MinerU المتداخل، وإصلاح WebSocket، والحد الأدنى Python 3.11+.

> **[2026.4.4]** [v1.0.0-beta.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.0-beta.1) — إعادة كتابة معمارية أصيلة للوكيل (~200 ألف سطر): نموذج إضافات الأدوات والقدرات، وCLI وSDK، وTutorBot، وCo-Writer، والتعلم الموجّه، والذاكرة الدائمة.

> **[2026.1.23]** [v0.6.0](https://github.com/HKUDS/DeepTutor/releases/tag/v0.6.0) — استمرارية الجلسة، ورفع المستندات التدريجي، واستيراد مرن لخط أنابيب RAG، وتوطين صيني كامل.

> **[2026.1.18]** [v0.5.2](https://github.com/HKUDS/DeepTutor/releases/tag/v0.5.2) — دعم Docling لـ RAG-Anything، وتحسين نظام التسجيل، وإصلاح الأخطاء.

> **[2026.1.15]** [v0.5.0](https://github.com/HKUDS/DeepTutor/releases/tag/v0.5.0) — تكوين موحّد للخدمة، واختيار خط أنابيب RAG لكل قاعدة معرفية، وتجديد توليد الأسئلة، وتخصيص الشريط الجانبي.

> **[2026.1.9]** [v0.4.0](https://github.com/HKUDS/DeepTutor/releases/tag/v0.4.0) — دعم نماذج لغوية كبيرة وتضمين متعدد المزودين، وصفحة رئيسية جديدة، وفصل وحدة RAG، وإعادة هيكلة متغيرات البيئة.

> **[2026.1.5]** [v0.3.0](https://github.com/HKUDS/DeepTutor/releases/tag/v0.3.0) — معمارية PromptManager الموحّدة، وCI/CD عبر GitHub Actions، وصور Docker مُبنية مسبقاً على GHCR.

> **[2026.1.2]** [v0.2.0](https://github.com/HKUDS/DeepTutor/releases/tag/v0.2.0) — نشر Docker، وترقية Next.js 16 وReact 19، وتصليب أمان WebSocket، وإصلاح ثغرات حرجة.

</details>

### 📰 الأخبار

> **[2026.5.22]** 🌐 موقع وثائقنا الرسمي متاح الآن على [**deeptutor.info**](https://deeptutor.info/) — الأدلة والمراجع وجولات القدرات كلها في مكان واحد.

> **[2026.4.19]** 🎉 وصلنا إلى 20 ألف نجمة بعد 111 يوماً! شكراً على الدعم الرائع — نلتزم بالتطوير المستمر نحو تدريس شخصي وذكي حقيقي للجميع.

> **[2026.4.10]** 📄 ورقتنا البحثية متاحة الآن على arXiv! اقرأ [النسخة الأولية](https://arxiv.org/abs/2604.26962) لتعرف المزيد عن التصميم والأفكار وراء DeepTutor.

> **[2026.4.4]** لم نرَ بعضنا منذ زمن! ✨ DeepTutor v1.0.0 هنا أخيراً — تطور أصيل للوكيل يتميز بإعادة كتابة معمارية من الصفر، وTutorBot، وتبديل وضع مرن تحت رخصة Apache-2.0. تبدأ فصل جديد، وتستمر قصتنا!

> **[2026.2.6]** 🚀 وصلنا إلى 10 آلاف نجمة في 39 يوماً فقط! شكر جزيل لمجتمعنا الرائع على هذا الدعم!

> **[2026.1.1]** سنة سعيدة! انضم إلى [Discord](https://discord.gg/eRsjPgMU4t)، أو [WeChat](https://github.com/HKUDS/DeepTutor/issues/78)، أو [النقاشات](https://github.com/HKUDS/DeepTutor/discussions) — لنشكّل معاً مستقبل DeepTutor!

> **[2025.12.29]** تم إطلاق DeepTutor رسمياً!

## ✨ المميزات الرئيسية

يتمحور DeepTutor حول بيئة تشغيل أصيلة للوكيل: يوجّه ChatOrchestrator المشترك كل دور إلى القدرات، ويكشف ToolRegistry عن أدوات من استخدام واحد عندما يحتاجها النموذج، ويتيح CapabilityRegistry لسير العمل الأعمق الاستيلاء على الدور عندما تحتاج المهمة إلى هيكلة.

<div align="center">
<img src="../../assets/figs/system/system%20architecture.png" alt="معمارية نظام DeepTutor" width="900">
</div>

**مساحة عمل تعليمية واحدة**

- **المحادثة كحلقة افتراضية** — يشترك التدريس غير الرسمي والأسئلة والأجوبة المرتكزة على المصادر وDeep Solve وDeep Question وDeep Research وVisualize والوضع التلقائي في نفس سياق الجلسة ومخزون المصادر.
- **أسطح التعلم المترابطة** — مسودات Co-Writer وصفحات الكتاب وقواعد المعرفة وأصول Space والذاكرة هي مساحات عمل منفصلة، لكنها تُغذّي نفس وقت تشغيل الوكيل بدلاً من أن تصبح تطبيقات معزولة.
- **الشركاء للرفقة الدائمة** — الرفقاء المتصلون بتطبيقات المراسلة الفورية يعملون الآن على نفس حلقة وكيل المحادثة للمنتج الرئيسي، مع مساحة عمل اصطناعية خاصة ومكتبة مخصصة.

**الأدوات والذاكرة والتحكم**

- **أدوات قابلة للتركيب** — يمكن تثبيت RAG وقراءة المصادر وقراءة/كتابة الذاكرة ودفاتر الملاحظات وجلب URL والبحث في GitHub وإيقاف السؤال للمستخدم والتنفيذ في صندوق الأمان وأدوات اختيارية للعصف الذهني/الويب/الأوراق/العقل وفقاً للسياق والإعدادات.
- **ذاكرة ثلاثية الطبقات** — آثار L1 وملخصات L2 لكل سطح وتوليف L3 عبر الأسطح تجعل التخصيص قابلاً للفحص بدلاً من إخفائه خلف صندوق أسود.
- **إعدادات موحّدة وCLI** — كتالوجات النماذج والتضمينات والبحث والشبكة وخوادم MCP والأدوات والقدرات وإعدادات النشر قابلة للتحرير من واجهة مستخدم الويب والبرمجة من `deeptutor`.

---

## 🚀 البدء

يأتي DeepTutor بأربعة مسارات تثبيت. وكلها تشترك في تخطيط مساحة عمل واحد: تعيش الإعدادات في `data/user/settings/` تحت الدليل الذي تُطلق منه التطبيق (أو تحت `DEEPTUTOR_HOME` / `deeptutor start --home` إذا حددت واحداً صراحةً). للتطبيق الكامل، التدفق الموصى به هو **اختر دليل مساحة عمل → تثبيت → `deeptutor init` → `deeptutor start`**.

> ✨ **v1.4.3 متاح الآن.** `pip install -U deeptutor` يحصل على أحدث إصدار مستقر. الإصدارات التجريبية (عند توفرها) تُفعَّل بـ `pip install --pre -U deeptutor`.

### الخيار 1 — التثبيت من PyPI

تطبيق ويب محلي كامل + CLI، لا يلزم الاستنساخ. يحتاج **Python 3.11+** وبيئة تشغيل **Node.js 20+** في PATH (يُشغَّل خادم Next.js المستقل المُحزَّم بواسطة `deeptutor start`).

```bash
mkdir -p my-deeptutor && cd my-deeptutor
pip install -U deeptutor
deeptutor init     # يطلب المنافذ + مزود LLM + تضمين اختياري
deeptutor start    # يشغّل الخلفية + الواجهة الأمامية؛ ابقِ الطرفية مفتوحة
```

يطلب `deeptutor init` منفذ الخلفية (افتراضي `8001`)، ومنفذ الواجهة الأمامية (افتراضي `3782`)، ومزود LLM / عنوان URL الأساسي / مفتاح API / النموذج، ومزود تضمين اختياري لقاعدة المعرفة / RAG.

بعد `deeptutor start`، افتح عنوان URL للواجهة الأمامية المطبوع في الطرفية — افتراضياً [http://127.0.0.1:3782](http://127.0.0.1:3782). اضغط `Ctrl+C` في تلك الطرفية لإيقاف الخلفية والواجهة الأمامية معاً. تخطي `deeptutor init` لا بأس به للتجربة السريعة؛ يُقلع التطبيق بالمنافذ الافتراضية وإعدادات نموذج فارغة، قم بتهيئتها لاحقاً في **الإعدادات ← النماذج**.

### الخيار 2 — التثبيت من المصدر

للتطوير مقابل نسخة مسحوبة. استخدم **Python 3.11+** و**Node.js 22 LTS** لمطابقة CI وDocker.

```bash
git clone https://github.com/HKUDS/DeepTutor.git
cd DeepTutor

# إنشاء venv (macOS/Linux). Windows PowerShell:
#   py -3.11 -m venv .venv ; .\.venv\Scripts\Activate.ps1
python3 -m venv .venv && source .venv/bin/activate
python -m pip install --upgrade pip

# تثبيت تبعيات الخلفية والواجهة الأمامية
python -m pip install -e .
( cd web && npm ci --legacy-peer-deps )

deeptutor init
deeptutor start
```

تشغّل تثبيتات المصدر Next.js في وضع التطوير مقابل دليل `web/` المحلي؛ كل شيء آخر (تخطيط التهيئة، المنافذ، الإيقاف بـ `Ctrl+C`) يطابق الخيار 1.

<details>
<summary><b>بيئة Conda</b> (بديلاً عن <code>venv</code>)</summary>

```bash
conda create -n deeptutor python=3.11
conda activate deeptutor
python -m pip install --upgrade pip
```

</details>

<details>
<summary><b>إضافات التثبيت الاختيارية</b> — dev / partners / matrix / math-animator</summary>

```bash
pip install -e ".[dev]"             # أدوات الاختبار/الفحص
pip install -e ".[partners]"        # SDK قنوات شركاء IM + عميل MCP
pip install -e ".[matrix]"          # قناة Matrix بدون E2EE/libolm
pip install -e ".[matrix-e2e]"      # Matrix E2EE؛ يتطلب libolm
pip install -e ".[math-animator]"   # إضافة Manim؛ تتطلب LaTeX/ffmpeg/مكتبات النظام
```

</details>

<details>
<summary><b>تعديلات تبعيات الواجهة الأمامية وحل مشاكل خادم التطوير</b></summary>

**تغيير تبعيات الواجهة الأمامية:** شغّل `npm install --legacy-peer-deps` لتحديث `web/package-lock.json`، ثم ارفع كلاً من `web/package.json` و`web/package-lock.json`.

**خادم تطوير متوقف:** إذا أبلغ `deeptutor start` عن واجهة أمامية موجودة لا تستجيب، أوقف الـ PID الذي يطبعه. إذا لم يكن هناك أي عملية Next.js تعمل فعلياً، فملفات القفل قديمة — احذفها وأعد المحاولة:

```bash
rm -f web/.next/dev/lock web/.next/lock
deeptutor start
```

</details>

### الخيار 3 — Docker

حاوية واحدة لتطبيق الويب الكامل. الصور على GitHub Container Registry:

- `ghcr.io/hkuds/deeptutor:latest` — إصدار مستقر
- `ghcr.io/hkuds/deeptutor:pre` — إصدار تجريبي، عند توفره

```bash
docker run --rm --name deeptutor \
  -p 127.0.0.1:3782:3782 \
  -p 127.0.0.1:8001:8001 \
  -v deeptutor-data:/app/data \
  ghcr.io/hkuds/deeptutor:latest
```

> ⚠️ **عيّن كلاً من `3782` و`8001`.** يخدم `3782` واجهة مستخدم الويب؛ `8001` هو خلفية FastAPI التي يستدعيها متصفحك مباشرةً — لا يوجد وكيل داخل الحاوية. تخطي تعيين `8001` والصفحة ستظل تُحمَّل، لكن **الإعدادات** ستُظهر "الخلفية غير متاحة" وستظل غير قابلة للاستخدام.

افتح [http://127.0.0.1:3782](http://127.0.0.1:3782). تُنشئ الحاوية `/app/data/user/settings/*.json` عند الإقلاع الأول؛ قم بتهيئة مزودي النماذج من صفحة إعدادات الويب. تبقى التهيئة ومفاتيح API والسجلات وملفات مساحة العمل والذاكرة وقواعد المعرفة في وحدة تخزين `deeptutor-data`.

- **منافذ مضيف مختلفة:** غيّر الجانب الأيسر من كل تعيين `-p host:container` (مثلاً `-p 127.0.0.1:8088:3782`). إذا غيّرت المنافذ على جانب الحاوية في `/app/data/user/settings/system.json`، أعد التشغيل وحدّث الجانب الأيمن من كل تعيين ليطابق ذلك.
- **وضع المنفصل:** أضف `-d`، ثم `docker logs -f deeptutor` للمتابعة، و`docker stop deeptutor` للإيقاف، و`docker rm deeptutor` قبل إعادة استخدام الاسم. تحتفظ وحدة تخزين `deeptutor-data` بإعداداتك ومساحة عملك عبر إعادات التشغيل.

**Docker عن بُعد / وكيل عكسي:** تعمل واجهة مستخدم الويب في المتصفح، لذا يحتاج المتصفح إلى عنوان URL للخلفية يمكنه الوصول إليه. للخوادم البعيدة، افتح **الإعدادات ← الشبكة** أو عدّل `data/user/settings/system.json`:

```json
{
  "next_public_api_base_external": "https://deeptutor.example.com"
}
```

يُقبَل `public_api_base` كاسم مستعار للتوافق ويُطبَّع إلى `next_public_api_base_external` عند الحفظ. يستخدم CORS **منشآت** الواجهة الأمامية، وليس عناوين URL لواجهة برمجة التطبيقات. مع تعطيل المصادقة، يسمح DeepTutor بمنشآت متصفح HTTP/HTTPS العادية افتراضياً. مع تفعيل المصادقة، أضف منشآت الواجهة الأمامية الدقيقة:

```json
{
  "cors_origins": ["https://deeptutor.example.com"]
}
```

<details>
<summary><b>الاتصال بـ Ollama / LM Studio / llama.cpp / vLLM / Lemonade على المضيف</b></summary>

داخل Docker، يشير `localhost` إلى الحاوية نفسها، وليس جهازك المضيف. للوصول إلى خدمة نموذج تعمل على المضيف، استخدم بوابة المضيف (موصى بها):

```bash
docker run --rm --name deeptutor \
  -p 127.0.0.1:3782:3782 -p 127.0.0.1:8001:8001 \
  --add-host=host.docker.internal:host-gateway \
  -v deeptutor-data:/app/data \
  ghcr.io/hkuds/deeptutor:latest
```

ثم في **الإعدادات ← النماذج**، وجّه عنوان URL الأساسي للمزود إلى `host.docker.internal`:

- Ollama LLM: `http://host.docker.internal:11434/v1`
- Ollama embedding: `http://host.docker.internal:11434/api/embed`
- LM Studio: `http://host.docker.internal:1234/v1`
- llama.cpp: `http://host.docker.internal:8080/v1`
- Lemonade: `http://host.docker.internal:13305/api/v1`

عادةً ما يحل Docker Desktop (macOS/Windows) `host.docker.internal` بدون `--add-host`. على Linux، يُعدّ هذا العلم الطريقة المحمولة لإنشاء هذا الاسم المضيف على Docker Engine الحديث.

**بديل Linux — شبكة المضيف:** أضف `--network=host` وأزل علامات `-p`. تشارك الحاوية شبكة المضيف مباشرةً، لذا افتح [http://127.0.0.1:3782](http://127.0.0.1:3782) (أو `frontend_port` في `system.json`)، ويمكن الوصول إلى خدمات المضيف بعناوين URL العادية لـ localhost مثل `http://127.0.0.1:11434/v1`. لاحظ أن شبكة المضيف تكشف منافذ الحاوية مباشرةً على المضيف وقد تتعارض مع الخدمات الموجودة.

</details>

### صندوق أمان تنفيذ الرمز (مهارات المكتب)

مهارات المكتب المدمجة — **docx / pdf / pptx / xlsx** — تعمل عن طريق جعل النموذج يكتب برنامج Python قصير (`python-docx`، `reportlab`، `openpyxl`، ...)، وتشغيله عبر أدوات `exec` / `code_execution`، وإرجاع عنوان URL للتنزيل. تُثبَّت هذه الأدوات عندما تكون خلفية صندوق الأمان نشطة، وهي كذلك **افتراضياً** في كل شكل نشر:

- **محلي (الخيار 1 / 2) وDocker (الخيار 3، حاوية واحدة):** يُشغَّل صندوق أمان عمليات فرعية مقيّدة لرمز النموذج (على المضيف محلياً، أو داخل الحاوية تحت Docker — والحاوية هي حدود عزلها الخاصة).
- **docker-compose:** يُوجَّه بدلاً من ذلك إلى **مرافق runner** محصَّن وأقل امتيازاً (`Dockerfile.runner`) عبر `DEEPTUTOR_SANDBOX_RUNNER_URL` — أقوى وضع، ويُفضَّل تلقائياً عند توفره.

يتحكم إعداد `sandbox_allow_subprocess` في `data/user/settings/system.json` (افتراضي `true`) في صندوق أمان العمليات الفرعية. تشغيل الرمز المُولَّد بواسطة النموذج على مضيفك هو قرار ثقة حقيقي — اضبطه على `false` (أو صدّر `DEEPTUTOR_SANDBOX_ALLOW_SUBPROCESS=0`) لتعطيل التنفيذ على جانب المضيف، على حساب عدم قدرة مهارات المكتب على إنتاج الملفات بعد الآن.

### الخيار 4 — واجهة سطر الأوامر فقط

عندما لا تحتاج إلى واجهة مستخدم الويب. يُثبَّت حزمة CLI فقط من نسخة مسحوبة من المصدر، وليس من PyPI.

```bash
git clone https://github.com/HKUDS/DeepTutor.git
cd DeepTutor

# إنشاء venv (macOS/Linux). Windows PowerShell:
#   py -3.11 -m venv .venv-cli ; .\.venv-cli\Scripts\Activate.ps1
python3 -m venv .venv-cli && source .venv-cli/bin/activate
python -m pip install --upgrade pip

python -m pip install -e ./packaging/deeptutor-cli
deeptutor init --cli
deeptutor chat
```

يشارك `deeptutor init --cli` نفس تخطيط `data/user/settings/` مع التطبيق الكامل لكنه يتخطى موجهات منفذ الخلفية/الواجهة الأمامية ويضبط التضمينات افتراضياً على **إيقاف** (اختر `نعم` إذا كنت تخطط لاستخدام `deeptutor kb …` أو أدوات RAG). لا يزال يكتب تخطيط وقت تشغيل كامل (`system.json`، `auth.json`، `integrations.json`، `model_catalog.json`، `main.yaml`، `agents.yaml`) ولا يزال يطلب مزود LLM النشط والنموذج.

<details>
<summary><b>الأوامر الشائعة</b></summary>

```bash
deeptutor chat                                          # REPL تفاعلي
deeptutor chat --capability deep_solve --tool rag --kb my-kb
deeptutor run chat "Explain Fourier transform"
deeptutor run deep_solve "Solve x^2 = 4" --tool rag --kb my-kb
deeptutor kb create my-kb --doc textbook.pdf
deeptutor memory show
deeptutor config show
```

</details>

لا يشحن تثبيت `deeptutor-cli` المحلي بأصول الويب أو تبعيات الخادم. احتفظ بالنسخة المسحوبة من المصدر — يشير التثبيت القابل للتحرير إليها. لإضافة تطبيق الويب لاحقاً، ثبّت حزمة PyPI (الخيار 1) وشغّل `deeptutor init` + `deeptutor start` من نفس مساحة العمل.

### مرجع التهيئة

<details>
<summary><b>ملفات التهيئة تحت <code>data/user/settings/</code></b> — مرجع JSON/YAML</summary>

كل شيء تحت `data/user/settings/` هو JSON/YAML عادي. صفحة **الإعدادات** في المتصفح هي المحرر الموصى به.

| الملف | الغرض |
|:---|:---|
| `model_catalog.json` | ملفات تعريف مزودي النماذج اللغوية الكبيرة والتضمين والبحث؛ مفاتيح API؛ النماذج النشطة |
| `system.json` | منافذ الخلفية/الواجهة الأمامية، وقاعدة API العامة، وCORS، والتحقق من SSL، ودليل المرفقات |
| `auth.json` | تبديل مصادقة اختياري، واسم مستخدم، وتجزئة كلمة مرور، وإعدادات الرمز/الكوكي |
| `integrations.json` | إعدادات تكامل PocketBase والمرافق الاختيارية |
| `interface.json` | تفضيلات لغة واجهة المستخدم / الثيمة / الشريط الجانبي |
| `main.yaml` | افتراضيات سلوك وقت التشغيل وحقن المسار |
| `agents.yaml` | إعدادات درجة حرارة القدرة/الأداة والرمز |

ملف `.env` في جذر المشروع **لا يُقرأ** كملف تهيئة للتطبيق. للإعداد الأدنى للنموذج، افتح **الإعدادات ← النماذج**، أضف ملف تعريف LLM (عنوان URL الأساسي / مفتاح API / اسم النموذج)، واحفظ. أضف ملف تعريف التضمين فقط إذا كنت تخطط لاستخدام ميزات قاعدة المعرفة / RAG.

</details>

## 📖 استكشاف DeepTutor

تتبع جولة README أسطح المنتج بالترتيب الذي ستقابلها غالباً: المحادثة، الشريك، Co-Writer، الكتاب، المعرفة، Space، الذاكرة، والإعدادات. اللقطات أدناه مأخوذة من شجرة `assets/figs` المُعاد تنظيمها؛ الصور القديمة المؤرشفة لا تُستخدم هنا عمداً.

### 💬 المحادثة — حلقة الوكيل التي تستخدمها فعلاً

<div align="center">
<img src="../../assets/figs/webui/chat.png" alt="مساحة عمل محادثة DeepTutor" width="900">
</div>

المحادثة هي القدرة الافتراضية والمكان الذي يبدأ فيه معظم العمل. يمكن لخيط واحد أن يتحدث عادياً، ويستدعي الأدوات، ويرتكز على قواعد المعرفة المحددة، ويقرأ المرفقات، ويكتب سجلات دفتر الملاحظات، ويستمر بنفس مخزون المصادر عبر الأدوار.

<div align="center">
<img src="../../assets/figs/system/chat-agent-loop.png" alt="حلقة وكيل محادثة DeepTutor" width="900">
</div>

الحلقة الحالية بسيطة عمداً: يفكر النموذج في جولات، ويستدعي الأدوات عند الحاجة، ويلاحظ نتائج الأدوات، وينتهي عندما يكون لديه دليل كافٍ. الأدوات القابلة للتبديل من قِبَل المستخدم هي `brainstorm` و`web_search` و`paper_search` و`reason`؛ الأدوات السياقية مثل `rag` و`read_source` و`read_memory` و`write_memory` و`read_skill` و`load_tools` و`exec` و`web_fetch` و`ask_user` و`list_notebook` و`write_note` و`github` تُثبَّت عندما يكون للدور السياق الصحيح.

المحادثة هي أيضاً نقطة انطلاق للقدرات الأعمق: `deep_solve` للتفكير المعمق، و`deep_question` لتوليد الأسئلة، و`deep_research` للتقارير المستشهَد بها، و`visualize` و`math_animator` للمخرجات المرئية، و`auto` للتوجيه، و`mastery_path` لتدفقات خطط التعلم.

### 🤝 الشريك — رفقاء دائمون على نفس الدماغ

<div align="center">
<img src="../../assets/figs/webui/partners.png" alt="مساحة عمل شركاء DeepTutor" width="900">
</div>

يحل الشركاء محل محرك TutorBot القديم بنموذج أنظف: كل رسالة ويب أو IM واردة تصبح دوراً عادياً لـ ChatOrchestrator داخل مساحة عمل محدودة بنطاق الشريك. لا يوجد دماغ بوت منفصل يجب الحفاظ على مزامنته.

<div align="center">
<img src="../../assets/figs/system/partners-architecture.png" alt="معمارية شركاء DeepTutor" width="900">
</div>

لكل شريك `SOUL.md` واختيار نموذج وقنوات وسياسة أدوات ومكتبة مخصصة. تُنسخ قواعد المعرفة والمهارات ودفاتر الملاحظات إلى `data/partners/<id>/workspace/`، لذا تعمل نفس أدوات RAG والمهارة ودفتر الملاحظات والذاكرة بدون حالات خاصة.

<div align="center">
<img src="../../assets/figs/webui/partners02.png" alt="عرض تفاصيل شريك DeepTutor" width="900">
</div>

طبقة القناة مدفوعة بالمخطط ويمكنها الاتصال بمنصات IM مثل Feishu وTelegram وSlack وDingTalk وQQ/Napcat وWeCom وWhatsApp وZulip وMatrix وMicrosoft Teams بناءً على الإضافات المثبتة والبيانات الاعتمادية المهيأة.

### ✍️ Co-Writer — صياغة Markdown واعية بالتحديد

Co-Writer هو مساحة عمل Markdown ذات عرض مقسَّم للتقارير والدروس التعليمية والملاحظات والقطع التعليمية الطويلة. تحفظ المستندات تلقائياً، وتُظهر معاينة مباشرة، ويمكن حفظها مرة أخرى في دفاتر الملاحظات عندما تصبح المسودة سياقاً قابلاً لإعادة الاستخدام.

حدد النص واطلب من DeepTutor إعادة كتابته أو توسيعه أو تقصيره. يحتفظ وكيل التحرير بآثار استدعاءات الأدوات ويمكنه ترسيخ التعديل في قاعدة معرفة أو دليل ويب، لذا يتصرف Co-Writer أكثر كمحرر مع استرداد بدلاً من كونه مربع نص منفصل.

### 📖 الكتاب — كتب حية من موادك

<p align="center">
<img src="../../assets/figs/webui/book01.png" alt="عرض قراءة كتاب DeepTutor" width="31%">
&nbsp;
<img src="../../assets/figs/webui/book02.png" alt="عرض كتلة تفاعلية في كتاب DeepTutor" width="31%">
&nbsp;
<img src="../../assets/figs/webui/book03.png" alt="عرض إنشاء كتاب DeepTutor" width="31%">
</p>

يحوّل الكتاب المصادر المحددة إلى مواد تعليمية تفاعلية. يمكن أن يبدأ الكتاب من قواعد المعرفة أو دفاتر الملاحظات أو بنوك الأسئلة أو تاريخ المحادثة؛ يقترح تدفق الإنشاء هيكلاً قبل توليد المحتوى، لذا يمكن للمستخدمين مراجعة الشكل بدلاً من قبول مخرجات عشوائية.

يُجمِّع BookEngine الصفحات إلى كتل مكتوبة: النص والأقسام والتنبيهات والاختبارات وبطاقات الفلاش والجداول الزمنية والرمز والأشكال وHTML التفاعلية والرسوم المتحركة وأشكال المفاهيم والغوص العميق وملاحظات المستخدم. أوامر الصيانة مثل `deeptutor book health` و`deeptutor book refresh-fingerprints` تساعد في الكشف عن انجراف المعرفة المصدرية من الصفحات المُجمَّعة.

### 📚 المعرفة — مكتبات RAG ذات إصدارات

<div align="center">
<img src="../../assets/figs/webui/knowledge.png" alt="مساحة عمل قاعدة المعرفة في DeepTutor" width="900">
</div>

قواعد المعرفة هي مجموعات المستندات وراء RAG. المكدس الحالي يعمل على LlamaIndex فقط، مع تخطيط تخزين مسطح `version-N` مُفهرَس بتوقيع التضمين. تحتفظ إعادة الفهرسة بالإصدارات السابقة وتتجنب الكتابة فوق الفهرس العامل أثناء معالجة المستندات الجديدة.

تعرض مساحة عمل الويب الملفات والرفع وإصدارات الفهرس والإعدادات. يعكس CLI نفس دورة الحياة بـ `deeptutor kb list` و`info` و`create` و`add` و`search` و`set-default` و`delete`.

### 🌐 Space — المهارات والشخصيات والسياق القابل لإعادة الاستخدام

<div align="center">
<img src="../../assets/figs/webui/space.png" alt="مساحة عمل Space في DeepTutor" width="900">
</div>

Space هو طبقة المكتبة للسياق القابل لإعادة الاستخدام. يجمع المهارات التي يؤلفها المستخدم والشخصيات ودفاتر الملاحظات وتاريخ المحادثة وأصول بنك الأسئلة حتى يمكن توجيه الوكيل بسياق متعمد بدلاً من الموجهات المخصصة.

تُخزَّن المهارات كملفات `SKILL.md` تحت مساحة عمل المستخدم ويمكن تصنيفها أو تحريرها أو إبقاؤها للقراءة فقط عندما تكون مدمجة. تتبع الشخصيات نفس الفكرة للدور والصوت. يمكن تعيين هذه الأصول للشركاء والإشارة إليها في المحادثة وإعادة استخدامها عبر سير عمل التعلم.

### 🧠 الذاكرة — تخصيص قابل للفحص

<div align="center">
<img src="../../assets/figs/webui/memory01.png" alt="محطة عمل الذاكرة في DeepTutor" width="900">
</div>

الذاكرة نظام ثلاثي الطبقات متجذّر في مساحة عمل المستخدم النشطة: `trace/<surface>/<date>.jsonl` لآثار أحداث L1، و`L2/<surface>.md` لحقائق كل سطح، و`L3/<recent|profile|scope|preferences>.md` للتوليف عبر الأسطح.

<div align="center">
<img src="../../assets/figs/webui/memory02.png" alt="رسم بياني لذاكرة DeepTutor" width="900">
</div>

أسطح الذاكرة المدعومة هي `chat` و`notebook` و`quiz` و`kb` و`book` و`tutorbot` و`cowriter`. يبقى اسم سطح `tutorbot` القديم في طبقة الذاكرة للتوافق حتى لو أصبح نموذج المرافق الموجّه للمنتج هو الشركاء الآن. تتيح لك محطة العمل الفحص والتحرير وتشغيل التوحيد واستخدام الرسم البياني لتتبع الادعاءات المُوليفة إلى حقائقها الداعمة والأحداث الخام.

### ⚙️ الإعدادات — لوحة تحكم واحدة

<div align="center">
<img src="../../assets/figs/webui/settings.png" alt="مساحة عمل الإعدادات في DeepTutor" width="900">
</div>

الإعدادات هي لوحة التحكم التشغيلية. تشمل المظهر ومنافذ الشبكة وقاعدة API الخارجية وكتالوجات LLM والتضمين ومزودي البحث وتحليل MinerU وميزانيات القدرات ونبضات الذاكرة وخوادم MCP والأدوات المدمجة وقائمة الأدوات الاختيارية المفعّلة.

تستخدم معظم الإعدادات تدفق صياغة-وتطبيق حتى يتمكن المستخدمون من اختبار المزودين قبل الالتزام بهم. ملفات `.env` في جذر المشروع تُتجاهل عمداً؛ يعيش تهيئة وقت التشغيل تحت `data/user/settings/*.json` إلا إذا وجّه `DEEPTUTOR_HOME` أو `deeptutor start --home` التطبيق في مكان آخر.

---

## ⌨️ واجهة سطر أوامر DeepTutor — الواجهة الأصيلة للوكلاء

DeepTutor أصيلة لـ CLI: يمكن لنفس نقطة دخول `deeptutor` تهيئة مساحة عمل، وتشغيل تطبيق الويب، وتشغيل قدرة من استخدام واحد، وفتح REPL تفاعلي، وإدارة قواعد المعرفة، وفحص الجلسات، وصيانة الكتب، وتشغيل الشركاء.

```bash
deeptutor run chat "Explain Fourier transform" --tool rag --kb textbook
deeptutor run deep_solve "Solve x^2 = 4" --tool reason
deeptutor chat --capability deep_research --kb papers
deeptutor partner create math-tutor --soul "Socratic math tutor"
deeptutor kb create calculus --doc textbook.pdf
```

<details>
<summary><b>مرجع الأوامر</b></summary>

| الأمر | الوصف |
|:---|:---|
| `deeptutor init` | إنشاء أو تحديث `data/user/settings` لمساحة العمل الحالية |
| `deeptutor start [--home PATH]` | تشغيل الخلفية + الواجهة الأمامية معاً |
| `deeptutor serve [--port PORT]` | تشغيل خلفية FastAPI فقط |
| `deeptutor run <capability> <message>` | تشغيل دور قدرة واحدة (`chat`، `deep_solve`، `deep_question`، `deep_research`، `visualize`، `math_animator`، `auto`، `mastery_path`) |
| `deeptutor chat` | REPL تفاعلي مع تحكمات القدرة والأداة وقاعدة المعرفة ودفتر الملاحظات والتاريخ |
| `deeptutor partner list/create/start/stop` | إدارة الشركاء المتصلين بـ IM |
| `deeptutor kb list/info/create/add/search/set-default/delete` | إدارة قواعد المعرفة LlamaIndex |
| `deeptutor memory show/clear` | فحص مستندات الذاكرة L2/L3 أو مسح ذاكرة L1/الكل |
| `deeptutor session list/show/open/rename/delete` | إدارة الجلسات المشتركة |
| `deeptutor notebook list/create/show/add-md/replace-md/remove-record` | إدارة دفاتر الملاحظات من ملفات Markdown |
| `deeptutor book list/health/refresh-fingerprints` | فحص الكتب وتحديث بصمات المصادر |
| `deeptutor plugin list/info` | فحص الأدوات والقدرات المسجلة |
| `deeptutor config show` | طباعة ملخص التهيئة |
| `deeptutor provider login <provider>` | إدارة تسجيل دخول OAuth للمزود حيثما كان مدعوماً |

</details>

توزيع CLI فقط موجود في `packaging/deeptutor-cli`؛ في هذه النسخة يجب تثبيته من المصدر بـ `python -m pip install -e ./packaging/deeptutor-cli`. حزمة `deeptutor-cli` العامة غير متاحة حالياً على PyPI، لذا يحتفظ قسم البدء الرئيسي بمسار التثبيت من المصدر.

---

## 👥 متعدد المستخدمين — النشر المشترك

<div align="center">
<img src="../../assets/figs/webui/multi-user.png" alt="مساحة عمل مشرف متعدد المستخدمين في DeepTutor" width="900">
</div>

المصادقة اختيارية ومعطلة افتراضياً. عند التفعيل، يصبح DeepTutor نشراً مشتركاً مع مساحة عمل مشرف واحدة، ومساحات عمل لكل مستخدم، ومساحات عمل للشركاء، وحالة النظام تحت شجرة `data/` واحدة.

```text
data/
├── user/                         # مساحة عمل المشرف والإعدادات
├── users/<uid>/                  # نطاق مستخدم غير مشرف
│   ├── user/chat_history.db
│   ├── user/settings/interface.json
│   ├── user/workspace/{chat,co-writer,book,memory,notebook,...}
│   └── knowledge_bases/...
├── partners/<id>/workspace/      # نطاق المستخدم الاصطناعي للشريك
└── system/
    ├── auth/users.json
    ├── grants/<uid>.json
    └── audit/usage.jsonl
```

يصبح المستخدم المسجَّل الأول مشرفاً ويمكنه تهيئة كتالوجات النماذج وبيانات اعتماد المزود وقواعد المعرفة والمهارات ومنح المستخدمين. يحصل المستخدمون غير المشرفين على تاريخ محادثة معزول وذاكرة ودفاتر ملاحظات وقواعد معرفة شخصية وصفحة إعدادات منقوصة؛ تظهر الموارد المعيّنة من المشرف كخيارات محدودة النطاق للقراءة فقط بدلاً من كشف مفاتيح API أو الداخل التقني للمزود.

لتجربة محلية، اضبط `data/user/settings/auth.json` لتفعيل المصادقة، وأعد تشغيل `deeptutor start`، وسجّل أول مشرف على `/register`، ثم أنشئ مستخدمين من `/admin/users` وعيّن النماذج وقواعد المعرفة والمهارات وسياسة الأدوات وسياسة MCP ووصول تنفيذ الرمز من خلال المنح.

يبقى وضع PocketBase تكاملاً لمستخدم واحد في هذه الشجرة؛ يجب على بيئات النشر متعددة المستخدمين إبقاء `integrations.pocketbase_url` فارغاً واستخدام مخازن المصادقة والجلسات JSON/SQLite الافتراضية ما لم يُصمَّم مخزن مستخدم خارجي صراحةً لبيئة النشر.

---
## 🌐 المجتمع والنظام البيئي

يقوم DeepTutor على أكتاف مشاريع مفتوحة المصدر متميزة:

| المشروع | الدور في DeepTutor |
|:---|:---|
| [**nanobot**](https://github.com/HKUDS/nanobot) | محرك وكيل خفيف الوزن للغاية مكّن TutorBot الأصلي (يعمل الشركاء الآن على حلقة وكيل محادثة DeepTutor) |
| [**LlamaIndex**](https://github.com/run-llama/llama_index) | العمود الفقري لخط أنابيب RAG وفهرسة المستندات |
| [**ManimCat**](https://github.com/Wing900/ManimCat) | توليد رسوم متحركة رياضية مدفوع بالذكاء الاصطناعي لـ Math Animator |

**من النظام البيئي لـ HKUDS:**

| [⚡ LightRAG](https://github.com/HKUDS/LightRAG) | [🤖 AutoAgent](https://github.com/HKUDS/AutoAgent) | [🔬 AI-Researcher](https://github.com/HKUDS/AI-Researcher) | [🧬 nanobot](https://github.com/HKUDS/nanobot) |
|:---:|:---:|:---:|:---:|
| RAG بسيط وسريع | إطار وكيل بدون رمز | بحث آلي | وكيل ذكاء اصطناعي خفيف الوزن للغاية |


## 🤝 المساهمة

<div align="center">

نأمل أن يصبح DeepTutor هدية للمجتمع. 🎁

<a href="https://github.com/HKUDS/DeepTutor/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=HKUDS/DeepTutor&max=999" alt="المساهمون" />
</a>

</div>

راجع [CONTRIBUTING.md](../../CONTRIBUTING.md) للحصول على إرشادات حول إعداد بيئة التطوير ومعايير الرمز وسير عمل طلبات السحب.

## ⭐ تاريخ النجوم

<div align="center">

<a href="https://www.star-history.com/#HKUDS/DeepTutor&type=timeline&legend=top-left">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=HKUDS/DeepTutor&type=timeline&theme=dark&legend=top-left" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=HKUDS/DeepTutor&type=timeline&legend=top-left" />
    <img alt="مخطط تاريخ النجوم" src="https://api.star-history.com/svg?repos=HKUDS/DeepTutor&type=timeline&legend=top-left" />
  </picture>
</a>

</div>

<p align="center">
 <a href="https://www.star-history.com/hkuds/deeptutor">
  <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/badge?repo=HKUDS/DeepTutor&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/badge?repo=HKUDS/DeepTutor" />
   <img alt="ترتيب تاريخ النجوم" src="https://api.star-history.com/badge?repo=HKUDS/DeepTutor" />
  </picture>
 </a>
</p>

<div align="center">

**[مختبر ذكاء البيانات @ جامعة هونغ كونغ](https://github.com/HKUDS)**

[⭐ أعطنا نجمة](https://github.com/HKUDS/DeepTutor/stargazers) · [🐛 أبلغ عن خطأ](https://github.com/HKUDS/DeepTutor/issues) · [💬 النقاشات](https://github.com/HKUDS/DeepTutor/discussions)

---

مرخّص بموجب [رخصة Apache 2.0](../../LICENSE).

<p>
  <img src="https://visitor-badge.laobi.icu/badge?page_id=HKUDS.DeepTutor&style=for-the-badge&color=00d4ff" alt="المشاهدات">
</p>

</div>
