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

<p align="center">
  <a href="https://github.com/HKUDS/DeepTutor/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/HKUDS/DeepTutor?style=social"></a>
  <a href="https://github.com/HKUDS/DeepTutor/releases"><img alt="GitHub release" src="https://img.shields.io/github/v/release/HKUDS/DeepTutor"></a>
  <a href="https://pypi.org/project/deeptutor/"><img alt="PyPI" src="https://img.shields.io/pypi/v/deeptutor"></a>
  <a href="https://github.com/HKUDS/DeepTutor/blob/main/LICENSE"><img alt="License" src="https://img.shields.io/github/license/HKUDS/DeepTutor"></a>
</p>

<p align="center">
  <a href="#-fonctionnalités-clés">Fonctionnalités</a> ·
  <a href="#-démarrage">Démarrer</a> ·
  <a href="#-explorer">Explorer</a> ·
  <a href="#-cli">CLI</a> ·
  <a href="#-écosystème--eduhub-et-la-communauté-de-compétences">Écosystème</a> ·
  <a href="#-communauté">Communauté</a>
</p>

</div>

---

## 🚀 Versions Récentes

> **[2026.6.17]** [v1.4.6](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.6) — Space devient un tableau de bord d'apprentissage avec **Mes Agents** importables et Memory en niveau supérieur ; le **Centre de Connaissances** ajoute les moteurs GraphRAG / PageIndex / LightRAG ainsi que les KB liées et les montages Obsidian ; les Paramètres ouvrent l'analyse de documents / la voix / l'image+vidéo ; les capacités LLM sont contrôlées par modèle assigné.

> **[2026.6.14]** [v1.4.5](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.5) — Apprentissage Guidé reconstruit sur la boucle d'agent de chat avec des portes de maîtrise strictes par type, un nouveau framework loop-plugin extensible, ainsi que l'export Markdown / sauvegarde dans le bloc-notes pour les conversations Partner.

> **[2026.6.13]** [v1.4.4](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.4) — Installez des compétences communautaires depuis [ClawHub](https://clawhub.ai/) avec `deeptutor skill install` derrière une porte de sécurité, plus de vraies prévisualisations DOCX/XLSX dans le navigateur pour les fichiers de base de connaissances.

<details>
<summary>Versions plus anciennes</summary>

> **[2026.6.12]** [v1.4.3](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.3) — TutorBot devient **Partners** sur un pipeline IM de qualité production (15 canaux, streaming en direct), Chat passe à une seule boucle d'agent, une véritable isolation par utilisateur, et un Visualize reconstruit.

> **[2026.6.10]** [v1.4.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.2) — Refonte du pipeline de recherche approfondie (réduction de 45% des lignes de code), unification de l'infrastructure des capacités avec la page `/settings/capabilities`, refonte complète de Visualize avec des SVG intégrés et réparation automatique, prévisualisation de fichiers DOCX/XLSX côté client, et panneau d'activité.

> **[2026.6.7]** [v1.4.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.1) — Sécurité sandbox, API HTTP TutorBot, pipeline multimodal deux étapes (corrige les images perdues Doubao/VolcEngine), site public avec documentation.

> **[2026.5.18]** [v1.4.0](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.0) — Chat passe à une boucle d'agent à tour unique, Animator fusionné dans Visualize, refonte du pipeline de recherche approfondie.

> **[2026.4.30]** [v1.3.0](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.0) — Maîtrise de la lecture de livres, génération de vidéos d'animation Manim, amélioration de la recherche multi-sources.

> **[2026.4.10]** [v1.2.0](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.0) — Article publié sur arXiv, améliorations du chat coopératif, Co-Écrivain bêta.

> **[2026.3.1]** [v1.1.0](https://github.com/HKUDS/DeepTutor/releases/tag/v1.1.0) — Quiz adaptatif, Chemin de Maîtrise, intégration de mémoire L2/L3.

> **[2026.1.15]** [v1.0.0](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.0) — Première version stable : Chat, Recherche, Visualize, base de connaissances RAG, mémoire L1.

</details>

---

## 📰 Actualités

- **2026-05-22** : Site de documentation officiel en ligne sur [deeptutor.info](https://deeptutor.info)
- **2026-04-19** : 20 000 étoiles en 111 jours
- **2026-04-10** : Article publié sur arXiv
- **2026-02-06** : 10 000 étoiles en 39 jours
- **2026-01-01** : Bonne Année
- **2025-12-29** : DeepTutor officiellement lancé

---

## ✨ Fonctionnalités Clés

- **Un runtime pour tous les modes** — Chat, Quiz, Research, Visualize, Solve et Mastery Path partagent la même boucle d'agent ; vous changez l'objectif, pas le moteur, et le contexte suit l'apprenant.
- **Contexte d'apprentissage connecté** — Bases de connaissances, livres, brouillons Co-Writer, carnets, banques de questions, personas et Memory restent disponibles dans tous les flux de travail au lieu de vivre dans des outils isolés.
- **Sous-agents et Partners** — Consultez Claude Code, Codex ou un Partner en direct depuis n'importe quel tour ; compagnons IM persistants sur le même cerveau.
- **Connaissances multi-moteur** — Bibliothèques RAG versionnées : LlamaIndex, PageIndex, GraphRAG, LightRAG ou un vault Obsidian lié, avec analyse de documents enfichable.
- **Outils et compétences extensibles** — Outils intégrés, serveurs MCP, modèles génératifs (images, vidéos, voix), et compétences communautaires installables depuis EduHub.
- **Mémoire inspectable** — Traces L1, résumés L2, synthèse L3 ; le Memory Graph retrace chaque affirmation jusqu'à son evidence.

---

## 🛠 Démarrage

### Option 1 — PyPI (recommandé)

```bash
pip install deeptutor
deeptutor start
```

### Option 2 — Depuis les sources

```bash
git clone https://github.com/HKUDS/DeepTutor.git
cd DeepTutor
pip install -e .
deeptutor start
```

### Option 3 — Docker

```bash
docker pull hkuds/deeptutor:latest
docker run -p 7860:7860 -v $(pwd)/data:/app/data hkuds/deeptutor:latest
```

### Option 4 — CLI uniquement

```bash
pip install deeptutor
deeptutor chat   # Démarre une session de chat dans le terminal
```

<details>
<summary>Configuration Conda (optionnel)</summary>

```bash
conda create -n deeptutor python=3.11
conda activate deeptutor
pip install deeptutor
deeptutor start
```

</details>

<details>
<summary>Extras optionnels</summary>

```bash
# Avec support MinerU pour l'analyse de documents
pip install deeptutor[mineru]

# Avec support GraphRAG
pip install deeptutor[graphrag]

# Toutes les dépendances optionnelles
pip install deeptutor[all]
```

</details>

<details>
<summary>Docker avec Ollama (modèles locaux)</summary>

```bash
# Démarrer Ollama séparément
ollama serve

# Exécuter DeepTutor en pointant vers Ollama local
docker run -p 7860:7860 \
  -e OLLAMA_BASE_URL=http://host.docker.internal:11434 \
  -v $(pwd)/data:/app/data \
  hkuds/deeptutor:latest
```

</details>

<details>
<summary>Référence de configuration</summary>

La configuration d'exécution vit sous `data/user/settings/*.json`. Les variables d'environnement clés :

| Variable | Description |
|----------|-------------|
| `DEEPTUTOR_HOME` | Répertoire de données personnalisé |
| `DEEPTUTOR_PORT` | Port du serveur (défaut : 7860) |
| `DEEPTUTOR_HOST` | Adresse d'écoute (défaut : 0.0.0.0) |

Lancez avec un répertoire home personnalisé :

```bash
deeptutor start --home /chemin/vers/data
```

Les fichiers `.env` à la racine du projet sont intentionnellement ignorés ; la configuration d'exécution vit sous `data/user/settings/*.json` sauf si `DEEPTUTOR_HOME` ou `deeptutor start --home` pointe l'application ailleurs.

</details>

---

## 🗺 Explorer

DeepTutor est organisé autour de surfaces interconnectées — chacune est un mode de travail distinct qui partage le même contexte, la même mémoire et les mêmes outils.

<p align="center">
  <img src="../../assets/figs/web-1.4.6+/OVERVIEW.png" alt="Aperçu DeepTutor" width="100%">
</p>

---

### 💬 Chat

<p align="center">
  <img src="../../assets/figs/web-1.4.6+/home/00-overview.png" alt="Aperçu du Chat" width="100%">
</p>

Chat est la capacité par défaut et là où commence la plupart du travail. Un seul fil peut discuter normalement, appeler des outils, s'ancrer dans des bases de connaissances sélectionnées, lire des pièces jointes et des images, générer des visuels, consulter des sous-agents, écrire des enregistrements dans le bloc-notes et continuer avec le même contexte à travers les tours.

La boucle est délibérément simple : le modèle réfléchit en rounds, appelle des outils quand c'est utile, observe les résultats et termine avec un message sans outil. `ask_user` est spécial — plutôt que de deviner, l'agent peut mettre le tour en pause, poser une question de clarification structurée, et reprendre une fois que vous répondez.

Les outils basculables par l'utilisateur sont `brainstorm`, `web_search`, `paper_search`, `reason` et `geogebra_analysis` — plus `imagegen` et `videogen` une fois que vous avez configuré le modèle de génération correspondant. Les outils contextuels tels que `rag`, `read_source`, `read_memory`, `write_memory`, `read_skill`, `load_tools`, `exec`, `web_fetch`, `ask_user`, `list_notebook`, `write_note`, `github` et `consult_subagent` se montent automatiquement quand le tour a le bon contexte.

Le contexte se présente en deux types : le contexte de session persistant (sous-agent, KB, persona, modèle, voix) vit sur la barre d'outils du compositeur et persiste entre les tours ; les références ponctuelles (fichiers, historique de chat, livres, carnets, banque de questions, agents importés) proviennent du menu + pour un seul tour.

Chat est aussi le point de lancement pour des capacités plus profondes : Quiz pour la génération de questions, Research pour les rapports cités, Visualize pour les graphiques/diagrammes/animations, Solve pour le raisonnement guidé et Mastery Path pour les flux de plans d'apprentissage.

<p align="center">
  <img src="../../assets/figs/system/chat-agent-loop.png" alt="Boucle d'agent de chat" width="80%">
</p>

---

### 🤝 Partner

<p align="center">
  <img src="../../assets/figs/web-1.4.6+/partners/00-partners%20overview.png" alt="Aperçu des Partners" width="100%">
</p>

Les Partners sont des compagnons persistants avec leur propre âme, politique de modèle, bibliothèque, mémoire et canaux. Ce ne sont pas un moteur de bot séparé : chaque message web ou IM entrant devient un tour normal de `ChatOrchestrator` dans un espace de travail à portée partner. Un partner est « un chat qui a une personnalité et un numéro de téléphone. »

Chaque partner a un `SOUL.md`, une sélection de modèle, des canaux, une politique d'outils et une bibliothèque assignée. Les bases de connaissances, les compétences et les carnets sont copiés dans `data/partners/<id>/workspace/`, de sorte que les mêmes outils RAG, compétence, carnet et mémoire fonctionnent sans cas particuliers. Un partner lit la mémoire de son propriétaire mais n'écrit que la sienne.

La couche de canaux est pilotée par schéma et peut se connecter à Feishu, Telegram, Slack, DingTalk, QQ/NapCat, WeCom, WhatsApp, Zulip, Matrix et Microsoft Teams. Un partner peut également être connecté comme sous-agent et consulté depuis un tour de chat normal — voir Mes Agents ci-dessous.

<p align="center">
  <img src="../../assets/figs/system/partners-architecture.png" alt="Architecture des Partners" width="80%">
</p>

<p align="center">
  <img src="../../assets/figs/web-1.4.6+/partners/02-IM%20config%20for%20each%20partner.png" alt="Configuration IM par partner" width="80%">
</p>

---

### 🧑‍🚀 Mes Agents

<p align="center">
  <img src="../../assets/figs/web-1.4.6+/myagents/00-overview.png" alt="Aperçu de Mes Agents" width="100%">
</p>

Mes Agents transforme d'autres agents en contexte pour DeepTutor, et fait deux choses distinctes. Connectez un agent en direct — un Claude Code ou Codex CLI sur votre machine, ou l'un de vos Partners — et consultez-le depuis l'intérieur d'un tour de chat via l'outil `consult_subagent` : DeepTutor exécute réellement l'autre agent et diffuse son travail dans le panneau d'Activité. Sélectionnez-le avec la puce Agent (ou tapez @), et définissez combien de rounds la consultation peut prendre.

Importez des conversations passées — apportez votre historique Claude Code et Codex existant comme des agents nommés, consultables et reprenables. Choisissez les jours à importer ; l'actualisation les re-synchronise. Référencez une conversation importée depuis n'importe quel tour de chat via + → Mes Agents, et DeepTutor la lit comme une transcription tierce — elle reste leur conversation, pas la voix propre de DeepTutor.

<p align="center">
  <img src="../../assets/figs/web-1.4.6+/home/08-subagent%20demo%20with%20claude%20code.png" alt="Démo sous-agent avec Claude Code" width="80%">
</p>

---

### ✍️ Co-Writer

<p align="center">
  <img src="../../assets/figs/web-1.4.6+/co-writer/00-overview.png" alt="Aperçu du Co-Writer" width="100%">
</p>

Co-Writer est un espace de travail Markdown à vue divisée pour les rapports, tutoriels, notes et artefacts d'apprentissage longs. Les documents se sauvegardent automatiquement et affichent un aperçu en direct (math KaTeX, clôtures de diagrammes), et peuvent être sauvegardés dans des carnets quand un brouillon devient un contexte réutilisable.

Son idée directrice est l'édition chirurgicale : sélectionnez une plage et demandez à DeepTutor de la réécrire, l'étendre ou la raccourcir. L'agent d'édition peut ancrer le changement dans une base de connaissances ou des preuves web, garde une trace de ses appels d'outils, et montre chaque changement comme un diff accepter/rejeter — rien ne se place donc jusqu'à ce que vous l'approuviez.

<p align="center">
  <img src="../../assets/figs/web-1.4.6+/co-writer/01-edit%20panel.png" alt="Panneau d'édition du Co-Writer" width="80%">
</p>

---

### 📖 Livre (Book)

<p align="center">
  <img src="../../assets/figs/web-1.4.6+/book/00-book_overview.png" alt="Aperçu du Livre" width="100%">
</p>

<p align="center">
  <img src="../../assets/figs/web-1.4.6+/book/01-book-demo-quiz%20card.png" alt="Carte quiz" width="31%">&nbsp;
  <img src="../../assets/figs/web-1.4.6+/book/02-book-demo-manim%20video.png" alt="Vidéo Manim" width="31%">&nbsp;
  <img src="../../assets/figs/web-1.4.6+/book/03-book-demo%20interactive%20module.png" alt="Module interactif" width="31%">
</p>

Livre transforme des sources sélectionnées en un livre interactif vivant — pas un PDF statique, mais un environnement de lecture construit à partir de blocs typés. Un livre peut démarrer depuis des bases de connaissances, des carnets, des banques de questions ou l'historique de chat ; le flux de création propose un plan de chapitre avant que le contenu soit généré, vous pouvez donc revoir la forme au lieu d'accepter une sortie en un seul coup aveugle.

Chaque chapitre se compile en blocs typés — texte, encadrés, quiz, fiches, chronologies, code, figures, HTML interactif, animations, graphes de concepts, approfondissements et notes utilisateur — et chaque page a son propre Chat de Page. Les blocs sont modifiables : insérez, déplacez, régénérez ou changez le type d'un bloc sans réécrire le chapitre.

---

### 📚 Centre de Connaissances

<p align="center">
  <img src="../../assets/figs/web-1.4.6+/knowledge/00-overview.png" alt="Aperçu du Centre de Connaissances" width="100%">
</p>

Les bases de connaissances sont les collections de documents derrière le RAG — elles ancrent les tours de Chat, les éditions Co-Writer, la génération de Livre et les conversations Partner. Ce qui est distinctif est un choix de moteurs de récupération : LlamaIndex (par défaut, vecteur local + BM25), PageIndex (hébergé, récupération par raisonnement avec citations au niveau de la page), GraphRAG et LightRAG (récupération par graphe de connaissances), ou un vault Obsidian lié que le tuteur lit et écrit en place. Chaque KB est indexée par un moteur.

En créant une KB, vous créez soit une nouvelle (uploadez des documents et construisez un index frais) soit liez une existante (réutilisez un index construit ailleurs, lu en place sans re-indexation). La re-indexation écrit un nouveau répertoire plat version-N et conserve les précédents, donc un index fonctionnel n'est jamais détruit en milieu de reconstruction. L'analyse de documents — Text-only, MinerU, Docling ou markitdown — est choisie dans Paramètres → Base de Connaissances, avec les téléchargements de modèles locaux désactivés par défaut.

<p align="center">
  <img src="../../assets/figs/web-1.4.6+/knowledge/01-create%20knowledge%20base.png" alt="Créer une base de connaissances" width="80%">
</p>

---

### 🌐 Espace d'Apprentissage

<p align="center">
  <img src="../../assets/figs/web-1.4.6+/learning-space/00-overview.png" alt="Aperçu de l'Espace d'Apprentissage" width="100%">
</p>

L'Espace d'Apprentissage est la couche de bibliothèque et de personnalisation — là où vivent les choses qui persistent. Conversations & Matériaux contient votre historique de chat, vos carnets et une banque de questions (chaque question sauvegardée conserve votre réponse, la réponse de référence et une explication). La personnalisation contient les parcours de maîtrise, les personas (préréglages de comportement tels que pair, assistant de recherche, enseignant) et les compétences (livrets de jeu SKILL.md que le modèle lit à la demande). Tout ici peut être réutilisé depuis Chat, Partners, Co-Writer et Livre.

Vous n'avez pas à écrire chaque compétence vous-même — Importer depuis EduHub parcourt le catalogue communautaire et télécharge une compétence directement dans votre bibliothèque via une porte de sécurité.

<p align="center">
  <img src="../../assets/figs/web-1.4.6+/learning-space/07-%20download%20skills%20from%20eduhub.png" alt="Télécharger des compétences depuis EduHub" width="80%">
</p>

---

### 🧠 Mémoire

<p align="center">
  <img src="../../assets/figs/web-1.4.6+/memory/00-overview.png" alt="Aperçu de la Mémoire" width="100%">
</p>

La Mémoire est un système en trois couches sauvegardé sur fichier que vous pouvez lire, organiser et auditer — délibérément pas un store vectoriel caché. L1 est le miroir de l'espace de travail plus une trace d'événements en ajout seul (`trace/<surface>/<date>.jsonl`) ; L2 sont des faits organisés par surface (`L2/<surface>.md`) ; L3 est la synthèse inter-surfaces (`L3/<profile|recent|scope>.md`). Parce que L2 cite L1 et L3 cite L2, rien dans votre profil n'est sans compte rendu.

Le Memory Graph montre toute la pyramide — la synthèse L3 au centre, L2 dans l'anneau du milieu, les traces L1 à l'extérieur — vous pouvez donc retracer n'importe quelle affirmation synthétisée jusqu'à l'événement brut exact qui la sous-tend. La Mémoire est suivie sur les surfaces chat, carnets, quiz, kb, livre, partner et cowriter ; les budgets Mise à jour / Audit / Déduplication du consolidateur sont réglés dans Paramètres → Mémoire.

<p align="center">
  <img src="../../assets/figs/web-1.4.6+/memory/01-3%20layer%20memory%20graph.png" alt="Graphe de mémoire à 3 couches" width="80%">
</p>

---

### ⚙️ Paramètres

<p align="center">
  <img src="../../assets/figs/web-1.4.6+/settings/00-setting%20overview.png" alt="Aperçu des Paramètres" width="100%">
</p>

Les Paramètres sont le plan de contrôle opérationnel, avec une bande de statut en direct (Backend, LLM, Embedding, Recherche) et une carte par zone : Apparence (thème + langue de l'interface), Réseau (base d'API, ports, CORS), Modèles (LLM, Embedding, Recherche, Texte-à-Parole, Parole-à-Texte, Génération d'Images, Génération de Vidéos), Base de Connaissances (moteur d'analyse de documents), Chat (outils, serveurs MCP, paramètres par capacité), Partners & Agents (les sous-agents que vous pouvez consulter depuis un tour) et Mémoire (les budgets du consolidateur).

La plupart des sections utilisent un flux brouillon-et-application, vous pouvez donc tester un fournisseur avant de vous y engager. Quatre thèmes sont livrés dans la boîte — Default, Cream, Dark et Glass. Les fichiers `.env` à la racine du projet sont intentionnellement ignorés ; la configuration d'exécution vit sous `data/user/settings/*.json` sauf si `DEEPTUTOR_HOME` ou `deeptutor start --home` pointe l'application ailleurs.

<p align="center">
  <img src="../../assets/figs/web-1.4.6+/settings/01-appearance%20settings.png" alt="Paramètres d'apparence" width="80%">
</p>

---

## 💻 CLI

DeepTutor est également entièrement utilisable depuis le terminal. Après `pip install deeptutor`, toutes les commandes sont disponibles sous `deeptutor`.

```bash
deeptutor start              # Démarrer le serveur web (port par défaut : 7860)
deeptutor chat               # Session de chat interactive dans le terminal
deeptutor skill install socratic-tutor   # Installer une compétence depuis EduHub
deeptutor --help             # Afficher toute l'aide
```

### Référence des commandes

| Commande | Description |
|----------|-------------|
| `deeptutor start [--home DIR] [--port PORT]` | Démarrer le serveur web DeepTutor |
| `deeptutor chat` | Démarrer une session de chat en mode terminal |
| `deeptutor status` | Afficher l'état du serveur et les services configurés |
| `deeptutor stop` | Arrêter le serveur en cours d'exécution |
| `deeptutor config` | Afficher ou modifier la configuration d'exécution |
| `deeptutor skill search/install/list/remove/login/publish/update` | Gérer les compétences, installer depuis les hubs et publier les siennes (`eduhub:<slug>` par défaut) |
| `deeptutor user create/list/grant` | Gérer les utilisateurs et les attributions (mode multi-utilisateur) |
| `deeptutor export` | Exporter les données de l'espace de travail |
| `deeptutor upgrade` | Mettre à jour DeepTutor vers la dernière version |

---

## 👥 Multi-Utilisateur

L'authentification est désactivée par défaut — DeepTutor fonctionne en mode mono-utilisateur. Activez-la et un seul arbre `data/` héberge un espace de travail administrateur, des espaces de travail per-utilisateur isolés et des espaces de travail partner côte à côte :

```
data/
├── user/                    # Espace de travail administrateur + paramètres globaux
├── users/<uid>/             # Portée par utilisateur : historique de chat, mémoire, carnets, KB
├── partners/<id>/workspace/ # Portée partner (utilisateur synthétique)
└── system/                  # auth/users.json · grants/<uid>.json · audit/usage.jsonl
```

Le premier utilisateur enregistré devient administrateur et possède les catalogues de modèles, les identifiants de fournisseur, les bases de connaissances partagées, les compétences et les attributions par utilisateur. Tous les autres obtiennent un espace de travail isolé et une page de Paramètres expurgée — les modèles, KB et compétences assignés par l'administrateur apparaissent comme des options à portée, en lecture seule, jamais comme des clés d'API brutes.

Activez-le : activez l'auth dans `data/user/settings/auth.json`, redémarrez `deeptutor start`, enregistrez le premier administrateur sur `/register`, puis ajoutez des utilisateurs depuis `/admin/users` et attribuez des modèles, KB, compétences, politique d'outils/MCP et accès à l'exécution de code via des attributions.

---

## 🧩 Écosystème — EduHub et la Communauté de Compétences

Les compétences DeepTutor utilisent le format ouvert Agent-Skills — un dossier avec un livret de jeu `SKILL.md` (frontmatter YAML + Markdown) et des fichiers de référence optionnels. DeepTutor inclut EduHub (https://eduhub.deeptutor.info/) comme hub par défaut — notre registre de compétences axé sur l'éducation câblé directement.

<details>
<summary>EduHub — l'écosystème de compétences de DeepTutor</summary>

EduHub est le hub communautaire lancé par DeepTutor pour partager des compétences d'agent orientées enseignement — tuteurs socratiques, constructeurs de fiches, retours sur les essais, plans d'examen, explicateurs de concepts, et plus encore. Il est intégré à DeepTutor, il n'y a donc rien à configurer : un slug nu ou un préfixe `eduhub:` le résout.

**Trouver et installer** — dans le navigateur, ouvrez Espace d'Apprentissage → Compétences → Importer depuis EduHub pour parcourir le catalogue et télécharger une compétence directement dans votre bibliothèque. Depuis le terminal :

```bash
deeptutor skill search "socratic tutor"               # rechercher sur EduHub (le hub par défaut)
deeptutor skill install socratic-tutor                # récupérer → vérifier → enregistrer
deeptutor skill install eduhub:socratic-tutor@1.2.0   # épingler un hub et une version
deeptutor skill list                                  # compétences locales avec leur provenance de hub
```

**Publiez la vôtre** — emballez un `SKILL.md` et partagez-le avec la communauté :

```bash
deeptutor skill login                                 # connexion navigateur à EduHub
deeptutor skill publish ./my-skill                    # interactif : choisir une piste + étiquettes, puis uploader
deeptutor skill update                                # revenir en arrière ou publier une nouvelle version
```

EduHub est également un registre autonome compatible ClawHub, de sorte que les agents qui ne sont pas DeepTutor (Claude Code, Codex, …) peuvent l'utiliser directement via le CLI eduhub — `npx eduhub install socratic-tutor`.

</details>

<details>
<summary>La porte de sécurité d'importation</summary>

Quelle que soit la source, chaque importation passe la même porte de sécurité avant que quoi que ce soit ne touche votre espace de travail :

- le verdict de sécurité du registre est vérifié en premier — les paquets signalés sont refusés sauf si vous passez `--allow-unverified` ;
- les archives sont extraites défensivement (protections zip-slip / zip-bomb) derrière une liste blanche de suffixes texte/script, donc les binaires n'atterrissent jamais dans l'espace de travail ;
- le frontmatter est normalisé et `always:` est toujours supprimé, donc une compétence téléchargée ne peut jamais se forcer dans chaque prompt système ;
- la provenance — hub, version, verdict et heure d'installation — est écrite dans `.hub-lock.json` pour les audits et les mises à jour.

Dans les déploiements multi-utilisateur, l'installation est réservée à l'administrateur.

</details>

<details>
<summary>Également compatible avec ClawHub (--hub clawhub)</summary>

Parce que DeepTutor parle le format ouvert Agent-Skills, [ClawHub](https://clawhub.ai/) fonctionne aussi comme une source de première classe — il est intégré aux côtés d'EduHub. Choisissez-le avec le préfixe hub :

```bash
deeptutor skill search "git release notes" --hub clawhub
deeptutor skill install clawhub:git-release-notes@1.0.1
```

Ajoutez d'autres registres dans `settings/skill_hubs.json`.

</details>

---

## 🌍 Communauté

### Contact & Équipe

DeepTutor est dirigé par **Bingxi Zhao** ([@pancacake](https://github.com/pancacake)) au sein du groupe HKUDS. C'est un projet open-source — aucun produit payant, aucun service géré. Pour tout contact direct : [bingxizhao39@gmail.com](mailto:bingxizhao39@gmail.com)

Nous remercions chaleureusement **Chao Huang**, les collègues du laboratoire HKUDS (**Jiahao Zhang**, **Zirui Guo**, **Xubin Ren**) et la communauté open-source au sens large pour leur soutien continu.

### Projets Liés

| Projet | Rôle dans DeepTutor |
|--------|---------------------|
| [LlamaIndex](https://github.com/run-llama/llama_index) | Moteur RAG par défaut |
| [nanobot](https://github.com/HKUDS/nanobot) | Moteur TutorBot original (HKUDS) |
| [LightRAG](https://github.com/HKUDS/LightRAG) | Récupération par graphe de connaissances (HKUDS) |
| [AutoAgent](https://github.com/HKUDS/AutoAgent) | Recherche agent (HKUDS) |
| [AI-Researcher](https://github.com/HKUDS/AI-Researcher) | Recherche approfondie (HKUDS) |
| [OpenClaw](https://github.com/clawhub/openclaw) | Format Agent-Skills (ClawHub) |
| [Codex](https://github.com/openai/codex) | CLI qui a inspiré l'intégration |
| [Claude Code](https://github.com/anthropics/claude-code) | A inspiré la boucle d'agent |
| [ManimCat](https://github.com/HKUDS/ManimCat) | Animateur mathématique |

### Feuille de Route & Contribution

- Feuille de route publique : [Issue #498](https://github.com/HKUDS/DeepTutor/issues/498)
- Guide de contribution : [CONTRIBUTING.md](../../CONTRIBUTING.md)
- Signalez des bugs ou proposez des fonctionnalités via les [Issues GitHub](https://github.com/HKUDS/DeepTutor/issues)

<a href="https://github.com/HKUDS/DeepTutor/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=HKUDS/DeepTutor" />
</a>

---

## ⭐ Historique des Étoiles

<div align="center">

<a href="https://star-history.com/#HKUDS/DeepTutor&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=HKUDS/DeepTutor&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=HKUDS/DeepTutor&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=HKUDS/DeepTutor&type=Date" />
 </picture>
</a>

</div>

---

<div align="center">

Apache 2.0 License · <a href="https://github.com/HKUDS/DeepTutor/blob/main/LICENSE">LICENSE</a>

<img src="https://visitor-badge.laobi.icu/badge?page_id=HKUDS.DeepTutor&style=for-the-badge&color=00d4ff" alt="Views">

</div>
