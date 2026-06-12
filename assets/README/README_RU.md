<div align="center">

<p align="center"><img src="../../assets/figs/logo/logo.png" alt="DeepTutor logo" height="56" style="vertical-align: middle;">&nbsp;<img src="../../assets/figs/logo/banner.png" alt="DeepTutor" height="48" style="vertical-align: middle;"></p>

# DeepTutor: Персонализированное Обучение на Базе Агентов

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
  <a href="README_RU.md"><img alt="Русский" height="40" src="https://img.shields.io/badge/Русский-BCDCF7"></a>&nbsp;
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

[![Discord](https://img.shields.io/badge/Discord-Сообщество-5865F2?style=flat-square&logo=discord&logoColor=white)](https://discord.gg/eRsjPgMU4t)
[![Feishu](https://img.shields.io/badge/Feishu-Группа-00D4AA?style=flat-square&logo=feishu&logoColor=white)](../../Communication.md)
[![WeChat](https://img.shields.io/badge/WeChat-Группа-07C160?style=flat-square&logo=wechat&logoColor=white)](https://github.com/HKUDS/DeepTutor/issues/78)

[Возможности](#-ключевые-возможности) · [Начало работы](#-начало-работы) · [Обзор](#-обзор-deeptutor) · [CLI](#%EF%B8%8F-cli-deeptutor--интерфейс-на-базе-агентов) · [Множественные пользователи](#-множественные-пользователи--совместные-развёртывания) · [Сообщество](#-сообщество--экосистема)

</div>

---

> 🤝 **Мы приветствуем любой вклад!** Голосуйте за пункты дорожной карты или предлагайте новые в [`Roadmap`](https://github.com/HKUDS/DeepTutor/issues/498), а также ознакомьтесь с нашим [Руководством по участию](../../CONTRIBUTING.md): стратегия ветвления, стандарты кода и как начать.

### 📦 Релизы

> **[2026.6.12]** [v1.4.3](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.3) — TutorBot превращается в **Partners** на производственном конвейере обмена сообщениями с потоковыми ответами в реальном времени и 15 каналами, Chat переходит на единый цикл агента, реальная изоляция каждого пользователя для многопользовательских развёртываний, Visualize перестроен с локальной валидацией и восстановлением, а также улучшения в Co-writer, файловом просмотрщике, облачном парсинге MinerU и CLI. Документация полностью обновлена на [deeptutor.info](https://deeptutor.info/).

> **[2026.5.28]** [v1.4.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.2) — Стабильность и полировка v1.4.1: разблокирован Gemini 2.5+ в Visualize и Chat, исправление маршрутизации аутентификации ContextVar (#485), усилен протокол меток рассуждений и нативных инструментов, плавный стриминг UX на всех поверхностях чата, новая сворачиваемая боковая панель «Недавние» и поддержка локального провайдера Lemonade.

> **[2026.5.27]** [v1.4.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.1) — Патч безопасности и стабильности: заблокирована песочница инструментов TutorBot, изоляция ресурсов на пользователя, мультимодальный откат изображений для провайдеров с поддержкой зрения, HTTP/SSE API для общения с TutorBot и исправление регрессии чата v1.4.0.

> **[2026.5.22]** [v1.4.0](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.0) — Выпуск GA v1.4: Auto Mode, трёхуровневая память, агентный Deep Research / Solve / Question, рефакторинг RAG на LlamaIndex, объединение Visualize/Animator, нормализация интенсивности рассуждений, откат схемы инструментов и устойчивое к перезапуску среда выполнения.

<details>
<summary><b>Прошлые релизы (более 2 недель назад)</b></summary>

> **[2026.5.21]** [v1.4.0-beta](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.0-beta) — Рабочее место с трёхуровневой памятью (L1/L2/L3), каждая возможность чата перестроена на едином агентном движке, RAG только на LlamaIndex и единая поверхность настроек и возможностей.

> **[2026.5.10]** [v1.3.10](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.10) — Восстановление CORS для удалённого Docker, `DISABLE_SSL_VERIFY` для SDK-провайдеров, более безопасные цитаты в блоках кода и необязательный надстройка Matrix E2EE.

> **[2026.5.9]** [v1.3.9](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.9) — Поддержка TutorBot Zulip и NVIDIA NIM, более безопасная маршрутизация моделей с рассуждениями, `deeptutor start`, подсказки в боковой панели и паритет хранилища сессий.

> **[2026.5.8]** [v1.3.8](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.8) — Необязательные многопользовательские развёртывания с изолированными рабочими пространствами пользователей, правами администратора, маршрутами аутентификации и ограниченным доступом к среде выполнения.

> **[2026.5.4]** [v1.3.7](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.7) — Исправления моделей/провайдеров с рассуждениями, видимая история индекса знаний и более безопасное редактирование шаблонов и очистка Co-Writer.

> **[2026.5.3]** [v1.3.6](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.6) — Выбор модели на основе каталога для чата и TutorBot, более безопасное повторное индексирование RAG, исправления лимита токенов OpenAI Responses и валидация редактора навыков.

> **[2026.5.2]** [v1.3.5](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.5) — Более плавные настройки локального запуска, более безопасные запросы RAG, более чистая аутентификация локальных эмбеддингов и полировка тёмного режима в настройках.

> **[2026.5.1]** [v1.3.4](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.4) — Сохранение и восстановление чата на страницах книги, ссылки из чата на книгу, более надёжная обработка языка/рассуждений, укрепление извлечения документов RAG.

> **[2026.4.30]** [v1.3.3](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.3) — Поддержка эмбеддингов NVIDIA NIM + Gemini, единый контекст Space для истории чата/навыков/памяти, снимки сессий, устойчивость повторного индексирования RAG.

> **[2026.4.29]** [v1.3.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.2) — Прозрачные URL-адреса конечных точек эмбеддингов, устойчивость повторного индексирования RAG к недействительным сохранённым векторам, очистка памяти для вывода моделей с рассуждениями, исправление среды выполнения Deep Solve.

> **[2026.4.28]** [v1.3.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.1) — Стабильность: более безопасная маршрутизация RAG и валидация эмбеддингов, сохранение данных в Docker, безопасный ввод IME, надёжность Windows/GBK.

> **[2026.4.27]** [v1.3.0](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.0) — Версионированные индексы базы знаний с процессом повторного индексирования, перестроенное рабочее пространство Knowledge, автообнаружение эмбеддингов с новыми адаптерами, центр Space.

> **[2026.4.25]** [v1.2.5](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.5) — Постоянные вложения в чате с боковой панелью предпросмотра файлов, конвейеры возможностей с учётом вложений, экспорт TutorBot в Markdown.

> **[2026.4.25]** [v1.2.4](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.4) — Вложения текст/код/SVG, одноразовый тур по настройке, экспорт чата в Markdown, компактный интерфейс управления базой знаний.

> **[2026.4.24]** [v1.2.3](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.3) — Вложения документов (PDF/DOCX/XLSX/PPTX), отображение блоков рассуждений, редактор шаблонов Soul, сохранение Co-Writer в блокнот.

> **[2026.4.22]** [v1.2.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.2) — Система навыков, созданных пользователем, переработка производительности ввода чата, автозапуск TutorBot, интерфейс библиотеки книг, полноэкранная визуализация.

> **[2026.4.21]** [v1.2.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.1) — Лимиты токенов на стадию, повторная генерация ответа во всех точках входа, исправления совместимости RAG и Gemma.

> **[2026.4.20]** [v1.2.0](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.0) — Компилятор «живых книг» Book Engine, многодокументный Co-Writer, интерактивные HTML-визуализации, упоминание банка вопросов через @.

> **[2026.4.18]** [v1.1.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.1.2) — Вкладка каналов на основе схемы, консолидация RAG в единый конвейер, вынесенные промпты чата.

> **[2026.4.17]** [v1.1.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.1.1) — Универсальный «Ответить сейчас», синхронизация прокрутки Co-Writer, единая панель настроек, кнопка остановки стриминга.

> **[2026.4.15]** [v1.1.0](https://github.com/HKUDS/DeepTutor/releases/tag/v1.1.0) — Переработка блочной математики LaTeX, диагностический зонд LLM, руководство по Docker и локальным LLM.

> **[2026.4.14]** [v1.1.0-beta](https://github.com/HKUDS/DeepTutor/releases/tag/v1.1.0-beta) — Сессии с закладками, тема Snow, сердцебиение WebSocket и автоматическое переподключение, переработка реестра эмбеддингов.

> **[2026.4.13]** [v1.0.3](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.3) — Блокнот вопросов с закладками и категориями, Mermaid в Visualize, обнаружение несоответствия эмбеддингов, совместимость с Qwen/vLLM, поддержка LM Studio и llama.cpp, и тема Glass.

> **[2026.4.11]** [v1.0.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.2) — Консолидация поиска с откатом на SearXNG, исправление переключения провайдера и исправления утечки ресурсов в frontend.

> **[2026.4.10]** [v1.0.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.1) — Возможность Visualize (Chart.js/SVG), предотвращение дублирования викторин и поддержка модели o4-mini.

> **[2026.4.10]** [v1.0.0-beta.4](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.0-beta.4) — Отслеживание прогресса эмбеддинга с повтором при ограничении скорости, кроссплатформенные исправления зависимостей и исправление валидации MIME.

> **[2026.4.8]** [v1.0.0-beta.3](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.0-beta.3) — Нативный SDK OpenAI/Anthropic (замена litellm), поддержка Math Animator для Windows, надёжный разбор JSON и полная i18n для китайского языка.

> **[2026.4.7]** [v1.0.0-beta.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.0-beta.2) — Горячая перезагрузка настроек, вложенный вывод MinerU, исправление WebSocket и минимальная версия Python 3.11+.

> **[2026.4.4]** [v1.0.0-beta.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.0-beta.1) — Переработка архитектуры на основе агентов (~200k строк): плагинная модель Tools + Capabilities, CLI и SDK, TutorBot, Co-Writer, Guided Learning и постоянная память.

> **[2026.1.23]** [v0.6.0](https://github.com/HKUDS/DeepTutor/releases/tag/v0.6.0) — Сохранение сессий, инкрементальная загрузка документов, гибкий импорт конвейера RAG и полная локализация на китайский.

> **[2026.1.18]** [v0.5.2](https://github.com/HKUDS/DeepTutor/releases/tag/v0.5.2) — Поддержка Docling для RAG-Anything, оптимизация системы логирования и исправления ошибок.

> **[2026.1.15]** [v0.5.0](https://github.com/HKUDS/DeepTutor/releases/tag/v0.5.0) — Единая конфигурация сервиса, выбор конвейера RAG для каждой базы знаний, переработка генерации вопросов и настройка боковой панели.

> **[2026.1.9]** [v0.4.0](https://github.com/HKUDS/DeepTutor/releases/tag/v0.4.0) — Поддержка нескольких провайдеров LLM и эмбеддингов, новая главная страница, разделение модуля RAG и рефакторинг переменных окружения.

> **[2026.1.5]** [v0.3.0](https://github.com/HKUDS/DeepTutor/releases/tag/v0.3.0) — Единая архитектура PromptManager, CI/CD с GitHub Actions и готовые Docker-образы на GHCR.

> **[2026.1.2]** [v0.2.0](https://github.com/HKUDS/DeepTutor/releases/tag/v0.2.0) — Развёртывание Docker, обновление до Next.js 16 и React 19, укрепление безопасности WebSocket и исправление критических уязвимостей.

</details>

### 📰 Новости

> **[2026.5.22]** 🌐 Наш официальный сайт документации запущен на [**deeptutor.info**](https://deeptutor.info/) — руководства, справочники и туры по возможностям в одном месте.

> **[2026.4.19]** 🎉 Мы достигли 20 тысяч звёзд за 111 дней! Спасибо за невероятную поддержку — мы продолжаем итерировать в направлении по-настоящему персонализированного интеллектуального обучения для каждого.

> **[2026.4.10]** 📄 Наша статья опубликована на arXiv! Прочитайте [препринт](https://arxiv.org/abs/2604.26962), чтобы узнать больше о дизайне и идеях DeepTutor.

> **[2026.4.4]** Давно не виделись! ✨ DeepTutor v1.0.0 наконец здесь — эволюция на основе агентов с полной переработкой архитектуры, TutorBot и гибким переключением режимов под лицензией Apache-2.0. Новая глава начинается, и наша история продолжается!

> **[2026.2.6]** 🚀 Мы достигли 10 тысяч звёзд всего за 39 дней! Огромная благодарность нашему невероятному сообществу за поддержку!

> **[2026.1.1]** С Новым годом! Присоединяйтесь к нашему [Discord](https://discord.gg/eRsjPgMU4t), [WeChat](https://github.com/HKUDS/DeepTutor/issues/78) или [Обсуждениям](https://github.com/HKUDS/DeepTutor/discussions) — вместе будем формировать будущее DeepTutor!

> **[2025.12.29]** DeepTutor официально выпущен!

## ✨ Ключевые возможности

DeepTutor построен вокруг среды выполнения на основе агентов: общий ChatOrchestrator направляет каждый ход к возможностям, ToolRegistry предоставляет одноразовые инструменты, когда они нужны модели, а CapabilityRegistry позволяет более глубоким рабочим процессам взять управление ходом, когда задача требует структуры.

<div align="center">
<img src="../../assets/figs/system/system%20architecture.png" alt="Системная архитектура DeepTutor" width="900">
</div>

**Единое учебное рабочее пространство**

- **Чат как основной цикл** — непринуждённое обучение, Q&A с опорой на источники, Deep Solve, Deep Question, Deep Research, Visualize и Auto Mode — всё это разделяет один контекст сессии и набор источников.
- **Учебные поверхности, которые остаются связанными** — черновики Co-Writer, страницы Book, базы знаний, ресурсы Space и Memory — это отдельные рабочие пространства, но все они питают единую агентную среду вместо того, чтобы становиться изолированными приложениями.
- **Partners для постоянного сопровождения** — компаньоны, подключённые к мессенджерам, теперь работают на том же цикле агента чата, что и основной продукт, со своим синтетическим рабочим пространством и назначенной библиотекой.

**Инструменты, память и управление**

- **Составные инструменты** — RAG, чтение источников, чтение/запись памяти, блокноты, загрузка URL, поиск на GitHub, паузы с вопросом к пользователю, выполнение в песочнице и необязательные инструменты мозгового штурма/веба/статей/рассуждений можно подключать в зависимости от контекста и настроек.
- **Трёхуровневая память** — трассировки L1, сводки L2 по поверхностям и синтез L3 между поверхностями делают персонализацию прозрачной, а не скрытой за чёрным ящиком.
- **Единые настройки и CLI** — каталоги моделей, эмбеддинги, поиск, сеть, серверы MCP, инструменты, возможности и настройки развёртывания редактируются из веб-интерфейса и доступны из скриптов через `deeptutor`.

---

## 🚀 Начало работы

DeepTutor предлагает четыре способа установки. Все они используют одну структуру рабочего пространства: настройки хранятся в `data/user/settings/` в каталоге, из которого вы запускаете приложение (или в `DEEPTUTOR_HOME` / `deeptutor start --home`, если вы задали его явно). Для полноценного приложения рекомендуемый процесс: **выбрать каталог рабочего пространства → установить → `deeptutor init` → `deeptutor start`**.

> ✨ **v1.4.3 доступна.** `pip install -U deeptutor` устанавливает последнюю стабильную версию. Предрелизные версии (если доступны) устанавливаются с `pip install --pre -U deeptutor`.

### Вариант 1 — Установка из PyPI

Полное локальное веб-приложение + CLI без необходимости клонирования. Требует **Python 3.11+** и **Node.js 20+** в PATH (автономный сервер Next.js запускается командой `deeptutor start`).

```bash
mkdir -p my-deeptutor && cd my-deeptutor
pip install -U deeptutor
deeptutor init     # запрашивает порты + провайдер LLM + необязательный эмбеддинг
deeptutor start    # запускает backend + frontend; держите терминал открытым
```

`deeptutor init` запрашивает порт backend (по умолчанию `8001`), порт frontend (по умолчанию `3782`), провайдер LLM / базовый URL / API-ключ / модель и необязательный провайдер эмбеддингов для базы знаний / RAG.

После `deeptutor start` откройте URL frontend, выведенный в терминале — по умолчанию [http://127.0.0.1:3782](http://127.0.0.1:3782). Нажмите `Ctrl+C` в этом терминале, чтобы остановить backend и frontend. Пропуск `deeptutor init` допустим для быстрого пробного запуска; приложение загрузится с портами по умолчанию и пустыми настройками модели, которые можно настроить позже в **Настройки → Модели**.

### Вариант 2 — Установка из исходного кода

Для разработки на основе клонированного репозитория. Используйте **Python 3.11+** и **Node.js 22 LTS** для соответствия CI и Docker.

```bash
git clone https://github.com/HKUDS/DeepTutor.git
cd DeepTutor

# Создайте venv (macOS/Linux). Windows PowerShell:
#   py -3.11 -m venv .venv ; .\.venv\Scripts\Activate.ps1
python3 -m venv .venv && source .venv/bin/activate
python -m pip install --upgrade pip

# Установите зависимости backend + frontend
python -m pip install -e .
( cd web && npm ci --legacy-peer-deps )

deeptutor init
deeptutor start
```

При установке из исходного кода Next.js запускается в режиме разработки из локального каталога `web/`; всё остальное (структура конфигурации, порты, остановка через `Ctrl+C`) совпадает с Вариантом 1.

<details>
<summary><b>Окружение Conda</b> (вместо <code>venv</code>)</summary>

```bash
conda create -n deeptutor python=3.11
conda activate deeptutor
python -m pip install --upgrade pip
```

</details>

<details>
<summary><b>Необязательные дополнения к установке</b> — dev / partners / matrix / math-animator</summary>

```bash
pip install -e ".[dev]"             # инструменты тестирования/линтинга
pip install -e ".[partners]"        # SDK каналов IM для Partners + клиент MCP
pip install -e ".[matrix]"          # канал Matrix без E2EE/libolm
pip install -e ".[matrix-e2e]"      # Matrix E2EE; требует libolm
pip install -e ".[math-animator]"   # надстройка Manim; требует LaTeX/ffmpeg/системных библиотек
```

</details>

<details>
<summary><b>Настройки зависимостей frontend и устранение неполадок dev-сервера</b></summary>

**Изменение зависимостей frontend:** выполните `npm install --legacy-peer-deps`, чтобы обновить `web/package-lock.json`, затем зафиксируйте `web/package.json` и `web/package-lock.json`.

**Зависший dev-сервер:** если `deeptutor start` сообщает о существующем frontend, который не отвечает, остановите PID, который он выводит. Если реально ни один процесс Next.js не запущен, файлы блокировки устарели — удалите их и повторите попытку:

```bash
rm -f web/.next/dev/lock web/.next/lock
deeptutor start
```

</details>

### Вариант 3 — Docker

Один контейнер для полного веб-приложения. Образы в GitHub Container Registry:

- `ghcr.io/hkuds/deeptutor:latest` — стабильный релиз
- `ghcr.io/hkuds/deeptutor:pre` — предрелизная версия, когда доступна

```bash
docker run --rm --name deeptutor \
  -p 127.0.0.1:3782:3782 \
  -p 127.0.0.1:8001:8001 \
  -v deeptutor-data:/app/data \
  ghcr.io/hkuds/deeptutor:latest
```

> ⚠️ **Пробросьте оба порта `3782` и `8001`.** `3782` обслуживает веб-интерфейс; `8001` — это backend FastAPI, к которому обращается ваш браузер напрямую — нет внутриконтейнерного прокси. Пропустите проброс `8001` — страница загрузится, но **Настройки** покажут «Backend недоступен» и останутся неработоспособными.

Откройте [http://127.0.0.1:3782](http://127.0.0.1:3782). Контейнер создаёт `/app/data/user/settings/*.json` при первом запуске; настройте провайдеров моделей на странице веб-настроек. Конфигурация, API-ключи, логи, файлы рабочего пространства, память и базы знаний сохраняются в томе `deeptutor-data`.

- **Другие порты хоста:** измените левую часть каждого маппинга `-p хост:контейнер` (например, `-p 127.0.0.1:8088:3782`). Если вы измените порты на стороне контейнера в `/app/data/user/settings/system.json`, перезапустите и обновите правую часть каждого маппинга соответственно.
- **Фоновый режим:** добавьте `-d`, затем `docker logs -f deeptutor` для просмотра логов, `docker stop deeptutor` для остановки, `docker rm deeptutor` перед повторным использованием имени. Том `deeptutor-data` сохраняет ваши настройки и рабочее пространство между перезапусками.

**Удалённый Docker / обратный прокси:** веб-интерфейс работает в браузере, поэтому браузеру нужен доступный URL backend. Для удалённых серверов откройте **Настройки → Сеть** или отредактируйте `data/user/settings/system.json`:

```json
{
  "next_public_api_base_external": "https://deeptutor.example.com"
}
```

`public_api_base` принимается как псевдоним совместимости и нормализуется в `next_public_api_base_external` при сохранении. CORS использует **origins** frontend, а не URL API. При отключённой аутентификации DeepTutor по умолчанию допускает обычные HTTP/HTTPS origins браузера. При включённой аутентификации добавьте точные origins frontend:

```json
{
  "cors_origins": ["https://deeptutor.example.com"]
}
```

<details>
<summary><b>Подключение к Ollama / LM Studio / llama.cpp / vLLM / Lemonade на хосте</b></summary>

Внутри Docker `localhost` — это сам контейнер, а не ваша хост-машина. Чтобы обратиться к сервису модели, запущенному на хосте, используйте шлюз хоста (рекомендуется):

```bash
docker run --rm --name deeptutor \
  -p 127.0.0.1:3782:3782 -p 127.0.0.1:8001:8001 \
  --add-host=host.docker.internal:host-gateway \
  -v deeptutor-data:/app/data \
  ghcr.io/hkuds/deeptutor:latest
```

Затем в **Настройки → Модели** укажите базовый URL провайдера на `host.docker.internal`:

- Ollama LLM: `http://host.docker.internal:11434/v1`
- Ollama embedding: `http://host.docker.internal:11434/api/embed`
- LM Studio: `http://host.docker.internal:1234/v1`
- llama.cpp: `http://host.docker.internal:8080/v1`
- Lemonade: `http://host.docker.internal:13305/api/v1`

Docker Desktop (macOS/Windows) обычно разрешает `host.docker.internal` без `--add-host`. На Linux этот флаг — переносимый способ создать такое имя хоста в современных версиях Docker Engine.

**Альтернатива для Linux — хостовая сеть:** добавьте `--network=host` и уберите флаги `-p`. Контейнер напрямую использует сеть хоста, поэтому откройте [http://127.0.0.1:3782](http://127.0.0.1:3782) (или `frontend_port` в `system.json`), и сервисы хоста доступны через обычные localhost URL вида `http://127.0.0.1:11434/v1`. Обратите внимание, что хостовая сеть открывает порты контейнера непосредственно на хосте и может конфликтовать с существующими сервисами.

</details>

### Песочница для выполнения кода (офисные навыки)

Встроенные офисные навыки — **docx / pdf / pptx / xlsx** — работают так: модель пишет короткий Python-скрипт (`python-docx`, `reportlab`, `openpyxl`, …), запускает его через инструменты `exec` / `code_execution` и возвращает URL для скачивания. Эти инструменты подключаются при наличии активного backend песочницы, что по умолчанию верно для каждого варианта развёртывания:

- **Локально (Вариант 1 / 2) и Docker (Вариант 3, единственный контейнер):** ограниченная sandbox-подпроцесс запускает код модели (локально на хосте, или внутри контейнера под Docker — контейнер сам является границей изоляции).
- **docker-compose:** вместо этого перенаправляется в защищённый, минимально-привилегированный **контейнер-исполнитель** (`Dockerfile.runner`) через `DEEPTUTOR_SANDBOX_RUNNER_URL` — наиболее строгая настройка, автоматически применяемая при его наличии.

Sandbox-подпроцесс управляется настройкой `sandbox_allow_subprocess` в `data/user/settings/system.json` (по умолчанию `true`). Запуск кода, сгенерированного моделью, на вашем хосте — это реальное решение о доверии — установите `false` (или экспортируйте `DEEPTUTOR_SANDBOX_ALLOW_SUBPROCESS=0`), чтобы отключить выполнение на стороне хоста, ценой того, что офисные навыки больше не смогут создавать файлы.

### Вариант 4 — Только CLI

Когда веб-интерфейс не нужен. Пакет только для CLI устанавливается из клонированного репозитория, а не из PyPI.

```bash
git clone https://github.com/HKUDS/DeepTutor.git
cd DeepTutor

# Создайте venv (macOS/Linux). Windows PowerShell:
#   py -3.11 -m venv .venv-cli ; .\.venv-cli\Scripts\Activate.ps1
python3 -m venv .venv-cli && source .venv-cli/bin/activate
python -m pip install --upgrade pip

python -m pip install -e ./packaging/deeptutor-cli
deeptutor init --cli
deeptutor chat
```

`deeptutor init --cli` использует ту же структуру `data/user/settings/`, что и полноценное приложение, но пропускает запросы порта backend/frontend и по умолчанию отключает эмбеддинги (выберите `Yes`, если планируете использовать `deeptutor kb …` или инструменты RAG). Тем не менее он записывает полную структуру среды выполнения (`system.json`, `auth.json`, `integrations.json`, `model_catalog.json`, `main.yaml`, `agents.yaml`) и по-прежнему запрашивает активного провайдера LLM и модель.

<details>
<summary><b>Основные команды</b></summary>

```bash
deeptutor chat                                          # интерактивный REPL
deeptutor chat --capability deep_solve --tool rag --kb my-kb
deeptutor run chat "Объясни преобразование Фурье"
deeptutor run deep_solve "Реши x^2 = 4" --tool rag --kb my-kb
deeptutor kb create my-kb --doc textbook.pdf
deeptutor memory show
deeptutor config show
```

</details>

Локальная установка `deeptutor-cli` не содержит веб-ресурсов и серверных зависимостей. Сохраните клонированный репозиторий — редактируемая установка указывает на него. Чтобы позже добавить веб-приложение, установите пакет из PyPI (Вариант 1) и запустите `deeptutor init` + `deeptutor start` из того же рабочего пространства.

### Справочник по конфигурации

<details>
<summary><b>Файлы конфигурации в <code>data/user/settings/</code></b> — справочник JSON/YAML</summary>

Всё в `data/user/settings/` — это обычный JSON/YAML. Страница **Настройки** в браузере является рекомендуемым редактором.

| Файл | Назначение |
|:---|:---|
| `model_catalog.json` | Профили провайдеров LLM, эмбеддингов и поиска; API-ключи; активные модели |
| `system.json` | Порты backend/frontend, внешний базовый URL API, CORS, проверка SSL, каталог вложений |
| `auth.json` | Необязательное переключение аутентификации, имя пользователя, хэш пароля, настройки токена/cookie |
| `integrations.json` | Необязательные настройки интеграции PocketBase и sidecar |
| `interface.json` | Язык UI / тема / предпочтения боковой панели |
| `main.yaml` | Настройки среды выполнения по умолчанию и инъекция путей |
| `agents.yaml` | Настройки температуры и токенов для возможностей/инструментов |

Файлы `.env` в корне проекта **не** читаются как файлы конфигурации приложения. Для минимальной настройки модели откройте **Настройки → Модели**, добавьте профиль LLM (Базовый URL / API-ключ / имя модели) и сохраните. Профиль эмбеддинга нужен только при использовании функций базы знаний / RAG.

</details>

## 📖 Обзор DeepTutor

Тур по README следует поверхностям продукта в том порядке, в котором вы наиболее часто с ними встречаетесь: Чат, Partner, Co-Writer, Book, Knowledge, Space, Memory и Настройки. Скриншоты ниже взяты из реорганизованного дерева `assets/figs`; устаревшие архивные изображения здесь намеренно не используются.

### 💬 Чат — Цикл агента, которым вы реально пользуетесь

<div align="center">
<img src="../../assets/figs/webui/chat.png" alt="Рабочее пространство чата DeepTutor" width="900">
</div>

Чат — это возможность по умолчанию и место, где начинается большинство работы. Один поток может общаться обычно, вызывать инструменты, опираться на выбранные базы знаний, читать вложения, записывать в блокнот и продолжать с тем же набором источников между ходами.

<div align="center">
<img src="../../assets/figs/system/chat-agent-loop.png" alt="Цикл агента чата DeepTutor" width="900">
</div>

Текущий цикл намеренно прост: модель думает раундами, вызывает инструменты когда нужно, наблюдает результаты инструментов и заканчивает, когда у неё достаточно доказательств. Инструменты, переключаемые пользователем: `brainstorm`, `web_search`, `paper_search` и `reason`; контекстные инструменты такие как `rag`, `read_source`, `read_memory`, `write_memory`, `read_skill`, `load_tools`, `exec`, `web_fetch`, `ask_user`, `list_notebook`, `write_note` и `github` подключаются, когда ход имеет правильный контекст.

Чат также является отправной точкой для более глубоких возможностей: `deep_solve` для проработанных рассуждений, `deep_question` для генерации вопросов, `deep_research` для цитируемых отчётов, `visualize` и `math_animator` для визуальных выходных данных, `auto` для маршрутизации и `mastery_path` для процессов планирования обучения.

### 🤝 Partner — Постоянные компаньоны на той же платформе

<div align="center">
<img src="../../assets/figs/webui/partners.png" alt="Рабочее пространство Partners DeepTutor" width="900">
</div>

Partners заменяют старый движок TutorBot более чистой моделью: каждое входящее веб- или IM-сообщение становится обычным ходом ChatOrchestrator внутри рабочего пространства, привязанного к конкретному партнёру. Нет отдельного «мозга бота», который нужно синхронизировать.

<div align="center">
<img src="../../assets/figs/system/partners-architecture.png" alt="Архитектура Partners DeepTutor" width="900">
</div>

Каждый партнёр имеет `SOUL.md`, выбор модели, каналы, политику инструментов и назначенную библиотеку. Базы знаний, навыки и блокноты копируются в `data/partners/<id>/workspace/`, поэтому те же инструменты RAG, навыков, блокнота и памяти работают без специальных случаев.

<div align="center">
<img src="../../assets/figs/webui/partners02.png" alt="Подробный вид партнёра DeepTutor" width="900">
</div>

Слой каналов управляется схемой и может подключаться к платформам обмена сообщениями таким как Feishu, Telegram, Slack, DingTalk, QQ/Napcat, WeCom, WhatsApp, Zulip, Matrix и Microsoft Teams в зависимости от установленных дополнений и настроенных учётных данных.

### ✍️ Co-Writer — Составление Markdown с учётом выделения

Co-Writer — это рабочее пространство Markdown с разделённым видом для отчётов, руководств, заметок и длинных учебных материалов. Документы автосохраняются, отображают живой предпросмотр и могут быть сохранены обратно в блокноты, когда черновик становится многоразовым контекстом.

Выделите текст и попросите DeepTutor переписать, расширить или сократить его. Агент редактирования ведёт трассировку вызовов инструментов и может основывать правку на базе знаний или веб-доказательствах, поэтому Co-Writer ведёт себя скорее как редактор с поиском, чем как отдельное текстовое поле.

### 📖 Book — Живые книги из ваших материалов

<p align="center">
<img src="../../assets/figs/webui/book01.png" alt="Вид чтения книги DeepTutor" width="31%">
&nbsp;
<img src="../../assets/figs/webui/book02.png" alt="Вид интерактивного блока книги DeepTutor" width="31%">
&nbsp;
<img src="../../assets/figs/webui/book03.png" alt="Вид создания книги DeepTutor" width="31%">
</p>

Book превращает выбранные источники в интерактивный учебный материал. Книга может начинаться из баз знаний, блокнотов, банков вопросов или истории чата; процесс создания предлагает структуру до того, как генерируется содержание, так что пользователи могут проверить форму вместо того, чтобы принимать слепой одноразовый вывод.

BookEngine компилирует страницы в типизированные блоки: текст, разделы, выноски, викторины, карточки, временные шкалы, код, рисунки, интерактивный HTML, анимации, графы понятий, глубокие погружения и заметки пользователя. Команды обслуживания такие как `deeptutor book health` и `deeptutor book refresh-fingerprints` помогают обнаружить, когда исходные знания разошлись с скомпилированными страницами.

### 📚 Knowledge — Версионированные библиотеки RAG

<div align="center">
<img src="../../assets/figs/webui/knowledge.png" alt="Рабочее пространство базы знаний DeepTutor" width="900">
</div>

Базы знаний — это коллекции документов, стоящие за RAG. Текущий стек использует только LlamaIndex с плоской структурой хранения `version-N`, ключём которой является сигнатура эмбеддинга. Повторное индексирование сохраняет предыдущие версии и не перезаписывает рабочий индекс, пока обрабатываются новые документы.

Веб-рабочее пространство предоставляет доступ к файлам, загрузке, версиям индекса и настройкам. CLI отражает тот же жизненный цикл с `deeptutor kb list`, `info`, `create`, `add`, `search`, `set-default` и `delete`.

### 🌐 Space — Навыки, персоны и многоразовый контекст

<div align="center">
<img src="../../assets/figs/webui/space.png" alt="Рабочее пространство Space DeepTutor" width="900">
</div>

Space — это библиотечный слой для многоразового контекста. Он объединяет авторские навыки пользователей, персоны, блокноты, историю чата и ресурсы в стиле банка вопросов, чтобы агентом можно было управлять с помощью преднамеренного контекста вместо специальных промптов.

Навыки хранятся как файлы `SKILL.md` в рабочем пространстве пользователя и могут быть помечены, отредактированы или оставлены только для чтения, если они встроены. Персоны следуют той же идее для роли и голоса. Эти ресурсы могут быть назначены партнёрам, упомянуты в чате и повторно использованы в учебных рабочих процессах.

### 🧠 Memory — Прозрачная персонализация

<div align="center">
<img src="../../assets/figs/webui/memory01.png" alt="Рабочее место памяти DeepTutor" width="900">
</div>

Memory — трёхуровневая система, корнем которой является активное рабочее пространство пользователя: `trace/<surface>/<date>.jsonl` для трассировок событий L1, `L2/<surface>.md` для фактов по поверхностям и `L3/<recent|profile|scope|preferences>.md` для синтеза между поверхностями.

<div align="center">
<img src="../../assets/figs/webui/memory02.png" alt="Граф памяти DeepTutor" width="900">
</div>

Поддерживаемые поверхности памяти: `chat`, `notebook`, `quiz`, `kb`, `book`, `tutorbot` и `cowriter`. Устаревшее имя поверхности `tutorbot` остаётся в слое памяти для совместимости, хотя обращённая к продукту модель компаньона теперь — Partners. Рабочее место позволяет просматривать, редактировать, запускать консолидацию и использовать граф для отслеживания синтезированных утверждений до поддерживающих их фактов и необработанных событий.

### ⚙️ Настройки — Единая плоскость управления

<div align="center">
<img src="../../assets/figs/webui/settings.png" alt="Рабочее пространство настроек DeepTutor" width="900">
</div>

Настройки — это операционная плоскость управления. Она охватывает внешний вид, сетевые порты и внешний базовый URL API, каталоги LLM и эмбеддингов, провайдеры поиска, парсинг MinerU, бюджеты возможностей, периодичность памяти, серверы MCP, встроенные инструменты и список включённых необязательных инструментов.

Большинство настроек используют процесс «черновик и применение», чтобы пользователи могли тестировать провайдеров перед их сохранением. Файлы `.env` в корне проекта намеренно игнорируются; конфигурация среды выполнения хранится в `data/user/settings/*.json`, если `DEEPTUTOR_HOME` или `deeptutor start --home` не указывает приложению другое место.

---

## ⌨️ CLI DeepTutor — Интерфейс на базе агентов

DeepTutor ориентирован на CLI: та же точка входа `deeptutor` может инициализировать рабочее пространство, запустить веб-приложение, выполнить одноразовую возможность, открыть интерактивный REPL, управлять базами знаний, проверять сессии, обслуживать книги и управлять партнёрами.

```bash
deeptutor run chat "Объясни преобразование Фурье" --tool rag --kb textbook
deeptutor run deep_solve "Реши x^2 = 4" --tool reason
deeptutor chat --capability deep_research --kb papers
deeptutor partner create math-tutor --soul "Сократовский репетитор по математике"
deeptutor kb create calculus --doc textbook.pdf
```

<details>
<summary><b>Справочник команд</b></summary>

| Команда | Описание |
|:---|:---|
| `deeptutor init` | Создать или обновить `data/user/settings` для текущего рабочего пространства |
| `deeptutor start [--home PATH]` | Запустить backend + frontend вместе |
| `deeptutor serve [--port PORT]` | Запустить только backend FastAPI |
| `deeptutor run <capability> <message>` | Выполнить один ход возможности (`chat`, `deep_solve`, `deep_question`, `deep_research`, `visualize`, `math_animator`, `auto`, `mastery_path`) |
| `deeptutor chat` | Интерактивный REPL с управлением возможностями, инструментами, базой знаний, блокнотом и историей |
| `deeptutor partner list/create/start/stop` | Управление партнёрами, подключёнными к мессенджерам |
| `deeptutor kb list/info/create/add/search/set-default/delete` | Управление базами знаний LlamaIndex |
| `deeptutor memory show/clear` | Просмотр документов памяти L2/L3 или очистка памяти L1/всей памяти |
| `deeptutor session list/show/open/rename/delete` | Управление общими сессиями |
| `deeptutor notebook list/create/show/add-md/replace-md/remove-record` | Управление блокнотами из файлов Markdown |
| `deeptutor book list/health/refresh-fingerprints` | Просмотр книг и обновление отпечатков источников |
| `deeptutor plugin list/info` | Просмотр зарегистрированных инструментов и возможностей |
| `deeptutor config show` | Вывод сводки конфигурации |
| `deeptutor provider login <provider>` | Управление OAuth-входом провайдера там, где поддерживается |

</details>

Дистрибутив только для CLI находится в `packaging/deeptutor-cli`; в этом репозитории его следует устанавливать из исходного кода с помощью `python -m pip install -e ./packaging/deeptutor-cli`. Публичный пакет `deeptutor-cli` в настоящее время недоступен на PyPI, поэтому в главном разделе начала работы используется путь установки из исходного кода.

---

## 👥 Множественные пользователи — Совместные развёртывания

<div align="center">
<img src="../../assets/figs/webui/multi-user.png" alt="Рабочее пространство администратора для множественных пользователей DeepTutor" width="900">
</div>

Аутентификация необязательна и отключена по умолчанию. При включении DeepTutor становится совместным развёртыванием с одним рабочим пространством администратора, рабочими пространствами каждого пользователя, рабочими пространствами партнёров и системным состоянием под одним деревом `data/`.

```text
data/
├── user/                         # Рабочее пространство и настройки администратора
├── users/<uid>/                  # Область пользователя без прав администратора
│   ├── user/chat_history.db
│   ├── user/settings/interface.json
│   ├── user/workspace/{chat,co-writer,book,memory,notebook,...}
│   └── knowledge_bases/...
├── partners/<id>/workspace/      # Область синтетического пользователя партнёра
└── system/
    ├── auth/users.json
    ├── grants/<uid>.json
    └── audit/usage.jsonl
```

Первый зарегистрированный пользователь становится администратором и может настраивать каталоги моделей, учётные данные провайдеров, базы знаний, навыки и права пользователей. Пользователи без прав администратора получают изолированную историю чата, память, блокноты, личные базы знаний и скрытую страницу настроек; ресурсы, назначенные администратором, отображаются как ограниченные опции только для чтения, не раскрывая API-ключи или внутренние настройки провайдеров.

Для локального тестирования установите `data/user/settings/auth.json`, чтобы включить аутентификацию, перезапустите `deeptutor start`, зарегистрируйте первого администратора на `/register`, затем создайте пользователей из `/admin/users` и назначьте модели, базы знаний, навыки, политику инструментов, политику MCP и доступ к выполнению кода через права.

Режим PocketBase остаётся однопользовательской интеграцией в этом дереве; многопользовательские развёртывания должны оставить `integrations.pocketbase_url` пустым и использовать хранилища аутентификации и сессий по умолчанию JSON/SQLite, если только внешнее хранилище пользователей не было явно спроектировано для данного развёртывания.

---
## 🌐 Сообщество и экосистема

DeepTutor стоит на плечах выдающихся проектов с открытым исходным кодом:

| Проект | Роль в DeepTutor |
|:---|:---|
| [**nanobot**](https://github.com/HKUDS/nanobot) | Сверхлёгкий движок агентов, питавший оригинальный TutorBot (Partners теперь работают на цикле агента чата DeepTutor) |
| [**LlamaIndex**](https://github.com/run-llama/llama_index) | Основа конвейера RAG и индексирования документов |
| [**ManimCat**](https://github.com/Wing900/ManimCat) | Генерация математических анимаций на основе AI для Math Animator |

**Из экосистемы HKUDS:**

| [⚡ LightRAG](https://github.com/HKUDS/LightRAG) | [🤖 AutoAgent](https://github.com/HKUDS/AutoAgent) | [🔬 AI-Researcher](https://github.com/HKUDS/AI-Researcher) | [🧬 nanobot](https://github.com/HKUDS/nanobot) |
|:---:|:---:|:---:|:---:|
| Простой и быстрый RAG | Фреймворк агентов без кода | Автоматизированные исследования | Сверхлёгкий AI-агент |


## 🤝 Участие в разработке

<div align="center">

Мы надеемся, что DeepTutor станет подарком для сообщества. 🎁

<a href="https://github.com/HKUDS/DeepTutor/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=HKUDS/DeepTutor&max=999" alt="Участники" />
</a>

</div>

Смотрите [CONTRIBUTING.md](../../CONTRIBUTING.md) для руководства по настройке среды разработки, стандартам кода и процессу pull request.

## ⭐ История звёзд

<div align="center">

<a href="https://www.star-history.com/#HKUDS/DeepTutor&type=timeline&legend=top-left">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=HKUDS/DeepTutor&type=timeline&theme=dark&legend=top-left" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=HKUDS/DeepTutor&type=timeline&legend=top-left" />
    <img alt="График истории звёзд" src="https://api.star-history.com/svg?repos=HKUDS/DeepTutor&type=timeline&legend=top-left" />
  </picture>
</a>

</div>

<p align="center">
 <a href="https://www.star-history.com/hkuds/deeptutor">
  <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/badge?repo=HKUDS/DeepTutor&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/badge?repo=HKUDS/DeepTutor" />
   <img alt="Рейтинг истории звёзд" src="https://api.star-history.com/badge?repo=HKUDS/DeepTutor" />
  </picture>
 </a>
</p>

<div align="center">

**[Лаборатория анализа данных @ HKU](https://github.com/HKUDS)**

[⭐ Поставьте звезду](https://github.com/HKUDS/DeepTutor/stargazers) · [🐛 Сообщить об ошибке](https://github.com/HKUDS/DeepTutor/issues) · [💬 Обсуждения](https://github.com/HKUDS/DeepTutor/discussions)

---

Лицензировано под [Apache License 2.0](../../LICENSE).

<p>
  <img src="https://visitor-badge.laobi.icu/badge?page_id=HKUDS.DeepTutor&style=for-the-badge&color=00d4ff" alt="Просмотры">
</p>

</div>
