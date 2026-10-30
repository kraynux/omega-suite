<!-- Copyright (c) 2026 kraynux - kraynux@proton.me - Licence MIT (voir fichier LICENSE) -->
<div align="center">
  <img src="https://raw.githubusercontent.com/kraynux/kraynux/refs/heads/main/docs/assets/omega-suite.png" alt="Omega-Suite" width="384">
</div>


#  OMEGA-SUITE

**「OMEGA」スキャナー群を 1 つのインターフェースと共有ライブラリに統合**

> **kraynux** が **Omega-server** のために開発 
[kraynux.snake-mackarel](https://kraynux.snake-mackarel.ts.net)

公式ページ：[OMEGA-SUITE](https://kraynux.snake-mackarel.ts.net/omega-suite/) &nbsp;   
スクリーンショット → [omega-scan](https://kraynux.snake-mackarel.ts.net/omega-scan/screenshots/) · [omega-check](https://kraynux.snake-mackarel.ts.net/omega-check/screenshots/) · [omega-deep](https://kraynux.snake-mackarel.ts.net/omega-deep/screenshots/) · [omega-fold](https://kraynux.snake-mackarel.ts.net/omega-fold/screenshots/) · [omega-track](https://kraynux.snake-mackarel.ts.net/omega-track/screenshots/) · [omega-fuzz](https://kraynux.snake-mackarel.ts.net/omega-fuzz/screenshots/) · [omega-stress](https://kraynux.snake-mackarel.ts.net/omega-stress/screenshots/) 

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../../../LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Linux-informational.svg)](https://www.linux.org/)
[![Interface](https://img.shields.io/badge/Interface-Textual%20TUI-cyan.svg)](https://github.com/Textualize/textual)

**言語：**
<img src="https://flagcdn.com/w20/fr.png" alt="France" style="height:14px;"> [Français](../../../README.md) · <img src="https://flagcdn.com/w20/gb.png" alt="English" style="height:14px;"> [English](../en/README.md) · <img src="https://flagcdn.com/w20/es.png" alt="Español" style="height:14px;"> [Español](../es/README.md) · <img src="https://flagcdn.com/w20/br.png" alt="Português (Brasil)" style="height:14px;"> [Português (Brasil)](../pt-BR/README.md) · <img src="https://flagcdn.com/w20/it.png" alt="Italiano" style="height:14px;"> [Italiano](../it/README.md) · <img src="https://flagcdn.com/w20/de.png" alt="Deutsch" style="height:14px;"> [Deutsch](../de/README.md) · <img src="https://flagcdn.com/w20/nl.png" alt="Nederlands" style="height:14px;"> [Nederlands](../nl/README.md) · <img src="https://flagcdn.com/w20/pl.png" alt="Polski" style="height:14px;"> [Polski](../pl/README.md) · <img src="https://flagcdn.com/w20/ru.png" alt="Русский" style="height:14px;"> [Русский](../ru/README.md) · <img src="https://flagcdn.com/w20/cn.png" alt="中文" style="height:14px;"> [中文](../zh-CN/README.md) · <img src="https://flagcdn.com/w20/vn.png" alt="Tiếng Việt" style="height:14px;"> [Tiếng Việt](../vi/README.md) · <img src="https://flagcdn.com/w20/th.png" alt="ไทย" style="height:14px;"> [ไทย](../th/README.md) · <img src="https://flagcdn.com/w20/id.png" alt="Bahasa Indonesia" style="height:14px;"> [Bahasa Indonesia](../id/README.md) · <img src="https://flagcdn.com/w20/jp.png" alt="日本語" style="height:14px;"> [日本語](README.md) · <img src="https://flagcdn.com/w20/kr.png" alt="한국어" style="height:14px;"> [한국어](../ko/README.md) · <img src="https://flagcdn.com/w20/in.png" alt="हिन्दी" style="height:14px;"> [हिन्दी](../hi/README.md) · <img src="https://flagcdn.com/w20/ae.png" alt="العربية" style="height:14px;"> [العربية](../ar/README.md)

---
**Omega-Suite** は **omega-** スキャナーツール群の統合インターフェースです：  
[omega-scan](https://github.com/kraynux/omega-scan)、[omega-check](https://github.com/kraynux/omega-check)、[omega-deep](https://github.com/kraynux/omega-deep)、[omega-fold](https://github.com/kraynux/omega-fold)、[omega-stress](https://github.com/kraynux/omega-stress)、[omega-track](https://github.com/kraynux/omega-track)、[omega-fuzz](https://github.com/kraynux/omega-fuzz)  
を 1 つの TUI アプリケーション（ユーザーの選択に応じてホームのグリッド、または常時表示のタブバー）にまとめ、共有ライブラリ [(`omega-lib`)](https://github.com/kraynux/omega-lib) を備えています。


各ツールは引き続き単独で実行できます（`omega-check scan ...`
はそのまま動作します）- omega-suite は追加のファサードであり、
置き換えではありません。

アーキテクチャと操作性に関する選択の詳細は、
`~/DEV/SUITE/OMEGA-SUITE_SPECIFICATIONS.md` と
`~/DEV/SUITE/DECISIONS_ARCHITECTURE.md`（D-014/D-015）を参照してください。

## 概要

Omega-Suite はネットワークセキュリティのための Omega スキャナー群の **操縦席** として機能します

### 目的

- 7 つの **omega スキャナー** を一貫したインターフェースにまとめ、それらを変更したり置き換えたりすることは決してない。
- 7 つのツールに対してテーマ、描画プロファイル、ナビゲーションスタイルを 1 つずつ - 7 回ではなく 1 回の設定で済ませる。
- コンテキストを失わずにツール間を移動する：各画面スタックはバックグラウンドでそのまま保持される。
- 7 つのツールをまとめても軽量に保つ：実際に初めて開くまで何もメモリに読み込まない。

## 機能

- Omega-SCAN、-CHECK、-DEEP、-FOLD、-STRESS、-TRACK、-FUZZ のための **単一の TUI アプリケーション**（Textual）。
- 選べる **2 つのナビゲーションスタイル**（設定、すぐに再起動を提案）：ホームからのボタングリッド、または深い階層（履歴、ツールの設定など）でも表示され続けるタブバー。ホームに戻る必要はありません。
- **遅延読み込み**：各ツール（Python コードと依存関係）はセッション内で最初に開いたときにだけインポートされる - 起動時間とメモリは実際に使うツールに比例したまま。
- **テーマと描画プロファイルの共有**：テーマは 7 つのツールすべてで同時に即時切り替え。より構造的な描画プロファイルとナビゲーションスタイルは、omega-suite のすぐの再起動を提案します。
- **コンテキストヘルプ**：ホームからはグローバルショートカットと 7 つのツールの範囲の概要、タブからはアクティブなツール固有のヘルプ。
- 7 つのツールの **エクスポートを一括削除**（スイートの設定）。セッションで一度も開いていないツールも対象。
- 1 つのアプリケーションを共有していても **7 つのツール間は厳密に分離**：あるツールから別のツールへのスタイルや状態の漏れはありません。
- **各ツールは完全に単独でも使用可能**（独自の TUI と CLI、`omega-check scan ...` はそのまま動作）- omega-suite は追加のファサードにすぎず、置き換えではありません。

## インストール

公式アーカイブは `.tar.gz` 形式で提供されます。インストール前に整合性を確認してください：

```bash
sha256sum omega-suite.tar.gz
```

```bash
./install.sh
./omega-suite.sh
```


## 使い方
### 起動

```bash
cd ~/omega-suite
./omega-suite.sh
```

###  またはエイリアスを作成済みなら、ターミナルで次を入力するだけ：
```bash
suite
```
## インターフェースの言語

インターフェースは 17 言語に対応しています。スイートの設定（「Langue / Language」）で選択し、インターフェースの再起動後に 7 つのツールすべてに適用されます。変数 `OMEGA_SUITE_LANG` で 1 回のセッションに言語を強制できます。別の設定「エクスポートの言語」で、7 つのツールがエクスポートするレポートの言語を指定します。Linux のテキストコンソール（TTY）では、ラテン文字以外の言語はそのセッションのあいだ英語で表示されます。コマンドラインはフランス語のままです。

## ターミナルの互換性

対話型インターフェース（Textual）はターミナルの機能（エミュレーター、サイズ）を自動検出し、それに応じて構造的なスタイルシート（`complete`/`standard`/`reduced`/`mono`）を調整します。手動のフラグは不要です。CLI モードは常にプレーンテキストのままで、ターミナルに依存しません。`omega-` スイート全体で共有されるポリシー（`omega-lib`、`terminal/policies.py`）— `omega-check`/`omega-fire` と同一です。

### 検出されたエミュレーターに応じたプロファイル

| エミュレーター | 初期プロファイル |
|---|---|
| Ghostty, Alacritty, WezTerm, Kitty | `complete` |
| Konsole, GNOME Terminal, Terminator, Xfce4 Terminal | `standard` |
| xterm, urxvt, 最新の SSH | `reduced` |
| Linux TTY, 古い SSH | `mono` |
| 不明なエミュレーター | `reduced`（既定のフォールバック） |

### ターミナルのサイズに応じたプロファイル

| 最小サイズ（列 × 行） | プロファイルの上限 |
|---|---|
| 120 × 32 | `complete` |
| 100 × 28 | `standard` |
| 80 × 24 | `reduced` |
| それ未満 | `mono` |

最終的に採用されるプロファイルは **2 つのうちより制限の厳しい方**（エミュレーターとサイズ）です — 全画面の Ghostty を 70 列に縮めると、エミュレーターが `complete` を許していても `mono` に下がります。`r` キーでその場で更新でき、スイートの設定（`s` キー）から手動で上書きすることもできます。

## アーキテクチャ

### 設計原則

- **合成のためのファサードであり、8 番目のビジネス層ではない**：omega-suite は独自の `domain/` を持たず、各プロジェクトが個別に検証済みの 7 つのコンテナーを組み立てるだけで、そのロジックを再実装しません。
- **7 つのツールのファイルは一切変更しない。** 共有の画面/ウィジェットクラスは、セッション内でそのツールを実際に初めて開いたときに一度だけメモリ上でパッチされます：CSS の分離（あるツールが別のツールのスタイルを継承することはない）、ツール内部の「終了」をスイートのホームタブへリダイレクト、そしてこのナビゲーションスタイルが有効ならタブバーを挿入。
- **`interfaces/tui/` 以外での `textual` は禁止**（変更のたびに `import-linter` で検証）：`app/` は表示から独立しており、理論上は別のインターフェースにも使えます。
- **2 段階の遅延構築**：ツールのアダプター（コードのインポート）、次にそのコンテナー（SQLite データベース、ネットワークプローブ）- どちらも、そのツールを実際に初めて訪れるまでコストは発生しません。

### データ構造

```text
src/omega_suite/
├── app/              組み立て：遅延 DependencyContainer、ブートストラップ、7 つのツールのアダプター
│                     (tool_adapters.py)、共有設定（テーマ、描画プロファイル、ナビゲーションスタイル）
├── infrastructure/   ランタイムのパス（var/）、設定の保存（JSON）
├── interfaces/
│   ├── tui/          Textual をインポートする唯一の場所：App、スイート固有の画面（ホーム、設定、
│   │                 ヘルプ、Splash）、7 つのツールの画面のメモリ上パッチ（screen_patching.py）
│   └── cli/          予約済み、現時点では空 - 各ツールは独自の CLI モードを保持し、直接呼び出される
└── ports/            app/ が期待する契約（SettingsStore）
```

## 前提条件

### システム

- Python 3.10+
- Linux（Textual は他のシステムでも動作しますが、本プロジェクトではテストもサポートもしていません）
- どんなターミナルでも可 - 実際の機能は自動検出され、描画がそれに合わせて調整されます（上の「ターミナルの互換性」を参照）。単純な TTY まで対応

### Python の依存関係

`pyproject.toml` で宣言され、1 つの仮想環境にすべてがまとまります（`install.sh` を参照）：

- `omega-lib`：共有ライブラリ（テーマ、ターミナル検出、信頼度レベル）
- `omega-scan`、`omega-check`、`omega-deep`、`omega-fold`、`omega-stress`、`omega-track`、`omega-fuzz`：統合された 7 つのツール。それぞれ独自の推移的依存関係を持つ
- `textual`：TUI インターフェース
- 開発用依存関係（`pip install -e ".[dev]"`）：`pytest`、`pytest-asyncio`、`pytest-cov`、`ruff`、`mypy`、`import-linter`

### エクスポート

各ツールは自身のエクスポートを `var/<ツール>/exports/` に、スクリーンショットを `var/<ツール>/screenshots/` に書き込みます - `var/` は omega-suite を起動したフォルダーからの相対パスで、`$OMEGA_SUITE_VAR_DIR` で上書きできます。これはツールを単独で起動したときの既定の `var/` とは決して同じになりません：2 つの使い方（単独またはスイートに統合）が混ざることはありません。各ツールは自身の設定から出力先フォルダーを再定義できます。「すべてのエクスポートを空にする」ボタン（スイートの設定）は、セッションで一度も開いていないツールも含め、7 つのツールのこのフォルダーを一度に空にします - 詳細はスイートのヘルプ（ホームから `a` キー）を参照してください。

---

## セキュリティ

- omega-suite 自体はネットワークリクエストを一切行わず、何もスキャンしません：7 つのツールの表示を統括するだけで、各ツールは自身の安全装置をすべて保持しています（それぞれの範囲はスイートのヘルプ、または各ツールの README を参照）。
- omega-suite 自体は秘密情報や認証情報を一切扱いません。各ツールが保存するもの（ピン留めした対象、履歴、独自の設定）は、それぞれのサブフォルダー `var/<ツール>/` に残り、スイートによって変更されることはありません。
- omega-suite 固有の唯一の状態（テーマ、描画プロファイル、ナビゲーションスタイル）は `var/settings.json` にあり、機密データは含みません。
- `import-linter` は変更のたびに `interfaces/tui/` 以外での `textual` のインポートを禁止します（アーキテクチャを参照）- 単なる慣習ではなく、構造的な保証です。

## テストと品質

```bash
source .venv/bin/activate
pip install -e ".[dev]"
lint-imports        # Dependency Rule を検証（interfaces/tui 以外での textual は禁止）
pytest -q
ruff check src tests
mypy -p omega_suite
```

## アンインストール

omega-suite は自身のフォルダーと起動用エイリアス以外には何も触れません：

1. `install.sh` が `~/.bashrc` と `~/.zshrc` に追加した `alias suite="..."` の行を削除する。
2. `omega-suite/` フォルダーを削除する（仮想環境 `.venv/`、データ `var/`、設定を含む）。

個別にインストールされた 7 つのツール（またはそれぞれのフォルダーで開発中のもの）は影響を受けません：それぞれ自身の README に従って独立してインストール/アンインストールできます。

## ライセンス

Omega-Suite は **MIT** ライセンスで配布されています。全文はファイル [`LICENSE`](../../../LICENSE) を参照してください。

---

> **Omega-Suite — 観察し、操縦し、監査し、よりよく守るために。**
>
> Omega- スキャナーのための統合 TUI インターフェース
