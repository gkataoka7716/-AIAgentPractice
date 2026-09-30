from langchain_core.tools import tool


@tool
def calculator(expression: str) -> str:
    """数学計算を実行する。例: 123 * 456"""

    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return str(result)
    except Exception as e:
        return f"計算エラー: {e}"