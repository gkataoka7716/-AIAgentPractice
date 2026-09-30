from langchain_core.messages import HumanMessage

from graph import graph


def main():
    print("AI Agent started.")
    print("exit で終了します。")

    while True:
        user_input = input("\nYou: ")

        if user_input.lower() == "exit":
            break

        result = graph.invoke(
            {
                "messages": [
                    HumanMessage(content=user_input)
                ]
            }
        )

        print("\nAI:")

        print(result["messages"][-1].content)


if __name__ == "__main__":
    main()