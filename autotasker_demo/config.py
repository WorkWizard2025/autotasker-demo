from pathlib import Path

# プロジェクトルート = このファイルの2階層上
PROJECT_ROOT = Path(__file__).resolve().parents[1]

DEFAULT_INPUT_DIR = PROJECT_ROOT / "sample_data"
DEFAULT_OUTPUT_DIR = PROJECT_ROOT / "output"