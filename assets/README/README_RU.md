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
[![License](https://img.shields.io/badge/License-Apache_2.0-blue?style=flat-square)](LICENSE)
[![GitHub release](https://img.shields.io/github/v/release/HKUDS/DeepTutor?style=flat-square&color=brightgreen)](https://github.com/HKUDS/DeepTutor/releases)
[![arXiv](https://img.shields.io/badge/arXiv-2604.26962-b31b1b?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2604.26962)

[![Discord](https://img.shields.io/badge/Discord-Сообщество-5865F2?style=flat-square&logo=discord&logoColor=white)](https://discord.gg/eRsjPgMU4t)
[![Feishu](https://img.shields.io/badge/Feishu-Группа-00D4AA?style=flat-square&logo=feishu&logoColor=white)](./Communication.md)
[![WeChat](https://img.shields.io/badge/WeChat-Группа-07C160?style=flat-square&logo=wechat&logoColor=white)](https://github.com/HKUDS/DeepTutor/issues/78)

[Возможности](#-ключевые-возможности) · [Начать](#-начало-работы) · [Исследовать](#-обзор-deeptutor) · [CLI](#%EF%B8%8F-deeptutor-cli--интерфейс-для-агентов) · [Экосистема](#-экосистема--eduhub-и-сообщество-навыков) · [Сообщество](#-сообщество)

</div>

---

> 🤝 **Мы приветствуем любые вклады в проект!** Голосуйте за элементы дорожной карты или предлагайте новые на странице [`Roadmap`](https://github.com/HKUDS/DeepTutor/issues/498), а также изучите наше [Руководство по участию](CONTRIBUTING.md) с описанием стратегии ветвления, стандартов кодирования и инструкций по началу работы.

### 📦 Релизы

> **[2026.6.17]** [v1.4.6](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.6) — Пространство становится обучающим дашбордом с импортируемыми **Моими Агентами** и памятью верхнего уровня; **Центр Знаний** получает движки GraphRAG / PageIndex / LightRAG, связанные KB и монтирование Obsidian; Настройки открывают парсинг документов / голос / генерацию изображений и видео; возможности LLM ограничиваются назначенной моделью.

> **[2026.6.14]** [v1.4.5](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.5) — Направляемое обучение перестроено на цикле агентного чата с жёсткими воротами освоения по типу и панелью `/learning`; новый расширяемый фреймворк loop-plugin; Markdown-экспорт и сохранение в блокнот для разговоров с Партнёрами.

> **[2026.6.13]** [v1.4.4](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.4) — Установка навыков сообщества из [ClawHub](https://clawhub.ai/) командой `deeptutor skill install` через шлюз безопасности; настоящий DOCX/XLSX предпросмотр в браузере для файлов базы знаний.

<details>
<summary><b>Прошлые релизы (более двух недель назад)</b></summary>

> **[2026.6.12]** [v1.4.3](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.3) — TutorBot становится **Партнёрами** на продакшен-IM-конвейере (15 каналов, потоковая передача); чат переходит на единый цикл агента; настоящая изоляция пользователей; обновлённый Visualize.

> **[2026.5.28]** [v1.4.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.2) — Стабильность и полировка: разблокирован Gemini 2.5+ для Visualize и Chat, исправлена маршрутизация аутентификации (#485), плавная потоковая передача чата, боковая панель «Недавние» и поддержка локального провайдера Lemonade.

> **[2026.5.27]** [v1.4.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.1) — Безопасность и стабильность: заблокирована песочница инструментов TutorBot, изоляция ресурсов на пользователя, мультимодальный запасной вариант для изображений, HTTP/SSE API для TutorBots и исправление регрессии чата v1.4.0.

> **[2026.5.22]** [v1.4.0](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.0) — Стабильный выпуск v1.4: Авто-режим, трёхуровневая Память, агентные Deep Research / Solve / Question, рефакторинг LlamaIndex RAG, объединение Visualize/Animator и устойчивый к перезапуску цикл выполнения.

> **[2026.5.21]** [v1.4.0-beta](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.0-beta) — Рабочее место трёхуровневой памяти (L1/L2/L3), все возможности чата перестроены на едином агентном движке, только LlamaIndex RAG, унифицированный интерфейс Настроек и Возможностей.

> **[2026.5.10]** [v1.3.10](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.10) — Восстановление CORS для удалённого Docker, `DISABLE_SSL_VERIFY` для провайдеров SDK, более безопасные ссылки в блоках кода и необязательное дополнение Matrix E2EE.

> **[2026.5.9]** [v1.3.9](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.9) — Поддержка TutorBot Zulip и NVIDIA NIM, более безопасная маршрутизация моделей-мыслителей, `deeptutor start`, подсказки боковой панели и паритет хранилища сессий.

> **[2026.5.8]** [v1.3.8](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.8) — Необязательные многопользовательские развёртывания с изолированными рабочими пространствами, грантами администратора, маршрутами аутентификации и ограниченным доступом к среде выполнения.

> **[2026.5.4]** [v1.3.7](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.7) — Исправления моделей-мыслителей/провайдеров, видимая история индексации базы знаний и более безопасное редактирование шаблонов Co-Writer.

> **[2026.5.3]** [v1.3.6](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.6) — Выбор модели на основе каталога для чата и TutorBot, более безопасное переиндексирование RAG, исправления лимита токенов OpenAI Responses и валидация редактора навыков.

> **[2026.5.2]** [v1.3.5](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.5) — Более плавные настройки локального запуска, более безопасные запросы RAG, чистая аутентификация локального встраивания и полировка тёмного режима в Настройках.

> **[2026.5.1]** [v1.3.4](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.4) — Сохранение чата на странице книги и потоки восстановления, ссылки чат→книга, более надёжная обработка языка и рассуждений, укрепление извлечения документов RAG.

> **[2026.4.30]** [v1.3.3](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.3) — Поддержка встраивания NVIDIA NIM + Gemini, унифицированный контекст Пространства для истории чата/навыков/памяти, снимки сессий, устойчивость переиндексирования RAG.

> **[2026.4.29]** [v1.3.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.2) — Прозрачные URL конечных точек встраивания, устойчивость переиндексирования RAG для недействительных персистентных векторов, очистка памяти для вывода моделей-мыслителей, исправление среды выполнения Deep Solve.

> **[2026.4.28]** [v1.3.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.1) — Стабильность: более безопасная маршрутизация RAG и валидация встраивания, сохранение Docker, безопасный ввод IME, надёжность на Windows/GBK.

> **[2026.4.27]** [v1.3.0](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.0) — Версионированные индексы KB с рабочим процессом переиндексирования, обновлённое рабочее пространство Знаний, автообнаружение встраивания с новыми адаптерами, хаб Пространства.

> **[2026.4.25]** [v1.2.5](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.5) — Постоянные вложения чата с панелью предварительного просмотра файлов, конвейеры возможностей с учётом вложений, экспорт Markdown TutorBot.

> **[2026.4.25]** [v1.2.4](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.4) — Вложения текста/кода/SVG, тур настройки в одну команду, экспорт чата в Markdown, компактный интерфейс управления KB.

> **[2026.4.24]** [v1.2.3](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.3) — Вложения документов (PDF/DOCX/XLSX/PPTX), отображение блоков рассуждений, редактор шаблонов Soul, сохранение Co-Writer в блокнот.

> **[2026.4.22]** [v1.2.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.2) — Система навыков, написанных пользователями, капитальный ремонт производительности ввода чата, автозапуск TutorBot, интерфейс библиотеки книг, полноэкранная визуализация.

> **[2026.4.21]** [v1.2.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.1) — Лимиты токенов на стадию, регенерация ответов во всех точках входа, исправления совместимости RAG и Gemma.

> **[2026.4.20]** [v1.2.0](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.0) — Движок книг «живая книга», многодокументный Co-Writer, интерактивные HTML-визуализации, @-упоминание в Банке вопросов.

> **[2026.4.18]** [v1.1.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.1.2) — Вкладка каналов на основе схемы, консолидация единого конвейера RAG, вынесенные подсказки чата.

> **[2026.4.17]** [v1.1.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.1.1) — Универсальный «Ответить сейчас», синхронизация прокрутки Co-Writer, унифицированная панель настроек, кнопка остановки потоковой передачи.

> **[2026.4.15]** [v1.1.0](https://github.com/HKUDS/DeepTutor/releases/tag/v1.1.0) — Капитальный ремонт блочной математики LaTeX, диагностический зонд LLM, руководство по Docker + локальным LLM.

> **[2026.4.14]** [v1.1.0-beta](https://github.com/HKUDS/DeepTutor/releases/tag/v1.1.0-beta) — Сессии с закладками, тема Snow, пульс WebSocket и автоматическое переподключение, переработка реестра встраивания.

> **[2026.4.13]** [v1.0.3](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.3) — Тетрадь вопросов с закладками и категориями, Mermaid в Visualize, обнаружение несоответствия встраивания, совместимость с Qwen/vLLM, поддержка LM Studio и llama.cpp, тема Glass.

> **[2026.4.11]** [v1.0.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.2) — Консолидация поиска с откатом SearXNG, исправление переключения провайдера, исправление утечки ресурсов во фронтенде.

> **[2026.4.10]** [v1.0.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.1) — Возможность Visualize (Chart.js/SVG), предотвращение дублирования в викторине и поддержка модели o4-mini.

> **[2026.4.10]** [v1.0.0-beta.4](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.0-beta.4) — Отслеживание прогресса встраивания с повторной попыткой при превышении лимита, кросс-платформенные исправления зависимостей и исправление валидации MIME.

> **[2026.4.8]** [v1.0.0-beta.3](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.0-beta.3) — Нативный SDK OpenAI/Anthropic (замена litellm), поддержка Math Animator на Windows, надёжный разбор JSON и полная китайская локализация.

> **[2026.4.7]** [v1.0.0-beta.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.0-beta.2) — Горячая перезагрузка настроек, вложенный вывод MinerU, исправление WebSocket и минимальная версия Python 3.11+.

> **[2026.4.4]** [v1.0.0-beta.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.0-beta.1) — Переписанная агентная архитектура (~200 тыс. строк): плагинная модель инструментов и возможностей, CLI и SDK, TutorBot, Co-Writer, Направленное обучение и постоянная память.

> **[2026.1.23]** [v0.6.0](https://github.com/HKUDS/DeepTutor/releases/tag/v0.6.0) — Сохранение сессий, инкрементная загрузка документов, гибкий импорт конвейера RAG и полная китайская локализация.

> **[2026.1.18]** [v0.5.2](https://github.com/HKUDS/DeepTutor/releases/tag/v0.5.2) — Поддержка Docling для RAG-Anything, оптимизация системы логирования и исправление ошибок.

> **[2026.1.15]** [v0.5.0](https://github.com/HKUDS/DeepTutor/releases/tag/v0.5.0) — Унифицированная конфигурация сервиса, выбор конвейера RAG для каждой базы знаний, переработка генерации вопросов и настройка боковой панели.

> **[2026.1.9]** [v0.4.0](https://github.com/HKUDS/DeepTutor/releases/tag/v0.4.0) — Поддержка нескольких провайдеров LLM и встраивания, новая домашняя страница, разделение модуля RAG и рефакторинг переменных среды.

> **[2026.1.5]** [v0.3.0](https://github.com/HKUDS/DeepTutor/releases/tag/v0.3.0) — Архитектура унифицированного PromptManager, GitHub Actions CI/CD и предсобранные Docker-образы на GHCR.

> **[2026.1.2]** [v0.2.0](https://github.com/HKUDS/DeepTutor/releases/tag/v0.2.0) — Развёртывание Docker, обновление Next.js 16 и React 19, усиление безопасности WebSocket и исправление критических уязвимостей.

</details>

### 📰 Новости

- **2026-06-17** 🚀 Запущен v1.4.6 — Центр Знаний с мультидвижковым RAG, Мои Агенты, голос и генерация изображений/видео.
- **2026-05-22** 🌐 Официальный сайт документации запущен на [**deeptutor.info**](https://deeptutor.info/) — руководства, справочники и туры по возможностям в одном месте.
- **2026-04-19** 🎉 20 тысяч звёзд за 111 дней! Благодарим за поддержку на пути к по-настоящему персонализированному интеллектуальному обучению.
- **2026-04-10** 📄 Наша статья опубликована на arXiv — прочитайте [препринт](https://arxiv.org/abs/2604.26962) о дизайне и идеях, лежащих в основе DeepTutor.
- **2026-02-06** 🚀 10 тысяч звёзд всего за 39 дней! Огромная благодарность нашему удивительному сообществу.
- **2026-01-01** 🎊 С Новым Годом! Присоединяйтесь к нашему [Discord](https://discord.gg/eRsjPgMU4t), [WeChat](https://github.com/HKUDS/DeepTutor/issues/78) или [Обсуждениям](https://github.com/HKUDS/DeepTutor/discussions) — давайте вместе формировать DeepTutor.
- **2025-12-29** 🎓 DeepTutor официально выпущен!

## ✨ Ключевые возможности

DeepTutor — это агентная учебная рабочая среда, объединяющая репетиторство, решение задач, генерацию викторин, исследования, визуализацию и практику освоения в одной расширяемой системе.

- **Единая среда выполнения для всех режимов** — Chat, Quiz, Research, Visualize, Solve и Mastery Path на одном цикле агента, переключается цель, а не движок, и контекст перемещается вместе с учащимся.
- **Связанный контекст обучения** — базы знаний, книги, черновики Co-Writer, блокноты, банки вопросов, персоны и Memory во всех рабочих процессах.
- **Субагенты и Partners** — консультировать живой Claude Code, Codex или Partner; постоянные IM-компаньоны на том же мозге.
- **Многодвигательные знания** — RAG-библиотеки: LlamaIndex, PageIndex, GraphRAG, LightRAG или связанный Obsidian.
- **Расширяемые инструменты и навыки** — инструменты, MCP-серверы, генерация изображений/видео/голоса, навыки EduHub.
- **Проверяемая память** — трассы L1, сводки L2, синтез L3, Memory Graph отслеживает каждое утверждение.

---

## 🚀 Начало работы

DeepTutor поставляется с четырьмя путями установки. Все они используют одну структуру рабочего пространства: настройки хранятся в `data/user/settings/` в директории запуска (или в `DEEPTUTOR_HOME` / `deeptutor start --home`, если задано явно). Для полного приложения рекомендуемый процесс: **выбрать директорию рабочего пространства → установить → `deeptutor init` → `deeptutor start`**.

<details>
<summary><b>Вариант 1 — Установка из PyPI</b> · полное локальное веб-приложение + CLI, клонирование не требуется</summary>

Полное локальное веб-приложение + CLI без необходимости клонирования. Требуется **Python 3.11+** и среда выполнения **Node.js 20+** в PATH (упакованный автономный сервер Next.js запускается командой `deeptutor start`).

```bash
mkdir -p my-deeptutor && cd my-deeptutor
pip install -U deeptutor
deeptutor init     # запрашивает порты + провайдер LLM + необязательное встраивание
deeptutor start    # запускает бэкенд + фронтенд; держите терминал открытым
```

`deeptutor init` запрашивает порт бэкенда (по умолчанию `8001`), порт фронтенда (по умолчанию `3782`), провайдер LLM / базовый URL / API-ключ / модель и необязательный провайдер встраивания для базы знаний / RAG.

После `deeptutor start` откройте URL фронтенда, напечатанный в терминале — по умолчанию [http://127.0.0.1:3782](http://127.0.0.1:3782). Нажмите `Ctrl+C` в этом терминале, чтобы остановить бэкенд и фронтенд. Пропустить `deeptutor init` можно для быстрого пробного запуска; приложение загружается с портами по умолчанию и пустыми настройками модели, которые можно настроить позже в **Настройки → Модели**.

</details>

<details>
<summary><b>Вариант 2 — Установка из исходного кода</b> · разработка на основе чекаута</summary>

Для разработки на основе чекаута. Используйте **Python 3.11+** и **Node.js 22 LTS** для соответствия CI и Docker.

```bash
git clone https://github.com/HKUDS/DeepTutor.git
cd DeepTutor

# Создание venv (macOS/Linux). Windows PowerShell:
#   py -3.11 -m venv .venv ; .\.venv\Scripts\Activate.ps1
python3 -m venv .venv && source .venv/bin/activate
python -m pip install --upgrade pip

# Установка зависимостей бэкенда + фронтенда
python -m pip install -e .
( cd web && npm ci --legacy-peer-deps )

deeptutor init
deeptutor start
```

Установки из исходного кода запускают Next.js в режиме разработки для локальной директории `web/`; всё остальное (структура конфигурации, порты, остановка с `Ctrl+C`) соответствует Варианту 1.

<details>
<summary><b>Среда Conda</b> (вместо <code>venv</code>)</summary>

```bash
conda create -n deeptutor python=3.11
conda activate deeptutor
python -m pip install --upgrade pip
```

</details>

<details>
<summary><b>Необязательные дополнения при установке</b> — dev / partners / matrix / math-animator</summary>

```bash
pip install -e ".[dev]"             # инструменты тестирования/линтинга
pip install -e ".[partners]"        # SDK каналов IM для Партнёров + MCP-клиент
pip install -e ".[matrix]"          # канал Matrix без E2EE/libolm
pip install -e ".[matrix-e2e]"      # Matrix E2EE; требует libolm
pip install -e ".[math-animator]"   # дополнение Manim; требует LaTeX/ffmpeg/системных библиотек
```

</details>

<details>
<summary><b>Настройка зависимостей фронтенда и устранение неполадок сервера разработки</b></summary>

**Изменение зависимостей фронтенда:** запустите `npm install --legacy-peer-deps` для обновления `web/package-lock.json`, затем зафиксируйте оба файла `web/package.json` и `web/package-lock.json`.

**Зависший сервер разработки:** если `deeptutor start` сообщает о существующем фронтенде, который не отвечает, остановите PID, который он печатает. Если процесс Next.js фактически не запущен, файлы блокировки устарели — удалите их и повторите попытку:

```bash
rm -f web/.next/dev/lock web/.next/lock
deeptutor start
```

</details>

</details>

<details>
<summary><b>Вариант 3 — Docker</b> · один автономный контейнер</summary>

Один контейнер для полного веб-приложения. Образы в GitHub Container Registry:

- `ghcr.io/hkuds/deeptutor:latest` — стабильный выпуск
- `ghcr.io/hkuds/deeptutor:pre` — предварительный выпуск, когда доступен

```bash
docker run --rm --name deeptutor \
  -p 127.0.0.1:3782:3782 \
  -p 127.0.0.1:8001:8001 \
  -v deeptutor-data:/app/data \
  ghcr.io/hkuds/deeptutor:latest
```

> ⚠️ **Пробросьте оба порта `3782` и `8001`.** `3782` обслуживает веб-интерфейс; `8001` — это бэкенд FastAPI, к которому обращается ваш браузер напрямую — прокси внутри контейнера нет. Пропустите маппинг `8001`, и страница всё равно загрузится, но **Настройки** покажут «Бэкенд недоступен» и останутся нерабочими.

Откройте [http://127.0.0.1:3782](http://127.0.0.1:3782). Контейнер создаёт `/app/data/user/settings/*.json` при первом запуске; настройте провайдеров моделей на странице веб-настроек. Конфигурация, API-ключи, логи, файлы рабочего пространства, память и базы знаний сохраняются в томе `deeptutor-data`.

- **Другие порты хоста:** измените левую часть каждого маппинга `-p host:container` (например, `-p 127.0.0.1:8088:3782`). Если вы измените порты на стороне контейнера в `/app/data/user/settings/system.json`, перезапустите и обновите правую часть каждого маппинга.
- **Фоновый режим:** добавьте `-d`, затем `docker logs -f deeptutor` для слежения, `docker stop deeptutor` для остановки, `docker rm deeptutor` перед повторным использованием имени. Том `deeptutor-data` сохраняет ваши настройки и рабочее пространство между перезапусками.

**Удалённый Docker / обратный прокси:** веб-интерфейс работает в браузере, поэтому браузеру нужен доступный URL бэкенда. Для удалённых серверов откройте **Настройки → Сеть** или отредактируйте `data/user/settings/system.json`:

```json
{
  "next_public_api_base_external": "https://deeptutor.example.com"
}
```

`public_api_base` принимается как псевдоним совместимости и нормализуется в `next_public_api_base_external` при сохранении. CORS использует **источники** фронтенда, а не URL API. При отключённой аутентификации DeepTutor разрешает обычные HTTP/HTTPS источники браузера по умолчанию. При включённой аутентификации добавьте точные источники фронтенда:

```json
{
  "cors_origins": ["https://deeptutor.example.com"]
}
```

<details>
<summary><b>Подключение к Ollama / LM Studio / llama.cpp / vLLM / Lemonade на хосте</b></summary>

Внутри Docker `localhost` — это сам контейнер, а не хост-машина. Чтобы обратиться к модельному сервису, запущенному на хосте, используйте шлюз хоста (рекомендуется):

```bash
docker run --rm --name deeptutor \
  -p 127.0.0.1:3782:3782 -p 127.0.0.1:8001:8001 \
  --add-host=host.docker.internal:host-gateway \
  -v deeptutor-data:/app/data \
  ghcr.io/hkuds/deeptutor:latest
```

Затем в **Настройки → Модели** укажите базовый URL провайдера как `host.docker.internal`:

- Ollama LLM: `http://host.docker.internal:11434/v1`
- Ollama embedding: `http://host.docker.internal:11434/api/embed`
- LM Studio: `http://host.docker.internal:1234/v1`
- llama.cpp: `http://host.docker.internal:8080/v1`
- Lemonade: `http://host.docker.internal:13305/api/v1`

Docker Desktop (macOS/Windows) обычно разрешает `host.docker.internal` без `--add-host`. На Linux этот флаг — переносимый способ создания этого имени хоста в современном Docker Engine.

**Альтернатива для Linux — сетевой режим хоста:** добавьте `--network=host` и уберите флаги `-p`. Контейнер напрямую использует сеть хоста, поэтому откройте [http://127.0.0.1:3782](http://127.0.0.1:3782) (или `frontend_port` в `system.json`), а сервисы хоста доступны через обычные localhost-URL, например `http://127.0.0.1:11434/v1`. Обратите внимание, что хостовый сетевой режим открывает порты контейнера напрямую на хосте и может конфликтовать с существующими сервисами.

</details>

</details>

<details>
<summary><b>Вариант 4 — Только CLI</b> · без веб-интерфейса, из чекаута исходного кода</summary>

Когда веб-интерфейс не нужен. Пакет только для CLI устанавливается из чекаута исходного кода, а не из PyPI.

```bash
git clone https://github.com/HKUDS/DeepTutor.git
cd DeepTutor

# Создание venv (macOS/Linux). Windows PowerShell:
#   py -3.11 -m venv .venv-cli ; .\.venv-cli\Scripts\Activate.ps1
python3 -m venv .venv-cli && source .venv-cli/bin/activate
python -m pip install --upgrade pip

python -m pip install -e ./packaging/deeptutor-cli
deeptutor init --cli
deeptutor chat
```

`deeptutor init --cli` использует ту же структуру `data/user/settings/`, что и полное приложение, но пропускает запросы портов бэкенда/фронтенда и по умолчанию отключает встраивание (выберите `Yes`, если планируете использовать `deeptutor kb …` или инструменты RAG). Он всё равно записывает полную структуру среды выполнения и запрашивает активный провайдер и модель LLM.

<details>
<summary><b>Основные команды</b></summary>

```bash
deeptutor chat                                          # интерактивный REPL
deeptutor chat --capability deep_solve --tool rag --kb my-kb
deeptutor run chat "Explain Fourier transform"
deeptutor run deep_solve "Solve x^2 = 4" --tool rag --kb my-kb
deeptutor kb create my-kb --doc textbook.pdf
deeptutor memory show
deeptutor config show
```

</details>

Локальная установка `deeptutor-cli` не включает веб-ресурсы или серверные зависимости. Сохраните чекаут исходного кода — редактируемая установка указывает на него. Чтобы позже добавить веб-приложение, установите пакет PyPI (Вариант 1) и запустите `deeptutor init` + `deeptutor start` из того же рабочего пространства.

</details>

<details>
<summary><b>Справочник конфигурации</b> — файлы конфигурации в <code>data/user/settings/</code> (JSON/YAML)</summary>

Всё в `data/user/settings/` — это обычный JSON/YAML. Страница **Настройки** в браузере является рекомендуемым редактором.

| Файл | Назначение |
|:---|:---|
| `model_catalog.json` | Профили провайдеров LLM, встраивания и поиска; API-ключи; активные модели |
| `system.json` | Порты бэкенда/фронтенда, публичный базовый URL API, CORS, верификация SSL, директория вложений |
| `auth.json` | Необязательное переключение аутентификации, имя пользователя, хэш пароля, настройки токенов/куки |
| `integrations.json` | Необязательные настройки интеграции PocketBase и сайдкара |
| `interface.json` | Язык интерфейса / тема / настройки боковой панели |
| `main.yaml` | Значения по умолчанию для среды выполнения и внедрение пути |
| `agents.yaml` | Настройки температуры и токенов для возможностей/инструментов |

Корневой файл `.env` проекта **не** читается как файл конфигурации приложения. Для минимальной настройки модели откройте **Настройки → Модели**, добавьте профиль LLM (базовый URL / API-ключ / имя модели) и сохраните. Добавляйте профиль встраивания только если планируете использовать функции базы знаний / RAG.

</details>

## 📖 Обзор DeepTutor

Начните с основных поверхностей, которые вы будете использовать ежедневно: Chat, Partners, My Agents, Co-Writer, Book, Knowledge Center, Learning Space, Memory и Settings. Затем тур охватывает многопользовательские развёртывания для общих изолированных рабочих пространств.

<div align="center">
<img src="../../assets/figs/web-1.4.6+/OVERVIEW.png" alt="Главная страница DeepTutor — рабочее пространство чата со всеми поверхностями на боковой панели" width="900">
</div>

### 💬 Чат

<div align="center">
<img src="../../assets/figs/web-1.4.6+/home/00-overview.png" alt="Рабочее пространство чата DeepTutor" width="900">
</div>

Чат — это возможность по умолчанию и место, где начинается большинство работ. Один поток может нормально общаться, вызывать инструменты, опираться на выбранные базы знаний, читать вложения, генерировать изображения, обращаться к субагентам, записывать в блокнот и продолжать с тем же контекстом в последующих ходах.

Цикл намеренно прост: модель думает раундами, вызывает инструменты при необходимости, наблюдает результаты и завершает сообщением без инструментов. `ask_user` особенный — вместо угадывания агент может приостановить ход, задать структурированный уточняющий вопрос и возобновить работу, когда вы ответите.

<div align="center">
<img src="../../assets/figs/system/chat-agent-loop.png" alt="Цикл агента чата DeepTutor" width="900">
</div>

Переключаемые пользователем инструменты: `brainstorm`, `web_search`, `paper_search`, `reason` и `geogebra_analysis` — плюс `imagegen` и `videogen` после настройки соответствующей генеративной модели. Контекстные инструменты, такие как `rag`, `read_source`, `read_memory`, `write_memory`, `read_skill`, `load_tools`, `exec`, `web_fetch`, `ask_user`, `list_notebook`, `write_note`, `github` и `consult_subagent`, монтируются автоматически, когда ход имеет подходящий контекст.

Контекст бывает двух видов: **постоянный контекст сессии** (субагент, базы знаний, персонаж, модель, голос) находится на панели инструментов редактора и сохраняется между ходами; **одноразовые ссылки** (файлы, история чата, книги, блокноты, банк вопросов, импортированные агенты) берутся из меню `+` для одного хода.

Чат также является точкой запуска более глубоких возможностей: **Quiz** для генерации вопросов, **Research** для цитируемых отчётов, **Visualize** для графиков / диаграмм / анимаций, и — в разделе *Дополнительные возможности* — **Solve** для обоснованных рассуждений и **Mastery Path** для учебных планов.

### 🤝 Partner

<div align="center">
<img src="../../assets/figs/web-1.4.6+/partners/00-partners%20overview.png" alt="Рабочее пространство партнёров DeepTutor" width="900">
</div>

Партнёры — это постоянные компаньоны со своей душой, политикой модели, библиотекой, памятью и каналами. Они не являются отдельным движком бота: каждое входящее веб- или IM-сообщение становится обычным ходом `ChatOrchestrator` внутри рабочего пространства, ограниченного партнёром. Партнёр — это «чат с личностью и номером телефона».

<div align="center">
<img src="../../assets/figs/system/partners-architecture.png" alt="Архитектура партнёров DeepTutor" width="900">
</div>

Каждый партнёр имеет `SOUL.md`, выбор модели, каналы, политику инструментов и назначенную библиотеку. Базы знаний, навыки и блокноты копируются в `data/partners/<id>/workspace/`, поэтому те же инструменты RAG, навыков, блокнотов и памяти работают без специальных случаев. Партнёр читает память своего владельца, но пишет только в собственную.

<div align="center">
<img src="../../assets/figs/web-1.4.6+/partners/02-IM%20config%20for%20each%20partner.png" alt="Конфигурация IM-канала для каждого партнёра" width="900">
</div>

Слой каналов управляется схемой и может подключаться к IM-платформам, таким как Feishu, Telegram, Slack, DingTalk, QQ/NapCat, WeCom, WhatsApp, Zulip, Matrix и Microsoft Teams, в зависимости от установленных дополнений и настроенных учётных данных. Партнёр также может быть подключён как субагент и использован из обычного хода чата — см. **Мои Агенты** ниже.

### 🧑‍🚀 Мои Агенты

<div align="center">
<img src="../../assets/figs/web-1.4.6+/myagents/00-overview.png" alt="Рабочее пространство «Мои Агенты» DeepTutor" width="900">
</div>

Мои Агенты превращают других агентов в контекст для DeepTutor и делают две разные вещи. **Подключите живого агента** — Claude Code или Codex CLI на вашей машине, или одного из ваших Партнёров — и обращайтесь к нему изнутри хода чата: DeepTutor фактически *запускает* другого агента и транслирует его работу в панель Activity через инструмент `consult_subagent`. Выберите его чипом агента (или введите `@`) и задайте, сколько раундов может занять обращение.

<div align="center">
<img src="../../assets/figs/web-1.4.6+/home/08-subagent%20demo%20with%20claude%20code.png" alt="Обращение к субагенту Claude Code в реальном времени" width="900">
</div>

**Импортируйте прошлые разговоры** — загрузите существующую историю Claude Code и Codex как именованных, доступных для поиска, возобновляемых агентов. Выберите, за какие дни импортировать; обновление повторно синхронизирует их. Ссылайтесь на импортированный разговор из любого хода чата через `+` → Мои Агенты, и DeepTutor читает его как транскрипт третьей стороны — это *их* разговор, а не собственный голос DeepTutor.

### ✍️ Co-Writer

<div align="center">
<img src="../../assets/figs/web-1.4.6+/co-writer/00-overview.png" alt="Рабочее пространство Co-Writer DeepTutor" width="900">
</div>

Co-Writer — это разделённое рабочее пространство Markdown для отчётов, руководств, заметок и долгосрочных учебных артефактов. Документы автосохраняются и отображают живой предварительный просмотр (математика KaTeX, ограждения диаграмм), и могут быть сохранены обратно в блокноты, когда черновик становится повторно используемым контекстом.

<div align="center">
<img src="../../assets/figs/web-1.4.6+/co-writer/01-edit%20panel.png" alt="Редактор Co-Writer с живым предварительным просмотром" width="900">
</div>

Его определяющая идея — **хирургическое редактирование**: выберите фрагмент и попросите DeepTutor переписать, расширить или сократить его. Агент редактирования может опираться на базу знаний или веб-данные, ведёт след вызовов инструментов и показывает каждое изменение как diff с принятием/отклонением — так ничто не применяется до вашего одобрения.

### 📖 Книга

<div align="center">
<img src="../../assets/figs/web-1.4.6+/book/00-book_overview.png" alt="Библиотека книг DeepTutor" width="900">
</div>

<p align="center">
<img src="../../assets/figs/web-1.4.6+/book/01-book-demo-quiz%20card.png" alt="Блок викторины книги" width="31%">
&nbsp;
<img src="../../assets/figs/web-1.4.6+/book/02-book-demo-manim%20video.png" alt="Блок анимации Manim книги" width="31%">
&nbsp;
<img src="../../assets/figs/web-1.4.6+/book/03-book-demo%20interactive%20module.png" alt="Блок интерактивного виджета книги" width="31%">
</p>

Книга превращает выбранные источники в интерактивную **живую книгу** — не статический PDF, а среда чтения, построенная из типизированных блоков. Книга может начинаться с баз знаний, блокнотов, банков вопросов или истории чата; процесс создания предлагает план глав перед генерацией содержания, поэтому вы рассматриваете структуру вместо того, чтобы принимать слепой одноразовый вывод.

Каждая глава компилируется в типизированные блоки — текст, выноски, викторины, флэш-карточки, временные шкалы, код, рисунки, интерактивный HTML, анимации, концептуальные графы, углублённые рассуждения и пользовательские заметки — и каждая страница имеет свой собственный чат. Блоки редактируемы: вставляйте, перемещайте, регенерируйте или меняйте тип блока без переписывания главы.

### 📚 Центр Знаний

<div align="center">
<img src="../../assets/figs/web-1.4.6+/knowledge/00-overview.png" alt="Центр Знаний DeepTutor" width="900">
</div>

Базы знаний — это коллекции документов для RAG, которые обосновывают ходы Chat, редакции Co-Writer, генерацию Book и разговоры с Партнёрами. Отличительной чертой является **выбор движков поиска**: **LlamaIndex** (по умолчанию, локальный вектор + BM25), **PageIndex** (размещённый, поиск с рассуждением с цитатами на уровне страницы), **GraphRAG** и **LightRAG** (поиск на основе графа знаний) или подключённое хранилище **Obsidian**, которое репетитор читает и записывает на месте. Каждая KB индексируется одним движком.

<div align="center">
<img src="../../assets/figs/web-1.4.6+/knowledge/01-create%20knowledge%20base.png" alt="Создание базы знаний" width="900">
</div>

При создании KB вы либо **создаёте новую** (загружаете документы и строите свежий индекс), либо **связываете существующую** (повторно используете индекс, построенный в другом месте, читаете на месте без переиндексирования). Переиндексирование записывает новую плоскую директорию `version-N` и сохраняет предыдущие, поэтому рабочий индекс никогда не уничтожается в процессе перестройки. Разбор документов — только текст, MinerU, Docling или markitdown — выбирается в **Настройки → База знаний**, с отключёнными по умолчанию загрузками локальных моделей.

### 🌐 Пространство Обучения

<div align="center">
<img src="../../assets/figs/web-1.4.6+/learning-space/00-overview.png" alt="Хаб Пространства Обучения DeepTutor" width="900">
</div>

Пространство Обучения — это библиотека и уровень персонализации — место, где живут постоянные вещи. **Разговоры и материалы** содержат историю чата, блокноты и банк вопросов (каждый сохранённый вопрос хранит ваш ответ, эталонный ответ и объяснение). **Персонализация** содержит пути мастерства, персонажей (поведенческие пресеты, такие как *коллега*, *исследовательский ассистент*, *учитель*) и навыки (сценарии `SKILL.md`, которые модель читает по требованию). Всё здесь можно повторно использовать из Chat, Partners, Co-Writer и Book.

<div align="center">
<img src="../../assets/figs/web-1.4.6+/learning-space/07-%20download%20skills%20from%20eduhub.png" alt="Импорт навыков из EduHub" width="900">
</div>

Вам не нужно писать каждый навык самостоятельно — **Импорт из EduHub** просматривает каталог сообщества и загружает навык прямо в вашу библиотеку через шлюз безопасности (см. [Экосистема](#-экосистема--eduhub-и-сообщество-навыков)).

### 🧠 Память

<div align="center">
<img src="../../assets/figs/web-1.4.6+/memory/00-overview.png" alt="Обзор Памяти DeepTutor" width="900">
</div>

Память — это трёхуровневая система на основе файлов, которую можно читать, курировать и проверять — намеренно *не* скрытое векторное хранилище. **L1** — зеркало рабочего пространства плюс трассировка событий только для добавления (`trace/<surface>/<date>.jsonl`); **L2** — курированные факты на уровне поверхности (`L2/<surface>.md`); **L3** — межповерхностный синтез (`L3/<profile|recent|scope>.md`). Поскольку L2 цитирует L1, а L3 цитирует L2, ничто в вашем профиле не является неотчётным.

<div align="center">
<img src="../../assets/figs/web-1.4.6+/memory/01-3%20layer%20memory%20graph.png" alt="Граф Памяти DeepTutor" width="900">
</div>

Граф памяти показывает всю пирамиду — синтез L3 в центре, L2 в среднем кольце, трассировки L1 снаружи — так что вы можете проследить любое синтезированное утверждение обратно до точного исходного события. Память отслеживается по поверхностям `chat`, `notebook`, `quiz`, `kb`, `book`, partner и `cowriter`; бюджеты обновления / аудита / дедупликации консолидатора настраиваются в **Настройки → Память**.

### ⚙️ Настройки

<div align="center">
<img src="../../assets/figs/web-1.4.6+/settings/00-setting%20overview.png" alt="Хаб настроек DeepTutor" width="900">
</div>

Настройки — это операционная панель управления с живой строкой статуса (Бэкенд, LLM, Встраивание, Поиск) и одной карточкой для каждой области: **Внешний вид** (тема + язык интерфейса), **Сеть** (базовый URL API, порты, CORS), **Модели** (LLM, Встраивание, Поиск, Синтез речи, Распознавание речи, Генерация изображений, Генерация видео), **База знаний** (движок разбора документов), **Чат** (инструменты, MCP-серверы, параметры по возможностям), **Партнёры и агенты** (субагенты, к которым можно обратиться из хода) и **Память** (бюджеты консолидатора).

<div align="center">
<img src="../../assets/figs/web-1.4.6+/settings/01-appearance%20settings.png" alt="Настройки внешнего вида и темы DeepTutor" width="900">
</div>

Большинство разделов используют поток черновика и применения, поэтому вы можете протестировать провайдера перед подтверждением. В комплект входят четыре темы — Default, Cream, Dark и Glass. Корневые файлы `.env` проекта намеренно игнорируются; конфигурация среды выполнения хранится в `data/user/settings/*.json`, если только `DEEPTUTOR_HOME` или `deeptutor start --home` не указывает приложению другое место.

---

## 👥 Многопользовательский режим

Аутентификация **отключена по умолчанию** — DeepTutor работает в однопользовательском режиме. Включите её, и одно дерево `data/` содержит рабочее пространство администратора, изолированные пользовательские рабочие пространства и партнёрские рабочие пространства рядом:

```text
data/
├── user/                    # Рабочее пространство администратора + глобальные настройки
├── users/<uid>/             # Пользовательская область: история чата, память, блокноты, KB
├── partners/<id>/workspace/ # Область партнёра (синтетического пользователя)
└── system/                  # auth/users.json · grants/<uid>.json · audit/usage.jsonl
```

**Первый зарегистрированный пользователь становится администратором** и владеет каталогами моделей, учётными данными провайдеров, общими базами знаний, навыками и грантами для пользователей. Все остальные получают изолированное рабочее пространство и отредактированную страницу Настроек — назначенные администратором модели, KB и навыки отображаются как ограниченные опции только для чтения, а не как сырые API-ключи.

**Включение:** включите аутентификацию в `data/user/settings/auth.json`, перезапустите `deeptutor start`, зарегистрируйте первого администратора по адресу `/register`, затем добавляйте пользователей из `/admin/users` и назначайте модели, KB, навыки, политику инструментов/MCP и доступ к выполнению кода через гранты.

---

## ⌨️ DeepTutor CLI — Интерфейс для агентов

Один бинарный файл `deeptutor`, два способа входа: интерактивный **REPL** для тех, кто живёт в терминале, и структурированный **JSON** для других агентов, которые управляют DeepTutor как инструментом. Одни и те же возможности, инструменты и базы знаний в любом случае.

Примеры команд:

```bash
deeptutor chat                                              # интерактивный REPL
deeptutor chat --capability deep_solve --kb my-kb --tool rag
deeptutor run chat "Explain the Fourier transform" --tool rag --kb textbook
deeptutor run deep_research "Survey 2026 papers on RAG" \
  --config mode=report --config depth=standard
```

<details>
<summary><b>Справочник команд</b></summary>

| Команда | Описание |
|:---|:---|
| `deeptutor init` | Создать или обновить `data/user/settings` для текущего рабочего пространства |
| `deeptutor start [--home PATH]` | Запустить бэкенд + фронтенд вместе |
| `deeptutor serve [--port PORT]` | Запустить только бэкенд FastAPI |
| `deeptutor run <capability> <message>` | Запустить один ход возможности (`chat`, `deep_solve`, `deep_question`, `deep_research`, `visualize`, `math_animator`, `mastery_path`); добавьте `--format json` для вывода NDJSON |
| `deeptutor chat` | Интерактивный REPL с управлением возможностями, инструментами, KB, блокнотами и историей |
| `deeptutor partner list/create/start/stop` | Управление партнёрами, подключёнными к IM |
| `deeptutor kb list/info/create/add/search/set-default/delete` | Управление базами знаний LlamaIndex |
| `deeptutor skill search/install/list/remove/login/publish/update` | Управление навыками, установка из хабов и публикация своих (`eduhub:<slug>` по умолчанию) |
| `deeptutor memory show/clear` | Просмотр документов памяти L2/L3 или очистка памяти L1/всей памяти |
| `deeptutor session list/show/open/rename/delete` | Управление общими сессиями |
| `deeptutor notebook list/create/show/add-md/replace-md/remove-record` | Управление блокнотами из файлов Markdown |
| `deeptutor book list/health/refresh-fingerprints` | Просмотр книг и обновление исходных отпечатков |
| `deeptutor plugin list/info` | Просмотр зарегистрированных инструментов и возможностей |
| `deeptutor config show` | Вывод сводки конфигурации |
| `deeptutor provider login <provider>` | Аутентификация провайдера (`openai-codex` вход через OAuth; `github-copilot` проверяет существующую сессию аутентификации Copilot) |

</details>

---

## 🧩 Экосистема — EduHub и Сообщество Навыков

Навыки DeepTutor используют открытый формат **Agent-Skills** — папку с плейбуком `SKILL.md` (YAML frontmatter + Markdown) и необязательными справочными файлами. В нём нет ничего специфичного для DeepTutor, поэтому любой реестр, говорящий на этом формате, становится источником для вашей библиотеки. DeepTutor поставляется с **[EduHub](https://eduhub.deeptutor.info/)** — нашим собственным образовательным реестром навыков — встроенным в качестве хаба по умолчанию.

<details>
<summary><b>EduHub — экосистема навыков DeepTutor</b></summary>

[**EduHub**](https://eduhub.deeptutor.info/) — это хаб сообщества, запущенный DeepTutor для обмена обучающими навыками агентов — сократовские репетиторы, создатели флэш-карточек, обратная связь по эссе, планы экзаменов, объяснители концепций и многое другое. Он встроен в DeepTutor, поэтому настраивать ничего не нужно: голый слаг или префикс `eduhub:` разрешается в него.

**Найти и установить** — в браузере откройте **Пространство Обучения → Навыки → Импорт из EduHub** для просмотра каталога и загрузки навыка прямо в вашу библиотеку. Из терминала:

```bash
deeptutor skill search "socratic tutor"               # поиск в EduHub (хаб по умолчанию)
deeptutor skill install socratic-tutor                # получить → проверить → зарегистрировать
deeptutor skill install eduhub:socratic-tutor@1.2.0   # указать хаб и версию
deeptutor skill list                                  # локальные навыки с их хабовой принадлежностью
```

**Опубликуйте свой** — упакуйте `SKILL.md` и поделитесь им обратно с сообществом:

```bash
deeptutor skill login                                 # вход через браузер в EduHub
deeptutor skill publish ./my-skill                    # интерактивно: выберите трек + теги, затем загрузите
deeptutor skill update                                # откатиться или выпустить новую версию
```

EduHub также является отдельным, совместимым с ClawHub реестром, поэтому агенты, отличные от DeepTutor (Claude Code, Codex, …), могут использовать его напрямую через CLI `eduhub` — `npx eduhub install socratic-tutor`.

</details>

<details>
<summary><b>Шлюз безопасности импорта</b></summary>

Независимо от источника, каждый импорт проходит через **один шлюз безопасности** перед тем, как что-либо коснётся вашего рабочего пространства:

- сначала проверяется **вердикт безопасности** реестра — отмеченные пакеты отклоняются, если вы не передали `--allow-unverified`;
- архивы извлекаются защищённо (защита от zip-slip / zip-bomb) за **белым списком суффиксов** для текста/скриптов, поэтому бинарные файлы никогда не попадают в рабочее пространство;
- frontmatter нормализуется по схеме DeepTutor, и `always:` **удаляется**, поэтому загруженный навык никогда не может принудить себя в каждый системный промпт;
- происхождение — хаб, версия, вердикт и время установки — записывается в `.hub-lock.json` для аудитов и обновлений.

В многопользовательских развёртываниях установка является исключительно привилегией администратора: новый навык попадает в каталог администратора и остаётся невидимым для других пользователей до тех пор, пока грант не назначит его, поэтому администратор может проверить его перед развёртыванием.

</details>

<details>
<summary><b>Также совместим с ClawHub</b></summary>

Поскольку DeepTutor использует открытый формат Agent-Skills, **[ClawHub](https://clawhub.ai/)** также работает как первоклассный источник — он встроен рядом с EduHub. Выберите его с префиксом хаба:

```bash
deeptutor skill search "git release notes" --hub clawhub
deeptutor skill install clawhub:git-release-notes@1.0.1
```

Добавляйте дополнительные реестры в `settings/skill_hubs.json`: запись `type: "clawhub"` указывает на любой совместимый HTTP API (EduHub и ClawHub оба его поддерживают), `type: "command"` оборачивает любой CLI получения, который поставляет реестр, а `"default"` выбирает хаб, используемый для голых слагов. Все они передаются через тот же шлюз импорта.

</details>

---

## 🌐 Сообщество

### 📮 Контакты

DeepTutor — это проект с открытым исходным кодом, который ведёт [Bingxi Zhao](https://github.com/pancacake) в составе группы [HKUDS](https://github.com/HKUDS), и он развивается в **полностью открытом формате**, создаваясь вместе с сообществом. До сих пор у нас **НЕТ** платных онлайн-продуктов в каком-либо виде. Не стесняйтесь обращаться по адресу **bingxizhao39@gmail.com** для обсуждений, идей или сотрудничества.

### 🙏 Благодарности

Сердечная благодарность [**Chao Huang**](https://sites.google.com/view/chaoh), директору Лаборатории интеллектуальных данных @ HKU, и нашим коллегам из HKUDS за их тёплую поддержку — особенно [**Jiahao Zhang**](https://github.com/zzhtx258), [**Zirui Guo**](https://github.com/LarFii) и [**Xubin Ren**](https://github.com/Re-bin). Мы также глубоко благодарны **сообществу открытого исходного кода**: ваши звёзды, вопросы, пул-реквесты и обсуждения каждый день формируют DeepTutor.

DeepTutor также стоит на плечах выдающихся проектов с открытым исходным кодом, которые дали нам инструменты и вдохновение:

| Проект | Роль / Вдохновение |
|:---|:---|
| [**LlamaIndex**](https://github.com/run-llama/llama_index) | Конвейер RAG и основа индексирования документов |
| [**nanobot**](https://github.com/HKUDS/nanobot) | Ультралёгкий движок агентов, обеспечивавший оригинальный TutorBot *(HKUDS)* |
| [**LightRAG**](https://github.com/HKUDS/LightRAG) | Простой и быстрый RAG *(HKUDS)* |
| [**AutoAgent**](https://github.com/HKUDS/AutoAgent) | Фреймворк агентов без кода *(HKUDS)* |
| [**AI-Researcher**](https://github.com/HKUDS/AI-Researcher) | Автоматизированный исследовательский конвейер *(HKUDS)* |
| [**OpenClaw**](https://github.com/openclaw/openclaw) | Открытый шлюз агентов и экосистема навыков за ClawHub |
| [**Codex**](https://github.com/openai/codex) | Агентный CLI кодирования, вдохновивший наш рабочий процесс CLI |
| [**Claude Code**](https://github.com/anthropics/claude-code) | Агентный CLI кодирования, вдохновивший цикл агента DeepTutor |
| [**ManimCat**](https://github.com/Wing900/ManimCat) | Генерация математической анимации на основе ИИ для Math Animator |

### 🗺️ Дорожная карта и участие

Мы хотим, чтобы DeepTutor продолжал развиваться и совершенствоваться — и в конечном итоге стал подарком, который мы возвращаем сообществу открытого исходного кода. Наша [**дорожная карта**](https://github.com/HKUDS/DeepTutor/issues/498) обновляется непрерывно; голосуйте там за пункты или предлагайте новые. Если вы хотите участвовать, см. [**Руководство по участию**](CONTRIBUTING.md) с описанием стратегии ветвления, стандартов кодирования и инструкций по началу работы.

<div align="center">

Мы надеемся, что DeepTutor станет подарком для сообщества. 🎁

<a href="https://github.com/HKUDS/DeepTutor/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=HKUDS/DeepTutor&max=999" alt="Участники" />
</a>

</div>

<div align="center">

<a href="https://www.star-history.com/#HKUDS/DeepTutor&type=timeline&legend=top-left">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=HKUDS/DeepTutor&type=timeline&theme=dark&legend=top-left" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=HKUDS/DeepTutor&type=timeline&legend=top-left" />
    <img alt="Диаграмма истории звёзд" src="https://api.star-history.com/svg?repos=HKUDS/DeepTutor&type=timeline&legend=top-left" />
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

Лицензировано по [Apache License 2.0](LICENSE).

<p>
  <img src="https://visitor-badge.laobi.icu/badge?page_id=HKUDS.DeepTutor&style=for-the-badge&color=00d4ff" alt="Views">
</p>

</div>
