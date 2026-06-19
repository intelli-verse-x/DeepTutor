<div align="center">

<p align="center"><img src="../../assets/figs/logo/logo.png" alt="DeepTutor ロゴ" height="56" style="vertical-align: middle;">&nbsp;<img src="../../assets/figs/logo/banner.png" alt="DeepTutor" height="48" style="vertical-align: middle;"></p>

# DeepTutor：エージェントネイティブなパーソナライズド個別指導

<p align="center">
  <a href="https://deeptutor.info" target="_blank"><img alt="Docs — deeptutor.info" src="https://img.shields.io/badge/Docs-deeptutor.info%20%E2%86%97-0A0A0A?style=for-the-badge&labelColor=F5F5F4" height="36"></a>
</p>

<a href="https://trendshift.io/repositories/17099" target="_blank"><img src="https://trendshift.io/api/badge/repositories/17099" alt="HKUDS%2FDeepTutor | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>

<p align="center">
  <a href="../../README.md"><img alt="English" height="40" src="https://img.shields.io/badge/English-CDCFD4"></a>&nbsp;
  <a href="README_CN.md"><img alt="简体中文" height="40" src="https://img.shields.io/badge/简体中文-CDCFD4"></a>&nbsp;
  <a href="README_JA.md"><img alt="日本語" height="40" src="https://img.shields.io/badge/日本語-BCDCF7"></a>&nbsp;
  <a href="README_ES.md"><img alt="Español" height="40" src="https://img.shields.io/badge/Español-CDCFD4"></a>&nbsp;
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

[機能](#-主な機能) · [はじめに](#-はじめに) · [探索](#-deeptuitorを探索する) · [CLI](#%EF%B8%8F-deeptutor-cli--エージェントネイティブインターフェース) · [エコシステム](#-エコシステム--eduhubとスキルコミュニティ) · [コミュニティ](#-コミュニティ)

</div>

---

> 🤝 **あらゆる形の貢献を歓迎します！** [`ロードマップ`](https://github.com/HKUDS/DeepTutor/issues/498) でアイテムに投票したり新しいアイデアを提案したりできます。ブランチ戦略、コーディング基準、参加方法については [貢献ガイド](../../CONTRIBUTING.md) をご覧ください。

### 📦 リリース

> **[2026.6.17]** [v1.4.6](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.6) — 4つのサーフェスを統合：SpaceはインポートできるMy Agentsとトップレベルのメモリを持つ学習ダッシュボードに、**Knowledge Center**にGraphRAG/PageIndex/LightRAGエンジン、リンクKBとObsidianマウントが追加、Settingsでドキュメント解析/音声/画像+動画が開放、LLM機能は割り当てモデルごとにゲート制御。

> **[2026.6.14]** [v1.4.5](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.5) — ガイド付き学習をチャットエージェントループ上で再構築、タイプごとの習熟度ハードゲートと`/learning`ダッシュボード、新しい拡張可能なループプラグインフレームワーク、Partnerコンバセーション用のMarkdownエクスポート/ノートブック保存。

> **[2026.6.13]** [v1.4.4](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.4) — セキュリティゲート付きの`deeptutor skill install`で[ClawHub](https://clawhub.ai/)からコミュニティスキルをインストール、知識ベースファイルの本物のブラウザ内DOCX/XLSXプレビュー。

> **[2026.6.12]** [v1.4.3](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.3) — TutorBotが**Partners**に（本番グレードIMパイプライン、15チャンネル、ライブストリーミング）、Chatが単一エージェントループへ移行、本物のユーザー単位分離、再構築されたVisualize。

<details>
<summary><b>過去のリリース（2週間以上前）</b></summary>

> **[2026.5.28]** [v1.4.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.2) — 安定性とポリッシュ：VisualizeとChatでGemini 2.5+がアンブロック、認証ルーティング修正(#485)、スムーズなストリーミングUX、最近のサイドバー、Lemonadeローカルプロバイダーサポート。

> **[2026.5.27]** [v1.4.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.1) — セキュリティと安定性：TutorBotツールサンドボックス強化、ユーザー単位リソース分離、マルチモーダル画像フォールバック、TutorBot HTTP/SSE API、v1.4.0チャット回帰修正。

> **[2026.5.22]** [v1.4.0](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.0) — v1.4 GA：オートモード、3層メモリ、エージェント型深層研究/解決/問題生成、LlamaIndex RAGリファクタリング、Visualize/Animatorマージ、再起動安全なターンランタイム。

> **[2026.5.21]** [v1.4.0-beta](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.0-beta) — 3層メモリワークベンチ(L1/L2/L3)、単一エージェントエンジンで再構築されたすべてのチャット機能、LlamaIndexのみのRAG、統合Settings + Capabilities。

> **[2026.5.10]** [v1.3.10](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.10) — リモートDockerCORS回復、SDK全体の`DISABLE_SSL_VERIFY`、安全なコードブロック引用、オプションのMatrix E2EEアドオン。

> **[2026.5.9]** [v1.3.9](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.9) — TutorBot ZulipとNVIDIA NIMサポート、安全な思考モデルルーティング、`deeptutor start`、サイドバーツールチップ、セッションストアの統一。

> **[2026.5.8]** [v1.3.8](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.8) — オプションのマルチユーザーデプロイメント：隔離されたユーザーワークスペース、管理者グラント、認証ルート、スコープ付きランタイムアクセス。

> **[2026.5.4]** [v1.3.7](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.7) — 思考モデル/プロバイダー修正、可視化された知識インデックス履歴、安全なCo-Writerクリア/テンプレート編集。

> **[2026.5.3]** [v1.3.6](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.6) — チャットとTutorBot用のカタログベースのモデル選択、安全なRAG再インデックス、OpenAI Responsesトークン制限修正、Skillsエディターバリデーション。

> **[2026.5.2]** [v1.3.5](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.5) — よりスムーズなローカル起動設定、安全なRAGクエリ、クリーンなローカル埋め込み認証、Settingsダークモードポリッシュ。

> **[2026.5.1]** [v1.3.4](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.4) — Bookページチャットの永続化と再構築フロー、チャットからBookへの参照、強化された言語/推論処理、RAGドキュメント抽出強化。

> **[2026.4.30]** [v1.3.3](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.3) — NVIDIA NIM + Gemini埋め込みサポート、チャット履歴/スキル/メモリの統合Spaceコンテキスト、セッションスナップショット、RAG再インデックス耐性。

> **[2026.4.29]** [v1.3.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.2) — 透明な埋め込みエンドポイントURL、無効な永続化ベクターのRAG再インデックス耐性、思考モデル出力のメモリクリーンアップ、Deep Solveランタイム修正。

> **[2026.4.28]** [v1.3.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.1) — 安定性：安全なRAGルーティングと埋め込みバリデーション、Docker永続化、IME安全入力、Windows/GBK堅牢性。

> **[2026.4.27]** [v1.3.0](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.0) — 再インデックスワークフロー付きのバージョン管理KBインデックス、再構築された知識ワークスペース、埋め込み自動検出と新しいアダプター、Spaceハブ。

> **[2026.4.25]** [v1.2.5](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.5) — ファイルプレビュードロワー付きの永続化チャット添付ファイル、添付ファイル対応機能パイプライン、TutorBot Markdownエクスポート。

> **[2026.4.25]** [v1.2.4](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.4) — テキスト/コード/SVG添付ファイル、ワンコマンドセットアップツアー、Markdownチャットエクスポート、コンパクトKB管理UI。

> **[2026.4.24]** [v1.2.3](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.3) — ドキュメント添付ファイル(PDF/DOCX/XLSX/PPTX)、推論思考ブロック表示、Soulテンプレートエディター、Co-Writerノートブック保存。

> **[2026.4.22]** [v1.2.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.2) — ユーザー作成Skillsシステム、チャット入力パフォーマンス全面改善、TutorBot自動起動、Book Library UI、ビジュアライゼーションフルスクリーン。

> **[2026.4.21]** [v1.2.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.1) — ステージ別トークン制限、すべてのエントリーポイントでの応答再生成、RAGとGemma互換性修正。

> **[2026.4.20]** [v1.2.0](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.0) — Book Engine「生きている本」コンパイラー、マルチドキュメントCo-Writer、インタラクティブHTMLビジュアライゼーション、Question Bank @-メンション。

> **[2026.4.18]** [v1.1.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.1.2) — スキーマ駆動Channelsタブ、RAG単一パイプライン統合、外部化チャットプロンプト。

> **[2026.4.17]** [v1.1.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.1.1) — ユニバーサル「今すぐ回答」、Co-Writerスクロール同期、統合設定パネル、ストリーミング停止ボタン。

> **[2026.4.15]** [v1.1.0](https://github.com/HKUDS/DeepTutor/releases/tag/v1.1.0) — LaTeXブロック数式全面改善、LLM診断プローブ、Docker + ローカルLLMガイダンス。

> **[2026.4.14]** [v1.1.0-beta](https://github.com/HKUDS/DeepTutor/releases/tag/v1.1.0-beta) — ブックマーク可能なセッション、Snowテーマ、WebSocketハートビートと自動再接続、埋め込みレジストリ全面改善。

> **[2026.4.13]** [v1.0.3](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.3) — ブックマークとカテゴリ付きQuestion Notebook、VisualizeでMermaid、埋め込みミスマッチ検出、Qwen/vLLM互換性、LM StudioとLlama.cppサポート、Glassテーマ。

> **[2026.4.11]** [v1.0.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.2) — SearXNGフォールバック付き検索統合、プロバイダー切り替え修正、フロントエンドリソースリーク修正。

> **[2026.4.10]** [v1.0.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.1) — Visualize機能(Chart.js/SVG)、クイズ重複防止、o4-miniモデルサポート。

> **[2026.4.10]** [v1.0.0-beta.4](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.0-beta.4) — レート制限リトライ付き埋め込み進捗トラッキング、クロスプラットフォーム依存関係修正、MIMEバリデーション修正。

> **[2026.4.8]** [v1.0.0-beta.3](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.0-beta.3) — ネイティブOpenAI/Anthropic SDK(litellm削除)、Windows Math Animatorサポート、堅牢なJSON解析、完全な中国語i18n。

> **[2026.4.7]** [v1.0.0-beta.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.0-beta.2) — ホット設定リロード、MinerUネスト出力、WebSocket修正、Python 3.11+最小要件。

> **[2026.4.4]** [v1.0.0-beta.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.0-beta.1) — エージェントネイティブアーキテクチャ書き直し(約20万行)：Tools + Capabilitiesプラグインモデル、CLIとSDK、TutorBot、Co-Writer、ガイド付き学習、永続メモリ。

> **[2026.1.23]** [v0.6.0](https://github.com/HKUDS/DeepTutor/releases/tag/v0.6.0) — セッション永続化、増分ドキュメントアップロード、柔軟なRAGパイプラインインポート、完全な中国語ローカライゼーション。

> **[2026.1.18]** [v0.5.2](https://github.com/HKUDS/DeepTutor/releases/tag/v0.5.2) — RAG-Anything用Doclingサポート、ロギングシステム最適化、バグ修正。

> **[2026.1.15]** [v0.5.0](https://github.com/HKUDS/DeepTutor/releases/tag/v0.5.0) — 統合サービス構成、知識ベースごとのRAGパイプライン選択、問題生成全面改善、サイドバーカスタマイズ。

> **[2026.1.9]** [v0.4.0](https://github.com/HKUDS/DeepTutor/releases/tag/v0.4.0) — マルチプロバイダーLLMと埋め込みサポート、新しいホームページ、RAGモジュール分離、環境変数リファクタリング。

> **[2026.1.5]** [v0.3.0](https://github.com/HKUDS/DeepTutor/releases/tag/v0.3.0) — 統合PromptManagerアーキテクチャ、GitHub Actions CI/CD、GHCRの事前構築Dockerイメージ。

> **[2026.1.2]** [v0.2.0](https://github.com/HKUDS/DeepTutor/releases/tag/v0.2.0) — Dockerデプロイメント、Next.js 16とReact 19アップグレード、WebSocketセキュリティ強化、重大な脆弱性修正。

</details>

### 📰 ニュース

- **2026-05-22** 🌐 公式ドキュメントサイトが [**deeptutor.info**](https://deeptutor.info/) で公開 — ガイド、リファレンス、機能ツアーを一か所に。
- **2026-04-19** 🎉 111日間で20kスター達成！真にパーソナライズされたインテリジェント個別指導に向けた支援に感謝します。
- **2026-04-10** 📄 arXivに論文を公開 — DeepTutorの設計とアイデアについては[プレプリント](https://arxiv.org/abs/2604.26962)をご覧ください。
- **2026-02-06** 🚀 わずか39日間で10kスター達成！素晴らしいコミュニティに心から感謝します。
- **2026-01-01** 🎊 あけましておめでとうございます！[Discord](https://discord.gg/eRsjPgMU4t)、[WeChat](https://github.com/HKUDS/DeepTutor/issues/78)、または[Discussions](https://github.com/HKUDS/DeepTutor/discussions)に参加して一緒にDeepTutorを形作りましょう。
- **2025-12-29** 🎓 DeepTutor正式リリース！

## ✨ 主な機能

DeepTutorは、個別指導、問題解決、クイズ生成、研究、ビジュアライゼーション、習熟度練習を1つの拡張可能なシステムに統合したエージェントネイティブな学習ワークスペースです。

- **すべてのモードで1つのランタイム** — Chat、Quiz、Research、Visualize、Solve、Mastery Pathが同じエージェントループで実行されるため、エンジンではなく目的を切り替えます。コンテキストは学習者とともに移動します。
- **接続された学習コンテキスト** — 知識ベース、本、Co-Writerの下書き、ノートブック、問題バンク、ペルソナ、Memoryが孤立したツールに閉じ込められることなく、すべてのワークフローで利用可能です。
- **サブエージェントとPartners** — 任意のターンからライブのClaude Code、Codex、またはPartnerに相談（または過去の会話をインポート）し、同じブレインで永続的なIMコンパニオンを実行します。
- **マルチエンジン知識** — LlamaIndex、PageIndex、GraphRAG、LightRAG、またはリンクされたObsidianボールトにまたがるバージョン管理されたRAGライブラリ（プラグ可能なドキュメント解析付き）。
- **拡張可能なツールとスキル** — 組み込みツール、MCPサーバー、画像/ビデオ/音声生成モデル、EduHubからインストール可能なコミュニティスキル。
- **検査可能なメモリ** — L1トレース、L2サーフェスサマリー、L3合成によりパーソナライズが可視化・編集可能となり、Memory Graphですべての主張を証拠まで追跡できます。

---

## 🚀 はじめに

DeepTutorは4つのインストールパスを提供しています。すべてのパスは同じワークスペースレイアウトを共有します。設定はデプロイするディレクトリ下の`data/user/settings/`に保存されます（明示的に設定した場合は`DEEPTUTOR_HOME`/`deeptutor start --home`の下）。完全なアプリの場合は **ワークスペースディレクトリの選択 → インストール → `deeptutor init` → `deeptutor start`** がお勧めのフローです。

<details>
<summary><b>オプション1 — PyPIからインストール</b> · クローン不要のフルローカルWebアプリ + CLI</summary>

クローン不要のフルローカルWebアプリ + CLI。**Python 3.11+** とPATH上の**Node.js 20+**ランタイムが必要です。

```bash
mkdir -p my-deeptutor && cd my-deeptutor
pip install -U deeptutor
deeptutor init     # ポート + LLMプロバイダー + オプション埋め込みを設定
deeptutor start    # バックエンド + フロントエンドを起動; ターミナルを開いたまま
```

`deeptutor start`後、ターミナルに出力されたフロントエンドURLを開いてください（デフォルトは[http://127.0.0.1:3782](http://127.0.0.1:3782)）。`Ctrl+C`でバックエンドとフロントエンドを同時に停止できます。

</details>

<details>
<summary><b>オプション2 — ソースからインストール</b> · チェックアウトに対して開発</summary>

チェックアウトに対して開発する場合。CIとDockerに合わせて**Python 3.11+**と**Node.js 22 LTS**を使用してください。

```bash
git clone https://github.com/HKUDS/DeepTutor.git
cd DeepTutor

# venvを作成(macOS/Linux)。Windows PowerShell:
#   py -3.11 -m venv .venv ; .\.venv\Scripts\Activate.ps1
python3 -m venv .venv && source .venv/bin/activate
python -m pip install --upgrade pip

# バックエンド + フロントエンドの依存関係をインストール
python -m pip install -e .
( cd web && npm ci --legacy-peer-deps )

deeptutor init
deeptutor start
```

<details>
<summary><b>Conda環境</b>（<code>venv</code>の代わり）</summary>

```bash
conda create -n deeptutor python=3.11
conda activate deeptutor
python -m pip install --upgrade pip
```

</details>

<details>
<summary><b>オプションインストールエクストラ</b> — dev / partners / matrix / math-animator</summary>

```bash
pip install -e ".[dev]"             # テスト/lintツール
pip install -e ".[partners]"        # Partner IMチャンネルSDK + MCPクライアント
pip install -e ".[matrix]"          # MatrixチャンネルE2EE/libolmなし
pip install -e ".[matrix-e2e]"      # Matrix E2EE; libolmが必要
pip install -e ".[math-animator]"   # Maninアドオン; LaTeX/ffmpeg/システムライブラリが必要
```

</details>

</details>

<details>
<summary><b>オプション3 — Docker</b> · 自己完結型コンテナ1つ</summary>

フルWebアプリ用のコンテナ1つ。GitHub Container Registryのイメージ：

```bash
docker run --rm --name deeptutor \
  -p 127.0.0.1:3782:3782 \
  -p 127.0.0.1:8001:8001 \
  -v deeptutor-data:/app/data \
  ghcr.io/hkuds/deeptutor:latest
```

> ⚠️ **`3782`と`8001`の両方をマップしてください。** `3782`はWeb UIを提供し、`8001`はブラウザが直接呼び出すFastAPIバックエンドです。

[http://127.0.0.1:3782](http://127.0.0.1:3782)を開いてください。

<details>
<summary><b>ホスト上のOllama / LM Studio / llama.cpp / vLLM / Lemonadeへの接続</b></summary>

Docker内では、`localhost`はホストマシンではなくコンテナ自体です。ホスト上で実行中のモデルサービスに接続するには：

```bash
docker run --rm --name deeptutor \
  -p 127.0.0.1:3782:3782 -p 127.0.0.1:8001:8001 \
  --add-host=host.docker.internal:host-gateway \
  -v deeptutor-data:/app/data \
  ghcr.io/hkuds/deeptutor:latest
```

**Settings → Models**でプロバイダーのBase URLを`host.docker.internal`に向けてください：
- Ollama LLM: `http://host.docker.internal:11434/v1`
- LM Studio: `http://host.docker.internal:1234/v1`
- llama.cpp: `http://host.docker.internal:8080/v1`
- Lemonade: `http://host.docker.internal:13305/api/v1`

</details>

</details>

<details>
<summary><b>オプション4 — CLIのみ</b> · ソースチェックアウトからWeb UIなし</summary>

```bash
git clone https://github.com/HKUDS/DeepTutor.git
cd DeepTutor

python3 -m venv .venv-cli && source .venv-cli/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ./packaging/deeptutor-cli
deeptutor init --cli
deeptutor chat
```

</details>

<details>
<summary><b>設定リファレンス</b> — <code>data/user/settings/</code>下の設定ファイル（JSON/YAML）</summary>

| ファイル | 目的 |
|:---|:---|
| `model_catalog.json` | LLM、埋め込み、検索プロバイダープロフィール；APIキー；アクティブモデル |
| `system.json` | バックエンド/フロントエンドポート、公開APIベース、CORS、SSL検証 |
| `auth.json` | オプション認証トグル、ユーザー名、パスワードハッシュ |
| `integrations.json` | オプションのPocketBaseとサイドカー統合設定 |
| `interface.json` | UIの言語/テーマ/サイドバー設定 |
| `main.yaml` | ランタイム動作のデフォルトとパス注入 |
| `agents.yaml` | 機能/ツールのtemperatureとトークン設定 |

</details>

## 📖 DeepTutorを探索する

日常的に使用するメインサーフェスから始めましょう：Chat、Partners、マイエージェント、Co-Writer、Book、Knowledge Center、Learning Space、Memory、Settings。

<div align="center">
<img src="../../assets/figs/web-1.4.6+/OVERVIEW.png" alt="DeepTutorホーム — すべてのサーフェスを含むチャットワークスペース" width="900">
</div>

### 💬 Chat — 実際に使うエージェントループ

<div align="center">
<img src="../../assets/figs/web-1.4.6+/home/00-overview.png" alt="DeepTutorチャットワークスペース" width="900">
</div>

Chatはデフォルト機能であり、ほとんどの作業が始まる場所です。1つのスレッドで通常の会話、ツールの呼び出し、選択した知識ベースへのグラウンディング、添付ファイルの読み取り、画像生成、サブエージェントとの相談、ノートブックレコードの書き込みが可能で、ターンをまたいで同じコンテキストを維持します。

<div align="center">
<img src="../../assets/figs/system/chat-agent-loop.png" alt="DeepTutorチャットエージェントループ" width="900">
</div>

ループは意図的にシンプルです。モデルはラウンドで考え、役に立つときにツールを呼び出し、結果を観察し、ツールなしのメッセージで終了します。`ask_user`は特別で、推測する代わりに、エージェントはターンを一時停止し、構造化された明確化の質問をして、あなたが答えた後に再開できます。

**スティッキーセッションコンテキスト**（サブエージェント、知識ベース、ペルソナ、モデル、音声）はコンポーザーツールバーに常駐し、ターンをまたいで持続します。**ワンタイム参照**（ファイル、チャット履歴、本、ノートブック、問題バンク、インポートしたエージェント）は単一のターンのために`+`メニューから追加します。

Chatはより深い機能へのローンチポイントでもあります：問題生成には**Quiz**、引用付きレポートには**Research**、チャート/図/アニメーションには**Visualize**、推論問題解決には**Solve**（「その他の機能」下）、学習計画フローには**Mastery Path**。

### 🤝 Partner — 同じブレインで動く永続コンパニオン

<div align="center">
<img src="../../assets/figs/web-1.4.6+/partners/00-partners%20overview.png" alt="DeepTutor Partnersワークスペース" width="900">
</div>

Partnersは独自のソウル、モデルポリシー、ライブラリ、メモリ、チャンネルを持つ永続コンパニオンです。別個のボットエンジンではありません。Webまたはそれぞれのソースからの受信メッセージは、パートナースコープのワークスペース内の通常の`ChatOrchestrator`ターンになります。Partnerは「個性を持ったチャットであり、IMの入り口」です。

<div align="center">
<img src="../../assets/figs/system/partners-architecture.png" alt="DeepTutor Partnersアーキテクチャ" width="900">
</div>

各Partnerには`SOUL.md`、モデル選択、チャンネル、ツールポリシー、割り当てられたライブラリがあります。知識ベース、スキル、ノートブックは`data/partners/<id>/workspace/`にコピーされるため、同じRAG、スキル、ノートブック、メモリツールが特別なケースなしに機能します。Partnerはオーナーのメモリを読み取れますが、自分自身のメモリにのみ書き込めます。

<div align="center">
<img src="../../assets/figs/web-1.4.6+/partners/02-IM%20config%20for%20each%20partner.png" alt="Partner ごとのIMチャンネル設定" width="900">
</div>

チャンネル層はスキーマ駆動で、インストール済みエクストラと設定された認証情報に応じて、Feishu、Telegram、Slack、DingTalk、QQ/NapCat、WeCom、WhatsApp、Zulip、Matrix、Microsoft Teamsなどのプラットフォームに接続できます。PartnerはサブエージェントとしてもMyAgentsに接続でき、通常のチャットターンから相談できます。

### 🧑‍🚀 マイエージェント — 他のエージェントと相談・インポート

<div align="center">
<img src="../../assets/figs/web-1.4.6+/myagents/00-overview.png" alt="DeepTutor マイエージェントワークスペース" width="900">
</div>

マイエージェントは他のエージェントをDeepTutorのコンテキストにし、2つの異なることを行います。**ライブエージェントを接続** — マシン上のClaude CodeやCodex CLI、またはPartnerの1つ — してチャットターン内から相談できます。DeepTutorは実際に他のエージェントを*実行*し、`consult_subagent`ツールを介してその作業をActivityパネルにストリーミングします。Agentチップ（または`@`入力）で選択し、相談で取れるラウンド数を設定します。

<div align="center">
<img src="../../assets/figs/web-1.4.6+/home/08-subagent%20demo%20with%20claude%20code.png" alt="Claude Codeサブエージェントをライブで相談" width="900">
</div>

**過去の会話をインポート** — 既存のClaude CodeやCodexの履歴を名前付き、検索可能、再開可能なエージェントとして取り込みます。インポートする日を選択してください。更新すると再同期されます。チャットターンから`+` → マイエージェントでインポートした会話を参照でき、DeepTutorはそれをサードパーティのトランスクリプトとして読み取ります。

### ✍️ Co-Writer — 選択対応Markdownドラフトツール

<div align="center">
<img src="../../assets/figs/web-1.4.6+/co-writer/00-overview.png" alt="DeepTutor Co-Writerワークスペース" width="900">
</div>

Co-Writerはレポート、チュートリアル、メモ、長文学習コンテンツのための分割表示Markdownワークスペースです。ドキュメントは自動保存され、ライブプレビュー（KaTeXの数式、図表フェンス）を表示し、下書きが再利用可能なコンテキストになったときにノートブックに保存できます。

<div align="center">
<img src="../../assets/figs/web-1.4.6+/co-writer/01-edit%20panel.png" alt="Co-Writerエディターとライブプレビュー" width="900">
</div>

その定義的なアイデアは**外科的編集**です。テキストの範囲を選択し、DeepTutorに書き直し、拡張、または短縮を依頼します。編集エージェントは知識ベースまたはウェブの証拠に基づいて変更をグラウンドし、ツール呼び出しのトレースを保持し、各変更を承認/拒否の差分として表示します。

### 📖 Book — 素材から生きている本を作成

<div align="center">
<img src="../../assets/figs/web-1.4.6+/book/00-book_overview.png" alt="DeepTutor Bookライブラリ" width="900">
</div>

Bookは選択したソースをインタラクティブな**生きている本**に変換します。静的なPDFではなく、タイプ指定されたブロックから構築された読書環境です。知識ベース、ノートブック、問題バンク、チャット履歴から本を開始できます。

<p align="center">
<img src="../../assets/figs/web-1.4.6+/book/01-book-demo-quiz%20card.png" alt="Bookクイズブロック" width="31%">
&nbsp;
<img src="../../assets/figs/web-1.4.6+/book/02-book-demo-manim%20video.png" alt="Book Maninアニメーションブロック" width="31%">
&nbsp;
<img src="../../assets/figs/web-1.4.6+/book/03-book-demo%20interactive%20module.png" alt="Bookインタラクティブウィジェットブロック" width="31%">
</p>

各章はタイプ指定されたブロックにコンパイルされます — テキスト、コールアウト、クイズ、フラッシュカード、タイムライン、コード、図、インタラクティブHTML、アニメーション、概念グラフ、詳細解説、ユーザーノート — 各ページには独自のPage Chatがあります。

### 📚 Knowledge Center — マルチエンジンRAGライブラリ

<div align="center">
<img src="../../assets/figs/web-1.4.6+/knowledge/00-overview.png" alt="DeepTutor Knowledge Center" width="900">
</div>

知識ベースはRAGの背後にあるドキュメントコレクションです。特徴は**検索エンジンの選択**です：**LlamaIndex**（デフォルト、ローカルベクター + BM25）、**PageIndex**（ホスト型、ページレベル引用付き推論検索）、**GraphRAG**と**LightRAG**（知識グラフ検索）、またはリンクされた**Obsidian**ボールト。各KBは1つのエンジンでインデックスされます。

<div align="center">
<img src="../../assets/figs/web-1.4.6+/knowledge/01-create%20knowledge%20base.png" alt="知識ベースの作成" width="900">
</div>

KBを作成する際は、**新規作成**（ドキュメントをアップロードして新しいインデックスを構築）または**既存をリンク**（再インデックスなしで既に構築されたインデックスを再利用）を選択します。ドキュメント解析（Text-only、MinerU、Docling、markitdown）は**Settings → Knowledge Base**で選択します。

### 🌐 Learning Space — スキル、ペルソナ、再利用可能なコンテキスト

<div align="center">
<img src="../../assets/figs/web-1.4.6+/learning-space/00-overview.png" alt="DeepTutor Learning Spaceハブ" width="900">
</div>

Learning Spaceはライブラリとパーソナライゼーション層です。**会話と素材**にはチャット履歴、ノートブック、問題バンクが含まれます。**パーソナライゼーション**には習熟パス、ペルソナ（*peer*、*research-assistant*、*teacher*などの動作プリセット）、スキル（モデルがオンデマンドで読み取る`SKILL.md`プレイブック）が含まれます。

<div align="center">
<img src="../../assets/figs/web-1.4.6+/learning-space/07-%20download%20skills%20from%20eduhub.png" alt="EduHubからスキルをインポート" width="900">
</div>

すべてのスキルを自分で書く必要はありません。**EduHubからインポート**でコミュニティカタログを参照し、セキュリティゲートを通じてスキルをライブラリに直接ダウンロードできます（[エコシステム](#-エコシステム--eduhubとスキルコミュニティ)参照）。

### 🧠 Memory — 検査可能なパーソナライゼーション

<div align="center">
<img src="../../assets/figs/web-1.4.6+/memory/00-overview.png" alt="DeepTutor Memoryの概要" width="900">
</div>

Memoryはファイルバックの3層システムで、読み取り、キュレーション、監査が可能です — 意図的に隠されたベクターストアではありません。**L1**はワークスペースミラーに加えた追記のみのイベントトレース（`trace/<surface>/<date>.jsonl`）、**L2**はサーフェスごとのキュレートされた事実（`L2/<surface>.md`）、**L3**はクロスサーフェス合成（`L3/<profile|recent|scope>.md`）です。

<div align="center">
<img src="../../assets/figs/web-1.4.6+/memory/01-3%20layer%20memory%20graph.png" alt="DeepTutor Memoryグラフ" width="900">
</div>

Memory Graphはピラミッド全体を表示します。L3合成が中心、L2が中間リング、L1トレースが外側。Memoryは`chat`、`notebook`、`quiz`、`kb`、`book`、partner、`cowriter`サーフェスで追跡されます。コンソリデーターのUpdate / Audit / Dedupバジェットは**Settings → Memory**で調整します。

### ⚙️ Settings — ワンコントロールプレーン

<div align="center">
<img src="../../assets/figs/web-1.4.6+/settings/00-setting%20overview.png" alt="DeepTutor Settingsハブ" width="900">
</div>

Settingsはオペレーションコントロールプレーンです。ライブステータスストリップ（バックエンド、LLM、埋め込み、検索）とエリアごとのカードがあります：**外観**（テーマ + UI言語）、**ネットワーク**（APIベース、ポート、CORS）、**モデル**（LLM、埋め込み、検索、TTS、STT、画像生成、動画生成）、**Knowledge Base**（ドキュメント解析エンジン）、**Chat**（ツール、MCPサーバー、機能パラメーター）、**Partners & Agents**（ターンから相談できるサブエージェント）、**Memory**（コンソリデーターのバジェット）。

<div align="center">
<img src="../../assets/figs/web-1.4.6+/settings/01-appearance%20settings.png" alt="DeepTutor外観設定とテーマ" width="900">
</div>

ほとんどのセクションはドラフトと適用フローを使用するため、コミットする前にプロバイダーをテストできます。4つのテーマが箱に入っています：Default、Cream、Dark、Glass。

---

## ⌨️ DeepTutor CLI — エージェントネイティブインターフェース

1つの`deeptutor`バイナリで2つの使い方：ターミナルで生活する人のためのインタラクティブな**REPL**と、DeepTutorをツールとして動かす他のエージェントのための構造化された**JSON**。

```bash
deeptutor chat                                              # インタラクティブREPL
deeptutor chat --capability deep_solve --kb my-kb --tool rag
deeptutor run chat "Explain the Fourier transform" --tool rag --kb textbook
deeptutor run deep_research "Survey 2026 papers on RAG" \
  --config mode=report --config depth=standard
```

<details>
<summary><b>コマンドリファレンス</b></summary>

| コマンド | 説明 |
|:---|:---|
| `deeptutor init` | 現在のワークスペースの`data/user/settings`を作成または更新 |
| `deeptutor start [--home PATH]` | バックエンド + フロントエンドを一緒に起動 |
| `deeptutor serve [--port PORT]` | FastAPIバックエンドのみ起動 |
| `deeptutor run <capability> <message>` | 単一機能ターンを実行(`chat`、`deep_solve`など)；`--format json`でNDJSON出力 |
| `deeptutor chat` | インタラクティブREPL |
| `deeptutor partner list/create/start/stop` | IM接続Partnersを管理 |
| `deeptutor kb list/info/create/add/search/set-default/delete` | 知識ベースを管理 |
| `deeptutor skill search/install/list/remove/login/publish/update` | スキルを管理、ハブからインストール、自分のスキルを公開（デフォルトは`eduhub:<slug>`） |
| `deeptutor memory show/clear` | L2/L3メモリドキュメントを検査またはL1/全メモリをクリア |
| `deeptutor session list/show/open/rename/delete` | 共有セッションを管理 |
| `deeptutor notebook list/create/show/add-md/replace-md/remove-record` | Markdownファイルからノートブックを管理 |
| `deeptutor book list/health/refresh-fingerprints` | 本を検査してソースフィンガープリントを更新 |
| `deeptutor plugin list/info` | 登録済みツールと機能を検査 |
| `deeptutor config show` | 設定サマリーを出力 |
| `deeptutor provider login <provider>` | プロバイダー認証(`openai-codex` OAuthログイン) |

</details>

---

## 👥 マルチユーザー — 共有デプロイメント

認証はデフォルトでオフです。オンにすると、1つの`data/`ツリーで管理者ワークスペース、分離されたユーザーワークスペース、Partnerワークスペースが同居します。

```text
data/
├── user/                    # 管理者ワークスペース + グローバル設定
├── users/<uid>/             # ユーザー単位スコープ：チャット履歴、メモリ、ノートブック、KB
├── partners/<id>/workspace/ # Partner（合成ユーザー）スコープ
└── system/                  # auth/users.json · grants/<uid>.json · audit/usage.jsonl
```

**最初に登録したユーザーが管理者**になり、モデルカタログ、プロバイダー認証情報、共有知識ベース、スキル、ユーザー単位グラントを所有します。他のユーザーは分離されたワークスペースと編集されたSettingsページを取得します。

**有効化：** `data/user/settings/auth.json`で認証をオンにし、`deeptutor start`を再起動し、`/register`で最初の管理者を登録し、`/admin/users`からユーザーを追加し、グラントを通じてモデル、KB、スキル、ツール/MCPポリシー、コード実行アクセスを割り当てます。

---

## 🧩 エコシステム — EduHubとスキルコミュニティ

DeepTutorスキルはオープンな**Agent-Skills**フォーマット（`SKILL.md`プレイブックと任意の参照ファイルを含むフォルダ）を使用します。DeepTutorには**[EduHub](https://eduhub.deeptutor.info/)** — 独自の教育特化スキルレジストリ — がデフォルトハブとして組み込まれています。

<details>
<summary><b>EduHub — DeepTutorのスキルエコシステム</b></summary>

[**EduHub**](https://eduhub.deeptutor.info/)は、DeepTutorが教育指向のエージェントスキルを共有するために立ち上げたコミュニティハブです — ソクラテス式チューター、フラッシュカードビルダー、エッセイフィードバック、試験ブループリント、概念説明者など。DeepTutorに組み込まれているため、設定不要です。

**検索とインストール** — ブラウザで**Learning Space → スキル → EduHubからインポート**を開いてカタログを参照し、スキルをライブラリに直接ダウンロードできます。ターミナルから：

```bash
deeptutor skill search "socratic tutor"               # EduHubを検索（デフォルトハブ）
deeptutor skill install socratic-tutor                # 取得 → 検証 → 登録
deeptutor skill install eduhub:socratic-tutor@1.2.0   # ハブとバージョンを指定
deeptutor skill list                                  # ハブの出所付きローカルスキル
```

**自分のスキルを公開** — `SKILL.md`をパッケージ化してコミュニティに共有：

```bash
deeptutor skill login                                 # EduHubへのブラウザサインイン
deeptutor skill publish ./my-skill                    # インタラクティブ：トラック + タグを選択してアップロード
deeptutor skill update                                # ロールバックまたは新バージョンをリリース
```

EduHubはまたスタンドアロンのClawHub互換レジストリでもあり、DeepTutor以外のエージェント（Claude Code、Codexなど）が`eduhub` CLI経由で直接使用できます — `npx eduhub install socratic-tutor`。

</details>

<details>
<summary><b>インポートセキュリティゲート</b></summary>

ソースに関わらず、すべてのインポートはワークスペースに触れる前に**同じセキュリティゲート**を通過します：

- レジストリの**セキュリティ判定**が最初にチェックされます — フラグが立てられたパッケージは`--allow-unverified`を渡さない限り拒否されます；
- アーカイブはテキスト/スクリプト**サフィックスホワイトリスト**の後ろで防御的に展開されます（zip-slip / zip-bombガード）；
- フロントマターが正規化され、`always:`が**削除**されます；
- 出所 — ハブ、バージョン、判定、インストール時間 — が`.hub-lock.json`に記録されます。

マルチユーザーデプロイメントでは、インストールは管理者のみです。

</details>

<details>
<summary><b>ClawHubとも互換性あり</b></summary>

DeepTutorはオープンなAgent-Skillsフォーマットに対応しているため、**[ClawHub](https://clawhub.ai/)**も一流のソースとして機能します — EduHubとともに組み込まれています。ハブプレフィックスで選択：

```bash
deeptutor skill search "git release notes" --hub clawhub
deeptutor skill install clawhub:git-release-notes@1.0.1
```

`settings/skill_hubs.json`にさらにレジストリを追加できます。

</details>

---

## 🌐 コミュニティ

### 📮 連絡先

DeepTutorは[Bingxi Zhao](https://github.com/pancacake)が[HKUDS](https://github.com/HKUDS)グループ内でリードするオープンソースプロジェクトです。**完全にオープンソースの形で**コミュニティと共に反復されています。現在、**いかなる有料オンライン製品も存在しません**。議論、アイデア、協力については**bingxizhao39@gmail.com**までお気軽にご連絡ください。

### 🙏 感謝

[**Chao Huang**](https://sites.google.com/view/chaoh)（HKUデータインテリジェンスラボディレクター）、HKUDSのラボメイト — 特に[**Jiahao Zhang**](https://github.com/zzhtx258)、[**Zirui Guo**](https://github.com/LarFii)、[**Xubin Ren**](https://github.com/Re-bin) — の温かいサポートに心から感謝します。また、毎日DeepTutorを形作ってくれる**オープンソースコミュニティ**にも深く感謝します。

DeepTutorは優れたオープンソースプロジェクトの肩の上に立っています：

| プロジェクト | 役割 / インスピレーション |
|:---|:---|
| [**LlamaIndex**](https://github.com/run-llama/llama_index) | RAGパイプラインとドキュメントインデックスのバックボーン |
| [**nanobot**](https://github.com/HKUDS/nanobot) | オリジナルTutorBotを動かした超軽量エージェントエンジン *(HKUDS)* |
| [**LightRAG**](https://github.com/HKUDS/LightRAG) | シンプルで高速なRAG *(HKUDS)* |
| [**AutoAgent**](https://github.com/HKUDS/AutoAgent) | ゼロコードエージェントフレームワーク *(HKUDS)* |
| [**AI-Researcher**](https://github.com/HKUDS/AI-Researcher) | 自動化研究パイプライン *(HKUDS)* |
| [**OpenClaw**](https://github.com/openclaw/openclaw) | ClawHubの背後にあるオープンエージェントゲートウェイとスキルエコシステム |
| [**Codex**](https://github.com/openai/codex) | CLIワークフローにインスピレーションを与えたエージェントネイティブコーディングCLI |
| [**Claude Code**](https://github.com/anthropics/claude-code) | DeepTutorエージェントループにインスピレーションを与えたエージェントコーディングCLI |
| [**ManimCat**](https://github.com/Wing900/ManimCat) | Math AnimatorのためのAI駆動数学アニメーション生成 |

### 🗺️ ロードマップと貢献

DeepTutorが反復し改善し続け、最終的にオープンソースコミュニティへのギフトになることを望んでいます。[**ロードマップ**](https://github.com/HKUDS/DeepTutor/issues/498)は継続的に更新されています。貢献したい方は、ブランチ戦略、コーディング基準、参加方法について[**貢献ガイド**](../../CONTRIBUTING.md)をご覧ください。

<div align="center">

DeepTutorがコミュニティへのギフトになることを願っています。 🎁

<a href="https://github.com/HKUDS/DeepTutor/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=HKUDS/DeepTutor&max=999" alt="Contributors" />
</a>

</div>

<div align="center">

<a href="https://www.star-history.com/#HKUDS/DeepTutor&type=timeline&legend=top-left">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=HKUDS/DeepTutor&type=timeline&theme=dark&legend=top-left" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=HKUDS/DeepTutor&type=timeline&legend=top-left" />
    <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=HKUDS/DeepTutor&type=timeline&legend=top-left" />
  </picture>
</a>

</div>

<div align="center">

[Apache License 2.0](../../LICENSE)に基づきライセンス。

<p>
  <img src="https://visitor-badge.laobi.icu/badge?page_id=HKUDS.DeepTutor&style=for-the-badge&color=00d4ff" alt="Views">
</p>

</div>
