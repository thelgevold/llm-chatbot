from langgraph.graph import StateGraph, START, END

from graph.graph_state import State
from nodes.chat_bot_node import ChatBotNode
from nodes.execute_tool_node import ExecuteToolNode
from nodes.call_agent_node import CallAgentNode

def bot_graph():
    graph_builder = StateGraph(State)
    graph_builder.add_node("chatbot", ChatBotNode)
    graph_builder.add_node("execute_tool", ExecuteToolNode)
    graph_builder.add_node("call_agent", CallAgentNode)

    graph_builder.add_edge(START, "chatbot")
    graph_builder.add_edge("chatbot", "execute_tool")
    graph_builder.add_edge("execute_tool", "call_agent")
    graph_builder.add_edge("call_agent", END)

    graph = graph_builder.compile()

    return graph