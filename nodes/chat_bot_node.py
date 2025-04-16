from agent.root_agent import RootAgent

from graph.graph_state import State

def ChatBotNode(state: State):
    root_agent = RootAgent()

    query = state["query"]

    tool = root_agent.select_agent(query)

    return {"tool_call": tool}