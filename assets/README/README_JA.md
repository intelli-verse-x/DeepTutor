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

[機能](#-主な機能) · [はじめに](#-はじめに) · [探索する](#-deeptutor-を探索する) · [CLI](#%EF%B8%8F-deeptutor-cli--エージェントネイティブインターフェース) · [マルチユーザー](#-マルチユーザーと共有デプロイ) · [コミュニティ](#-コミュニティとエコシステム)

</div>

---

> 🤝 **あらゆる形でのコントリビューションを歓迎します！** [`Roadmap`](https://github.com/HKUDS/DeepTutor/issues/498) でロードマップアイテムへの投票や新しい提案ができます。ブランチ戦略、コーディング規約、はじめ方については [Contributing Guide](../../CONTRIBUTING.md) をご覧ください。

### 📦 リリース

> **[2026.6.12]** [v1.4.3](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.3) — TutorBot が本番グレードの IM パイプライン上でライブストリーミング返信と 15 チャンネルを持つ **Partners** に進化。Chat が単一エージェントループに移行し、マルチユーザーデプロイの真のユーザーごとの分離を実現。Visualize がローカルのバリデート＋リペア機能付きで再構築。Co-writer、ファイルビューワー、MinerU クラウド解析、CLI にわたるアップグレードも含む。ドキュメントは [deeptutor.info](https://deeptutor.info/) で全面刷新。

> **[2026.5.28]** [v1.4.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.2) — v1.4.1 の安定性・ポリッシュ改善：Visualize と Chat で Gemini 2.5+ のブロック解除、ContextVar 認証ルーティング修正 (#485)、推論＋ネイティブツールのラベルプロトコル強化、すべてのチャット画面でのスムースストリーミング UX、新しい折りたたみ可能なリーセントサイドバー、Lemonade ローカルプロバイダーサポート。

> **[2026.5.27]** [v1.4.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.1) — セキュリティ・安定性パッチ：TutorBot ツールサンドボックスのロックダウン、ユーザーごとのリソース分離、ビジョン対応プロバイダー向けマルチモーダル画像フォールバック、TutorBot と通信するための HTTP/SSE API、v1.4.0 チャット後退バグの修正。

> **[2026.5.22]** [v1.4.0](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.0) — v1.4 の GA 版：Auto Mode、三層 Memory、エージェント型 Deep Research / Solve / Question、LlamaIndex RAG リファクタリング、Visualize/Animator マージ、推論努力の正規化、ツールスキーマのフォールバック、再起動安全なターンランタイム。

<details>
<summary><b>過去のリリース（2週間以上前）</b></summary>

> **[2026.5.21]** [v1.4.0-beta](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.0-beta) — 三層 Memory ワークベンチ（L1/L2/L3）、すべてのチャット機能を単一エージェントエンジン上で再構築、LlamaIndex のみの RAG、統合 Settings + Capabilities 画面。

> **[2026.5.10]** [v1.3.10](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.10) — リモート Docker の CORS 復旧、SDK プロバイダー全体での `DISABLE_SSL_VERIFY`、より安全なコードブロック引用、オプションの Matrix E2EE アドオン。

> **[2026.5.9]** [v1.3.9](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.9) — TutorBot の Zulip と NVIDIA NIM サポート、より安全な思考モデルルーティング、`deeptutor start`、サイドバーツールチップ、セッションストアの同等性。

> **[2026.5.8]** [v1.3.8](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.8) — 分離されたユーザーワークスペース、管理者グラント、認証ルート、スコープ付きランタイムアクセスを備えたオプションのマルチユーザーデプロイ。

> **[2026.5.4]** [v1.3.7](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.7) — 思考モデル/プロバイダーの修正、可視 Knowledge インデックス履歴、より安全な Co-Writer のクリア/テンプレート編集。

> **[2026.5.3]** [v1.3.6](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.6) — チャットと TutorBot 向けカタログベースのモデル選択、より安全な RAG 再インデックス、OpenAI Responses トークン制限の修正、Skills エディタのバリデーション。

> **[2026.5.2]** [v1.3.5](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.5) — よりスムーズなローカル起動設定、より安全な RAG クエリ、クリーンなローカル埋め込み認証、Settings ダークモードのポリッシュ。

> **[2026.5.1]** [v1.3.4](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.4) — Book ページチャットの永続化と再構築フロー、チャットから Book への参照、より強固な言語/推論処理、RAG ドキュメント抽出の堅牢化。

> **[2026.4.30]** [v1.3.3](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.3) — NVIDIA NIM + Gemini 埋め込みサポート、チャット履歴/スキル/メモリのための統合 Space コンテキスト、セッションスナップショット、RAG 再インデックスの耐性強化。

> **[2026.4.29]** [v1.3.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.2) — 透明な埋め込みエンドポイント URL、無効な永続化ベクターに対する RAG 再インデックスの耐性、思考モデル出力のメモリクリーンアップ、Deep Solve ランタイム修正。

> **[2026.4.28]** [v1.3.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.1) — 安定性：より安全な RAG ルーティング＆埋め込みバリデーション、Docker 永続化、IME 安全な入力、Windows/GBK の堅牢性。

> **[2026.4.27]** [v1.3.0](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.0) — バージョン管理された KB インデックスと再インデックスワークフロー、Knowledge ワークスペースの再構築、新アダプターを使った埋め込み自動検出、Space ハブ。

> **[2026.4.25]** [v1.2.5](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.5) — ファイルプレビュードロワー付きの永続チャット添付ファイル、添付ファイル対応ケイパビリティパイプライン、TutorBot Markdown エクスポート。

> **[2026.4.25]** [v1.2.4](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.4) — テキスト/コード/SVG 添付ファイル、ワンコマンドセットアップツアー、Markdown チャットエクスポート、コンパクトな KB 管理 UI。

> **[2026.4.24]** [v1.2.3](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.3) — ドキュメント添付ファイル（PDF/DOCX/XLSX/PPTX）、推論思考ブロック表示、Soul テンプレートエディタ、Co-Writer の notebook 保存。

> **[2026.4.22]** [v1.2.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.2) — ユーザー作成 Skills システム、チャット入力パフォーマンスの大幅改善、TutorBot 自動起動、Book Library UI、ビジュアライゼーション全画面表示。

> **[2026.4.21]** [v1.2.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.1) — ステージごとのトークン制限、すべてのエントリーポイントでのレスポンス再生成、RAG と Gemma の互換性修正。

> **[2026.4.20]** [v1.2.0](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.0) — Book Engine「生きた本」コンパイラ、マルチドキュメント Co-Writer、インタラクティブ HTML ビジュアライゼーション、Question Bank の @メンション。

> **[2026.4.18]** [v1.1.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.1.2) — スキーマ駆動の Channels タブ、RAG シングルパイプライン統合、外部化されたチャットプロンプト。

> **[2026.4.17]** [v1.1.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.1.1) — ユニバーサル「今すぐ回答」、Co-Writer スクロール同期、統合設定パネル、ストリーミング停止ボタン。

> **[2026.4.15]** [v1.1.0](https://github.com/HKUDS/DeepTutor/releases/tag/v1.1.0) — LaTeX ブロック数式の大幅改善、LLM 診断プローブ、Docker + ローカル LLM ガイダンス。

> **[2026.4.14]** [v1.1.0-beta](https://github.com/HKUDS/DeepTutor/releases/tag/v1.1.0-beta) — ブックマーク可能なセッション、Snow テーマ、WebSocket ハートビート＆自動再接続、埋め込みレジストリの大幅改善。

> **[2026.4.13]** [v1.0.3](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.3) — ブックマーク＆カテゴリ付き Question Notebook、Visualize での Mermaid、埋め込みミスマッチ検出、Qwen/vLLM 互換性、LM Studio と llama.cpp サポート、Glass テーマ。

> **[2026.4.11]** [v1.0.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.2) — SearXNG フォールバック付き検索統合、プロバイダー切り替え修正、フロントエンドリソースリーク修正。

> **[2026.4.10]** [v1.0.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.1) — Visualize ケイパビリティ（Chart.js/SVG）、クイズ重複防止、o4-mini モデルサポート。

> **[2026.4.10]** [v1.0.0-beta.4](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.0-beta.4) — レート制限リトライ付き埋め込み進捗追跡、クロスプラットフォーム依存関係修正、MIME バリデーション修正。

> **[2026.4.8]** [v1.0.0-beta.3](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.0-beta.3) — ネイティブ OpenAI/Anthropic SDK（litellm 廃止）、Windows Math Animator サポート、堅牢な JSON 解析、完全な中国語 i18n。

> **[2026.4.7]** [v1.0.0-beta.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.0-beta.2) — ホット設定リロード、MinerU ネスト出力、WebSocket 修正、Python 3.11+ 最小要件。

> **[2026.4.4]** [v1.0.0-beta.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.0-beta.1) — エージェントネイティブアーキテクチャの書き直し（約20万行）：Tools + Capabilities プラグインモデル、CLI & SDK、TutorBot、Co-Writer、Guided Learning、永続メモリ。

> **[2026.1.23]** [v0.6.0](https://github.com/HKUDS/DeepTutor/releases/tag/v0.6.0) — セッション永続化、増分ドキュメントアップロード、柔軟な RAG パイプラインインポート、完全な中国語ローカライズ。

> **[2026.1.18]** [v0.5.2](https://github.com/HKUDS/DeepTutor/releases/tag/v0.5.2) — RAG-Anything 向け Docling サポート、ログシステムの最適化、バグ修正。

> **[2026.1.15]** [v0.5.0](https://github.com/HKUDS/DeepTutor/releases/tag/v0.5.0) — 統合サービス設定、ナレッジベースごとの RAG パイプライン選択、質問生成の大幅改善、サイドバーカスタマイズ。

> **[2026.1.9]** [v0.4.0](https://github.com/HKUDS/DeepTutor/releases/tag/v0.4.0) — マルチプロバイダー LLM＆埋め込みサポート、新ホームページ、RAG モジュールの分離、環境変数リファクタリング。

> **[2026.1.5]** [v0.3.0](https://github.com/HKUDS/DeepTutor/releases/tag/v0.3.0) — 統合 PromptManager アーキテクチャ、GitHub Actions CI/CD、GHCR 上のビルド済み Docker イメージ。

> **[2026.1.2]** [v0.2.0](https://github.com/HKUDS/DeepTutor/releases/tag/v0.2.0) — Docker デプロイ、Next.js 16 & React 19 アップグレード、WebSocket セキュリティ強化、重大な脆弱性修正。

</details>

### 📰 ニュース

> **[2026.5.22]** 🌐 公式ドキュメントサイトが [**deeptutor.info**](https://deeptutor.info/) で公開されました — ガイド、リファレンス、ケイパビリティツアーがすべて一か所に。

> **[2026.4.19]** 🎉 111 日で 20,000 スターに到達しました！素晴らしいサポートに感謝します — すべての人に真にパーソナライズされたインテリジェントな個別指導を目指して継続的に改善してまいります。

> **[2026.4.10]** 📄 論文が arXiv で公開されました！DeepTutor の設計とアイデアについては [プレプリント](https://arxiv.org/abs/2604.26962) をご覧ください。

> **[2026.4.4]** お久しぶりです！✨ DeepTutor v1.0.0 がついにリリースされました — エージェントネイティブな進化として、ゼロから書き直されたアーキテクチャ、TutorBot、Apache-2.0 ライセンスの下での柔軟なモード切り替えを特徴としています。新たな章が始まり、私たちの物語は続きます！

> **[2026.2.6]** 🚀 わずか 39 日で 10,000 スターに到達しました！素晴らしいコミュニティの皆様に心より感謝申し上げます！

> **[2026.1.1]** 新年おめでとうございます！[Discord](https://discord.gg/eRsjPgMU4t)、[WeChat](https://github.com/HKUDS/DeepTutor/issues/78)、または [Discussions](https://github.com/HKUDS/DeepTutor/discussions) にぜひ参加してください — DeepTutor の未来を一緒に作りましょう！

> **[2025.12.29]** DeepTutor が正式リリースされました！

## ✨ 主な機能

DeepTutor はエージェントネイティブなランタイムを中心に構成されています：共有 ChatOrchestrator がすべてのターンをケイパビリティにルーティングし、ToolRegistry がモデルに必要なときに単発ツールを公開し、CapabilityRegistry がタスクに構造が必要なときに深いワークフローがターンを引き継げるようにします。

<div align="center">
<img src="../../assets/figs/system/system%20architecture.png" alt="DeepTutor システムアーキテクチャ" width="900">
</div>

**ひとつの学習ワークスペース**

- **デフォルトループとしての Chat** — カジュアルな個別指導、ソースに根ざした Q&A、Deep Solve、Deep Question、Deep Research、Visualize、Auto Mode はすべて同じセッションコンテキストとソースインベントリを共有します。
- **つながり続ける学習画面** — Co-Writer の下書き、Book ページ、Knowledge Base、Space アセット、Memory は別々のワークスペースですが、孤立したアプリになるのではなく、同じエージェントランタイムにフィードします。
- **永続的なコンパニオンとしての Partners** — IM 接続されたコンパニオンが、独自の合成ワークスペースと割り当てられたライブラリを持ち、メインプロダクトと同じチャットエージェントループ上で動作します。

**ツール、メモリ、コントロール**

- **コンポーザブルなツール** — RAG、ソース読み取り、メモリの読み書き、ノートブック、URL フェッチ、GitHub 検索、ask-user 一時停止、サンドボックス実行、オプションのブレインストーム/Web/論文/推論ツールをコンテキストと設定に応じてマウントできます。
- **三層メモリ** — L1 トレース、L2 サーフェスごとのサマリー、L3 クロスサーフェス合成により、パーソナライゼーションがブラックボックスの背後に隠れることなく検査可能になります。
- **統合設定と CLI** — モデルカタログ、埋め込み、検索、ネットワーク、MCP サーバー、ツール、ケイパビリティ、デプロイ設定は Web UI から編集でき、`deeptutor` からスクリプト化できます。

---

## 🚀 はじめに

DeepTutor には 4 つのインストール方法があります。すべて同一のワークスペースレイアウトを共有します：設定は起動ディレクトリ（または明示的に設定した場合は `DEEPTUTOR_HOME` / `deeptutor start --home`）の下の `data/user/settings/` に保存されます。フルアプリの場合、推奨フローは **ワークスペースディレクトリを選択 → インストール → `deeptutor init` → `deeptutor start`** です。

> ✨ **v1.4.3 が公開中。** `pip install -U deeptutor` で最新の安定版を取得できます。プレリリース（利用可能な場合）は `pip install --pre -U deeptutor` でオプトインします。

### オプション 1 — PyPI からインストール

クローン不要のフルローカル Web アプリ + CLI。**Python 3.11+** と PATH 上の **Node.js 20+** ランタイムが必要です（パッケージ化された Next.js スタンドアロンサーバーが `deeptutor start` によって起動されます）。

```bash
mkdir -p my-deeptutor && cd my-deeptutor
pip install -U deeptutor
deeptutor init     # ポート + LLM プロバイダー + オプションの埋め込みを設定
deeptutor start    # バックエンド + フロントエンドを起動；ターミナルを開いたままにしてください
```

`deeptutor init` はバックエンドポート（デフォルト `8001`）、フロントエンドポート（デフォルト `3782`）、LLM プロバイダー / ベース URL / API キー / モデル、および Knowledge Base / RAG 用のオプションの埋め込みプロバイダーを設定します。

`deeptutor start` 後、ターミナルに表示されるフロントエンド URL を開いてください — デフォルトは [http://127.0.0.1:3782](http://127.0.0.1:3782) です。そのターミナルで `Ctrl+C` を押すとバックエンドとフロントエンドの両方が停止します。クイックトライアルなら `deeptutor init` をスキップしても構いません；アプリはデフォルトポートと空のモデル設定で起動し、後で **Settings → Models** で設定できます。

### オプション 2 — ソースからインストール

チェックアウトに対する開発用。CI および Docker に合わせて **Python 3.11+** と **Node.js 22 LTS** を使用してください。

```bash
git clone https://github.com/HKUDS/DeepTutor.git
cd DeepTutor

# venv を作成（macOS/Linux）。Windows PowerShell:
#   py -3.11 -m venv .venv ; .\.venv\Scripts\Activate.ps1
python3 -m venv .venv && source .venv/bin/activate
python -m pip install --upgrade pip

# バックエンド + フロントエンドの依存関係をインストール
python -m pip install -e .
( cd web && npm ci --legacy-peer-deps )

deeptutor init
deeptutor start
```

ソースインストールはローカルの `web/` ディレクトリに対して Next.js を開発モードで実行します；その他すべて（設定レイアウト、ポート、`Ctrl+C` での停止）はオプション 1 と同じです。

<details>
<summary><b>Conda 環境</b>（<code>venv</code> の代わりに）</summary>

```bash
conda create -n deeptutor python=3.11
conda activate deeptutor
python -m pip install --upgrade pip
```

</details>

<details>
<summary><b>オプションのインストールエクストラ</b> — dev / partners / matrix / math-animator</summary>

```bash
pip install -e ".[dev]"             # テスト/lint ツール
pip install -e ".[partners]"        # Partner IM チャンネル SDK + MCP クライアント
pip install -e ".[matrix]"          # E2EE/libolm なしの Matrix チャンネル
pip install -e ".[matrix-e2e]"      # Matrix E2EE；libolm が必要
pip install -e ".[math-animator]"   # Manim アドオン；LaTeX/ffmpeg/システムライブラリが必要
```

</details>

<details>
<summary><b>フロントエンド依存関係の調整と開発サーバーのトラブルシューティング</b></summary>

**フロントエンド依存関係の変更：** `npm install --legacy-peer-deps` を実行して `web/package-lock.json` を更新し、`web/package.json` と `web/package-lock.json` の両方をコミットします。

**スタックした開発サーバー：** `deeptutor start` が応答しない既存のフロントエンドを報告する場合、表示された PID を停止してください。実際に Next.js プロセスが動いていない場合、ロックファイルが古くなっています — 削除して再試行してください：

```bash
rm -f web/.next/dev/lock web/.next/lock
deeptutor start
```

</details>

### オプション 3 — Docker

フル Web アプリ用の単一コンテナ。GitHub Container Registry 上のイメージ：

- `ghcr.io/hkuds/deeptutor:latest` — 安定リリース
- `ghcr.io/hkuds/deeptutor:pre` — プレリリース（利用可能な場合）

```bash
docker run --rm --name deeptutor \
  -p 127.0.0.1:3782:3782 \
  -p 127.0.0.1:8001:8001 \
  -v deeptutor-data:/app/data \
  ghcr.io/hkuds/deeptutor:latest
```

> ⚠️ **`3782` と `8001` の両方をマップしてください。** `3782` は Web UI を提供し、`8001` はブラウザが直接呼び出す FastAPI バックエンドです — コンテナ内プロキシはありません。`8001` のマッピングをスキップするとページは読み込まれますが、**Settings** が「Backend unreachable」と表示され使用不能になります。

[http://127.0.0.1:3782](http://127.0.0.1:3782) を開いてください。コンテナは最初の起動時に `/app/data/user/settings/*.json` を作成します；Web Settings ページからモデルプロバイダーを設定してください。設定、API キー、ログ、ワークスペースファイル、メモリ、ナレッジベースは `deeptutor-data` ボリュームに永続化されます。

- **異なるホストポート：** 各 `-p host:container` マッピングの左側を変更します（例：`-p 127.0.0.1:8088:3782`）。`/app/data/user/settings/system.json` でコンテナ側のポートを変更した場合は、再起動して各マッピングの右側を合わせて更新してください。
- **デタッチモード：** `-d` を追加し、`docker logs -f deeptutor` でフォロー、`docker stop deeptutor` で停止、名前を再利用する前に `docker rm deeptutor` を実行します。`deeptutor-data` ボリュームにより、再起動をまたいで設定とワークスペースが保持されます。

**リモート Docker / リバースプロキシ：** Web UI はブラウザで実行されるため、ブラウザが到達できるバックエンド URL が必要です。リモートサーバーの場合、**Settings -> Network** を開くか `data/user/settings/system.json` を編集してください：

```json
{
  "next_public_api_base_external": "https://deeptutor.example.com"
}
```

`public_api_base` は互換性エイリアスとして受け入れられ、保存時に `next_public_api_base_external` に正規化されます。CORS は API URL ではなくフロントエンドの**オリジン**を使用します。認証が無効の場合、DeepTutor はデフォルトで通常の HTTP/HTTPS ブラウザオリジンを許可します。認証が有効の場合、正確なフロントエンドオリジンを追加してください：

```json
{
  "cors_origins": ["https://deeptutor.example.com"]
}
```

<details>
<summary><b>ホスト上の Ollama / LM Studio / llama.cpp / vLLM / Lemonade への接続</b></summary>

Docker 内では `localhost` はホストマシンではなくコンテナ自身を指します。ホスト上で動作するモデルサービスに到達するには、ホストゲートウェイを使用します（推奨）：

```bash
docker run --rm --name deeptutor \
  -p 127.0.0.1:3782:3782 -p 127.0.0.1:8001:8001 \
  --add-host=host.docker.internal:host-gateway \
  -v deeptutor-data:/app/data \
  ghcr.io/hkuds/deeptutor:latest
```

その後、**Settings → Models** でプロバイダーのベース URL を `host.docker.internal` に向けます：

- Ollama LLM: `http://host.docker.internal:11434/v1`
- Ollama 埋め込み: `http://host.docker.internal:11434/api/embed`
- LM Studio: `http://host.docker.internal:1234/v1`
- llama.cpp: `http://host.docker.internal:8080/v1`
- Lemonade: `http://host.docker.internal:13305/api/v1`

Docker Desktop（macOS/Windows）は通常 `--add-host` なしで `host.docker.internal` を解決します。Linux では、このフラグが最新の Docker Engine 上でそのホスト名を作成するポータブルな方法です。

**Linux の代替方法 — ホストネットワーキング：** `--network=host` を追加して `-p` フラグを削除します。コンテナはホストネットワークを直接共有するため、[http://127.0.0.1:3782](http://127.0.0.1:3782)（または `system.json` の `frontend_port`）を開き、ホストサービスには `http://127.0.0.1:11434/v1` のような通常の localhost URL でアクセスできます。ホストネットワーキングはコンテナポートをホスト上に直接公開するため、既存のサービスと競合する可能性があることに注意してください。

</details>

### コード実行サンドボックス（オフィス スキル）

組み込みオフィス スキル — **docx / pdf / pptx / xlsx** — は、モデルが短い Python スクリプト（`python-docx`、`reportlab`、`openpyxl` など）を書き、`exec` / `code_execution` ツールを通じて実行し、ダウンロード URL を返す仕組みで動作します。これらのツールはサンドボックスバックエンドがアクティブなときにマウントされ、すべてのデプロイ形態でデフォルトで有効です：

- **ローカル（オプション 1 / 2）と Docker（オプション 3、単一コンテナ）：** 制限されたサブプロセスサンドボックスがモデルのコードを実行します（ローカルではホスト上、Docker ではコンテナ内 — コンテナ自体が分離境界となります）。
- **docker-compose：** 代わりに `DEEPTUTOR_SANDBOX_RUNNER_URL` 経由でハードニングされた最小権限の**ランナーサイドカー**（`Dockerfile.runner`）にルーティングされます — 最も強固な構成であり、存在する場合は自動的に優先されます。

サブプロセスサンドボックスは `data/user/settings/system.json` の `sandbox_allow_subprocess` 設定（デフォルト `true`）で制御されます。モデル生成コードをホスト上で実行することは実際の信頼の決定です — `false` に設定する（または `DEEPTUTOR_SANDBOX_ALLOW_SUBPROCESS=0` をエクスポートする）とホスト側の実行が無効になりますが、オフィス スキルがファイルを生成できなくなります。

### オプション 4 — CLI のみ

Web UI が不要な場合。CLI のみのパッケージはソースチェックアウトからインストールします（PyPI からではありません）。

```bash
git clone https://github.com/HKUDS/DeepTutor.git
cd DeepTutor

# venv を作成（macOS/Linux）。Windows PowerShell:
#   py -3.11 -m venv .venv-cli ; .\.venv-cli\Scripts\Activate.ps1
python3 -m venv .venv-cli && source .venv-cli/bin/activate
python -m pip install --upgrade pip

python -m pip install -e ./packaging/deeptutor-cli
deeptutor init --cli
deeptutor chat
```

`deeptutor init --cli` はフルアプリと同じ `data/user/settings/` レイアウトを共有しますが、バックエンド/フロントエンドのポート設定をスキップし、埋め込みをデフォルトで**オフ**にします（`deeptutor kb …` や RAG ツールを使用する予定なら `Yes` を選択）。それでも完全なランタイムレイアウト（`system.json`、`auth.json`、`integrations.json`、`model_catalog.json`、`main.yaml`、`agents.yaml`）を書き込み、アクティブな LLM プロバイダーとモデルの設定を求めます。

<details>
<summary><b>よく使うコマンド</b></summary>

```bash
deeptutor chat                                          # インタラクティブ REPL
deeptutor chat --capability deep_solve --tool rag --kb my-kb
deeptutor run chat "フーリエ変換を説明して"
deeptutor run deep_solve "x^2 = 4 を解け" --tool rag --kb my-kb
deeptutor kb create my-kb --doc textbook.pdf
deeptutor memory show
deeptutor config show
```

</details>

ローカルの `deeptutor-cli` インストールには Web アセットやサーバー依存関係は含まれていません。ソースチェックアウトを保持してください — 編集可能インストールはそこを参照します。後で Web アプリを追加するには、PyPI パッケージ（オプション 1）をインストールして同じワークスペースから `deeptutor init` + `deeptutor start` を実行します。

### 設定リファレンス

<details>
<summary><b><code>data/user/settings/</code> 以下の設定ファイル</b> — JSON/YAML リファレンス</summary>

`data/user/settings/` 以下のすべてはプレーンな JSON/YAML です。ブラウザの **Settings** ページが推奨のエディタです。

| ファイル | 目的 |
|:---|:---|
| `model_catalog.json` | LLM、埋め込み、検索プロバイダープロファイル；API キー；アクティブモデル |
| `system.json` | バックエンド/フロントエンドポート、パブリック API ベース、CORS、SSL 検証、添付ディレクトリ |
| `auth.json` | オプションの認証トグル、ユーザー名、パスワードハッシュ、トークン/クッキー設定 |
| `integrations.json` | オプションの PocketBase とサイドカー統合設定 |
| `interface.json` | UI 言語 / テーマ / サイドバー設定 |
| `main.yaml` | ランタイム動作のデフォルトとパス注入 |
| `agents.yaml` | ケイパビリティ/ツールの温度とトークン設定 |

プロジェクトルートの `.env` はアプリケーション設定ファイルとして読み込まれません。最小限のモデルセットアップには、**Settings → Models** を開き、LLM プロファイル（ベース URL / API キー / モデル名）を追加して保存してください。Knowledge Base / RAG 機能を使用する予定の場合のみ埋め込みプロファイルを追加してください。

</details>

## 📖 DeepTutor を探索する

README ツアーは最もよく使うプロダクトサーフェスの順序で進みます：Chat、Partner、Co-Writer、Book、Knowledge、Space、Memory、Settings。以下のスクリーンショットは再編成された `assets/figs` ツリーからのものです；アーカイブされた旧来の画像はここでは意図的に使用していません。

### 💬 Chat — 実際に使うエージェントループ

<div align="center">
<img src="../../assets/figs/webui/chat.png" alt="DeepTutor チャットワークスペース" width="900">
</div>

Chat はデフォルトのケイパビリティであり、ほとんどの作業が始まる場所です。単一のスレッドで普通に話したり、ツールを呼び出したり、選択したナレッジベースを基盤にしたり、添付ファイルを読んだり、ノートブックレコードを書いたり、ターンをまたいで同じソースインベントリを継続して使えます。

<div align="center">
<img src="../../assets/figs/system/chat-agent-loop.png" alt="DeepTutor チャットエージェントループ" width="900">
</div>

現在のループはシンプルな設計です：モデルはラウンドで考え、必要なときにツールを呼び出し、ツールの結果を観察し、十分な証拠が得られたら終了します。ユーザーが切り替えられるツールは `brainstorm`、`web_search`、`paper_search`、`reason` です；`rag`、`read_source`、`read_memory`、`write_memory`、`read_skill`、`load_tools`、`exec`、`web_fetch`、`ask_user`、`list_notebook`、`write_note`、`github` などのコンテキストツールは適切なコンテキストがあるターンにマウントされます。

Chat はより深いケイパビリティの起点でもあります：作業推論のための `deep_solve`、質問生成のための `deep_question`、引用付きレポートのための `deep_research`、ビジュアル出力のための `visualize` と `math_animator`、ルーティングのための `auto`、学習計画フローのための `mastery_path`。

### 🤝 Partner — 同じブレインで動く永続コンパニオン

<div align="center">
<img src="../../assets/figs/webui/partners.png" alt="DeepTutor Partners ワークスペース" width="900">
</div>

Partners は旧来の TutorBot エンジンをよりクリーンなモデルで置き換えます：すべての受信 Web または IM メッセージが、パートナースコープのワークスペース内の通常の ChatOrchestrator ターンになります。同期を保つための別個のボットブレインは存在しません。

<div align="center">
<img src="../../assets/figs/system/partners-architecture.png" alt="DeepTutor Partners アーキテクチャ" width="900">
</div>

各パートナーには `SOUL.md`、モデル選択、チャンネル、ツールポリシー、割り当てられたライブラリがあります。ナレッジベース、スキル、ノートブックは `data/partners/<id>/workspace/` にコピーされるため、特別なケースなしに同じ RAG、スキル、ノートブック、メモリツールが動作します。

<div align="center">
<img src="../../assets/figs/webui/partners02.png" alt="DeepTutor Partner 詳細ビュー" width="900">
</div>

チャンネルレイヤーはスキーマ駆動で、インストールされたエクストラと設定された認証情報に応じて Feishu、Telegram、Slack、DingTalk、QQ/Napcat、WeCom、WhatsApp、Zulip、Matrix、Microsoft Teams などの IM プラットフォームに接続できます。

### ✍️ Co-Writer — 選択範囲認識 Markdown 下書き

Co-Writer はレポート、チュートリアル、ノート、長文学習成果物のための分割ビュー Markdown ワークスペースです。ドキュメントは自動保存され、ライブプレビューを表示し、下書きが再利用可能なコンテキストになったときにノートブックに保存できます。

テキストを選択して DeepTutor に書き直し、拡張、短縮を依頼できます。編集エージェントはツール呼び出しのトレースを保持し、ナレッジベースや Web の証拠を基に編集を行えるため、Co-Writer は切り離されたテキストボックスよりも検索機能付きエディタのように動作します。

### 📖 Book — 資料から作る生きた本

<p align="center">
<img src="../../assets/figs/webui/book01.png" alt="DeepTutor Book 読書ビュー" width="31%">
&nbsp;
<img src="../../assets/figs/webui/book02.png" alt="DeepTutor Book インタラクティブブロックビュー" width="31%">
&nbsp;
<img src="../../assets/figs/webui/book03.png" alt="DeepTutor Book 作成ビュー" width="31%">
</p>

Book は選択されたソースをインタラクティブな学習資料に変換します。ナレッジベース、ノートブック、問題バンク、チャット履歴から始めることができます；コンテンツが生成される前に構造を提案するため、ユーザーは一発限りの盲目的な出力を受け入れるのではなく、形を確認できます。

BookEngine はページを型付きブロックにコンパイルします：テキスト、セクション、コールアウト、クイズ、フラッシュカード、タイムライン、コード、図、インタラクティブ HTML、アニメーション、概念グラフ、詳細解説、ユーザーノート。`deeptutor book health` や `deeptutor book refresh-fingerprints` などのメンテナンスコマンドは、ソース知識がコンパイル済みページからドリフトしたときに検出するのに役立ちます。

### 📚 Knowledge — バージョン管理された RAG ライブラリ

<div align="center">
<img src="../../assets/figs/webui/knowledge.png" alt="DeepTutor ナレッジベースワークスペース" width="900">
</div>

Knowledge Base は RAG の背後にあるドキュメントコレクションです。現在のスタックは LlamaIndex のみで、埋め込みシグネチャでキーとなるフラットな `version-N` ストレージレイアウトを使用しています。再インデックスは以前のバージョンを保持し、新しいドキュメントの処理中に動作中のインデックスを上書きしません。

Web ワークスペースはファイル、アップロード、インデックスバージョン、設定を公開します。CLI は `deeptutor kb list`、`info`、`create`、`add`、`search`、`set-default`、`delete` で同じライフサイクルを反映します。

### 🌐 Space — スキル、ペルソナ、再利用可能なコンテキスト

<div align="center">
<img src="../../assets/figs/webui/space.png" alt="DeepTutor Space ワークスペース" width="900">
</div>

Space は再利用可能なコンテキストのライブラリレイヤーです。ユーザー作成スキル、ペルソナ、ノートブック、チャット履歴、問題バンク形式のアセットをまとめることで、場当たり的なプロンプティングではなく意図的なコンテキストでエージェントを誘導できます。

スキルはユーザーワークスペース以下の `SKILL.md` ファイルとして保存され、タグ付け、編集、または組み込みの場合は読み取り専用として保持できます。ペルソナも役割と声について同様のアイデアに従います。これらのアセットはパートナーに割り当て、チャットで参照し、学習ワークフロー全体で再利用できます。

### 🧠 Memory — 検査可能なパーソナライゼーション

<div align="center">
<img src="../../assets/figs/webui/memory01.png" alt="DeepTutor Memory ワークベンチ" width="900">
</div>

Memory はアクティブなユーザーワークスペースに根ざした三層システムです：L1 イベントトレースの `trace/<surface>/<date>.jsonl`、サーフェスごとの事実の `L2/<surface>.md`、クロスサーフェス合成の `L3/<recent|profile|scope|preferences>.md`。

<div align="center">
<img src="../../assets/figs/webui/memory02.png" alt="DeepTutor Memory グラフ" width="900">
</div>

サポートされているメモリサーフェスは `chat`、`notebook`、`quiz`、`kb`、`book`、`tutorbot`、`cowriter` です。プロダクト向けのコンパニオンモデルが現在 Partners になっているにもかかわらず、後方互換性のためにレガシーの `tutorbot` サーフェス名がメモリレイヤーに残っています。ワークベンチでは、検査、編集、統合実行ができ、グラフを使って合成されたクレームをそれを支持する事実や生のイベントまでトレースできます。

### ⚙️ Settings — 一元的なコントロールプレーン

<div align="center">
<img src="../../assets/figs/webui/settings.png" alt="DeepTutor Settings ワークスペース" width="900">
</div>

Settings は運用上のコントロールプレーンです。外観、ネットワークポートと外部 API ベース、LLM と埋め込みカタログ、検索プロバイダー、MinerU 解析、ケイパビリティバジェット、メモリケイデンス、MCP サーバー、組み込みツール、有効なオプションツールリストをカバーします。

ほとんどの設定はドラフト＆適用フローを使用するため、ユーザーはコミットする前にプロバイダーをテストできます。プロジェクトルートの `.env` ファイルは意図的に無視されます；ランタイム設定は `DEEPTUTOR_HOME` または `deeptutor start --home` がアプリを別の場所に向けない限り `data/user/settings/*.json` に保存されます。

---

## ⌨️ DeepTutor CLI — エージェントネイティブインターフェース

DeepTutor は CLI ネイティブです：同じ `deeptutor` エントリーポイントでワークスペースの初期化、Web アプリの起動、単発ケイパビリティの実行、インタラクティブ REPL の起動、ナレッジベースの管理、セッションの検査、本のメンテナンス、パートナーの操作ができます。

```bash
deeptutor run chat "フーリエ変換を説明して" --tool rag --kb textbook
deeptutor run deep_solve "x^2 = 4 を解け" --tool reason
deeptutor chat --capability deep_research --kb papers
deeptutor partner create math-tutor --soul "ソクラテス式数学チューター"
deeptutor kb create calculus --doc textbook.pdf
```

<details>
<summary><b>コマンドリファレンス</b></summary>

| コマンド | 説明 |
|:---|:---|
| `deeptutor init` | 現在のワークスペースの `data/user/settings` を作成または更新 |
| `deeptutor start [--home PATH]` | バックエンド + フロントエンドを一緒に起動 |
| `deeptutor serve [--port PORT]` | FastAPI バックエンドのみを起動 |
| `deeptutor run <capability> <message>` | 単一ケイパビリティターンを実行（`chat`、`deep_solve`、`deep_question`、`deep_research`、`visualize`、`math_animator`、`auto`、`mastery_path`） |
| `deeptutor chat` | ケイパビリティ、ツール、KB、ノートブック、履歴コントロール付きインタラクティブ REPL |
| `deeptutor partner list/create/start/stop` | IM 接続パートナーを管理 |
| `deeptutor kb list/info/create/add/search/set-default/delete` | LlamaIndex ナレッジベースを管理 |
| `deeptutor memory show/clear` | L2/L3 メモリドキュメントの検査または L1/全メモリのクリア |
| `deeptutor session list/show/open/rename/delete` | 共有セッションを管理 |
| `deeptutor notebook list/create/show/add-md/replace-md/remove-record` | Markdown ファイルからノートブックを管理 |
| `deeptutor book list/health/refresh-fingerprints` | 本を検査してソースフィンガープリントを更新 |
| `deeptutor plugin list/info` | 登録されたツールとケイパビリティを検査 |
| `deeptutor config show` | 設定サマリーを表示 |
| `deeptutor provider login <provider>` | サポートされているプロバイダーの OAuth ログインを管理 |

</details>

CLI のみのディストリビューションは `packaging/deeptutor-cli` に存在します；このチェックアウトでは `python -m pip install -e ./packaging/deeptutor-cli` でソースからインストールする必要があります。公開 `deeptutor-cli` パッケージは現在 PyPI では利用できないため、メインのはじめにセクションではソースインストールパスを維持しています。

---

## 👥 マルチユーザーと共有デプロイ

<div align="center">
<img src="../../assets/figs/webui/multi-user.png" alt="DeepTutor マルチユーザー管理者ワークスペース" width="900">
</div>

認証はオプションでデフォルトではオフです。有効にすると、DeepTutor は 1 つの `data/` ツリー内に管理者ワークスペース、ユーザーごとのワークスペース、パートナーワークスペース、システム状態を持つ共有デプロイになります。

```text
data/
├── user/                         # 管理者ワークスペースと設定
├── users/<uid>/                  # 非管理者ユーザースコープ
│   ├── user/chat_history.db
│   ├── user/settings/interface.json
│   ├── user/workspace/{chat,co-writer,book,memory,notebook,...}
│   └── knowledge_bases/...
├── partners/<id>/workspace/      # Partner 合成ユーザースコープ
└── system/
    ├── auth/users.json
    ├── grants/<uid>.json
    └── audit/usage.jsonl
```

最初に登録されたユーザーが管理者になり、モデルカタログ、プロバイダー認証情報、ナレッジベース、スキル、ユーザーグラントを設定できます。非管理者ユーザーは分離されたチャット履歴、メモリ、ノートブック、個人ナレッジベース、編集された Settings ページを取得します；管理者が割り当てたリソースは API キーやプロバイダー内部を公開するのではなく、スコープ付きの読み取り専用オプションとして表示されます。

ローカルトライアルの場合、`data/user/settings/auth.json` で認証を有効にし、`deeptutor start` を再起動して、`/register` で最初の管理者を登録し、`/admin/users` からユーザーを作成して、グラントを通じてモデル、KB、スキル、ツールポリシー、MCP ポリシー、コード実行アクセスを割り当てます。

PocketBase モードはこのツリーでは単一ユーザー統合として残ります；マルチユーザーデプロイでは、外部ユーザーストアがデプロイのために明示的に設計されていない限り、`integrations.pocketbase_url` を空白のままにして、デフォルトの JSON/SQLite 認証とセッションストアを使用してください。

---
## 🌐 コミュニティとエコシステム

DeepTutor は優れたオープンソースプロジェクトの上に成り立っています：

| プロジェクト | DeepTutor での役割 |
|:---|:---|
| [**nanobot**](https://github.com/HKUDS/nanobot) | 元の TutorBot を動かした超軽量エージェントエンジン（Partners は現在 DeepTutor のチャットエージェントループ上で動作） |
| [**LlamaIndex**](https://github.com/run-llama/llama_index) | RAG パイプラインとドキュメントインデックスのバックボーン |
| [**ManimCat**](https://github.com/Wing900/ManimCat) | Math Animator 向け AI 駆動数学アニメーション生成 |

**HKUDS エコシステムから：**

| [⚡ LightRAG](https://github.com/HKUDS/LightRAG) | [🤖 AutoAgent](https://github.com/HKUDS/AutoAgent) | [🔬 AI-Researcher](https://github.com/HKUDS/AI-Researcher) | [🧬 nanobot](https://github.com/HKUDS/nanobot) |
|:---:|:---:|:---:|:---:|
| シンプル＆高速 RAG | ゼロコードエージェントフレームワーク | 自動化研究 | 超軽量 AI エージェント |


## 🤝 コントリビューション

<div align="center">

DeepTutor がコミュニティへの贈り物になることを願っています。🎁

<a href="https://github.com/HKUDS/DeepTutor/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=HKUDS/DeepTutor&max=999" alt="コントリビューター" />
</a>

</div>

開発環境のセットアップ、コード標準、プルリクエストワークフローのガイドラインについては [CONTRIBUTING.md](../../CONTRIBUTING.md) をご覧ください。

## ⭐ スター履歴

<div align="center">

<a href="https://www.star-history.com/#HKUDS/DeepTutor&type=timeline&legend=top-left">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=HKUDS/DeepTutor&type=timeline&theme=dark&legend=top-left" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=HKUDS/DeepTutor&type=timeline&legend=top-left" />
    <img alt="スター履歴チャート" src="https://api.star-history.com/svg?repos=HKUDS/DeepTutor&type=timeline&legend=top-left" />
  </picture>
</a>

</div>

<p align="center">
 <a href="https://www.star-history.com/hkuds/deeptutor">
  <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/badge?repo=HKUDS/DeepTutor&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/badge?repo=HKUDS/DeepTutor" />
   <img alt="スター履歴ランク" src="https://api.star-history.com/badge?repo=HKUDS/DeepTutor" />
  </picture>
 </a>
</p>

<div align="center">

**[Data Intelligence Lab @ HKU](https://github.com/HKUDS)**

[⭐ スターをつける](https://github.com/HKUDS/DeepTutor/stargazers) · [🐛 バグを報告する](https://github.com/HKUDS/DeepTutor/issues) · [💬 ディスカッション](https://github.com/HKUDS/DeepTutor/discussions)

---

[Apache License 2.0](../../LICENSE) の下でライセンスされています。

<p>
  <img src="https://visitor-badge.laobi.icu/badge?page_id=HKUDS.DeepTutor&style=for-the-badge&color=00d4ff" alt="ビュー数">
</p>

</div>
