<div align="center">

<p align="center"><img src="../../assets/figs/logo/logo.png" alt="DeepTutor logo" height="56" style="vertical-align: middle;">&nbsp;<img src="../../assets/figs/logo/banner.png" alt="DeepTutor" height="48" style="vertical-align: middle;"></p>

# DeepTutor: Tutoria Personalizada Nativa de Agentes

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
  <a href="README_PT.md"><img alt="Português" height="40" src="https://img.shields.io/badge/Português-BCDCF7"></a>&nbsp;
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

[Recursos](#-recursos-principais) · [Começar](#-começar) · [Explorar](#-explorar-o-deeptutor) · [CLI](#️-deeptutor-cli--interface-nativa-de-agentes) · [Ecossistema](#-ecossistema--eduhub-e-a-comunidade-de-skills) · [Comunidade](#-comunidade)

</div>

---

> 🤝 **Damos as boas-vindas a todo tipo de contribuições!** Vote em itens do roadmap ou proponha novos em [`Roadmap`](https://github.com/HKUDS/DeepTutor/issues/498), e consulte o nosso [Guia de Contribuição](../../CONTRIBUTING.md) para a estratégia de branches, padrões de código e como começar.

### 📦 Lançamentos

> **[2026.6.17]** [v1.4.6](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.6) — Space torna-se painel de aprendizado com **Meus Agentes** importáveis e Memory de nível superior; **Centro de Conhecimento** adiciona motores GraphRAG / PageIndex / LightRAG mais KB vinculadas e suporte Obsidian; Configurações abre análise de documentos / voz / imagem+vídeo; capacidades LLM controladas por modelo atribuído.

> **[2026.6.14]** [v1.4.5](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.5) — Aprendizado Guiado reconstruído no loop de chat do agente com portões de domínio rígidos por tipo e painel `/learning`; novo framework de loop-plugin extensível; exportação Markdown / guardar-em-notebook para conversas de Partners.

> **[2026.6.13]** [v1.4.4](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.4) — Instalar habilidades da comunidade do [ClawHub](https://clawhub.ai/) com `deeptutor skill install` atrás de uma porta de segurança; visualizações DOCX/XLSX reais no navegador para ficheiros de base de conhecimento.

> **[2026.6.12]** [v1.4.3](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.3) — TutorBot torna-se **Partners** numa pipeline IM de nível produção com respostas em streaming em tempo real e 15 canais, Chat passa para um único loop de agente, isolamento real por utilizador para implementações multi-utilizador, Visualize reconstruído com validação+reparação local, além de melhorias no Co-writer, visualizador de ficheiros, análise MinerU na nuvem e na CLI. Documentação completamente atualizada em [deeptutor.info](https://deeptutor.info/).

<details>
<summary><b>Lançamentos anteriores (mais de 2 semanas)</b></summary>

> **[2026.5.28]** [v1.4.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.2) — Estabilidade + polimento em v1.4.1: Gemini 2.5+ desbloqueado no Visualize e Chat, correção de roteamento de autenticação ContextVar (#485), protocolo de etiquetas de raciocínio + ferramentas nativas reforçado, UX de streaming suave em todas as superfícies de chat, nova barra lateral de Recentes recolhível e suporte ao provedor local Lemonade.

> **[2026.5.27]** [v1.4.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.1) — Correção de segurança + estabilidade: sandbox de ferramentas TutorBot bloqueado, isolamento de recursos por utilizador, fallback de imagem multimodal para provedores com capacidade de visão, uma API HTTP/SSE para comunicar com um TutorBot e correção de regressão de chat do v1.4.0.

> **[2026.5.22]** [v1.4.0](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.0) — Corte GA do v1.4: Modo Auto, Memória de três camadas, Deep Research / Solve / Question agênticos, refatoração de RAG com LlamaIndex, fusão Visualize/Animator, normalização de esforço de raciocínio, fallback de esquema de ferramentas e runtime de turno seguro contra reinicializações.

> **[2026.5.21]** [v1.4.0-beta](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.0-beta) — Bancada de trabalho de Memória de três camadas (L1/L2/L3), todas as capacidades de chat reconstruídas sobre um único motor agêntico, RAG exclusivo de LlamaIndex e uma superfície unificada de Settings + Capabilities.

> **[2026.5.10]** [v1.3.10](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.10) — Recuperação de CORS do Docker remoto, `DISABLE_SSL_VERIFY` para provedores SDK, citações de blocos de código mais seguras e add-on Matrix E2EE opcional.

> **[2026.5.9]** [v1.3.9](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.9) — Suporte Zulip e NVIDIA NIM para TutorBot, roteamento de modelo de pensamento mais seguro, `deeptutor start`, dicas de barra lateral e paridade de armazenamento de sessões.

> **[2026.5.8]** [v1.3.8](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.8) — Implementações multi-utilizador opcionais com espaços de trabalho de utilizador isolados, concessões de administrador, rotas de autenticação e acesso de runtime com escopo.

> **[2026.5.4]** [v1.3.7](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.7) — Correções de modelo de pensamento/provedor, histórico de índice de Knowledge visível e edição mais segura de templates/limpeza do Co-Writer.

> **[2026.5.3]** [v1.3.6](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.6) — Seleção de modelos baseada em catálogo para chat e TutorBot, reindexação de RAG mais segura, correções de limite de tokens do OpenAI Responses e validação do editor de Skills.

> **[2026.5.2]** [v1.3.5](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.5) — Configurações de lançamento local mais suaves, consultas RAG mais seguras, autenticação de embeddings local mais clara e polimento do modo escuro de Settings.

> **[2026.5.1]** [v1.3.4](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.4) — Persistência de chat em páginas do Book e fluxos de reconstrução, referências de chat para Book, tratamento mais robusto de idioma/raciocínio, extração de documentos RAG reforçada.

> **[2026.4.30]** [v1.3.3](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.3) — Suporte de embeddings NVIDIA NIM + Gemini, contexto Space unificado para histórico de chat/skills/memória, instantâneos de sessão, resiliência de reindexação RAG.

> **[2026.4.29]** [v1.3.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.2) — URLs de endpoints de embeddings transparentes, resiliência de reindexação RAG para vetores persistidos inválidos, limpeza de memória para saída de modelo de pensamento, correção de runtime do Deep Solve.

> **[2026.4.28]** [v1.3.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.1) — Estabilidade: roteamento RAG e validação de embeddings mais seguros, persistência do Docker, entrada segura para IME, robustez no Windows/GBK.

> **[2026.4.27]** [v1.3.0](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.0) — Índices KB versionados com fluxo de trabalho de reindexação, espaço de trabalho Knowledge reconstruído, autodescoberta de embeddings com novos adaptadores, hub Space.

> **[2026.4.25]** [v1.2.5](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.5) — Anexos de chat persistentes com gaveta de pré-visualização de ficheiros, pipelines de capacidades com consciência de anexos, exportação Markdown do TutorBot.

> **[2026.4.25]** [v1.2.4](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.4) — Anexos de texto/código/SVG, Setup Tour de um comando, exportação Markdown de chat, UI de gestão KB compacta.

> **[2026.4.24]** [v1.2.3](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.3) — Anexos de documentos (PDF/DOCX/XLSX/PPTX), exibição de blocos de pensamento de raciocínio, editor de templates Soul, guardar Co-Writer no notebook.

> **[2026.4.22]** [v1.2.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.2) — Sistema de Skills criado por utilizadores, revisão do desempenho de entrada de chat, início automático do TutorBot, UI da Book Library, visualização em ecrã inteiro.

> **[2026.4.21]** [v1.2.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.1) — Limites de tokens por etapa, regeneração de resposta em todos os pontos de entrada, correções de compatibilidade de RAG e Gemma.

> **[2026.4.20]** [v1.2.0](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.0) — Compilador de "livro vivo" Book Engine, Co-Writer multi-documento, visualizações HTML interativas, @-menção do Question Bank.

> **[2026.4.18]** [v1.1.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.1.2) — Separador Channels orientado por esquema, consolidação de pipeline único RAG, prompts de chat externalizados.

> **[2026.4.17]** [v1.1.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.1.1) — "Responder agora" universal, sincronização de rolagem do Co-Writer, painel de configurações unificado, botão Stop de streaming.

> **[2026.4.15]** [v1.1.0](https://github.com/HKUDS/DeepTutor/releases/tag/v1.1.0) — Revisão de matemática de bloco LaTeX, sonda de diagnóstico LLM, orientação de Docker + LLM local.

> **[2026.4.14]** [v1.1.0-beta](https://github.com/HKUDS/DeepTutor/releases/tag/v1.1.0-beta) — Sessões marcáveis, tema Snow, heartbeat WebSocket e reconexão automática, revisão do registo de embeddings.

> **[2026.4.13]** [v1.0.3](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.3) — Question Notebook com marcadores e categorias, Mermaid no Visualize, deteção de incompatibilidade de embeddings, compatibilidade Qwen/vLLM, suporte LM Studio e llama.cpp, tema Glass.

> **[2026.4.11]** [v1.0.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.2) — Consolidação de pesquisa com fallback SearXNG, correção de troca de provedor, correções de fugas de recursos do frontend.

> **[2026.4.10]** [v1.0.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.1) — Capacidade Visualize (Chart.js/SVG), prevenção de duplicados em quizzes, suporte do modelo o4-mini.

> **[2026.4.10]** [v1.0.0-beta.4](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.0-beta.4) — Rastreamento do progresso de embeddings com retry de limite de taxa, correções de dependências multiplataforma, correção de validação MIME.

> **[2026.4.8]** [v1.0.0-beta.3](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.0-beta.3) — SDK nativo OpenAI/Anthropic (remover litellm), suporte de Math Animator no Windows, análise JSON robusta e i18n completo em chinês.

> **[2026.4.7]** [v1.0.0-beta.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.0-beta.2) — Recarga a quente de configurações, saída aninhada MinerU, correção de WebSocket e mínimo Python 3.11+.

> **[2026.4.4]** [v1.0.0-beta.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.0-beta.1) — Reescrita de arquitetura nativa de agentes (~200k linhas): modelo de plugins Tools + Capabilities, CLI e SDK, TutorBot, Co-Writer, Guided Learning e memória persistente.

> **[2026.1.23]** [v0.6.0](https://github.com/HKUDS/DeepTutor/releases/tag/v0.6.0) — Persistência de sessões, carregamento incremental de documentos, importação flexível de pipeline RAG e localização completa para chinês.

> **[2026.1.18]** [v0.5.2](https://github.com/HKUDS/DeepTutor/releases/tag/v0.5.2) — Suporte de Docling para RAG-Anything, otimização do sistema de logs e correções de erros.

> **[2026.1.15]** [v0.5.0](https://github.com/HKUDS/DeepTutor/releases/tag/v0.5.0) — Configuração de serviço unificada, seleção de pipeline RAG por base de conhecimento, revisão de geração de perguntas e personalização da barra lateral.

> **[2026.1.9]** [v0.4.0](https://github.com/HKUDS/DeepTutor/releases/tag/v0.4.0) — Suporte de LLM e embeddings multi-provedor, nova página inicial, desacoplamento do módulo RAG e refatoração de variáveis de ambiente.

> **[2026.1.5]** [v0.3.0](https://github.com/HKUDS/DeepTutor/releases/tag/v0.3.0) — Arquitetura PromptManager unificada, GitHub Actions CI/CD e imagens Docker pré-construídas no GHCR.

> **[2026.1.2]** [v0.2.0](https://github.com/HKUDS/DeepTutor/releases/tag/v0.2.0) — Implementação Docker, atualização para Next.js 16 e React 19, reforço de segurança WebSocket e correções de vulnerabilidades críticas.

</details>

### 📰 Notícias

- **2026-05-22** 🌐 Site oficial de documentação disponível em [**deeptutor.info**](https://deeptutor.info/) — guias, referências e tours de capacidades num só lugar.
- **2026-04-19** 🎉 Atingimos 20k estrelas em 111 dias! Obrigado pelo apoio incrível rumo a uma tutoria verdadeiramente personalizada e inteligente para todos.
- **2026-04-10** 📄 O nosso artigo está agora no arXiv! Leia o [preprint](https://arxiv.org/abs/2604.26962) para saber mais sobre o design e as ideias por trás do DeepTutor.
- **2026-02-06** 🚀 Atingimos 10k estrelas em apenas 39 dias! Um enorme obrigado à nossa incrível comunidade pelo apoio!
- **2026-01-01** 🎊 Feliz Ano Novo! Junte-se ao nosso [Discord](https://discord.gg/eRsjPgMU4t), [WeChat](https://github.com/HKUDS/DeepTutor/issues/78) ou [Discussions](https://github.com/HKUDS/DeepTutor/discussions) — juntos damos forma ao futuro do DeepTutor!
- **2025-12-29** 🎓 DeepTutor está oficialmente lançado!

## ✨ Recursos Principais

O DeepTutor é um espaço de trabalho de aprendizagem nativo de agentes que conecta tutoria, resolução de problemas, geração de quizzes, pesquisa, visualização e prática de domínio num sistema extensível.

- **Um runtime para todos os modos** — Chat, Quiz, Research, Visualize, Solve e Mastery Path correm no mesmo loop de agente, pelo que muda o objetivo, não o motor, e o contexto acompanha o utilizador.
- **Contexto de aprendizado conectado** — bases de conhecimento, livros, rascunhos Co-Writer, cadernos, bancos de questões, personas e Memory permanecem disponíveis em todos os fluxos de trabalho em vez de viverem em ferramentas isoladas.
- **Subagentes e Partners** — consultar um Claude Code, Codex ou Partner ao vivo a partir de qualquer turno (ou importar as suas conversas anteriores), e correr companheiros IM persistentes no mesmo cérebro.
- **Conhecimento multi-motor** — bibliotecas RAG com versões: LlamaIndex, PageIndex, GraphRAG, LightRAG ou um vault Obsidian vinculado, com análise de documentos conectável.
- **Ferramentas e habilidades extensíveis** — ferramentas integradas, servidores MCP, modelos de geração de imagem / vídeo / voz e habilidades da comunidade instaláveis do EduHub.
- **Memória inspecionável** — rastreamentos L1, resumos de superfície L2 e síntese L3 tornam a personalização visível e editável, com um Memory Graph que rastreia cada afirmação até à sua evidência.

---

## 🚀 Começar

O DeepTutor inclui quatro caminhos de instalação. Todos partilham um layout de espaço de trabalho: as configurações vivem em `data/user/settings/` sob o diretório a partir do qual é iniciado (ou sob `DEEPTUTOR_HOME` / `deeptutor start --home` se definido explicitamente). Para a aplicação completa, o fluxo recomendado é **escolher um diretório de espaço de trabalho → instalar → `deeptutor init` → `deeptutor start`**.

> ✨ **v1.4.6 está disponível.** `pip install -U deeptutor` obtém a versão estável mais recente. As versões pré-lançamento (quando disponíveis) são ativadas com `pip install --pre -U deeptutor`.

### Opção 1 — Instalar a partir do PyPI

Aplicação web local completa + CLI, sem necessidade de clonar. Requer **Python 3.11+** e um runtime **Node.js 20+** no PATH (o servidor standalone Next.js empacotado é iniciado por `deeptutor start`).

```bash
mkdir -p my-deeptutor && cd my-deeptutor
pip install -U deeptutor
deeptutor init     # solicita portas + provedor LLM + embedding opcional
deeptutor start    # inicia backend + frontend; manter o terminal aberto
```

`deeptutor init` solicita a porta de backend (predefinição `8001`), a porta de frontend (predefinição `3782`), provedor LLM / URL base / chave API / modelo e um provedor de embeddings opcional para Base de Conhecimento / RAG.

Após `deeptutor start`, abra a URL do frontend impressa no terminal — por predefinição [http://127.0.0.1:3782](http://127.0.0.1:3782). Prima `Ctrl+C` nesse terminal para parar tanto o backend como o frontend. Omitir `deeptutor init` é adequado para um teste rápido; a aplicação arranca com portas predefinidas e configuração de modelo vazia, configure-as depois em **Settings → Models**.

### Opção 2 — Instalar a partir do Código-Fonte

Para desenvolvimento num checkout. Use **Python 3.11+** e **Node.js 22 LTS** para coincidir com CI e Docker.

```bash
git clone https://github.com/HKUDS/DeepTutor.git
cd DeepTutor

# Criar um venv (macOS/Linux). Windows PowerShell:
#   py -3.11 -m venv .venv ; .\.venv\Scripts\Activate.ps1
python3 -m venv .venv && source .venv/bin/activate
python -m pip install --upgrade pip

# Instalar dependências de backend + frontend
python -m pip install -e .
( cd web && npm ci --legacy-peer-deps )

deeptutor init
deeptutor start
```

As instalações a partir de fonte executam o Next.js em modo de desenvolvimento contra o diretório `web/` local; todo o resto (layout de configuração, portas, parar com `Ctrl+C`) corresponde à Opção 1.

<details>
<summary><b>Ambiente Conda</b> (em vez de <code>venv</code>)</summary>

```bash
conda create -n deeptutor python=3.11
conda activate deeptutor
python -m pip install --upgrade pip
```

</details>

<details>
<summary><b>Extras de instalação opcionais</b> — dev / partners / matrix / math-animator</summary>

```bash
pip install -e ".[dev]"             # ferramentas de testes/lint
pip install -e ".[partners]"        # SDKs de canais IM de Partners + cliente MCP
pip install -e ".[matrix]"          # canal Matrix sem E2EE/libolm
pip install -e ".[matrix-e2e]"      # Matrix E2EE; requer libolm
pip install -e ".[math-animator]"   # add-on Manim; requer LaTeX/ffmpeg/libs do sistema
```

</details>

<details>
<summary><b>Ajustes de dependências do frontend e resolução de problemas do servidor de desenvolvimento</b></summary>

**Alterar dependências do frontend:** execute `npm install --legacy-peer-deps` para atualizar `web/package-lock.json`, depois confirme tanto `web/package.json` como `web/package-lock.json`.

**Servidor de desenvolvimento bloqueado:** se `deeptutor start` reportar um frontend existente que não responde, pare o PID que imprime. Se não houver nenhum processo Next.js em execução, os ficheiros de bloqueio estão desatualizados — remova-os e tente novamente:

```bash
rm -f web/.next/dev/lock web/.next/lock
deeptutor start
```

</details>

### Opção 3 — Docker

Um contentor para a aplicação web completa. Imagens no GitHub Container Registry:

- `ghcr.io/hkuds/deeptutor:latest` — lançamento estável
- `ghcr.io/hkuds/deeptutor:pre` — pré-lançamento, quando disponível

```bash
docker run --rm --name deeptutor \
  -p 127.0.0.1:3782:3782 \
  -p 127.0.0.1:8001:8001 \
  -v deeptutor-data:/app/data \
  ghcr.io/hkuds/deeptutor:latest
```

> ⚠️ **Mapeie tanto `3782` como `8001`.** `3782` serve a UI web; `8001` é o backend FastAPI que o seu navegador chama diretamente — não há proxy dentro do contentor. Omitir o mapeamento de `8001` e a página ainda carrega, mas **Settings** mostra "Backend unreachable" e não pode ser utilizado.

Abra [http://127.0.0.1:3782](http://127.0.0.1:3782). O contentor cria `/app/data/user/settings/*.json` no primeiro arranque; configure os provedores de modelos a partir da página de Settings web. A configuração, as chaves API, os logs, os ficheiros do espaço de trabalho, a memória e as bases de conhecimento persistem no volume `deeptutor-data`.

- **Portas de host diferentes:** altere o lado esquerdo de cada mapeamento `-p host:container` (ex. `-p 127.0.0.1:8088:3782`). Se alterar as portas do lado do contentor em `/app/data/user/settings/system.json`, reinicie e atualize o lado direito de cada mapeamento para corresponder.
- **Desconectado:** adicione `-d`, depois `docker logs -f deeptutor` para seguir, `docker stop deeptutor` para parar, `docker rm deeptutor` antes de reutilizar o nome. O volume `deeptutor-data` mantém as suas configurações e espaço de trabalho entre reinicializações.

**Docker remoto / proxy inverso:** a UI web corre no navegador, por isso o navegador precisa de um URL de backend que consiga alcançar. Para servidores remotos, abra **Settings -> Network** ou edite `data/user/settings/system.json`:

```json
{
  "next_public_api_base_external": "https://deeptutor.example.com"
}
```

`public_api_base` é aceite como alias de compatibilidade e é normalizado em `next_public_api_base_external` ao guardar. CORS usa **origens** de frontend, não URLs de API. Com a autenticação desativada, o DeepTutor permite origens normais de navegador HTTP/HTTPS por predefinição. Com a autenticação ativada, adicione as origens exatas do frontend:

```json
{
  "cors_origins": ["https://deeptutor.example.com"]
}
```

<details>
<summary><b>Ligar ao Ollama / LM Studio / llama.cpp / vLLM / Lemonade no host</b></summary>

Dentro do Docker, `localhost` é o próprio contentor, não a sua máquina host. Para alcançar um serviço de modelo em execução no host, use o host gateway (recomendado):

```bash
docker run --rm --name deeptutor \
  -p 127.0.0.1:3782:3782 -p 127.0.0.1:8001:8001 \
  --add-host=host.docker.internal:host-gateway \
  -v deeptutor-data:/app/data \
  ghcr.io/hkuds/deeptutor:latest
```

Depois em **Settings → Models**, aponte o URL Base do provedor para `host.docker.internal`:

- Ollama LLM: `http://host.docker.internal:11434/v1`
- Ollama embedding: `http://host.docker.internal:11434/api/embed`
- LM Studio: `http://host.docker.internal:1234/v1`
- llama.cpp: `http://host.docker.internal:8080/v1`
- Lemonade: `http://host.docker.internal:13305/api/v1`

O Docker Desktop (macOS/Windows) geralmente resolve `host.docker.internal` sem `--add-host`. No Linux, o flag é a forma portátil de criar esse nome de host no Docker Engine moderno.

**Alternativa para Linux — rede do host:** adicione `--network=host` e remova os flags `-p`. O contentor partilha a rede do host diretamente, por isso abra [http://127.0.0.1:3782](http://127.0.0.1:3782) (ou o `frontend_port` em `system.json`), e os serviços do host podem ser alcançados com URLs de localhost normais como `http://127.0.0.1:11434/v1`. Note que a rede do host expõe as portas do contentor diretamente no host e pode entrar em conflito com serviços existentes.

</details>

### Sandbox de Execução de Código (skills de escritório)

As skills de escritório integradas — **docx / pdf / pptx / xlsx** — funcionam fazendo com que o modelo escreva um script Python curto (`python-docx`, `reportlab`, `openpyxl`, …), o execute através das ferramentas `exec` / `code_execution` e devolva um URL de download. Essas ferramentas montam sempre que um backend de sandbox está ativo, o que é o caso **por predefinição** em cada forma de implementação:

- **Local (Opção 1 / 2) e Docker (Opção 3, contentor único):** um sandbox de subprocesso restrito executa o código do modelo (localmente no host, ou dentro do contentor sob Docker — o contentor sendo o seu próprio limite de isolamento).
- **docker-compose:** encaminhado em vez disso para um **sidecar runner** endurecido e com privilégios mínimos (`Dockerfile.runner`) via `DEEPTUTOR_SANDBOX_RUNNER_URL` — a postura mais sólida, e preferida automaticamente quando presente.

O sandbox de subprocesso é controlado pela configuração `sandbox_allow_subprocess` em `data/user/settings/system.json` (predefinição `true`). Executar código gerado pelo modelo no seu host é uma decisão real de confiança — defina-o como `false` (ou exporte `DEEPTUTOR_SANDBOX_ALLOW_SUBPROCESS=0`) para desativar a execução do lado do host, à custa das skills de escritório já não conseguirem produzir ficheiros.

### Opção 4 — Apenas CLI

Quando não precisa da UI web. O pacote de apenas CLI é instalado a partir de um checkout de fonte, não a partir do PyPI.

```bash
git clone https://github.com/HKUDS/DeepTutor.git
cd DeepTutor

# Criar um venv (macOS/Linux). Windows PowerShell:
#   py -3.11 -m venv .venv-cli ; .\.venv-cli\Scripts\Activate.ps1
python3 -m venv .venv-cli && source .venv-cli/bin/activate
python -m pip install --upgrade pip

python -m pip install -e ./packaging/deeptutor-cli
deeptutor init --cli
deeptutor chat
```

`deeptutor init --cli` partilha o mesmo layout `data/user/settings/` que a aplicação completa mas omite as solicitações de portas de backend/frontend e define embeddings como **desativado** (escolha `Yes` se planear usar `deeptutor kb …` ou ferramentas RAG). Ainda escreve um layout de runtime completo (`system.json`, `auth.json`, `integrations.json`, `model_catalog.json`, `main.yaml`, `agents.yaml`) e ainda solicita o provedor LLM e modelo ativos.

<details>
<summary><b>Comandos comuns</b></summary>

```bash
deeptutor chat                                          # REPL interativo
deeptutor chat --capability deep_solve --tool rag --kb my-kb
deeptutor run chat "Explain Fourier transform"
deeptutor run deep_solve "Solve x^2 = 4" --tool rag --kb my-kb
deeptutor kb create my-kb --doc textbook.pdf
deeptutor memory show
deeptutor config show
```

</details>

A instalação local de `deeptutor-cli` não inclui ativos web nem dependências de servidor. Mantenha o checkout de fonte por perto — a instalação editável aponta para ele. Para adicionar a aplicação web mais tarde, instale o pacote PyPI (Opção 1) e execute `deeptutor init` + `deeptutor start` a partir do mesmo espaço de trabalho.

### Referência de Configuração

<details>
<summary><b>Ficheiros de configuração sob <code>data/user/settings/</code></b> — referência JSON/YAML</summary>

Tudo sob `data/user/settings/` é JSON/YAML simples. A página **Settings** no navegador é o editor recomendado.

| Ficheiro | Propósito |
|:---|:---|
| `model_catalog.json` | Perfis de provedores LLM, embeddings e pesquisa; chaves API; modelos ativos |
| `system.json` | Portas de backend/frontend, base de API pública, CORS, verificação SSL, diretório de anexos |
| `auth.json` | Interruptor de autenticação opcional, nome de utilizador, hash de palavra-passe, configurações de token/cookie |
| `integrations.json` | Configurações opcionais de PocketBase e integrações sidecar |
| `interface.json` | Preferências de idioma / tema / barra lateral da UI |
| `main.yaml` | Predefinições de comportamento de runtime e injeção de caminhos |
| `agents.yaml` | Configurações de temperatura e tokens de capacidades/ferramentas |

O `.env` da raiz do projeto **não** é lido como ficheiro de configuração da aplicação. Para uma configuração mínima do modelo, abra **Settings → Models**, adicione um perfil LLM (URL Base / chave API / nome do modelo) e guarde. Adicione um perfil de embeddings apenas se planear usar funcionalidades de Base de Conhecimento / RAG.

</details>

---

## 📖 Explorar o DeepTutor

Comece pelas superfícies principais que usará no dia a dia: Chat, Partners, Meus Agentes, Co-Writer, Book, Centro de Conhecimento, Espaço de Aprendizado, Memory e Configurações.

<div align="center">
<img src="../../assets/figs/web-1.4.6+/OVERVIEW.png" alt="DeepTutor — espaço de trabalho Chat com todas as superfícies na barra lateral" width="900">
</div>

### 💬 Chat — O Loop de Agente que Realmente Usa

<div align="center">
<img src="../../assets/figs/web-1.4.6+/home/00-overview.png" alt="Espaço de trabalho de chat DeepTutor" width="900">
</div>

Chat é a capacidade predefinida e o lugar onde a maior parte do trabalho começa. Um único thread pode conversar normalmente, chamar ferramentas, fundamentar-se em bases de conhecimento selecionadas, ler anexos, gerar imagens, consultar subagentes, escrever registos de notebook e continuar com o mesmo contexto entre turnos.

O loop é deliberadamente simples: o modelo pensa em rondas, chama ferramentas quando útil, observa os resultados e termina com uma mensagem sem ferramentas. `ask_user` é especial — em vez de adivinhar, o agente pode pausar o turno, fazer uma pergunta de esclarecimento estruturada e retomar assim que responder.

<div align="center">
<img src="../../assets/figs/system/chat-agent-loop.png" alt="Loop de agente de chat DeepTutor" width="900">
</div>

As ferramentas ativáveis pelo utilizador são `brainstorm`, `web_search`, `paper_search`, `reason` e `geogebra_analysis` — mais `imagegen` e `videogen` depois de configurar o modelo de geração correspondente. Ferramentas contextuais como `rag`, `read_source`, `read_memory`, `write_memory`, `read_skill`, `load_tools`, `exec`, `web_fetch`, `ask_user`, `list_notebook`, `write_note`, `github` e `consult_subagent` montam automaticamente quando o turno tem o contexto certo.

O contexto é de dois tipos: **contexto de sessão fixo** (subagente, bases de conhecimento, persona, modelo, voz) vive na barra de ferramentas do compositor e persiste entre turnos; **referências únicas** (ficheiros, histórico de chat, livros, notebooks, banco de questões, agentes importados) vêm do menu `+` para um único turno.

Chat é também o ponto de lançamento para capacidades mais profundas: **Quiz** para geração de perguntas, **Research** para relatórios com citações, **Visualize** para gráficos / diagramas / animações, e — em *More Capabilities* — **Solve** para raciocínio trabalhado e **Mastery Path** para fluxos de planos de aprendizagem.

### 🤝 Partner — Companheiros Persistentes no Mesmo Cérebro

<div align="center">
<img src="../../assets/figs/web-1.4.6+/partners/00-partners%20overview.png" alt="Espaço de trabalho de partners DeepTutor" width="900">
</div>

Os Partners são companheiros persistentes com a sua própria alma, política de modelo, biblioteca, memória e canais. Não são um motor de bot separado: cada mensagem web ou IM recebida torna-se um turno normal do ChatOrchestrator dentro de um espaço de trabalho com âmbito de partner. Um partner é "um chat que tem personalidade e número de telefone."

<div align="center">
<img src="../../assets/figs/system/partners-architecture.png" alt="Arquitetura de partners DeepTutor" width="900">
</div>

Cada partner tem um `SOUL.md`, seleção de modelo, canais, política de ferramentas e biblioteca atribuída. As bases de conhecimento, skills e notebooks são copiadas para `data/partners/<id>/workspace/`, pelo que as mesmas ferramentas de RAG, skill, notebook e memória funcionam sem casos especiais. Um partner lê a memória do seu proprietário mas escreve apenas a sua própria.

<div align="center">
<img src="../../assets/figs/web-1.4.6+/partners/02-IM%20config%20for%20each%20partner.png" alt="Configuração de canal IM por partner" width="900">
</div>

A camada de canais é orientada por esquema e pode ligar-se a plataformas IM como Feishu, Telegram, Slack, DingTalk, QQ/NapCat, WeCom, WhatsApp, Zulip, Matrix e Microsoft Teams dependendo dos extras instalados e das credenciais configuradas. Um partner também pode ser conectado como subagente e consultado a partir de um turno de chat normal — veja **Meus Agentes** abaixo.

### 🧑‍🚀 Meus Agentes — Consultar e Importar Outros Agentes

<div align="center">
<img src="../../assets/figs/web-1.4.6+/myagents/00-overview.png" alt="Espaço de trabalho Meus Agentes DeepTutor" width="900">
</div>

Meus Agentes transforma outros agentes em contexto para o DeepTutor, e faz duas coisas distintas. **Conectar um agente ao vivo** — um Claude Code ou Codex CLI na sua máquina, ou um dos seus Partners — e consultá-lo a partir de dentro de um turno de chat: o DeepTutor *executa* mesmo o outro agente e transmite o seu trabalho para o painel de Atividade via a ferramenta `consult_subagent`. Selecione-o com o chip de Agente (ou escreva `@`) e defina quantas rondas a consulta pode ter.

<div align="center">
<img src="../../assets/figs/web-1.4.6+/home/08-subagent%20demo%20with%20claude%20code.png" alt="Consultar um subagente Claude Code ao vivo" width="900">
</div>

**Importar conversas anteriores** — traga o seu histórico existente do Claude Code e Codex como agentes nomeados, pesquisáveis e retomáveis. Escolha quais os dias a importar; atualizar ressincroniza-os. Referencie uma conversa importada a partir de qualquer turno de chat via `+` → Meus Agentes, e o DeepTutor lê-a como uma transcrição de terceiros — permanece *a conversa deles*, não a voz própria do DeepTutor.

### ✍️ Co-Writer — Rascunho Markdown com Consciência de Seleção

<div align="center">
<img src="../../assets/figs/web-1.4.6+/co-writer/00-overview.png" alt="Espaço de trabalho Co-Writer DeepTutor" width="900">
</div>

Co-Writer é um espaço de trabalho Markdown de vista dividida para relatórios, tutoriais, notas e artefactos de aprendizagem de formato longo. Os documentos guardam automaticamente, renderizam uma pré-visualização em tempo real (matemática KaTeX, cercas de diagramas) e podem ser guardados de volta em notebooks quando um rascunho se torna contexto reutilizável.

<div align="center">
<img src="../../assets/figs/web-1.4.6+/co-writer/01-edit%20panel.png" alt="Editor Co-Writer com pré-visualização em tempo real" width="900">
</div>

A sua ideia central é a **edição cirúrgica**: selecione um trecho e peça ao DeepTutor para reescrever, expandir ou encurtar. O agente de edição pode fundamentar a alteração numa base de conhecimento ou evidência web, mantém um rasto das suas chamadas de ferramentas e mostra cada alteração como um diff aceitar/rejeitar — pelo que nada aterra até que aprove.

### 📖 Book (Livro) — Livros Vivos dos Seus Materiais

<div align="center">
<img src="../../assets/figs/web-1.4.6+/book/00-book_overview.png" alt="Biblioteca de livros DeepTutor" width="900">
</div>

Book converte fontes selecionadas num **livro vivo** interativo — não um PDF estático, mas um ambiente de leitura construído a partir de blocos tipados. Um livro pode começar a partir de bases de conhecimento, notebooks, bancos de perguntas ou histórico de chat; o fluxo de criação propõe uma estrutura de capítulos antes de o conteúdo ser gerado, para que os utilizadores possam rever a forma em vez de aceitar uma saída cega de disparo único.

<p align="center">
<img src="../../assets/figs/web-1.4.6+/book/01-book-demo-quiz%20card.png" alt="Bloco de quiz do Book" width="31%">
&nbsp;
<img src="../../assets/figs/web-1.4.6+/book/02-book-demo-manim%20video.png" alt="Bloco de animação Manim do Book" width="31%">
&nbsp;
<img src="../../assets/figs/web-1.4.6+/book/03-book-demo%20interactive%20module.png" alt="Bloco de widget interativo do Book" width="31%">
</p>

Cada capítulo compila em blocos tipados — texto, callouts, quizzes, cartões flash, linhas do tempo, código, figuras, HTML interativo, animações, gráficos de conceitos, mergulhos profundos e notas de utilizador — e cada página tem o seu próprio Page Chat. Os blocos são editáveis: inserir, mover, regenerar ou mudar o tipo de um bloco sem reescrever o capítulo. Os comandos de manutenção como `deeptutor book health` e `deeptutor book refresh-fingerprints` ajudam a detetar quando o conhecimento de origem divergiu das páginas compiladas.

### 📚 Centro de Conhecimento — Bibliotecas RAG Multi-Motor

<div align="center">
<img src="../../assets/figs/web-1.4.6+/knowledge/00-overview.png" alt="Centro de Conhecimento DeepTutor" width="900">
</div>

As bases de conhecimento são as coleções de documentos por trás do RAG — fundamentam os turnos do Chat, edições do Co-Writer, geração do Book e conversas do Partner. O que é distintivo é uma **escolha de motores de recuperação**: **LlamaIndex** (o padrão, vetor local + BM25), **PageIndex** (alojado, recuperação de raciocínio com citações ao nível da página), **GraphRAG** e **LightRAG** (recuperação de grafo de conhecimento), ou um vault **Obsidian** vinculado que o tutor lê e escreve no lugar. Cada KB é indexada por um motor.

<div align="center">
<img src="../../assets/figs/web-1.4.6+/knowledge/01-create%20knowledge%20base.png" alt="Criar uma base de conhecimento" width="900">
</div>

Ao criar uma KB, pode **criar nova** (carregar documentos e construir um índice novo) ou **vincular existente** (reutilizar um índice construído noutro lugar, ler no lugar sem reindexação). A reindexação escreve um novo diretório plano `version-N` e mantém os anteriores, pelo que um índice funcional nunca é destruído a meio de uma reconstrução. A análise de documentos — Somente Texto, MinerU, Docling ou markitdown — é escolhida em **Settings → Knowledge Base**, com downloads de modelos locais desativados por predefinição. A CLI espelha o ciclo de vida com `deeptutor kb list`, `info`, `create`, `add`, `search`, `set-default` e `delete`.

### 🌐 Espaço de Aprendizado — Skills, Personas e Contexto Reutilizável

<div align="center">
<img src="../../assets/figs/web-1.4.6+/learning-space/00-overview.png" alt="Hub do Espaço de Aprendizado DeepTutor" width="900">
</div>

O Espaço de Aprendizado é a camada de biblioteca e personalização — onde vivem as coisas que persistem. **Conversas e Materiais** contém o seu histórico de chat, notebooks e um banco de questões (cada pergunta guardada mantém a sua resposta, a resposta de referência e uma explicação). **Personalização** contém caminhos de domínio, personas (predefinições de comportamento como *par*, *assistente de pesquisa*, *professor*) e skills (playbooks `SKILL.md` que o modelo lê a pedido). Tudo aqui pode ser reutilizado a partir do Chat, Partners, Co-Writer e Book.

<div align="center">
<img src="../../assets/figs/web-1.4.6+/learning-space/07-%20download%20skills%20from%20eduhub.png" alt="Importar skills do EduHub" width="900">
</div>

Não tem de escrever cada skill você mesmo — **Importar do EduHub** navega no catálogo da comunidade e descarrega uma skill diretamente para a sua biblioteca através de uma porta de segurança (veja [Ecossistema](#-ecossistema--eduhub-e-a-comunidade-de-skills)).

### 🧠 Memória — Personalização Inspecionável

<div align="center">
<img src="../../assets/figs/web-1.4.6+/memory/00-overview.png" alt="Visão geral da memória DeepTutor" width="900">
</div>

A Memória é um sistema de três camadas suportado por ficheiros que pode ler, curar e auditar — deliberadamente *não* um armazém de vetores oculto. **L1** é o espelho do espaço de trabalho mais um rasto de eventos append-only (`trace/<surface>/<date>.jsonl`); **L2** são factos curados por superfície (`L2/<surface>.md`); **L3** é a síntese entre superfícies (`L3/<profile|recent|scope>.md`). Como L2 cita L1 e L3 cita L2, nada no seu perfil é incontabilizável.

<div align="center">
<img src="../../assets/figs/web-1.4.6+/memory/01-3%20layer%20memory%20graph.png" alt="Gráfico de memória de três camadas DeepTutor" width="900">
</div>

O Memory Graph mostra toda a pirâmide — síntese L3 no centro, L2 no anel do meio, rastreamentos L1 no exterior — para que possa rastrear qualquer afirmação sintetizada até ao evento bruto exato que lhe deu origem. A memória é rastreada nas superfícies `chat`, `notebook`, `quiz`, `kb`, `book`, partner e `cowriter`; os orçamentos de Atualização / Auditoria / Deduplicação do consolidador são ajustados em **Settings → Memory**.

### ⚙️ Configurações — Um Plano de Controlo

<div align="center">
<img src="../../assets/figs/web-1.4.6+/settings/00-setting%20overview.png" alt="Hub de configurações DeepTutor" width="900">
</div>

Configurações é o plano de controlo operacional, com uma faixa de estado em tempo real (Backend, LLM, Embedding, Search) e um cartão por área: **Aparência** (tema + idioma da UI), **Rede** (base de API, portas, CORS), **Modelos** (LLM, Embedding, Search, Text-to-Speech, Speech-to-Text, Geração de Imagem, Geração de Vídeo), **Base de Conhecimento** (motor de análise de documentos), **Chat** (ferramentas, servidores MCP, parâmetros por capacidade), **Partners e Agentes** (os subagentes que pode consultar a partir de um turno) e **Memória** (os orçamentos do consolidador).

<div align="center">
<img src="../../assets/figs/web-1.4.6+/settings/01-appearance%20settings.png" alt="Configurações de aparência e temas DeepTutor" width="900">
</div>

A maioria das secções usa um fluxo de rascunho e aplicação, para que possa testar um provedor antes de o confirmar. Quatro temas incluídos — Default, Cream, Dark e Glass. Os ficheiros `.env` da raiz do projeto são intencionalmente ignorados; a configuração de runtime vive sob `data/user/settings/*.json` a menos que `DEEPTUTOR_HOME` ou `deeptutor start --home` aponte a aplicação para outro lugar.

---

## ⌨️ DeepTutor CLI — Interface Nativa de Agentes

O DeepTutor é nativo de CLI: o mesmo ponto de entrada `deeptutor` pode inicializar um espaço de trabalho, iniciar a aplicação web, executar uma capacidade de disparo único, abrir um REPL interativo, gerir bases de conhecimento, inspecionar sessões, manter livros e operar partners. Dois modos de entrada: um **REPL** interativo para pessoas que vivem no terminal, e **JSON** estruturado para outros agentes que conduzem o DeepTutor como uma ferramenta.

```bash
deeptutor run chat "Explain Fourier transform" --tool rag --kb textbook
deeptutor run deep_solve "Solve x^2 = 4" --tool reason
deeptutor chat --capability deep_research --kb papers
deeptutor partner create math-tutor --soul "Socratic math tutor"
deeptutor kb create calculus --doc textbook.pdf
```

<details>
<summary><b>Conduzir você mesmo</b></summary>

`deeptutor chat` abre um REPL interativo; `deeptutor run <capability> "<message>"` dispara um único turno e sai. Ambos usam os mesmos flags `--capability`, `--tool`, `--kb` e `--config`.

```bash
deeptutor chat                                              # REPL interativo
deeptutor chat --capability deep_solve --kb my-kb --tool rag
deeptutor run chat "Explain the Fourier transform" --tool rag --kb textbook
deeptutor run deep_research "Survey 2026 papers on RAG" \
  --config mode=report --config depth=standard
```

Tudo o que a aplicação Web faz também está aqui — bases de conhecimento (`kb`), sessões (`session`), partners (`partner`), skills (`skill`), notebooks, memória e configuração.

</details>

<details>
<summary><b>Deixar um agente conduzir</b></summary>

O DeepTutor foi construído para ser *operado por outro agente*. Adicione `--format json` a qualquer `run` e cada turno transmite **NDJSON — um evento por linha** (`content`, `tool_call`, `tool_result`, `done`, …), cada linha marcada com o seu `session_id`. As execuções são seguras sem TTY: uma pausa `ask_user` sem TTY resolve-se automaticamente com uma resposta vazia em vez de bloquear.

```bash
# Disparo único, legível por máquina
deeptutor run deep_solve "Find d/dx[sin(x^2)]" --tool reason --format json

# Encadear turnos numa sessão com estado — capturar o id, reutilizá-lo
SID=$(deeptutor run deep_research "Survey 2026 papers on RAG" \
  --config mode=report --config depth=standard --format json \
  | jq -r 'select(.type=="done").session_id')
deeptutor run deep_question "Quiz me on that survey" --session "$SID" --format json
```

O repositório inclui um [`SKILL.md`](../../SKILL.md) raiz — um documento de transferência de ~150 linhas que ensina qualquer LLM com uso de ferramentas toda a superfície numa leitura. Passe-o ao Claude Code, Codex ou OpenCode (eles pegam no `SKILL.md` automaticamente), ou envolva `deeptutor run` como uma ferramenta num loop LangChain / AutoGen.

</details>

<details>
<summary><b>Referência de comandos</b></summary>

| Comando | Descrição |
|:---|:---|
| `deeptutor init` | Criar ou atualizar `data/user/settings` para o espaço de trabalho atual |
| `deeptutor start [--home PATH]` | Lançar backend + frontend juntos |
| `deeptutor serve [--port PORT]` | Iniciar apenas o backend FastAPI |
| `deeptutor run <capability> <message>` | Executar um turno de capacidade único (`chat`, `deep_solve`, `deep_question`, `deep_research`, `visualize`, `math_animator`, `mastery_path`); adicionar `--format json` para saída NDJSON |
| `deeptutor chat` | REPL interativo com controlos de capacidade, ferramenta, KB, notebook e histórico |
| `deeptutor partner list/create/start/stop` | Gerir partners ligados por IM |
| `deeptutor kb list/info/create/add/search/set-default/delete` | Gerir bases de conhecimento LlamaIndex |
| `deeptutor skill search/install/list/remove/login/publish/update` | Gerir habilidades, instalar de hubs e publicar as suas (`eduhub:<slug>` por padrão, veja Ecossistema) |
| `deeptutor memory show/clear` | Inspecionar documentos de memória L2/L3 ou limpar memória L1/toda |
| `deeptutor session list/show/open/rename/delete` | Gerir sessões partilhadas |
| `deeptutor notebook list/create/show/add-md/replace-md/remove-record` | Gerir notebooks a partir de ficheiros Markdown |
| `deeptutor book list/health/refresh-fingerprints` | Inspecionar livros e atualizar impressões digitais de fontes |
| `deeptutor plugin list/info` | Inspecionar ferramentas e capacidades registadas |
| `deeptutor config show` | Imprimir resumo de configuração |
| `deeptutor provider login <provider>` | Gerir login OAuth do provedor onde suportado |

</details>

A distribuição de apenas CLI está em `packaging/deeptutor-cli`; neste checkout deve ser instalada a partir de fonte com `python -m pip install -e ./packaging/deeptutor-cli`. O pacote público `deeptutor-cli` não está atualmente disponível no PyPI, pelo que a secção principal de Começar mantém o caminho de instalação a partir de fonte.

---

## 👥 Multi-Utilizador — Implementações Partilhadas

A autenticação está **desativada por predefinição** — o DeepTutor corre em modo de utilizador único. Ative-a e uma árvore `data/` aloja um espaço de trabalho de administrador, espaços de trabalho por utilizador isolados e espaços de trabalho de partners lado a lado:

```text
data/
├── user/                         # Espaço de trabalho e configurações do administrador
├── users/<uid>/                  # Âmbito do utilizador não administrador
│   ├── user/chat_history.db
│   ├── user/settings/interface.json
│   ├── user/workspace/{chat,co-writer,book,memory,notebook,...}
│   └── knowledge_bases/...
├── partners/<id>/workspace/      # Âmbito do utilizador sintético do partner
└── system/
    ├── auth/users.json
    ├── grants/<uid>.json
    └── audit/usage.jsonl
```

O **primeiro utilizador registado torna-se administrador** e pode configurar catálogos de modelos, credenciais de provedores, bases de conhecimento partilhadas, skills e concessões de utilizador. Os utilizadores não administradores obtêm um espaço de trabalho isolado e uma página de Settings editada — modelos, KBs e skills atribuídos pelo administrador aparecem como opções com âmbito somente leitura, nunca como chaves API brutas.

Para ativar: defina auth em `data/user/settings/auth.json`, reinicie `deeptutor start`, registe o primeiro administrador em `/register`, depois crie utilizadores a partir de `/admin/users` e atribua modelos, KBs, skills, política de ferramentas/MCP e acesso de execução de código através de concessões.

> O modo PocketBase continua a ser uma integração de utilizador único — mantenha `integrations.pocketbase_url` em branco para implementações multi-utilizador a menos que tenha ligado explicitamente um armazém de utilizadores externo.

---

## 🧩 Ecossistema — EduHub e a Comunidade de Skills

O DeepTutor inclui o [**EduHub**](https://eduhub.deeptutor.info/) — o nosso próprio registo de skills focado em educação — como hub padrão. As skills do DeepTutor usam o formato aberto **Agent-Skills** — uma pasta com um playbook `SKILL.md` (frontmatter YAML + Markdown) e ficheiros de referência opcionais. Nada nisto é específico do DeepTutor, por isso qualquer registo que fale o formato torna-se uma fonte para a sua biblioteca.

<details>
<summary><b>EduHub — o ecossistema de habilidades do DeepTutor</b></summary>

[**EduHub**](https://eduhub.deeptutor.info/) é o hub da comunidade que o DeepTutor lançou para partilhar skills de agentes orientadas para o ensino — tutores socráticos, construtores de cartões flash, feedback de redações, planos de exames, explicadores de conceitos e muito mais. Está integrado no DeepTutor, por isso não há nada a configurar: um slug simples ou um prefixo `eduhub:` resolve para ele.

**Encontrar e instalar** — no navegador, abra **Espaço de Aprendizado → Skills → Importar do EduHub** para navegar no catálogo e descarregar uma skill diretamente para a sua biblioteca. Do terminal:

```bash
deeptutor skill search "socratic tutor"               # pesquisar EduHub (o hub padrão)
deeptutor skill install socratic-tutor                # buscar → verificar → registar
deeptutor skill install eduhub:socratic-tutor@1.2.0   # fixar um hub e uma versão
deeptutor skill list                                  # skills locais com a sua proveniência de hub
```

**Publicar a sua própria** — empacote um `SKILL.md` e partilhe-o de volta com a comunidade:

```bash
deeptutor skill login                                 # login no navegador para o EduHub
deeptutor skill publish ./my-skill                    # interativo: escolher uma faixa + etiquetas, depois carregar
deeptutor skill update                                # reverter ou lançar uma nova versão
```

O EduHub também é um registo independente compatível com ClawHub, por isso agentes que não são o DeepTutor (Claude Code, Codex, …) podem usá-lo diretamente através da CLI `eduhub` — `npx eduhub install socratic-tutor`.

</details>

<details>
<summary><b>A porta de segurança de importação</b></summary>

Seja qual for a fonte, cada importação passa pela **mesma porta de segurança** antes de qualquer coisa tocar no seu espaço de trabalho:

- o **veredicto de segurança** do registo é verificado primeiro — os pacotes sinalizados são recusados a menos que passe `--allow-unverified`;
- os arquivos são extraídos defensivamente (proteções zip-slip / zip-bomb) atrás de uma **lista branca de sufixos** de texto/script, para que binários nunca aterrem no espaço de trabalho;
- o frontmatter é normalizado para o esquema do DeepTutor e `always:` é **removido**, por isso uma skill descarregada nunca pode forçar-se em cada prompt do sistema;
- a proveniência — hub, versão, veredicto e hora de instalação — é escrita em `.hub-lock.json` para auditorias e atualizações.

Em implementações multi-utilizador, instalar é exclusivo do administrador: uma nova skill aterra no catálogo do administrador e permanece invisível para outros utilizadores até que uma concessão a atribua, para que um administrador possa verificá-la antes de a implementar.

</details>

<details>
<summary><b>Também compatível com ClawHub (--hub clawhub)</b></summary>

Como o DeepTutor fala o formato aberto Agent-Skills, o [**ClawHub**](https://clawhub.ai/) também funciona como fonte de primeira classe — está integrado juntamente com o EduHub. Escolha-o com o prefixo de hub:

```bash
deeptutor skill search "git release notes" --hub clawhub
deeptutor skill install clawhub:git-release-notes@1.0.1
```

Adicione mais registos em `settings/skill_hubs.json`: uma entrada `type: "clawhub"` aponta para qualquer API HTTP compatível (EduHub e ClawHub falam ambos), `type: "command"` envolve qualquer CLI de busca que um registo forneça, e `"default"` escolhe o hub usado para slugs simples. Todos eles alimentam a mesma porta de importação.

</details>

---

## 🌐 Comunidade

### 📮 Contacto

O DeepTutor é um projeto de código aberto liderado por [Bingxi Zhao](https://github.com/pancacake) dentro do Grupo [HKUDS](https://github.com/HKUDS), e itera numa **forma totalmente de código aberto**, construído em conjunto com a comunidade. Até agora, **NÃO** temos produtos online pagos de qualquer forma. Sinta-se à vontade para contactar em **bingxizhao39@gmail.com** para discussões, ideias ou colaboração.

### 🙏 Agradecimentos

Um agradecimento sincero a [**Chao Huang**](https://sites.google.com/view/chaoh), diretor do Data Intelligence Lab @ HKU, e aos nossos colegas do HKUDS pelo seu caloroso apoio — especialmente [**Jiahao Zhang**](https://github.com/zzhtx258), [**Zirui Guo**](https://github.com/LarFii) e [**Xubin Ren**](https://github.com/Re-bin). Também somos profundamente gratos à **comunidade de código aberto**: as suas estrelas, issues, pull requests e discussões moldam o DeepTutor todos os dias.

O DeepTutor também assenta nos ombros de projetos de código aberto excepcionais que nos deram tanto ferramentas como inspiração:

| Projeto | Papel / Inspiração |
|:---|:---|
| [**LlamaIndex**](https://github.com/run-llama/llama_index) | Espinha dorsal da pipeline RAG e indexação de documentos |
| [**nanobot**](https://github.com/HKUDS/nanobot) | Motor de agente ultraligeiro que alimentou o TutorBot original *(HKUDS)* |
| [**LightRAG**](https://github.com/HKUDS/LightRAG) | RAG Simples e Rápido *(HKUDS)* |
| [**AutoAgent**](https://github.com/HKUDS/AutoAgent) | Framework de Agentes Sem Código *(HKUDS)* |
| [**AI-Researcher**](https://github.com/HKUDS/AI-Researcher) | Pipeline de investigação automatizada *(HKUDS)* |
| [**OpenClaw**](https://github.com/openclaw/openclaw) | Gateway aberto de agentes e ecossistema de skills por trás do ClawHub |
| [**Codex**](https://github.com/openai/codex) | CLI de programação nativa de agentes que inspirou o nosso fluxo de trabalho CLI |
| [**Claude Code**](https://github.com/anthropics/claude-code) | CLI de programação agêntica que inspirou o loop de agente do DeepTutor |
| [**ManimCat**](https://github.com/Wing900/ManimCat) | Geração de animações matemáticas impulsionada por IA para o Math Animator |

### 🗺️ Roadmap & Contribuir

Queremos que o DeepTutor continue a iterar e a melhorar — e, em última análise, a tornar-se um presente que devolvemos à comunidade de código aberto. O nosso [**roadmap**](https://github.com/HKUDS/DeepTutor/issues/498) é atualizado continuamente; vote em itens lá ou proponha novos. Se quiser contribuir, veja o [**Guia de Contribuição**](../../CONTRIBUTING.md) para a estratégia de branches, padrões de código e como começar.

<div align="center">

Esperamos que o DeepTutor se torne um presente para a comunidade. 🎁

<a href="https://github.com/HKUDS/DeepTutor/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=HKUDS/DeepTutor&max=999" alt="Contribuidores" />
</a>

</div>

<div align="center">

<a href="https://www.star-history.com/#HKUDS/DeepTutor&type=timeline&legend=top-left">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=HKUDS/DeepTutor&type=timeline&theme=dark&legend=top-left" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=HKUDS/DeepTutor&type=timeline&legend=top-left" />
    <img alt="Gráfico de histórico de estrelas" src="https://api.star-history.com/svg?repos=HKUDS/DeepTutor&type=timeline&legend=top-left" />
  </picture>
</a>

</div>

<p align="center">
 <a href="https://www.star-history.com/hkuds/deeptutor">
  <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/badge?repo=HKUDS/DeepTutor&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/badge?repo=HKUDS/DeepTutor" />
   <img alt="Classificação do histórico de estrelas" src="https://api.star-history.com/badge?repo=HKUDS/DeepTutor" />
  </picture>
 </a>
</p>

<div align="center">

**[Data Intelligence Lab @ HKU](https://github.com/HKUDS)**

[⭐ Dê-nos uma estrela](https://github.com/HKUDS/DeepTutor/stargazers) · [🐛 Reportar um erro](https://github.com/HKUDS/DeepTutor/issues) · [💬 Discussões](https://github.com/HKUDS/DeepTutor/discussions)

---

Licenciado sob [Apache License 2.0](../../LICENSE).

<p>
  <img src="https://visitor-badge.laobi.icu/badge?page_id=HKUDS.DeepTutor&style=for-the-badge&color=00d4ff" alt="Visualizações">
</p>

</div>
