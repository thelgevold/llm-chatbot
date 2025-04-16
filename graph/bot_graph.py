from langgraph.graph import StateGraph, START, END

from graph.graph_state import State
from nodes.chat_bot_node import ChatBotNode

def bot_graph():
    graph_builder = StateGraph(State)
    graph_builder.add_node("chatbot", ChatBotNode)

    graph_builder.add_edge(START, "chatbot")
    graph_builder.add_edge("chatbot", END)

    graph = graph_builder.compile()

    return graph