from graph.graph_state import State
from uuid import uuid4

async def CallAgentNode(state: State):
    prompt = state["query"]
    client = state["client"]
    payload = state["payload"]
   
    taskResult = await client.send_task(payload)
   
    return {"result": taskResult.model_dump_json(exclude_none=True)}
