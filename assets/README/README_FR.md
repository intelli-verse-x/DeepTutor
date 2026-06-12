<div align="center">

<p align="center"><img src="../../assets/figs/logo/logo.png" alt="DeepTutor logo" height="56" style="vertical-align: middle;">&nbsp;<img src="../../assets/figs/logo/banner.png" alt="DeepTutor" height="48" style="vertical-align: middle;"></p>

# DeepTutor : Tutorat Personnalisé Natif à l'Agent

<p align="center">
  <a href="https://deeptutor.info" target="_blank"><img alt="Docs — deeptutor.info" src="https://img.shields.io/badge/Docs-deeptutor.info%20%E2%86%97-0A0A0A?style=for-the-badge&labelColor=F5F5F4" height="36"></a>
</p>

<a href="https://trendshift.io/repositories/17099" target="_blank"><img src="https://trendshift.io/api/badge/repositories/17099" alt="HKUDS%2FDeepTutor | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>

<p align="center">
  <a href="../../README.md"><img alt="English" height="40" src="https://img.shields.io/badge/English-CDCFD4"></a>&nbsp;
  <a href="README_CN.md"><img alt="简体中文" height="40" src="https://img.shields.io/badge/简体中文-CDCFD4"></a>&nbsp;
  <a href="README_JA.md"><img alt="日本語" height="40" src="https://img.shields.io/badge/日本語-CDCFD4"></a>&nbsp;
  <a href="README_ES.md"><img alt="Español" height="40" src="https://img.shields.io/badge/Español-CDCFD4"></a>&nbsp;
  <a href="README_FR.md"><img alt="Français" height="40" src="https://img.shields.io/badge/Français-BCDCF7"></a>&nbsp;
  <a href="README_AR.md"><img alt="Arabic" height="40" src="https://img.shields.io/badge/Arabic-CDCFD4"></a>&nbsp;
  <a href="README_RU.md"><img alt="Русский" height="40" src="https://img.shields.io/badge/Русский-CDCFD4"></a>&nbsp;
  <a href="README_HI.md"><img alt="Hindi" height="40" src="https://img.shields.io/badge/Hindi-CDCFD4"></a>&nbsp;
  <a href="README_PT.md"><img alt="Português" height="40" src="https://img.shields.io/badge/Português-CDCFD4"></a>&nbsp;
  <a href="README_TH.md"><img alt="Thai" height="40" src="https://img.shields.io/badge/Thai-CDCFD4"></a>&nbsp;
  <a href="README_PL.md"><img alt="Polski" height="40" src="https://img.shields.io/badge/Polski-CDCFD4"></a>
</p>

[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![Next.js 16](https://img.shields.io/badge/Next.js-16-000000?style=flat-square&logo=next.js&logoColor=white)](https://nextjs.org/)
[![Licence](https://img.shields.io/badge/Licence-Apache_2.0-blue?style=flat-square)](../../LICENSE)
[![GitHub release](https://img.shields.io/github/v/release/HKUDS/DeepTutor?style=flat-square&color=brightgreen)](https://github.com/HKUDS/DeepTutor/releases)
[![arXiv](https://img.shields.io/badge/arXiv-2604.26962-b31b1b?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2604.26962)

[![Discord](https://img.shields.io/badge/Discord-Communauté-5865F2?style=flat-square&logo=discord&logoColor=white)](https://discord.gg/eRsjPgMU4t)
[![Feishu](https://img.shields.io/badge/Feishu-Groupe-00D4AA?style=flat-square&logo=feishu&logoColor=white)](../../Communication.md)
[![WeChat](https://img.shields.io/badge/WeChat-Groupe-07C160?style=flat-square&logo=wechat&logoColor=white)](https://github.com/HKUDS/DeepTutor/issues/78)

[Fonctionnalités](#-fonctionnalités-clés) · [Démarrage](#-démarrage) · [Explorer](#-explorer-deeptutor) · [CLI](#%EF%B8%8F-deeptutor-cli--interface-native-à-lagent) · [Multi-utilisateurs](#-multi-utilisateurs--déploiements-partagés) · [Communauté](#-communauté--écosystème)

</div>

---

> 🤝 **Toute contribution est la bienvenue !** Votez sur les éléments de la feuille de route ou proposez-en de nouveaux sur [`Roadmap`](https://github.com/HKUDS/DeepTutor/issues/498), et consultez notre [Guide de contribution](../../CONTRIBUTING.md) pour la stratégie de branches, les normes de code, et les étapes pour commencer.

### 📦 Versions

> **[2026.6.12]** [v1.4.3](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.3) — TutorBot devient **Partners** sur un pipeline de messagerie instantanée de niveau production avec des réponses en streaming en direct et 15 canaux, Chat passe à une boucle d'agent unique, véritable isolation par utilisateur pour les déploiements multi-utilisateurs, Visualize reconstruit avec validation+réparation locale, ainsi que des améliorations dans Co-writer, le visualiseur de fichiers, l'analyse cloud MinerU et le CLI. La documentation est entièrement actualisée sur [deeptutor.info](https://deeptutor.info/).

> **[2026.5.28]** [v1.4.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.2) — Stabilité et peaufinage de v1.4.1 : Gemini 2.5+ débloqué dans Visualize et Chat, correction du routage d'authentification ContextVar (#485), protocole d'étiquettes raisonnement + outils natifs renforcé, UX de streaming fluide sur toutes les surfaces de chat, nouvelle barre latérale Recents repliable, et support du fournisseur local Lemonade.

> **[2026.5.27]** [v1.4.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.1) — Correctif de sécurité et de stabilité : sandbox des outils TutorBot verrouillée, isolation des ressources par utilisateur, repli d'image multimodale pour les fournisseurs compatibles vision, une API HTTP/SSE pour communiquer avec un TutorBot, et correction d'une régression de chat v1.4.0.

> **[2026.5.22]** [v1.4.0](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.0) — Version GA de v1.4 : Mode Auto, Mémoire en trois couches, Deep Research / Solve / Question agentiques, refactorisation RAG LlamaIndex, fusion Visualize/Animator, plus normalisation des efforts de raisonnement, repli de schéma d'outil, et runtime de tour sûr au redémarrage.

<details>
<summary><b>Versions antérieures (il y a plus de 2 semaines)</b></summary>

> **[2026.5.21]** [v1.4.0-beta](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.0-beta) — Établi de Mémoire en trois couches (L1/L2/L3), toutes les capacités de chat reconstruites sur un seul moteur agentique, RAG LlamaIndex uniquement, et une surface unifiée Paramètres + Capacités.

> **[2026.5.10]** [v1.3.10](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.10) — Récupération CORS Docker distant, `DISABLE_SSL_VERIFY` sur les fournisseurs SDK, citations de blocs de code plus sûres, et add-on optionnel Matrix E2EE.

> **[2026.5.9]** [v1.3.9](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.9) — Support TutorBot Zulip et NVIDIA NIM, routage de modèle de raisonnement plus sûr, `deeptutor start`, infobulles de barre latérale, et parité de stockage de session.

> **[2026.5.8]** [v1.3.8](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.8) — Déploiements multi-utilisateurs optionnels avec espaces de travail utilisateur isolés, autorisations admin, routes d'authentification, et accès runtime limité.

> **[2026.5.4]** [v1.3.7](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.7) — Corrections de modèle/fournisseur de raisonnement, historique d'index de la base de connaissances visible, et édition de modèle/effacement Co-Writer plus sûre.

> **[2026.5.3]** [v1.3.6](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.6) — Sélection de modèle basée sur le catalogue pour le chat et TutorBot, ré-indexation RAG plus sûre, corrections de limites de tokens OpenAI Responses, et validation de l'éditeur Skills.

> **[2026.5.2]** [v1.3.5](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.5) — Paramètres de lancement local plus fluides, requêtes RAG plus sûres, authentification d'embedding local plus propre, et peaufinage du mode sombre des Paramètres.

> **[2026.5.1]** [v1.3.4](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.4) — Persistance et reconstruction des flux de chat de page de livre, références chat-vers-livre, gestion renforcée de la langue/du raisonnement, durcissement de l'extraction de documents RAG.

> **[2026.4.30]** [v1.3.3](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.3) — Support d'embedding NVIDIA NIM + Gemini, contexte Space unifié pour l'historique de chat/compétences/mémoire, instantanés de session, résilience de ré-indexation RAG.

> **[2026.4.29]** [v1.3.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.2) — URL d'endpoint d'embedding transparentes, résilience de ré-indexation RAG pour les vecteurs persistés invalides, nettoyage mémoire pour la sortie de modèle de raisonnement, correction du runtime Deep Solve.

> **[2026.4.28]** [v1.3.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.1) — Stabilité : routage RAG et validation d'embedding plus sûrs, persistance Docker, saisie sûre pour IME, robustesse Windows/GBK.

> **[2026.4.27]** [v1.3.0](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.0) — Index de base de connaissances versionnés avec flux de ré-indexation, espace de travail Knowledge reconstruit, auto-découverte d'embedding avec de nouveaux adaptateurs, hub Space.

> **[2026.4.25]** [v1.2.5](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.5) — Pièces jointes de chat persistantes avec tiroir d'aperçu de fichier, pipelines de capacité tenant compte des pièces jointes, export Markdown TutorBot.

> **[2026.4.25]** [v1.2.4](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.4) — Pièces jointes texte/code/SVG, Tour de configuration en une commande, export Markdown de chat, interface de gestion KB compacte.

> **[2026.4.24]** [v1.2.3](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.3) — Pièces jointes de documents (PDF/DOCX/XLSX/PPTX), affichage du bloc de réflexion de raisonnement, éditeur de modèles Soul, Co-Writer sauvegarde vers le carnet.

> **[2026.4.22]** [v1.2.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.2) — Système de compétences créées par l'utilisateur, refonte des performances de saisie du chat, démarrage automatique TutorBot, interface Book Library, visualisation en plein écran.

> **[2026.4.21]** [v1.2.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.1) — Limites de tokens par étape, Régénérer la réponse sur tous les points d'entrée, corrections de compatibilité RAG et Gemma.

> **[2026.4.20]** [v1.2.0](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.0) — Compilateur de "livre vivant" Book Engine, Co-Writer multi-documents, visualisations HTML interactives, @-mention de la Question Bank.

> **[2026.4.18]** [v1.1.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.1.2) — Onglet Channels piloté par schéma, consolidation du pipeline unique RAG, prompts de chat externalisés.

> **[2026.4.17]** [v1.1.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.1.1) — "Répondre maintenant" universel, synchronisation de défilement Co-Writer, panneau de paramètres unifié, bouton Stop de streaming.

> **[2026.4.15]** [v1.1.0](https://github.com/HKUDS/DeepTutor/releases/tag/v1.1.0) — Refonte des mathématiques LaTeX en blocs, sonde de diagnostic LLM, guide Docker + LLM local.

> **[2026.4.14]** [v1.1.0-beta](https://github.com/HKUDS/DeepTutor/releases/tag/v1.1.0-beta) — Sessions avec signets, thème Snow, battement de cœur WebSocket et reconnexion automatique, refonte du registre d'embedding.

> **[2026.4.13]** [v1.0.3](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.3) — Carnet de questions avec signets et catégories, Mermaid dans Visualize, détection de désaccord d'embedding, compatibilité Qwen/vLLM, support LM Studio et llama.cpp, et thème Glass.

> **[2026.4.11]** [v1.0.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.2) — Consolidation de la recherche avec repli SearXNG, correction de changement de fournisseur, et corrections de fuites de ressources frontend.

> **[2026.4.10]** [v1.0.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.1) — Capacité Visualize (Chart.js/SVG), prévention des doublons de quiz, et support du modèle o4-mini.

> **[2026.4.10]** [v1.0.0-beta.4](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.0-beta.4) — Suivi de progression d'embedding avec relance sur limitation de débit, corrections de dépendances multiplateforme, et correction de validation MIME.

> **[2026.4.8]** [v1.0.0-beta.3](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.0-beta.3) — SDK natif OpenAI/Anthropic (abandon de litellm), support Windows Math Animator, analyse JSON robuste, et i18n chinois complet.

> **[2026.4.7]** [v1.0.0-beta.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.0-beta.2) — Rechargement à chaud des paramètres, sortie imbriquée MinerU, correction WebSocket, et Python 3.11+ minimum.

> **[2026.4.4]** [v1.0.0-beta.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.0-beta.1) — Réécriture de l'architecture native à l'agent (~200k lignes) : modèle de plugins Outils + Capacités, CLI et SDK, TutorBot, Co-Writer, Guided Learning, et mémoire persistante.

> **[2026.1.23]** [v0.6.0](https://github.com/HKUDS/DeepTutor/releases/tag/v0.6.0) — Persistance de session, téléchargement incrémental de documents, import de pipeline RAG flexible, et localisation chinoise complète.

> **[2026.1.18]** [v0.5.2](https://github.com/HKUDS/DeepTutor/releases/tag/v0.5.2) — Support Docling pour RAG-Anything, optimisation du système de journalisation, et corrections de bugs.

> **[2026.1.15]** [v0.5.0](https://github.com/HKUDS/DeepTutor/releases/tag/v0.5.0) — Configuration de service unifiée, sélection de pipeline RAG par base de connaissances, refonte de la génération de questions, et personnalisation de la barre latérale.

> **[2026.1.9]** [v0.4.0](https://github.com/HKUDS/DeepTutor/releases/tag/v0.4.0) — Support LLM et embedding multi-fournisseurs, nouvelle page d'accueil, découplage du module RAG, et refactorisation des variables d'environnement.

> **[2026.1.5]** [v0.3.0](https://github.com/HKUDS/DeepTutor/releases/tag/v0.3.0) — Architecture PromptManager unifiée, CI/CD GitHub Actions, et images Docker pré-construites sur GHCR.

> **[2026.1.2]** [v0.2.0](https://github.com/HKUDS/DeepTutor/releases/tag/v0.2.0) — Déploiement Docker, mise à niveau Next.js 16 et React 19, durcissement de la sécurité WebSocket, et corrections de vulnérabilités critiques.

</details>

### 📰 Actualités

> **[2026.5.22]** 🌐 Notre site de documentation officiel est en ligne sur [**deeptutor.info**](https://deeptutor.info/) — guides, références et visites des capacités en un seul endroit.

> **[2026.4.19]** 🎉 Nous avons atteint 20 000 étoiles après 111 jours ! Merci pour le soutien incroyable — nous nous engageons à itérer en continu vers un tutorat vraiment personnalisé et intelligent pour tous.

> **[2026.4.10]** 📄 Notre article est maintenant disponible sur arXiv ! Lisez le [preprint](https://arxiv.org/abs/2604.26962) pour en savoir plus sur la conception et les idées derrière DeepTutor.

> **[2026.4.4]** Longtemps sans nouvelles ! ✨ DeepTutor v1.0.0 est enfin là — une évolution native à l'agent avec une réécriture complète de l'architecture, TutorBot, et une commutation de mode flexible sous la licence Apache-2.0. Un nouveau chapitre commence, et notre histoire continue !

> **[2026.2.6]** 🚀 Nous avons atteint 10 000 étoiles en seulement 39 jours ! Un immense merci à notre incroyable communauté pour son soutien !

> **[2026.1.1]** Bonne année ! Rejoignez notre [Discord](https://discord.gg/eRsjPgMU4t), [WeChat](https://github.com/HKUDS/DeepTutor/issues/78), ou [Discussions](https://github.com/HKUDS/DeepTutor/discussions) — façonnons ensemble l'avenir de DeepTutor !

> **[2025.12.29]** DeepTutor est officiellement lancé !

## ✨ Fonctionnalités Clés

DeepTutor est organisé autour d'un runtime natif à l'agent : un ChatOrchestrator partagé achemine chaque tour vers des capacités, un ToolRegistry expose des outils à usage unique lorsque le modèle en a besoin, et un CapabilityRegistry permet à des flux de travail plus profonds de prendre en charge le tour lorsque la tâche nécessite de la structure.

<div align="center">
<img src="../../assets/figs/system/system%20architecture.png" alt="Architecture du système DeepTutor" width="900">
</div>

**Un seul espace de travail d'apprentissage**

- **Le Chat comme boucle par défaut** — tutorat informel, Q&R ancré dans les sources, Deep Solve, Deep Question, Deep Research, Visualize, et Mode Auto partagent tous le même contexte de session et le même inventaire de sources.
- **Des surfaces d'apprentissage restant connectées** — les brouillons Co-Writer, les pages Book, les bases de connaissances, les actifs Space et la Mémoire sont des espaces de travail séparés, mais ils alimentent le même runtime d'agent au lieu de devenir des applications isolées.
- **Partners pour un accompagnement persistant** — les compagnons connectés à la messagerie instantanée fonctionnent maintenant sur la même boucle d'agent de chat que le produit principal, avec leur propre espace de travail synthétique et leur bibliothèque assignée.

**Outils, mémoire et contrôle**

- **Outils composables** — RAG, lecture de sources, lecture/écriture de mémoire, carnets, récupération d'URL, recherche GitHub, pauses ask-user, exécution en sandbox, et des outils optionnels de brainstorming/web/article/raisonnement peuvent être montés selon le contexte et les paramètres.
- **Mémoire en trois couches** — les traces L1, les résumés L2 par surface, et la synthèse L3 inter-surfaces rendent la personnalisation inspectable plutôt que cachée derrière une boîte noire.
- **Paramètres unifiés et CLI** — les catalogues de modèles, les embeddings, la recherche, le réseau, les serveurs MCP, les outils, les capacités et les paramètres de déploiement sont modifiables depuis l'interface web et scriptables depuis `deeptutor`.

---

## 🚀 Démarrage

DeepTutor propose quatre chemins d'installation. Tous partagent une même disposition d'espace de travail : les paramètres se trouvent dans `data/user/settings/` sous le répertoire depuis lequel vous lancez (ou sous `DEEPTUTOR_HOME` / `deeptutor start --home` si vous en définissez un explicitement). Pour l'application complète, le flux recommandé est **choisir un répertoire d'espace de travail → installer → `deeptutor init` → `deeptutor start`**.

> ✨ **v1.4.3 est disponible.** `pip install -U deeptutor` récupère la dernière version stable. Les pré-versions (lorsque disponibles) s'installent avec `pip install --pre -U deeptutor`.

### Option 1 — Installation depuis PyPI

Application Web locale complète + CLI, sans clonage requis. Nécessite **Python 3.11+** et un runtime **Node.js 20+** dans le PATH (le serveur standalone Next.js intégré est lancé par `deeptutor start`).

```bash
mkdir -p my-deeptutor && cd my-deeptutor
pip install -U deeptutor
deeptutor init     # demande les ports + fournisseur LLM + embedding optionnel
deeptutor start    # démarre le backend + le frontend ; gardez le terminal ouvert
```

`deeptutor init` demande le port backend (par défaut `8001`), le port frontend (par défaut `3782`), le fournisseur LLM / URL de base / clé API / modèle, et un fournisseur d'embedding optionnel pour la Base de Connaissances / RAG.

Après `deeptutor start`, ouvrez l'URL frontend affichée dans le terminal — par défaut [http://127.0.0.1:3782](http://127.0.0.1:3782). Appuyez sur `Ctrl+C` dans ce terminal pour arrêter le backend et le frontend. Ignorer `deeptutor init` est possible pour un essai rapide ; l'application démarre avec les ports par défaut et des paramètres de modèle vides, configurables ultérieurement dans **Paramètres → Modèles**.

### Option 2 — Installation depuis les sources

Pour le développement à partir d'un checkout. Utilisez **Python 3.11+** et **Node.js 22 LTS** pour correspondre à la CI et Docker.

```bash
git clone https://github.com/HKUDS/DeepTutor.git
cd DeepTutor

# Créer un venv (macOS/Linux). Windows PowerShell :
#   py -3.11 -m venv .venv ; .\.venv\Scripts\Activate.ps1
python3 -m venv .venv && source .venv/bin/activate
python -m pip install --upgrade pip

# Installer les dépendances backend + frontend
python -m pip install -e .
( cd web && npm ci --legacy-peer-deps )

deeptutor init
deeptutor start
```

Les installations depuis les sources font tourner Next.js en mode dev contre le répertoire local `web/` ; tout le reste (disposition de la configuration, ports, arrêt avec `Ctrl+C`) correspond à l'Option 1.

<details>
<summary><b>Environnement Conda</b> (à la place de <code>venv</code>)</summary>

```bash
conda create -n deeptutor python=3.11
conda activate deeptutor
python -m pip install --upgrade pip
```

</details>

<details>
<summary><b>Extras d'installation optionnels</b> — dev / partners / matrix / math-animator</summary>

```bash
pip install -e ".[dev]"             # outils de tests/lint
pip install -e ".[partners]"        # SDK de canaux IM Partner + client MCP
pip install -e ".[matrix]"          # canal Matrix sans E2EE/libolm
pip install -e ".[matrix-e2e]"      # Matrix E2EE ; nécessite libolm
pip install -e ".[math-animator]"   # addon Manim ; nécessite LaTeX/ffmpeg/libs système
```

</details>

<details>
<summary><b>Ajustements des dépendances frontend et résolution des problèmes du serveur de développement</b></summary>

**Modification des dépendances frontend :** exécutez `npm install --legacy-peer-deps` pour actualiser `web/package-lock.json`, puis validez à la fois `web/package.json` et `web/package-lock.json`.

**Serveur de développement bloqué :** si `deeptutor start` signale un frontend existant qui ne répond pas, arrêtez le PID qu'il affiche. Si aucun processus Next.js n'est réellement en cours d'exécution, les fichiers de verrouillage sont périmés — supprimez-les et réessayez :

```bash
rm -f web/.next/dev/lock web/.next/lock
deeptutor start
```

</details>

### Option 3 — Docker

Un conteneur pour l'application Web complète. Images sur GitHub Container Registry :

- `ghcr.io/hkuds/deeptutor:latest` — version stable
- `ghcr.io/hkuds/deeptutor:pre` — pré-version, lorsque disponible

```bash
docker run --rm --name deeptutor \
  -p 127.0.0.1:3782:3782 \
  -p 127.0.0.1:8001:8001 \
  -v deeptutor-data:/app/data \
  ghcr.io/hkuds/deeptutor:latest
```

> ⚠️ **Mappez à la fois `3782` et `8001`.** `3782` sert l'interface web ; `8001` est le backend FastAPI que votre navigateur appelle directement — il n'y a pas de proxy interne au conteneur. Omettez le mapping `8001` et la page se chargera quand même, mais **les Paramètres** afficheront "Backend inaccessible" et resteront inutilisables.

Ouvrez [http://127.0.0.1:3782](http://127.0.0.1:3782). Le conteneur crée `/app/data/user/settings/*.json` au premier démarrage ; configurez les fournisseurs de modèles depuis la page Paramètres Web. La configuration, les clés API, les journaux, les fichiers de l'espace de travail, la mémoire et les bases de connaissances persistent dans le volume `deeptutor-data`.

- **Ports hôte différents :** modifiez le côté gauche de chaque mapping `-p hôte:conteneur` (ex. `-p 127.0.0.1:8088:3782`). Si vous modifiez les ports côté conteneur dans `/app/data/user/settings/system.json`, redémarrez et mettez à jour le côté droit de chaque mapping en conséquence.
- **Mode détaché :** ajoutez `-d`, puis `docker logs -f deeptutor` pour suivre, `docker stop deeptutor` pour arrêter, `docker rm deeptutor` avant de réutiliser le nom. Le volume `deeptutor-data` conserve vos paramètres et votre espace de travail entre les redémarrages.

**Docker distant / proxy inverse :** l'interface Web s'exécute dans le navigateur, donc le navigateur a besoin d'une URL backend accessible. Pour les serveurs distants, ouvrez **Paramètres -> Réseau** ou modifiez `data/user/settings/system.json` :

```json
{
  "next_public_api_base_external": "https://deeptutor.example.com"
}
```

`public_api_base` est accepté comme alias de compatibilité et est normalisé en `next_public_api_base_external` à la sauvegarde. CORS utilise les **origines** du frontend, pas les URL d'API. Sans authentification, DeepTutor autorise les origines de navigateur HTTP/HTTPS normales par défaut. Avec l'authentification activée, ajoutez les origines frontend exactes :

```json
{
  "cors_origins": ["https://deeptutor.example.com"]
}
```

<details>
<summary><b>Connexion à Ollama / LM Studio / llama.cpp / vLLM / Lemonade sur l'hôte</b></summary>

Dans Docker, `localhost` est le conteneur lui-même, pas votre machine hôte. Pour atteindre un service de modèle s'exécutant sur l'hôte, utilisez la passerelle hôte (recommandé) :

```bash
docker run --rm --name deeptutor \
  -p 127.0.0.1:3782:3782 -p 127.0.0.1:8001:8001 \
  --add-host=host.docker.internal:host-gateway \
  -v deeptutor-data:/app/data \
  ghcr.io/hkuds/deeptutor:latest
```

Puis dans **Paramètres → Modèles**, pointez l'URL de base du fournisseur vers `host.docker.internal` :

- LLM Ollama : `http://host.docker.internal:11434/v1`
- Embedding Ollama : `http://host.docker.internal:11434/api/embed`
- LM Studio : `http://host.docker.internal:1234/v1`
- llama.cpp : `http://host.docker.internal:8080/v1`
- Lemonade : `http://host.docker.internal:13305/api/v1`

Docker Desktop (macOS/Windows) résout généralement `host.docker.internal` sans `--add-host`. Sur Linux, l'option est la façon portable de créer ce nom d'hôte sur les moteurs Docker modernes.

**Alternative Linux — réseau hôte :** ajoutez `--network=host` et supprimez les options `-p`. Le conteneur partage directement le réseau de l'hôte, ouvrez donc [http://127.0.0.1:3782](http://127.0.0.1:3782) (ou le `frontend_port` dans `system.json`), et les services hôtes sont accessibles avec des URL localhost normales comme `http://127.0.0.1:11434/v1`. Notez que le réseau hôte expose les ports du conteneur directement sur l'hôte et peut entrer en conflit avec des services existants.

</details>

### Sandbox d'exécution de code (compétences bureautiques)

Les compétences bureautiques intégrées — **docx / pdf / pptx / xlsx** — fonctionnent en faisant écrire par le modèle un court script Python (`python-docx`, `reportlab`, `openpyxl`, …), en l'exécutant via les outils `exec` / `code_execution`, et en renvoyant une URL de téléchargement. Ces outils se montent chaque fois qu'un backend sandbox est actif, ce qui est le cas **par défaut** dans chaque forme de déploiement :

- **Local (Option 1 / 2) et Docker (Option 3, conteneur unique) :** un sandbox de sous-processus restreint exécute le code du modèle (sur l'hôte localement, ou dans le conteneur sous Docker — le conteneur étant sa propre frontière d'isolation).
- **docker-compose :** acheminé vers un **sidecar runner** durci avec le moins de privilèges possible (`Dockerfile.runner`) via `DEEPTUTOR_SANDBOX_RUNNER_URL` — la posture la plus robuste, préférée automatiquement lorsqu'elle est présente.

Le sandbox de sous-processus est contrôlé par le paramètre `sandbox_allow_subprocess` dans `data/user/settings/system.json` (par défaut `true`). Exécuter du code généré par le modèle sur votre hôte est une vraie décision de confiance — mettez-le à `false` (ou exportez `DEEPTUTOR_SANDBOX_ALLOW_SUBPROCESS=0`) pour désactiver l'exécution côté hôte, au prix que les compétences bureautiques ne puissent plus produire de fichiers.

### Option 4 — CLI uniquement

Lorsque vous n'avez pas besoin de l'interface Web. Le package CLI uniquement est installé depuis un checkout des sources, pas depuis PyPI.

```bash
git clone https://github.com/HKUDS/DeepTutor.git
cd DeepTutor

# Créer un venv (macOS/Linux). Windows PowerShell :
#   py -3.11 -m venv .venv-cli ; .\.venv-cli\Scripts\Activate.ps1
python3 -m venv .venv-cli && source .venv-cli/bin/activate
python -m pip install --upgrade pip

python -m pip install -e ./packaging/deeptutor-cli
deeptutor init --cli
deeptutor chat
```

`deeptutor init --cli` partage la même disposition `data/user/settings/` que l'application complète mais ignore les invites de port backend/frontend et configure les embeddings sur **désactivé** par défaut (choisissez `Oui` si vous prévoyez d'utiliser `deeptutor kb …` ou les outils RAG). Il génère quand même une disposition de runtime complète (`system.json`, `auth.json`, `integrations.json`, `model_catalog.json`, `main.yaml`, `agents.yaml`) et invite toujours à choisir le fournisseur LLM actif et le modèle.

<details>
<summary><b>Commandes courantes</b></summary>

```bash
deeptutor chat                                          # REPL interactif
deeptutor chat --capability deep_solve --tool rag --kb my-kb
deeptutor run chat "Expliquer la transformée de Fourier"
deeptutor run deep_solve "Résoudre x^2 = 4" --tool rag --kb my-kb
deeptutor kb create my-kb --doc textbook.pdf
deeptutor memory show
deeptutor config show
```

</details>

L'installation locale de `deeptutor-cli` ne comprend aucun actif Web ni dépendance serveur. Conservez le checkout des sources — l'installation modifiable y pointe. Pour ajouter l'application Web ultérieurement, installez le package PyPI (Option 1) et exécutez `deeptutor init` + `deeptutor start` depuis le même espace de travail.

### Référence de configuration

<details>
<summary><b>Fichiers de configuration sous <code>data/user/settings/</code></b> — référence JSON/YAML</summary>

Tout ce qui se trouve sous `data/user/settings/` est du JSON/YAML simple. La page **Paramètres** du navigateur est l'éditeur recommandé.

| Fichier | Rôle |
|:---|:---|
| `model_catalog.json` | Profils de fournisseurs LLM, embedding et recherche ; clés API ; modèles actifs |
| `system.json` | Ports backend/frontend, base API publique, CORS, vérification SSL, répertoire des pièces jointes |
| `auth.json` | Bascule d'authentification optionnelle, nom d'utilisateur, hash de mot de passe, paramètres de token/cookie |
| `integrations.json` | Paramètres d'intégration optionnels PocketBase et sidecar |
| `interface.json` | Préférences de langue / thème / barre latérale de l'interface |
| `main.yaml` | Valeurs par défaut du comportement runtime et injection de chemins |
| `agents.yaml` | Paramètres de température et de tokens pour les capacités/outils |

Le fichier `.env` à la racine du projet n'est **pas** lu comme fichier de configuration d'application. Pour une configuration de modèle minimale, ouvrez **Paramètres → Modèles**, ajoutez un profil LLM (URL de base / clé API / nom du modèle), et sauvegardez. Ajoutez un profil d'embedding uniquement si vous prévoyez d'utiliser les fonctionnalités Base de Connaissances / RAG.

</details>

## 📖 Explorer DeepTutor

La visite du README suit les surfaces du produit dans l'ordre où vous les rencontrerez le plus souvent : Chat, Partner, Co-Writer, Book, Knowledge, Space, Memory, et Paramètres. Les captures d'écran ci-dessous proviennent de l'arborescence `assets/figs` réorganisée ; les images héritées archivées ne sont intentionnellement pas utilisées ici.

### 💬 Chat — La boucle d'agent que vous utilisez vraiment

<div align="center">
<img src="../../assets/figs/webui/chat.png" alt="Espace de travail chat DeepTutor" width="900">
</div>

Chat est la capacité par défaut et l'endroit où la plupart des travaux commencent. Un seul fil peut discuter normalement, appeler des outils, s'ancrer dans des bases de connaissances sélectionnées, lire des pièces jointes, écrire des enregistrements dans le carnet, et continuer avec le même inventaire de sources d'un tour à l'autre.

<div align="center">
<img src="../../assets/figs/system/chat-agent-loop.png" alt="Boucle d'agent chat DeepTutor" width="900">
</div>

La boucle actuelle est délibérément simple : le modèle réfléchit par tours, appelle des outils lorsque c'est utile, observe les résultats des outils, et termine lorsqu'il dispose de suffisamment d'éléments. Les outils activables par l'utilisateur sont `brainstorm`, `web_search`, `paper_search` et `reason` ; les outils contextuels tels que `rag`, `read_source`, `read_memory`, `write_memory`, `read_skill`, `load_tools`, `exec`, `web_fetch`, `ask_user`, `list_notebook`, `write_note` et `github` se montent lorsque le tour dispose du bon contexte.

Chat est aussi le point de lancement pour des capacités plus profondes : `deep_solve` pour le raisonnement travaillé, `deep_question` pour la génération de questions, `deep_research` pour les rapports cités, `visualize` et `math_animator` pour les sorties visuelles, `auto` pour le routage, et `mastery_path` pour les flux de plan d'apprentissage.

### 🤝 Partner — Compagnons persistants sur le même cerveau

<div align="center">
<img src="../../assets/figs/webui/partners.png" alt="Espace de travail partners DeepTutor" width="900">
</div>

Partners remplace l'ancien moteur TutorBot par un modèle plus propre : chaque message web ou de messagerie instantanée entrant devient un tour ChatOrchestrator normal dans un espace de travail limité au partner. Il n'y a pas de cerveau de bot séparé à synchroniser.

<div align="center">
<img src="../../assets/figs/system/partners-architecture.png" alt="Architecture partners DeepTutor" width="900">
</div>

Chaque partner possède un `SOUL.md`, une sélection de modèle, des canaux, une politique d'outils, et une bibliothèque assignée. Les bases de connaissances, compétences et carnets sont copiés dans `data/partners/<id>/workspace/`, de sorte que les mêmes outils RAG, compétences, carnet et mémoire fonctionnent sans cas particuliers.

<div align="center">
<img src="../../assets/figs/webui/partners02.png" alt="Vue détaillée d'un partner DeepTutor" width="900">
</div>

La couche de canaux est pilotée par un schéma et peut se connecter aux plateformes de messagerie instantanée telles que Feishu, Telegram, Slack, DingTalk, QQ/Napcat, WeCom, WhatsApp, Zulip, Matrix et Microsoft Teams selon les extras installés et les identifiants configurés.

### ✍️ Co-Writer — Rédaction Markdown consciente de la sélection

Co-Writer est un espace de travail Markdown en vue divisée pour les rapports, tutoriels, notes et artefacts d'apprentissage longs. Les documents se sauvegardent automatiquement, affichent un aperçu en direct, et peuvent être sauvegardés dans des carnets lorsque le brouillon devient du contexte réutilisable.

Sélectionnez du texte et demandez à DeepTutor de le réécrire, développer ou raccourcir. L'agent d'édition conserve une trace des appels d'outils et peut ancrer une modification dans une base de connaissances ou des preuves web, de sorte que Co-Writer se comporte davantage comme un éditeur avec récupération qu'une boîte de texte détachée.

### 📖 Book — Livres vivants issus de vos matériaux

<p align="center">
<img src="../../assets/figs/webui/book01.png" alt="Vue de lecture de livre DeepTutor" width="31%">
&nbsp;
<img src="../../assets/figs/webui/book02.png" alt="Vue de bloc interactif de livre DeepTutor" width="31%">
&nbsp;
<img src="../../assets/figs/webui/book03.png" alt="Vue de création de livre DeepTutor" width="31%">
</p>

Book transforme les sources sélectionnées en matériel d'apprentissage interactif. Un livre peut démarrer à partir de bases de connaissances, carnets, banques de questions ou historique de chat ; le flux de création propose une structure avant que le contenu soit généré, afin que les utilisateurs puissent examiner la forme plutôt que d'accepter une sortie en une seule fois à l'aveugle.

Le BookEngine compile les pages en blocs typés : texte, sections, encadrés, quiz, cartes flash, chronologies, code, figures, HTML interactif, animations, graphes de concepts, approfondissements et notes utilisateur. Les commandes de maintenance telles que `deeptutor book health` et `deeptutor book refresh-fingerprints` aident à détecter quand les connaissances sources ont divergé des pages compilées.

### 📚 Knowledge — Bibliothèques RAG versionnées

<div align="center">
<img src="../../assets/figs/webui/knowledge.png" alt="Espace de travail de la base de connaissances DeepTutor" width="900">
</div>

Les Bases de Connaissances sont les collections de documents derrière RAG. La pile actuelle est LlamaIndex uniquement, avec une disposition de stockage `version-N` plate indexée par signature d'embedding. La ré-indexation préserve les versions antérieures et évite d'écraser un index fonctionnel pendant que de nouveaux documents sont traités.

L'espace de travail web expose les fichiers, le téléchargement, les versions d'index et les paramètres. Le CLI reflète le même cycle de vie avec `deeptutor kb list`, `info`, `create`, `add`, `search`, `set-default` et `delete`.

### 🌐 Space — Compétences, Personas et Contexte Réutilisable

<div align="center">
<img src="../../assets/figs/webui/space.png" alt="Espace de travail Space DeepTutor" width="900">
</div>

Space est la couche de bibliothèque pour le contexte réutilisable. Il rassemble les compétences créées par l'utilisateur, les personas, les carnets, l'historique de chat et les actifs de style banque de questions afin que l'agent puisse être guidé avec un contexte délibéré plutôt que des prompts ad hoc.

Les compétences sont stockées sous forme de fichiers `SKILL.md` dans l'espace de travail utilisateur et peuvent être étiquetées, modifiées, ou conservées en lecture seule lorsqu'elles sont intégrées. Les personas suivent la même idée pour le rôle et la voix. Ces actifs peuvent être assignés aux partners, référencés dans le chat, et réutilisés dans les flux d'apprentissage.

### 🧠 Memory — Personnalisation Inspectable

<div align="center">
<img src="../../assets/figs/webui/memory01.png" alt="Établi de mémoire DeepTutor" width="900">
</div>

La Mémoire est un système en trois couches enraciné dans l'espace de travail utilisateur actif : `trace/<surface>/<date>.jsonl` pour les traces d'événements L1, `L2/<surface>.md` pour les faits par surface, et `L3/<recent|profile|scope|preferences>.md` pour la synthèse inter-surfaces.

<div align="center">
<img src="../../assets/figs/webui/memory02.png" alt="Graphe de mémoire DeepTutor" width="900">
</div>

Les surfaces de mémoire supportées sont `chat`, `notebook`, `quiz`, `kb`, `book`, `tutorbot` et `cowriter`. Le nom de surface hérité `tutorbot` reste dans la couche de mémoire pour la compatibilité même si le modèle de compagnon orienté produit est maintenant Partners. L'établi vous permet d'inspecter, modifier, exécuter la consolidation, et utiliser le graphe pour remonter les affirmations synthétisées jusqu'à leurs faits de support et événements bruts.

### ⚙️ Settings — Un seul plan de contrôle

<div align="center">
<img src="../../assets/figs/webui/settings.png" alt="Espace de travail des paramètres DeepTutor" width="900">
</div>

Settings est le plan de contrôle opérationnel. Il couvre l'apparence, les ports réseau et la base API externe, les catalogues LLM et d'embedding, les fournisseurs de recherche, l'analyse MinerU, les budgets de capacités, la cadence de mémoire, les serveurs MCP, les outils intégrés et la liste des outils optionnels activés.

La plupart des paramètres utilisent un flux brouillon-et-appliquer afin que les utilisateurs puissent tester les fournisseurs avant de les valider. Les fichiers `.env` à la racine du projet sont intentionnellement ignorés ; la configuration runtime se trouve sous `data/user/settings/*.json` sauf si `DEEPTUTOR_HOME` ou `deeptutor start --home` pointe l'application ailleurs.

---

## ⌨️ DeepTutor CLI — Interface Native à l'Agent

DeepTutor est natif en CLI : le même point d'entrée `deeptutor` peut initialiser un espace de travail, démarrer l'application web, exécuter une capacité en une seule fois, ouvrir un REPL interactif, gérer les bases de connaissances, inspecter les sessions, maintenir les livres, et opérer les partners.

```bash
deeptutor run chat "Expliquer la transformée de Fourier" --tool rag --kb textbook
deeptutor run deep_solve "Résoudre x^2 = 4" --tool reason
deeptutor chat --capability deep_research --kb papers
deeptutor partner create math-tutor --soul "Tuteur de maths socratique"
deeptutor kb create calculus --doc textbook.pdf
```

<details>
<summary><b>Référence des commandes</b></summary>

| Commande | Description |
|:---|:---|
| `deeptutor init` | Créer ou mettre à jour `data/user/settings` pour l'espace de travail actuel |
| `deeptutor start [--home CHEMIN]` | Lancer le backend + le frontend ensemble |
| `deeptutor serve [--port PORT]` | Démarrer uniquement le backend FastAPI |
| `deeptutor run <capacité> <message>` | Exécuter un seul tour de capacité (`chat`, `deep_solve`, `deep_question`, `deep_research`, `visualize`, `math_animator`, `auto`, `mastery_path`) |
| `deeptutor chat` | REPL interactif avec contrôles de capacité, outil, KB, carnet et historique |
| `deeptutor partner list/create/start/stop` | Gérer les partners connectés à la messagerie instantanée |
| `deeptutor kb list/info/create/add/search/set-default/delete` | Gérer les bases de connaissances LlamaIndex |
| `deeptutor memory show/clear` | Inspecter les docs mémoire L2/L3 ou effacer la mémoire L1/toute |
| `deeptutor session list/show/open/rename/delete` | Gérer les sessions partagées |
| `deeptutor notebook list/create/show/add-md/replace-md/remove-record` | Gérer les carnets depuis des fichiers Markdown |
| `deeptutor book list/health/refresh-fingerprints` | Inspecter les livres et actualiser les empreintes de sources |
| `deeptutor plugin list/info` | Inspecter les outils et capacités enregistrés |
| `deeptutor config show` | Afficher le résumé de la configuration |
| `deeptutor provider login <fournisseur>` | Gérer la connexion OAuth des fournisseurs lorsque supporté |

</details>

La distribution CLI uniquement se trouve dans `packaging/deeptutor-cli` ; dans ce checkout, elle doit être installée depuis les sources avec `python -m pip install -e ./packaging/deeptutor-cli`. Le package public `deeptutor-cli` n'est pas actuellement disponible sur PyPI, donc la section principale Démarrage conserve le chemin d'installation depuis les sources.

---

## 👥 Multi-Utilisateurs — Déploiements Partagés

<div align="center">
<img src="../../assets/figs/webui/multi-user.png" alt="Espace de travail admin multi-utilisateurs DeepTutor" width="900">
</div>

L'authentification est optionnelle et désactivée par défaut. Lorsqu'elle est activée, DeepTutor devient un déploiement partagé avec un espace de travail admin, des espaces de travail par utilisateur, des espaces de travail de partners, et l'état système sous une seule arborescence `data/`.

```text
data/
├── user/                         # Espace de travail et paramètres admin
├── users/<uid>/                  # Portée utilisateur non-admin
│   ├── user/chat_history.db
│   ├── user/settings/interface.json
│   ├── user/workspace/{chat,co-writer,book,memory,notebook,...}
│   └── knowledge_bases/...
├── partners/<id>/workspace/      # Portée utilisateur synthétique du partner
└── system/
    ├── auth/users.json
    ├── grants/<uid>.json
    └── audit/usage.jsonl
```

Le premier utilisateur enregistré devient admin et peut configurer les catalogues de modèles, les identifiants de fournisseurs, les bases de connaissances, les compétences et les autorisations utilisateur. Les utilisateurs non-admin obtiennent un historique de chat, une mémoire, des carnets et des bases de connaissances personnelles isolés, ainsi qu'une page Paramètres expurgée ; les ressources assignées par l'admin apparaissent comme des options limitées et en lecture seule plutôt qu'exposant les clés API ou les détails internes des fournisseurs.

Pour un essai local, définissez `data/user/settings/auth.json` pour activer l'authentification, redémarrez `deeptutor start`, enregistrez le premier admin sur `/register`, puis créez des utilisateurs depuis `/admin/users` et assignez des modèles, bases de connaissances, compétences, politique d'outils, politique MCP et accès à l'exécution de code via les autorisations.

Le mode PocketBase reste une intégration mono-utilisateur dans cette arborescence ; les déploiements multi-utilisateurs doivent laisser `integrations.pocketbase_url` vide et utiliser les stores d'authentification et de session JSON/SQLite par défaut, sauf si un store utilisateur externe a été explicitement conçu pour le déploiement.

---
## 🌐 Communauté & Écosystème

DeepTutor s'appuie sur des projets open-source remarquables :

| Projet | Rôle dans DeepTutor |
|:---|:---|
| [**nanobot**](https://github.com/HKUDS/nanobot) | Moteur d'agent ultra-léger qui a propulsé le TutorBot original (Partners tourne maintenant sur la boucle d'agent chat de DeepTutor) |
| [**LlamaIndex**](https://github.com/run-llama/llama_index) | Pipeline RAG et colonne vertébrale d'indexation de documents |
| [**ManimCat**](https://github.com/Wing900/ManimCat) | Génération d'animations mathématiques pilotée par IA pour Math Animator |

**De l'écosystème HKUDS :**

| [⚡ LightRAG](https://github.com/HKUDS/LightRAG) | [🤖 AutoAgent](https://github.com/HKUDS/AutoAgent) | [🔬 AI-Researcher](https://github.com/HKUDS/AI-Researcher) | [🧬 nanobot](https://github.com/HKUDS/nanobot) |
|:---:|:---:|:---:|:---:|
| RAG Simple et Rapide | Framework d'Agent sans Code | Recherche Automatisée | Agent IA Ultra-Léger |


## 🤝 Contribuer

<div align="center">

Nous espérons que DeepTutor deviendra un cadeau pour la communauté. 🎁

<a href="https://github.com/HKUDS/DeepTutor/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=HKUDS/DeepTutor&max=999" alt="Contributeurs" />
</a>

</div>

Consultez [CONTRIBUTING.md](../../CONTRIBUTING.md) pour les directives sur la configuration de votre environnement de développement, les normes de code, et le flux de travail des pull requests.

## ⭐ Historique des étoiles

<div align="center">

<a href="https://www.star-history.com/#HKUDS/DeepTutor&type=timeline&legend=top-left">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=HKUDS/DeepTutor&type=timeline&theme=dark&legend=top-left" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=HKUDS/DeepTutor&type=timeline&legend=top-left" />
    <img alt="Graphique de l'historique des étoiles" src="https://api.star-history.com/svg?repos=HKUDS/DeepTutor&type=timeline&legend=top-left" />
  </picture>
</a>

</div>

<p align="center">
 <a href="https://www.star-history.com/hkuds/deeptutor">
  <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/badge?repo=HKUDS/DeepTutor&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/badge?repo=HKUDS/DeepTutor" />
   <img alt="Classement de l'historique des étoiles" src="https://api.star-history.com/badge?repo=HKUDS/DeepTutor" />
  </picture>
 </a>
</p>

<div align="center">

**[Data Intelligence Lab @ HKU](https://github.com/HKUDS)**

[⭐ Étoilez-nous](https://github.com/HKUDS/DeepTutor/stargazers) · [🐛 Signaler un bug](https://github.com/HKUDS/DeepTutor/issues) · [💬 Discussions](https://github.com/HKUDS/DeepTutor/discussions)

---

Sous licence [Apache License 2.0](../../LICENSE).

<p>
  <img src="https://visitor-badge.laobi.icu/badge?page_id=HKUDS.DeepTutor&style=for-the-badge&color=00d4ff" alt="Vues">
</p>

</div>
