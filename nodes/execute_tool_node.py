from graph.graph_state import State
from langchain_core.messages import ToolMessage

from tools.select_agent import select_current_agent

tools = [select_current_agent]
tools_names = {t.name: t for t in tools}

def ExecuteToolNode(state: State):
    tool = state["tool_call"]

    a2a_client = tools_names[tool["tool_name"]].invoke(tool["tool_argument"])

    return {"client": a2a_client}

    #return {"messages": [ToolMessage(artifact=res, content="Completed calling tools to categorize articles", tool_call_id="123")], "structured_response": structured_response}
