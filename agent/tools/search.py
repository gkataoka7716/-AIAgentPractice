from langchain_core.tools import tool


documents = [
    {
        "title": "Python",
        "content": "Pythonは汎用プログラミング言語です。",
    },
    {
        "title": "LangChain",
        "content": "LangChainはLLMアプリケーションを構築するためのフレームワークです。",
    },
    {
        "title": "LangGraph",
        "content": "LangGraphは状態を持つAIエージェントのワークフローを構築できます。",
    },
    {
        "title": "Ollama",
        "content": "Ollamaはローカル環境でLLMを実行できます。",
    },
]


@tool
def search_knowledge(query: str) -> str:
    """登録されている知識から質問に関連する情報を検索する。"""

    results = []

    for document in documents:
        if (
            query.lower() in document["title"].lower()
            or query.lower() in document["content"].lower()
        ):
            results.append(
                f"{document['title']}: {document['content']}"
            )

    if not results:
        return "関連する情報が見つかりませんでした。"

    return "\n".join(results)