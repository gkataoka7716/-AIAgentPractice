from langgraph.graph import START, END, StateGraph
from langgraph.prebuilt import ToolNode, tools_condition

from llm.ollama import llm
from state import AgentState

from tools.calculator import calculator
from tools.file_reader import read_file
from tools.search import search_knowledge


tools = [
    calculator,
    read_file,
    search_knowledge,
]

llm_with_tools = llm.bind_tools(tools)


def call_agent(state: AgentState):
    response = llm_with_tools.invoke(state["messages"])

    return {
        "messages": [response]
    }


tool_node = ToolNode(tools)


builder = StateGraph(AgentState)

builder.add_node("agent", call_agent)
builder.add_node("tools", tool_node)

builder.add_edge(START, "agent")

builder.add_conditional_edges(
    "agent",
    tools_condition,
)

builder.add_edge("tools", "agent")

graph = builder.compile()