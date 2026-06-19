<div align="center">

<p align="center"><img src="../../assets/figs/logo/logo.png" alt="DeepTutor logo" height="56" style="vertical-align: middle;">&nbsp;<img src="../../assets/figs/logo/banner.png" alt="DeepTutor" height="48" style="vertical-align: middle;"></p>

# DeepTutor: Tutoría Personalizada Nativa de Agentes

<p align="center">
  <a href="https://deeptutor.info" target="_blank"><img alt="Docs — deeptutor.info" src="https://img.shields.io/badge/Docs-deeptutor.info%20%E2%86%97-0A0A0A?style=for-the-badge&labelColor=F5F5F4" height="36"></a>
</p>

<a href="https://trendshift.io/repositories/17099" target="_blank"><img src="https://trendshift.io/api/badge/repositories/17099" alt="HKUDS%2FDeepTutor | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>

<p align="center">
  <a href="../../README.md"><img alt="English" height="40" src="https://img.shields.io/badge/English-CDCFD4"></a>&nbsp;
  <a href="README_CN.md"><img alt="简体中文" height="40" src="https://img.shields.io/badge/简体中文-CDCFD4"></a>&nbsp;
  <a href="README_JA.md"><img alt="日本語" height="40" src="https://img.shields.io/badge/日本語-CDCFD4"></a>&nbsp;
  <a href="README_ES.md"><img alt="Español" height="40" src="https://img.shields.io/badge/Español-BCDCF7"></a>&nbsp;
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

[Características](#-características-principales) · [Comenzar](#-comenzar) · [Explorar](#-explorar-deeptutor) · [CLI](#️-deeptutor-cli--interfaz-nativa-de-agentes) · [Ecosistema](#-ecosistema--eduhub-y-la-comunidad-de-skills) · [Comunidad](#-comunidad)

</div>

---

> 🤝 **¡Damos la bienvenida a cualquier tipo de contribución!** Vota en los elementos del roadmap o propone nuevos en [`Roadmap`](https://github.com/HKUDS/DeepTutor/issues/498), y consulta nuestra [Guía de Contribución](../../CONTRIBUTING.md) para la estrategia de ramas, estándares de código y cómo comenzar.

### 📦 Versiones

> **[2026.6.17]** [v1.4.6](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.6) — Space se convierte en un dashboard de aprendizaje con Mis Agentes y Memory de nivel superior; el Centro de Conocimiento añade motores GraphRAG, PageIndex y LightRAG junto con bases de conocimiento vinculadas y Obsidian; Settings incorpora análisis de documentos, voz e imagen+video; capacidades bloqueadas por modelo LLM.

> **[2026.6.14]** [v1.4.5](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.5) — Guided Learning reconstruido sobre el bucle de chat; puertas de dominio; marco de loop-plugins; exportación Markdown para Partners.

> **[2026.6.13]** [v1.4.4](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.4) — Habilidades comunitarias desde ClawHub; previsualizaciones de DOCX/XLSX en el navegador.

> **[2026.6.12]** [v1.4.3](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.3) — TutorBot se convierte en **Partners** con un pipeline de IM de nivel producción con respuestas en streaming en vivo y 15 canales, Chat pasa a un único bucle de agente, aislamiento real por usuario para despliegues multi-usuario, Visualize reconstruido con validación+reparación local, más mejoras en Co-writer, visor de archivos, análisis MinerU en la nube y la CLI. Documentación completamente actualizada en [deeptutor.info](https://deeptutor.info/).

<details>
<summary><b>Versiones anteriores (más de 2 semanas)</b></summary>

> **[2026.5.28]** [v1.4.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.2) — Estabilidad + pulido sobre v1.4.1: Gemini 2.5+ desbloqueado en Visualize y Chat, corrección de enrutamiento de autenticación ContextVar (#485), protocolo de etiquetas de razonamiento + herramientas nativas endurecido, UX de streaming fluido en todas las superficies de chat, nueva barra lateral de Recientes plegable y soporte del proveedor local Lemonade.

> **[2026.5.27]** [v1.4.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.1) — Parche de seguridad + estabilidad: sandbox de herramientas TutorBot bloqueado, aislamiento de recursos por usuario, alternativa de imagen multimodal para proveedores con visión, una API HTTP/SSE para hablar con un TutorBot y corrección de regresión de chat de v1.4.0.

> **[2026.5.22]** [v1.4.0](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.0) — Versión GA de v1.4: Modo Auto, Memoria de tres capas, Deep Research / Solve / Question agénticos, refactorización de RAG con LlamaIndex, fusión Visualize/Animator, normalización de esfuerzo de razonamiento, alternativa de esquema de herramientas y tiempo de ejecución de turno seguro ante reinicios.

> **[2026.5.21]** [v1.4.0-beta](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.0-beta) — Banco de trabajo de Memoria de tres capas (L1/L2/L3), todas las capacidades de chat reconstruidas sobre un único motor agéntico, RAG exclusivo de LlamaIndex y una superficie unificada de Settings + Capabilities.

> **[2026.5.10]** [v1.3.10](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.10) — Recuperación de CORS de Docker remoto, `DISABLE_SSL_VERIFY` para proveedores SDK, citas de bloques de código más seguras y complemento Matrix E2EE opcional.

> **[2026.5.9]** [v1.3.9](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.9) — Soporte de Zulip y NVIDIA NIM para TutorBot, enrutamiento de modelo de pensamiento más seguro, `deeptutor start`, tooltips de barra lateral y paridad de almacén de sesiones.

> **[2026.5.8]** [v1.3.8](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.8) — Despliegues multi-usuario opcionales con espacios de trabajo de usuario aislados, permisos de administrador, rutas de autenticación y acceso de tiempo de ejecución limitado.

> **[2026.5.4]** [v1.3.7](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.7) — Correcciones de modelo de pensamiento/proveedor, historial de índice de Knowledge visible y edición más segura de plantillas/limpieza de Co-Writer.

> **[2026.5.3]** [v1.3.6](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.6) — Selección de modelos basada en catálogo para chat y TutorBot, reindexado de RAG más seguro, correcciones de límite de tokens de OpenAI Responses y validación del editor de Skills.

> **[2026.5.2]** [v1.3.5](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.5) — Configuración de inicio local más fluida, consultas RAG más seguras, autenticación de embeddings local más clara y pulido del modo oscuro de Settings.

> **[2026.5.1]** [v1.3.4](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.4) — Persistencia de chat en páginas de Book y flujos de reconstrucción, referencias de chat a Book, manejo más robusto de idioma/razonamiento, extracción de documentos RAG endurecida.

> **[2026.4.30]** [v1.3.3](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.3) — Soporte de embeddings NVIDIA NIM + Gemini, contexto Space unificado para historial de chat/skills/memoria, instantáneas de sesión, resiliencia de reindexado RAG.

> **[2026.4.29]** [v1.3.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.2) — URLs de endpoints de embeddings transparentes, resiliencia de reindexado RAG para vectores persistidos inválidos, limpieza de memoria para salida de modelo de pensamiento, corrección de tiempo de ejecución de Deep Solve.

> **[2026.4.28]** [v1.3.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.1) — Estabilidad: enrutamiento RAG y validación de embeddings más seguros, persistencia de Docker, entrada segura para IME, robustez en Windows/GBK.

> **[2026.4.27]** [v1.3.0](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.0) — Índices KB versionados con flujo de trabajo de reindexado, espacio de trabajo Knowledge reconstruido, autodescubrimiento de embeddings con nuevos adaptadores, hub Space.

> **[2026.4.25]** [v1.2.5](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.5) — Adjuntos de chat persistentes con cajón de vista previa de archivos, pipelines de capacidades con conciencia de adjuntos, exportación Markdown de TutorBot.

> **[2026.4.25]** [v1.2.4](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.4) — Adjuntos de texto/código/SVG, Setup Tour de un comando, exportación Markdown de chat, UI de gestión KB compacta.

> **[2026.4.24]** [v1.2.3](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.3) — Adjuntos de documentos (PDF/DOCX/XLSX/PPTX), visualización de bloques de pensamiento de razonamiento, editor de plantillas Soul, guardar Co-Writer en notebook.

> **[2026.4.22]** [v1.2.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.2) — Sistema de Skills creado por usuarios, revisión del rendimiento de entrada de chat, inicio automático de TutorBot, UI de Book Library, pantalla completa de visualización.

> **[2026.4.21]** [v1.2.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.1) — Límites de tokens por etapa, regeneración de respuesta en todos los puntos de entrada, correcciones de compatibilidad de RAG y Gemma.

> **[2026.4.20]** [v1.2.0](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.0) — Compilador de "libro vivo" Book Engine, Co-Writer multi-documento, visualizaciones HTML interactivas, @-mención de Question Bank.

> **[2026.4.18]** [v1.1.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.1.2) — Pestaña Channels impulsada por esquema, consolidación de pipeline único RAG, prompts de chat externalizados.

> **[2026.4.17]** [v1.1.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.1.1) — "Responder ahora" universal, sincronización de desplazamiento Co-Writer, panel de configuración unificado, botón Stop de streaming.

> **[2026.4.15]** [v1.1.0](https://github.com/HKUDS/DeepTutor/releases/tag/v1.1.0) — Revisión de matemáticas de bloque LaTeX, sonda de diagnóstico LLM, guía de Docker + LLM local.

> **[2026.4.14]** [v1.1.0-beta](https://github.com/HKUDS/DeepTutor/releases/tag/v1.1.0-beta) — Sesiones marcables, tema Snow, latido de WebSocket y reconexión automática, revisión del registro de embeddings.

> **[2026.4.13]** [v1.0.3](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.3) — Question Notebook con marcadores y categorías, Mermaid en Visualize, detección de desajuste de embeddings, compatibilidad Qwen/vLLM, soporte LM Studio y llama.cpp, tema Glass.

> **[2026.4.11]** [v1.0.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.2) — Consolidación de búsqueda con respaldo SearXNG, corrección de cambio de proveedor, correcciones de fugas de recursos del frontend.

> **[2026.4.10]** [v1.0.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.1) — Capacidad Visualize (Chart.js/SVG), prevención de duplicados en quizzes, soporte del modelo o4-mini.

> **[2026.4.10]** [v1.0.0-beta.4](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.0-beta.4) — Seguimiento del progreso de embeddings con reintento de límite de tasa, correcciones de dependencias multiplataforma, corrección de validación MIME.

> **[2026.4.8]** [v1.0.0-beta.3](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.0-beta.3) — SDK nativo OpenAI/Anthropic (eliminar litellm), soporte de Math Animator en Windows, análisis JSON robusto e i18n completo en chino.

> **[2026.4.7]** [v1.0.0-beta.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.0-beta.2) — Recarga en caliente de configuración, salida anidada MinerU, corrección de WebSocket y mínimo Python 3.11+.

> **[2026.4.4]** [v1.0.0-beta.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.0-beta.1) — Reescritura de arquitectura nativa de agentes (~200k líneas): modelo de plugins Tools + Capabilities, CLI y SDK, TutorBot, Co-Writer, Guided Learning y memoria persistente.

> **[2026.1.23]** [v0.6.0](https://github.com/HKUDS/DeepTutor/releases/tag/v0.6.0) — Persistencia de sesiones, carga incremental de documentos, importación flexible de pipeline RAG y localización completa al chino.

> **[2026.1.18]** [v0.5.2](https://github.com/HKUDS/DeepTutor/releases/tag/v0.5.2) — Soporte de Docling para RAG-Anything, optimización del sistema de registro y correcciones de errores.

> **[2026.1.15]** [v0.5.0](https://github.com/HKUDS/DeepTutor/releases/tag/v0.5.0) — Configuración de servicio unificada, selección de pipeline RAG por base de conocimiento, revisión de generación de preguntas y personalización de barra lateral.

> **[2026.1.9]** [v0.4.0](https://github.com/HKUDS/DeepTutor/releases/tag/v0.4.0) — Soporte de LLM y embeddings multi-proveedor, nueva página de inicio, desacoplamiento del módulo RAG y refactorización de variables de entorno.

> **[2026.1.5]** [v0.3.0](https://github.com/HKUDS/DeepTutor/releases/tag/v0.3.0) — Arquitectura PromptManager unificada, GitHub Actions CI/CD e imágenes Docker preconstruidas en GHCR.

> **[2026.1.2]** [v0.2.0](https://github.com/HKUDS/DeepTutor/releases/tag/v0.2.0) — Despliegue Docker, actualización a Next.js 16 y React 19, endurecimiento de seguridad WebSocket y correcciones de vulnerabilidades críticas.

</details>

### 📰 Noticias

> **[2026.5.22]** 🌐 Nuestro sitio de documentación oficial está en línea en [**deeptutor.info**](https://deeptutor.info/) — guías, referencias y tours de capacidades, todo en un solo lugar.

> **[2026.4.19]** 🎉 ¡Hemos alcanzado las 20k estrellas en 111 días! Gracias por el increíble apoyo — estamos comprometidos con la iteración continua hacia una tutoría verdaderamente personalizada e inteligente para todos.

> **[2026.4.10]** 📄 ¡Nuestro artículo ya está en arXiv! Lee el [preprint](https://arxiv.org/abs/2604.26962) para conocer más sobre el diseño y las ideas detrás de DeepTutor.

> **[2026.2.6]** 🚀 ¡Hemos alcanzado 10k estrellas en solo 39 días! ¡Un enorme agradecimiento a nuestra increíble comunidad!

> **[2026.1.1]** ¡Feliz Año Nuevo! Únete a nuestro [Discord](https://discord.gg/eRsjPgMU4t), [WeChat](https://github.com/HKUDS/DeepTutor/issues/78) o [Discussions](https://github.com/HKUDS/DeepTutor/discussions) — ¡juntos demos forma al futuro de DeepTutor!

> **[2025.12.29]** ¡DeepTutor está oficialmente lanzado!

## ✨ Características Principales

DeepTutor se organiza en torno a un runtime nativo de agentes: un ChatOrchestrator compartido enruta cada turno a las capacidades, un ToolRegistry expone herramientas de un solo disparo cuando el modelo las necesita, y un CapabilityRegistry permite que flujos de trabajo más profundos tomen el control del turno cuando la tarea necesita estructura.

<div align="center">
<img src="../../assets/figs/system/system%20architecture.png" alt="Arquitectura del sistema DeepTutor" width="900">
</div>

- **Un runtime para todos los modos** — Chat, Quiz, Research, Visualize, Solve y Mastery Path comparten el mismo bucle de agente, el mismo inventario de fuentes y el mismo contexto de sesión.
- **Contexto de aprendizaje conectado** — Bases de conocimiento, libros, borradores de Co-Writer, cuadernos, bancos de preguntas, personas y Memory disponibles en todos los flujos de trabajo en lugar de aplicaciones aisladas.
- **Subagentes y Partners** — consulta Claude Code, Codex o un Partner en vivo desde cualquier turno; ejecuta compañeros IM persistentes que corren el mismo bucle de agente.
- **Conocimiento multi-motor** — bibliotecas RAG con versiones: LlamaIndex, PageIndex, GraphRAG, LightRAG u Obsidian vinculado, cada una intercambiable por base de conocimiento.
- **Herramientas y habilidades extensibles** — herramientas integradas, servidores MCP, modelos de generación de imagen/video/voz, habilidades de EduHub y ClawHub.
- **Memoria inspectable** — trazas L1, resúmenes L2, síntesis L3; Memory Graph traza cada afirmación hasta su evidencia de respaldo y eventos brutos.

---

## 🚀 Comenzar

DeepTutor incluye cuatro rutas de instalación. Todas comparten un diseño de espacio de trabajo: la configuración vive en `data/user/settings/` bajo el directorio desde el que se inicia (o bajo `DEEPTUTOR_HOME` / `deeptutor start --home` si se establece explícitamente). Para la aplicación completa, el flujo recomendado es **elegir un directorio de espacio de trabajo → instalar → `deeptutor init` → `deeptutor start`**.

> ✨ **v1.4.6 está disponible.** `pip install -U deeptutor` obtiene la versión estable más reciente. Las versiones preliminares (cuando estén disponibles) se activan con `pip install --pre -U deeptutor`.

### Opción 1 — Instalar desde PyPI

Aplicación web local completa + CLI, sin necesidad de clonar. Requiere **Python 3.11+** y un runtime **Node.js 20+** en PATH (el servidor standalone Next.js empaquetado es iniciado por `deeptutor start`).

```bash
mkdir -p my-deeptutor && cd my-deeptutor
pip install -U deeptutor
deeptutor init     # solicita puertos + proveedor LLM + embedding opcional
deeptutor start    # inicia backend + frontend; mantener la terminal abierta
```

`deeptutor init` solicita el puerto de backend (predeterminado `8001`), el puerto de frontend (predeterminado `3782`), proveedor LLM / URL base / clave API / modelo y un proveedor de embeddings opcional para Base de Conocimiento / RAG.

Después de `deeptutor start`, abre la URL del frontend impresa en la terminal — por defecto [http://127.0.0.1:3782](http://127.0.0.1:3782). Presiona `Ctrl+C` en esa terminal para detener tanto el backend como el frontend. Omitir `deeptutor init` está bien para una prueba rápida; la aplicación arranca con puertos predeterminados y configuración de modelo vacía, configúralos luego en **Settings → Models**.

### Opción 2 — Instalar desde el Código Fuente

Para desarrollo en un checkout. Usa **Python 3.11+** y **Node.js 22 LTS** para coincidir con CI y Docker.

```bash
git clone https://github.com/HKUDS/DeepTutor.git
cd DeepTutor

# Crear un venv (macOS/Linux). Windows PowerShell:
#   py -3.11 -m venv .venv ; .\.venv\Scripts\Activate.ps1
python3 -m venv .venv && source .venv/bin/activate
python -m pip install --upgrade pip

# Instalar dependencias de backend + frontend
python -m pip install -e .
( cd web && npm ci --legacy-peer-deps )

deeptutor init
deeptutor start
```

Las instalaciones desde fuente ejecutan Next.js en modo de desarrollo contra el directorio `web/` local; todo lo demás (diseño de configuración, puertos, detener con `Ctrl+C`) coincide con la Opción 1.

<details>
<summary><b>Entorno Conda</b> (en lugar de <code>venv</code>)</summary>

```bash
conda create -n deeptutor python=3.11
conda activate deeptutor
python -m pip install --upgrade pip
```

</details>

<details>
<summary><b>Extras de instalación opcionales</b> — dev / partners / matrix / math-animator</summary>

```bash
pip install -e ".[dev]"             # herramientas de pruebas/lint
pip install -e ".[partners]"        # SDKs de canales IM de Partners + cliente MCP
pip install -e ".[matrix]"          # canal Matrix sin E2EE/libolm
pip install -e ".[matrix-e2e]"      # Matrix E2EE; requiere libolm
pip install -e ".[math-animator]"   # complemento Manim; requiere LaTeX/ffmpeg/libs del sistema
```

</details>

<details>
<summary><b>Ajustes de dependencias del frontend y solución de problemas del servidor de desarrollo</b></summary>

**Cambiar dependencias del frontend:** ejecuta `npm install --legacy-peer-deps` para actualizar `web/package-lock.json`, luego confirma tanto `web/package.json` como `web/package-lock.json`.

**Servidor de desarrollo atascado:** si `deeptutor start` informa de un frontend existente que no responde, detén el PID que imprime. Si no hay ningún proceso Next.js en ejecución, los archivos de bloqueo están obsoletos — elimínalos y vuelve a intentarlo:

```bash
rm -f web/.next/dev/lock web/.next/lock
deeptutor start
```

</details>

### Opción 3 — Docker

Un contenedor para la aplicación web completa. Imágenes en GitHub Container Registry:

- `ghcr.io/hkuds/deeptutor:latest` — versión estable
- `ghcr.io/hkuds/deeptutor:pre` — versión preliminar, cuando esté disponible

```bash
docker run --rm --name deeptutor \
  -p 127.0.0.1:3782:3782 \
  -p 127.0.0.1:8001:8001 \
  -v deeptutor-data:/app/data \
  ghcr.io/hkuds/deeptutor:latest
```

> ⚠️ **Mapea tanto `3782` como `8001`.** `3782` sirve la UI web; `8001` es el backend FastAPI al que tu navegador llama directamente — no hay proxy dentro del contenedor. Omitir el mapeo de `8001` y la página carga, pero **Settings** muestra "Backend unreachable" y no se puede usar.

Abre [http://127.0.0.1:3782](http://127.0.0.1:3782). El contenedor crea `/app/data/user/settings/*.json` en el primer arranque; configura los proveedores de modelos desde la página de Settings web. La configuración, las claves API, los registros, los archivos del espacio de trabajo, la memoria y las bases de conocimiento persisten en el volumen `deeptutor-data`.

- **Puertos de host diferentes:** cambia el lado izquierdo de cada mapeo `-p host:container` (ej. `-p 127.0.0.1:8088:3782`). Si cambias los puertos del lado del contenedor en `/app/data/user/settings/system.json`, reinicia y actualiza el lado derecho de cada mapeo para que coincida.
- **Desconectado:** agrega `-d`, luego `docker logs -f deeptutor` para seguir, `docker stop deeptutor` para detener, `docker rm deeptutor` antes de reutilizar el nombre. El volumen `deeptutor-data` mantiene tu configuración y espacio de trabajo entre reinicios.

**Docker remoto / proxy inverso:** la UI web se ejecuta en el navegador, por lo que el navegador necesita una URL de backend a la que pueda llegar. Para servidores remotos, abre **Settings -> Network** o edita `data/user/settings/system.json`:

```json
{
  "next_public_api_base_external": "https://deeptutor.example.com"
}
```

`public_api_base` se acepta como alias de compatibilidad y se normaliza en `next_public_api_base_external` al guardar. CORS usa **orígenes** de frontend, no URLs de API. Con la autenticación deshabilitada, DeepTutor permite los orígenes normales de navegador HTTP/HTTPS por defecto. Con la autenticación habilitada, agrega los orígenes exactos del frontend:

```json
{
  "cors_origins": ["https://deeptutor.example.com"]
}
```

<details>
<summary><b>Conectarse a Ollama / LM Studio / llama.cpp / vLLM / Lemonade en el host</b></summary>

Dentro de Docker, `localhost` es el propio contenedor, no tu máquina host. Para llegar a un servicio de modelo que se ejecuta en el host, usa la puerta de enlace del host (recomendado):

```bash
docker run --rm --name deeptutor \
  -p 127.0.0.1:3782:3782 -p 127.0.0.1:8001:8001 \
  --add-host=host.docker.internal:host-gateway \
  -v deeptutor-data:/app/data \
  ghcr.io/hkuds/deeptutor:latest
```

Luego en **Settings → Models**, apunta la URL Base del proveedor a `host.docker.internal`:

- Ollama LLM: `http://host.docker.internal:11434/v1`
- Ollama embedding: `http://host.docker.internal:11434/api/embed`
- LM Studio: `http://host.docker.internal:1234/v1`
- llama.cpp: `http://host.docker.internal:8080/v1`
- Lemonade: `http://host.docker.internal:13305/api/v1`

Docker Desktop (macOS/Windows) generalmente resuelve `host.docker.internal` sin `--add-host`. En Linux, el flag es la forma portátil de crear ese nombre de host en Docker Engine moderno.

**Alternativa para Linux — red del host:** agrega `--network=host` y elimina los flags `-p`. El contenedor comparte la red del host directamente, así que abre [http://127.0.0.1:3782](http://127.0.0.1:3782) (o el `frontend_port` en `system.json`), y los servicios del host se pueden alcanzar con URLs de localhost normales como `http://127.0.0.1:11434/v1`. Nota que la red del host expone los puertos del contenedor directamente en el host y puede entrar en conflicto con servicios existentes.

</details>

### Sandbox de Ejecución de Código (skills de oficina)

Las skills de oficina integradas — **docx / pdf / pptx / xlsx** — funcionan haciendo que el modelo escriba un script Python corto (`python-docx`, `reportlab`, `openpyxl`, …), lo ejecute a través de las herramientas `exec` / `code_execution` y devuelva una URL de descarga. Esas herramientas se montan siempre que un backend de sandbox esté activo, lo cual ocurre **por defecto** en cada forma de despliegue:

- **Local (Opción 1 / 2) y Docker (Opción 3, contenedor único):** un sandbox de subproceso restringido ejecuta el código del modelo (localmente en el host, o dentro del contenedor bajo Docker — el contenedor siendo su propio límite de aislamiento).
- **docker-compose:** enrutado en su lugar a un **sidecar runner** endurecido y con privilegios mínimos (`Dockerfile.runner`) a través de `DEEPTUTOR_SANDBOX_RUNNER_URL` — la postura más sólida, y preferida automáticamente cuando está presente.

El sandbox de subproceso está controlado por la configuración `sandbox_allow_subprocess` en `data/user/settings/system.json` (predeterminado `true`). Ejecutar código generado por el modelo en tu host es una decisión real de confianza — establécelo en `false` (o exporta `DEEPTUTOR_SANDBOX_ALLOW_SUBPROCESS=0`) para deshabilitar la ejecución del lado del host, a costa de que las skills de oficina ya no puedan producir archivos.

### Opción 4 — Solo CLI

Cuando no necesitas la UI web. El paquete de solo CLI se instala desde un checkout de fuente, no desde PyPI.

```bash
git clone https://github.com/HKUDS/DeepTutor.git
cd DeepTutor

# Crear un venv (macOS/Linux). Windows PowerShell:
#   py -3.11 -m venv .venv-cli ; .\.venv-cli\Scripts\Activate.ps1
python3 -m venv .venv-cli && source .venv-cli/bin/activate
python -m pip install --upgrade pip

python -m pip install -e ./packaging/deeptutor-cli
deeptutor init --cli
deeptutor chat
```

`deeptutor init --cli` comparte el mismo diseño `data/user/settings/` que la aplicación completa pero omite las solicitudes de puertos de backend/frontend y establece embeddings en **desactivado** (elige `Yes` si planeas usar `deeptutor kb …` o herramientas RAG). Aún escribe un diseño de runtime completo (`system.json`, `auth.json`, `integrations.json`, `model_catalog.json`, `main.yaml`, `agents.yaml`) y aún solicita el proveedor LLM y modelo activos.

<details>
<summary><b>Comandos comunes</b></summary>

```bash
deeptutor chat                                          # REPL interactivo
deeptutor chat --capability deep_solve --tool rag --kb my-kb
deeptutor run chat "Explain Fourier transform"
deeptutor run deep_solve "Solve x^2 = 4" --tool rag --kb my-kb
deeptutor kb create my-kb --doc textbook.pdf
deeptutor memory show
deeptutor config show
```

</details>

La instalación local de `deeptutor-cli` no incluye activos web ni dependencias de servidor. Mantén el checkout de fuente cerca — la instalación editable apunta a él. Para agregar la aplicación web más tarde, instala el paquete PyPI (Opción 1) y ejecuta `deeptutor init` + `deeptutor start` desde el mismo espacio de trabajo.

### Referencia de Configuración

<details>
<summary><b>Archivos de configuración bajo <code>data/user/settings/</code></b> — referencia JSON/YAML</summary>

Todo bajo `data/user/settings/` es JSON/YAML plano. La página **Settings** en el navegador es el editor recomendado.

| Archivo | Propósito |
|:---|:---|
| `model_catalog.json` | Perfiles de proveedores LLM, embeddings y búsqueda; claves API; modelos activos |
| `system.json` | Puertos de backend/frontend, base de API pública, CORS, verificación SSL, directorio de adjuntos |
| `auth.json` | Interruptor de autenticación opcional, nombre de usuario, hash de contraseña, configuración de token/cookie |
| `integrations.json` | Configuración opcional de PocketBase e integraciones sidecar |
| `interface.json` | Preferencias de idioma / tema / barra lateral de UI |
| `main.yaml` | Valores predeterminados de comportamiento de runtime e inyección de rutas |
| `agents.yaml` | Configuración de temperatura y tokens de capacidades/herramientas |

El `.env` de la raíz del proyecto **no** se lee como archivo de configuración de la aplicación. Para una configuración mínima del modelo, abre **Settings → Models**, agrega un perfil LLM (URL Base / clave API / nombre del modelo) y guarda. Agrega un perfil de embeddings solo si planeas usar funciones de Base de Conocimiento / RAG.

</details>

---

## 📖 Explorar DeepTutor

El tour del README sigue las superficies del producto en el orden en que las encontrarás con más frecuencia: Chat, Partner, Mis Agentes, Co-Writer, Book, Centro de Conocimiento, Espacio de Aprendizaje, Memory y Settings.

<div align="center">
<img src="../../assets/figs/web-1.4.6+/OVERVIEW.png" alt="Visión general de DeepTutor" width="900">
</div>

### 💬 Chat

<div align="center">
<img src="../../assets/figs/web-1.4.6+/home/00-overview.png" alt="Espacio de trabajo de chat DeepTutor" width="900">
</div>

Chat es la capacidad predeterminada y el lugar donde comienza la mayor parte del trabajo. Un único hilo puede conversar normalmente, llamar herramientas, fundamentarse en bases de conocimiento seleccionadas, leer adjuntos, escribir registros de notebook y continuar con el mismo inventario de fuentes entre turnos.

<div align="center">
<img src="../../assets/figs/system/chat-agent-loop.png" alt="Bucle de agente de chat DeepTutor" width="900">
</div>

El bucle actual es deliberadamente simple: el modelo piensa en rondas, llama herramientas cuando es útil, observa los resultados de las herramientas y termina cuando tiene suficiente evidencia. La herramienta `ask_user` pausa el turno para pedir aclaraciones al usuario antes de continuar.

**Herramientas que el usuario puede activar:** `brainstorm`, `web_search`, `paper_search`, `reason`, `geogebra_analysis`, `imagegen`, `videogen`.

**Contexto persistente (barra de herramientas):** subagente activo, bases de conocimiento, persona, modelo, voz.

**Referencias de un solo uso (menú +):** archivos, historial de chat, libros, cuadernos, banco de preguntas, agentes importados.

Chat también es el punto de lanzamiento para capacidades más profundas: `deep_solve` para razonamiento trabajado, `deep_question` para generación de preguntas, `deep_research` para informes con citas, `visualize` y `math_animator` para salidas visuales, `auto` para enrutamiento y `mastery_path` para flujos de planes de aprendizaje.

### 🤝 Partner

<div align="center">
<img src="../../assets/figs/web-1.4.6+/partners/00-partners%20overview.png" alt="Vista general de partners DeepTutor" width="900">
</div>

Los Partners son compañeros persistentes que se ejecutan directamente en el mismo bucle de agente de chat — no hay un motor de bot separado que mantener sincronizado. Cada mensaje web o IM entrante se convierte en un turno normal de ChatOrchestrator dentro de un espacio de trabajo con alcance de partner.

<div align="center">
<img src="../../assets/figs/system/partners-architecture.png" alt="Arquitectura de partners DeepTutor" width="900">
</div>

Cada partner tiene un `SOUL.md`, selección de modelo, canales, política de herramientas y biblioteca asignada. Las bases de conocimiento, skills y notebooks se copian en `data/partners/<id>/workspace/`, por lo que las mismas herramientas de RAG, skill, notebook y memoria funcionan sin casos especiales. Un Partner lee la memoria del propietario pero solo escribe en su propio espacio de memoria.

<div align="center">
<img src="../../assets/figs/web-1.4.6+/partners/02-IM%20config%20for%20each%20partner.png" alt="Configuración de canales IM de partners" width="900">
</div>

La capa de canales está impulsada por esquema y puede conectarse a: Feishu, Telegram, Slack, DingTalk, QQ/NapCat, WeCom, WhatsApp, Zulip, Matrix y Microsoft Teams. Los Partners también pueden conectarse como subagentes y ser consultados directamente desde cualquier turno de chat.

### 🧑‍🚀 Mis Agentes

<div align="center">
<img src="../../assets/figs/web-1.4.6+/myagents/00-overview.png" alt="Vista general de Mis Agentes" width="900">
</div>

Mis Agentes reúne dos capacidades: conectar un agente en vivo (Claude Code, Codex o un Partner) para consultas en tiempo real, e importar conversaciones pasadas de agentes para contexto de referencia.

<div align="center">
<img src="../../assets/figs/web-1.4.6+/home/08-subagent%20demo%20with%20claude%20code.png" alt="Demo de subagente con Claude Code" width="900">
</div>

Una vez conectado, la herramienta `consult_subagent` permite consultar al agente desde cualquier turno de chat. El agente también aparece como un chip en la barra de herramientas o se puede mencionar con `@`. Para conversaciones importadas, selecciona una carpeta de historial de Claude Code o Codex, elige cuántos días importar y DeepTutor las convierte en sesiones consultables con actualización por demanda.

### ✍️ Co-Writer

<div align="center">
<img src="../../assets/figs/web-1.4.6+/co-writer/00-overview.png" alt="Vista general de Co-Writer" width="900">
</div>

<div align="center">
<img src="../../assets/figs/web-1.4.6+/co-writer/01-edit%20panel.png" alt="Panel de edición de Co-Writer" width="900">
</div>

Co-Writer es un espacio de trabajo Markdown de vista dividida para informes, tutoriales, notas y artefactos de aprendizaje de formato largo. Los documentos se guardan automáticamente y renderizan una vista previa en vivo.

Selecciona texto y pide a DeepTutor que lo reescriba, expanda o acorte — cada edición se muestra como un diff de aceptar/rechazar. El agente de edición puede fundamentar una revisión en una base de conocimiento o evidencia web, por lo que Co-Writer se comporta más como un editor con recuperación que como un cuadro de texto desconectado. Los borradores terminados se pueden guardar de vuelta en notebooks como contexto reutilizable.

### 📖 Book (Libro)

<div align="center">
<img src="../../assets/figs/web-1.4.6+/book/00-book_overview.png" alt="Vista general de Book" width="900">
</div>

<p align="center">
<img src="../../assets/figs/web-1.4.6+/book/01-book-demo-quiz%20card.png" alt="Tarjeta de quiz en Book" width="31%">
&nbsp;
<img src="../../assets/figs/web-1.4.6+/book/02-book-demo-manim%20video.png" alt="Video Manim en Book" width="31%">
&nbsp;
<img src="../../assets/figs/web-1.4.6+/book/03-book-demo%20interactive%20module.png" alt="Módulo interactivo en Book" width="31%">
</p>

Book convierte las fuentes seleccionadas en un libro vivo interactivo. El contenido se compila en bloques tipados: texto, secciones, callouts, quizzes, tarjetas flash, líneas de tiempo, código, figuras, HTML interactivo, animaciones, gráficos de conceptos y notas de usuario. Cada página tiene un Page Chat propio para discutir el contenido de esa sección en contexto.

### 📚 Centro de Conocimiento

<div align="center">
<img src="../../assets/figs/web-1.4.6+/knowledge/00-overview.png" alt="Vista general del Centro de Conocimiento" width="900">
</div>

<div align="center">
<img src="../../assets/figs/web-1.4.6+/knowledge/01-create%20knowledge%20base.png" alt="Crear base de conocimiento" width="900">
</div>

El Centro de Conocimiento es la consola para las bibliotecas RAG. Soporta cinco motores: **LlamaIndex**, **PageIndex**, **GraphRAG**, **LightRAG** y **Obsidian**. Puedes crear una nueva base de conocimiento desde documentos o vincular una ya existente como puntero de solo lectura (incluyendo vaults de Obsidian).

El análisis de documentos soporta cuatro modos: Text-only, MinerU (extracción avanzada de PDF), Docling y markitdown. El espacio de trabajo web expone archivos, carga, versiones de índice y configuración de motor por KB. La CLI refleja el mismo ciclo de vida con `deeptutor kb list`, `info`, `create`, `add`, `search`, `set-default` y `delete`.

### 🌐 Espacio de Aprendizaje

<div align="center">
<img src="../../assets/figs/web-1.4.6+/learning-space/00-overview.png" alt="Vista general del Espacio de Aprendizaje" width="900">
</div>

El Espacio de Aprendizaje es el dashboard central para gestionar materiales de aprendizaje y personalización. Reúne:

**Conversaciones y materiales:** historial de chat, cuadernos, banco de preguntas.

**Personalización:** rutas de dominio (Mastery Path), personas, habilidades.

<div align="center">
<img src="../../assets/figs/web-1.4.6+/learning-space/07-%20download%20skills%20from%20eduhub.png" alt="Importar habilidades desde EduHub" width="900">
</div>

Las habilidades se pueden instalar directamente desde EduHub con un clic — navega el catálogo, previsualiza y descarga al espacio de trabajo local. Las Personas siguen el mismo patrón para el rol y la voz del agente. Estos activos se pueden asignar a Partners, referenciar en chat y reutilizar en flujos de trabajo de aprendizaje.

### 🧠 Memory (Memoria)

<div align="center">
<img src="../../assets/figs/web-1.4.6+/memory/00-overview.png" alt="Vista general de Memory" width="900">
</div>

Memory es un sistema de tres capas arraigado en el espacio de trabajo del usuario activo y respaldado por archivos planos:

- **L1** — trazas de eventos brutas por sesión (`trace/<surface>/<date>.jsonl`)
- **L2** — hechos consolidados por superficie (`L2/<surface>.md`)
- **L3** — síntesis entre superficies (`L3/<recent|profile|scope|preferences>.md`)

<div align="center">
<img src="../../assets/figs/web-1.4.6+/memory/01-3%20layer%20memory%20graph.png" alt="Gráfico de memoria de 3 capas" width="900">
</div>

El Memory Graph permite rastrear cada afirmación sintetizada hasta sus hechos de respaldo y eventos brutos, haciendo que la personalización sea inspeccionable en lugar de estar oculta detrás de una caja negra. El banco de trabajo permite inspeccionar, editar y ejecutar consolidación manual.

### ⚙️ Configuración

<div align="center">
<img src="../../assets/figs/web-1.4.6+/settings/00-setting%20overview.png" alt="Vista general de configuración" width="900">
</div>

<div align="center">
<img src="../../assets/figs/web-1.4.6+/settings/01-appearance%20settings.png" alt="Configuración de apariencia" width="900">
</div>

Settings es el panel de control operativo. Tarjetas disponibles: **Apariencia** (4 temas: Default, Cream, Dark, Glass), **Red** (puertos, base de API externa, CORS), **Modelos** (catálogos LLM/embeddings/búsqueda), **KB** (análisis de documentos, MinerU), **Chat** (herramientas, capacidades, servidores MCP), **Partners & Agents** (configuración de canales), **Memory** (cadencia de consolidación, presupuestos).

La mayoría de las configuraciones usan un flujo de borrador y aplicación para que los usuarios puedan probar los proveedores antes de confirmarlos.

---

## ⌨️ DeepTutor CLI — Interfaz Nativa de Agentes

DeepTutor es nativo de CLI: el mismo punto de entrada `deeptutor` puede inicializar un espacio de trabajo, iniciar la aplicación web, ejecutar una capacidad de un solo disparo, abrir un REPL interactivo, gestionar bases de conocimiento, inspeccionar sesiones, mantener libros y operar partners.

```bash
deeptutor run chat "Explain Fourier transform" --tool rag --kb textbook
deeptutor run deep_solve "Solve x^2 = 4" --tool reason
deeptutor chat --capability deep_research --kb papers
deeptutor partner create math-tutor --soul "Socratic math tutor"
deeptutor kb create calculus --doc textbook.pdf
```

<details>
<summary><b>Referencia de comandos</b></summary>

| Comando | Descripción |
|:---|:---|
| `deeptutor init` | Crear o actualizar `data/user/settings` para el espacio de trabajo actual |
| `deeptutor start [--home PATH]` | Lanzar backend + frontend juntos |
| `deeptutor serve [--port PORT]` | Iniciar solo el backend FastAPI |
| `deeptutor run <capability> <message>` | Ejecutar un turno de capacidad único (`chat`, `deep_solve`, `deep_question`, `deep_research`, `visualize`, `math_animator`, `auto`, `mastery_path`) |
| `deeptutor chat` | REPL interactivo con controles de capacidad, herramienta, KB, notebook e historial |
| `deeptutor partner list/create/start/stop` | Gestionar partners conectados por IM |
| `deeptutor kb list/info/create/add/search/set-default/delete` | Gestionar bases de conocimiento |
| `deeptutor memory show/clear` | Inspeccionar documentos de memoria L2/L3 o borrar memoria L1/toda |
| `deeptutor session list/show/open/rename/delete` | Gestionar sesiones compartidas |
| `deeptutor notebook list/create/show/add-md/replace-md/remove-record` | Gestionar notebooks desde archivos Markdown |
| `deeptutor book list/health/refresh-fingerprints` | Inspeccionar libros y actualizar huellas dactilares de fuentes |
| `deeptutor skill search/install/list/remove/login/publish/update` | Gestionar habilidades, instalar desde hubs y publicar las propias (`eduhub:<slug>` por defecto) |
| `deeptutor plugin list/info` | Inspeccionar herramientas y capacidades registradas |
| `deeptutor config show` | Imprimir resumen de configuración |
| `deeptutor provider login <provider>` | Gestionar inicio de sesión OAuth del proveedor donde sea compatible |

</details>

La distribución de solo CLI está en `packaging/deeptutor-cli`; en este checkout debe instalarse desde fuente con `python -m pip install -e ./packaging/deeptutor-cli`. El paquete público `deeptutor-cli` no está actualmente disponible en PyPI, por lo que la sección principal de Comenzar mantiene la ruta de instalación desde fuente.

---

## 👥 Multi-Usuario — Despliegues Compartidos

La autenticación es opcional y está desactivada por defecto. Cuando se habilita, DeepTutor se convierte en un despliegue compartido con un espacio de trabajo de administrador, espacios de trabajo por usuario, espacios de trabajo de partners y estado del sistema bajo un árbol `data/`.

```text
data/
├── user/                         # Espacio de trabajo y configuración del administrador
├── users/<uid>/                  # Alcance del usuario no administrador
│   ├── user/chat_history.db
│   ├── user/settings/interface.json
│   ├── user/workspace/{chat,co-writer,book,memory,notebook,...}
│   └── knowledge_bases/...
├── partners/<id>/workspace/      # Alcance del usuario sintético del partner
└── system/
    ├── auth/users.json
    ├── grants/<uid>.json
    └── audit/usage.jsonl
```

El primer usuario registrado se convierte en administrador y puede configurar catálogos de modelos, credenciales de proveedores, bases de conocimiento, skills y permisos de usuario. Los usuarios no administradores obtienen historial de chat aislado, memoria, notebooks, bases de conocimiento personales y una página de Settings redactada.

Para una prueba local, establece `data/user/settings/auth.json` para habilitar la autenticación, reinicia `deeptutor start`, registra al primer administrador en `/register`, luego crea usuarios desde `/admin/users` y asigna modelos, KBs, skills, política de herramientas, política MCP y acceso de ejecución de código a través de permisos.

---

## 🧩 Ecosistema — EduHub y la Comunidad de Skills

DeepTutor incluye [EduHub](https://eduhub.deeptutor.info) (`eduhub.deeptutor.info`) como hub de habilidades predeterminado — un repositorio educativo donde la comunidad publica, versiona e instala skills.

<details>
<summary><b>EduHub — el ecosistema de habilidades de DeepTutor</b></summary>

EduHub es el hub educativo oficial de DeepTutor. Las habilidades publicadas aparecen en el catálogo y se pueden instalar directamente desde el Espacio de Aprendizaje → Habilidades → Importar desde EduHub, o desde la CLI:

```bash
deeptutor skill search "calculus"
deeptutor skill install eduhub:calculus-solver
deeptutor skill list
deeptutor skill login          # autenticación para publicar
deeptutor skill publish        # publicar en EduHub
deeptutor skill update         # listar las propias y actualizar versiones
```

También puedes instalar usando el CLI propio de EduHub:

```bash
npx eduhub install calculus-solver
```

</details>

<details>
<summary><b>La puerta de seguridad de importación</b></summary>

Cada skill pasa por una puerta de seguridad antes de instalarse:

- **Veredicto de seguridad** — análisis estático del contenido de la habilidad antes de la instalación.
- **Protección zip-slip** — los archivos zip se inspeccionan para prevenir traversal de rutas.
- **Lista blanca de sufijos** — solo se aceptan tipos de archivo declarados explícitamente.
- **`always:` eliminado** — las entradas `always:` en skills de terceros se ignoran para evitar montaje forzado de herramientas.
- **`.hub-lock.json`** — archivo de bloqueo que registra el origen exacto y el hash de cada skill instalada.

</details>

<details>
<summary><b>También compatible con ClawHub</b></summary>

DeepTutor también es compatible con [ClawHub](https://github.com/OpenClaw/clawhub) como hub alternativo:

```bash
deeptutor skill install --hub clawhub my-skill
```

O configura el hub predeterminado en `skill_hubs.json` bajo el directorio de configuración.

</details>

---

## 🤝 Comunidad

**Contacto:** Bingxi Zhao · [HKUDS Group](https://github.com/HKUDS) · bingxizhao39@gmail.com

**Agradecimientos:** Chao Huang, Jiahao Zhang, Zirui Guo, Xubin Ren — por sus contribuciones fundamentales al diseño y la implementación de DeepTutor.

DeepTutor se apoya en proyectos de código abierto excepcionales:

| Proyecto | Rol en DeepTutor |
|:---|:---|
| [**LlamaIndex**](https://github.com/run-llama/llama_index) | Columna vertebral del pipeline RAG y la indexación de documentos |
| [**nanobot**](https://github.com/HKUDS/nanobot) | Motor de agente ultraligero que impulsó el TutorBot original |
| [**LightRAG**](https://github.com/HKUDS/LightRAG) | Motor KB de grafo RAG simple y rápido |
| [**AutoAgent**](https://github.com/HKUDS/AutoAgent) | Marco de agentes sin código del ecosistema HKUDS |
| [**AI-Researcher**](https://github.com/HKUDS/AI-Researcher) | Investigación automatizada del ecosistema HKUDS |
| [**OpenClaw**](https://github.com/OpenClaw/clawhub) | Infraestructura ClawHub para distribución de skills |
| [**Codex**](https://github.com/openai/codex) | Agente de codificación en CLI compatible como subagente |
| [**Claude Code**](https://github.com/anthropics/claude-code) | Agente de codificación en CLI compatible como subagente |
| [**ManimCat**](https://github.com/Wing900/ManimCat) | Generación de animaciones matemáticas impulsada por IA |

**Del ecosistema HKUDS:**

| [⚡ LightRAG](https://github.com/HKUDS/LightRAG) | [🤖 AutoAgent](https://github.com/HKUDS/AutoAgent) | [🔬 AI-Researcher](https://github.com/HKUDS/AI-Researcher) | [🧬 nanobot](https://github.com/HKUDS/nanobot) |
|:---:|:---:|:---:|:---:|
| RAG Simple y Rápido | Marco de Agentes Sin Código | Investigación Automatizada | Agente IA Ultraligero |

Vota en los elementos del roadmap o propone nuevos en [issue #498](https://github.com/HKUDS/DeepTutor/issues/498). Consulta [CONTRIBUTING.md](../../CONTRIBUTING.md) para obtener pautas sobre cómo configurar tu entorno de desarrollo, estándares de código y flujo de trabajo de pull requests.

<div align="center">

Esperamos que DeepTutor se convierta en un regalo para la comunidad. 🎁

<a href="https://github.com/HKUDS/DeepTutor/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=HKUDS/DeepTutor&max=999" alt="Contribuidores" />
</a>

</div>

## ⭐ Historial de Estrellas

<div align="center">

<a href="https://www.star-history.com/#HKUDS/DeepTutor&type=timeline&legend=top-left">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=HKUDS/DeepTutor&type=timeline&theme=dark&legend=top-left" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=HKUDS/DeepTutor&type=timeline&legend=top-left" />
    <img alt="Gráfico de historial de estrellas" src="https://api.star-history.com/svg?repos=HKUDS/DeepTutor&type=timeline&legend=top-left" />
  </picture>
</a>

</div>

<p align="center">
 <a href="https://www.star-history.com/hkuds/deeptutor">
  <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/badge?repo=HKUDS/DeepTutor&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/badge?repo=HKUDS/DeepTutor" />
   <img alt="Clasificación del historial de estrellas" src="https://api.star-history.com/badge?repo=HKUDS/DeepTutor" />
  </picture>
 </a>
</p>

<div align="center">

**[Data Intelligence Lab @ HKU](https://github.com/HKUDS)**

[⭐ Danos una estrella](https://github.com/HKUDS/DeepTutor/stargazers) · [🐛 Reportar un error](https://github.com/HKUDS/DeepTutor/issues) · [💬 Discusiones](https://github.com/HKUDS/DeepTutor/discussions)

---

Licenciado bajo [Apache License 2.0](../../LICENSE).

<p>
  <img src="https://visitor-badge.laobi.icu/badge?page_id=HKUDS.DeepTutor&style=for-the-badge&color=00d4ff" alt="Vistas">
</p>

</div>
