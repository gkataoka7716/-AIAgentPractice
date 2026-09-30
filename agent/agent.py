import os

from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.graph import START, END, StateGraph
from langgraph.graph import MessagesState


# Ollamaの接続設定
llm = ChatOllama(
    model="llama3.2",
    base_url=os.getenv(
        "OLLAMA_BASE_URL",
        "http://localhost:11434",
    ),
)


# AIエージェントの処理
def call_model(state: MessagesState):
    response = llm.invoke(
        [
            SystemMessage(
                content="あなたは親切なAIアシスタントです。"
            ),
            *state["messages"],
        ]
    )

    return {"messages": [response]}


# LangGraphの構築
builder = StateGraph(MessagesState)

builder.add_node("agent", call_model)

builder.add_edge(START, "agent")
builder.add_edge("agent", END)

graph = builder.compile()


# 実行
def main():
    print("AIエージェントを起動しました。")
    print("終了するには exit と入力してください。")

    while True:
        user_input = input("\nあなた: ")

        if user_input.lower() == "exit":
            break

        result = graph.invoke(
            {
                "messages": [
                    HumanMessage(content=user_input)
                ]
            }
        )

        print("\nAI:", result["messages"][-1].content)


if __name__ == "__main__":
    main()