from pathlib import Path
from typing import List, Tuple

import pandas as pd


def find_csv_files(input_dir: Path) -> List[Path]:
    """指定ディレクトリ内の CSV ファイルをすべて探して返す"""
    return sorted(input_dir.glob("*.csv"))


def load_and_merge(csv_files: List[Path]) -> pd.DataFrame:
    """CSV ファイルをすべて読み込み、1つの DataFrame に結合する"""
    if not csv_files:
        raise FileNotFoundError("CSV ファイルが見つかりませんでした。")

    frames = []
    for path in csv_files:
        df = pd.read_csv(path)
        df["__source_file"] = path.name  # どのファイル由来か分かるように
        frames.append(df)

    merged = pd.concat(frames, ignore_index=True)
    return merged


def add_year_month_columns(df: pd.DataFrame) -> pd.DataFrame:
    """date 列から year, month を追加する（列名は必要に応じて調整）"""
    if "date" not in df.columns:
        # date 列が存在しない場合はそのまま返す
        return df

    # pandas が自動で日付に変換（エラーは NaT）
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month
    return df


def summarize_by_month(df: pd.DataFrame) -> pd.DataFrame:
    """年月別に amount の合計を集計する"""
    # 必要な列がない場合は空の DataFrame を返す
    for col in ("year", "month", "amount"):
        if col not in df.columns:
            return pd.DataFrame()

    summary = (
        df.groupby(["year", "month"], as_index=False)["amount"]
        .sum()
        .sort_values(["year", "month"])
    )
    return summary


def export_results(
    merged: pd.DataFrame,
    summary: pd.DataFrame,
    output_dir: Path,
) -> Tuple[Path, Path | None]:
    """結果を CSV として出力する"""
    output_dir.mkdir(parents=True, exist_ok=True)

    merged_path = output_dir / "merged_data.csv"
    merged.to_csv(merged_path, index=False)

    summary_path = None
    if not summary.empty:
        summary_path = output_dir / "summary_by_month.csv"
        summary.to_csv(summary_path, index=False)

    return merged_path, summary_path