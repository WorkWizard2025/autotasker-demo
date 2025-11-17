# AutoTasker Demo

AutoTasker のデモ版サンプルツールです。  
複数の CSV ファイルをまとめて読み込み、結合・加工・集計して出力する  
「データ処理自動化ツール」の最小構成デモとして公開しています。

実案件では、ここから機能追加することで  
「Excel 自動処理」「PDF レポート自動生成」「条件分岐レポート」など  
自由に拡張できます。

---

## 📂 機能概要

- `sample_data/` 内の CSV をすべて読み込む
- 縦に結合して 1 つの DataFrame にする
- `date` 列から `year` / `month` を自動抽出
- 年月ごとの売上サマリを作る
- `output/` ディレクトリに以下を出力
  - `merged_data.csv` … 結合済みデータ
  - `summary_by_month.csv` … 月別サマリ

---

## ▶ 使い方

### 1. 依存ライブラリをインストール

pip install -r requirements.txt


---

### 2. 実行方法

プロジェクトのルートフォルダで以下を実行します：



python -m autotasker_demo.main


※ `python autotasker_demo/main.py` では動きません  
（相対インポートが使えないため）

---

### 3. 出力結果

実行後、`output/` フォルダに以下が生成されます：

output/
├─ merged_data.csv
└─ summary_by_month.csv


---

## 🗂 ディレクトリ構成



autotasker-demo/
│
├─ README.md
├─ requirements.txt
│
├─ autotasker_demo/
│ ├─ init.py
│ ├─ main.py
│ ├─ config.py
│ └─ processor.py
│
└─ sample_data/
├─ sales_2024_01.csv
└─ sales_2024_02.csv


---

## 🔧 カスタマイズ例（実案件）

AutoTasker 本体は、業務内容に合わせてカスタマイズできる柔軟なデータ処理ツールです。  
以下のような拡張が可能です：

- PDF レポート自動生成  
- Excel テンプレートへの自動書き込み  
- 特定フォルダを監視して自動処理（バッチ処理）  
- 月次・週次レポート自動生成  
- 画像ファイル一覧 → Excel 変換  
- Web スクレイピング → CSV 出力  
- API 連携（Google Sheets, Slack など）  

「業務の手作業を丸ごと自動化するツール」に成長させることができます。


---

## 🔧 今後の拡張予定（Roadmap）

AutoTasker は現在デモ版のため、最低限の機能のみを搭載しています。  
商用版では以下の機能追加を予定しています：


---

### ▶ 今後追加予定の機能
- Excel（.xlsx）への自動書き込み  
- PDF レポート自動生成（帳票・分析レポート）  
- 条件付きレポート（特定店舗などの自動抽出）  
- 入力フォルダの自動監視 → 即自動処理  
- Web UI（Flask/Django）の管理画面  
- Google スプレッドシート対応  
- 月次レポートの自動メール送信  
- 複数フォルダの一括バッチ処理  

これらは実案件に合わせて柔軟にカスタマイズ可能です。

---

## 📩 問い合わせ

Python データ処理ツールの制作依頼も受けています。  

お気軽にご連絡ください！
