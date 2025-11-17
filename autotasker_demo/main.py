import argparse
from pathlib import Path

from . import config
from .processor import (
    find_csv_files,
    load_and_merge,
    add_year_month_columns,
    summarize_by_month,
    export_results,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="AutoTasker Demo - CSV 自動集計ツール"
    )
    parser.add_argument(
        "--input-dir",
        type=str,
        default=str(config.DEFAULT_INPUT_DIR),
        help="入力 CSV フォルダのパス（デフォルト: sample_data）",
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default=str(config.DEFAULT_OUTPUT_DIR),
        help="出力フォルダのパス（デフォルト: output）",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    input_dir = Path(args.input_dir)
    output_dir = Path(args.output_dir)

    print(f"[INFO] 入力フォルダ: {input_dir}")
    print(f"[INFO] 出力フォルダ: {output_dir}")

    csv_files = find_csv_files(input_dir)
    print(f"[INFO] 見つかった CSV ファイル数: {len(csv_files)}")

    if not csv_files:
        print("[ERROR] CSV ファイルが 1 件も見つかりませんでした。処理を終了します。")
        return

    # 1. 読み込み & 結合
    merged = load_and_merge(csv_files)
    print(f"[INFO] 結合後の行数: {len(merged)}")

    # 2. 年月列を追加
    merged = add_year_month_columns(merged)

    # 3. 集計
    summary = summarize_by_month(merged)
    if summary.empty:
        print("[WARN] 集計に必要な列 (year, month, amount) が不足しているため、サマリは出力しません。")
    else:
        print(f"[INFO] サマリ行数: {len(summary)}")

    # 4. 出力
    merged_path, summary_path = export_results(merged, summary, output_dir)

    print(f"[OK] 結合データを出力しました: {merged_path}")
    if summary_path:
        print(f"[OK] 月別サマリを出力しました: {summary_path}")


if __name__ == "__main__":
    main()