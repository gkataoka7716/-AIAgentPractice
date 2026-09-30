from pathlib import Path

from langchain_core.tools import tool


@tool
def read_file(filename: str) -> str:
    """dataディレクトリにあるテキストファイルを読み取る。"""

    path = Path("/app/data") / filename

    if not path.exists():
        return f"ファイルが見つかりません: {filename}"

    if not path.is_file():
        return f"ファイルではありません: {filename}"

    try:
        return path.read_text(encoding="utf-8")
    except Exception as e:
        return f"ファイル読み込みエラー: {e}"