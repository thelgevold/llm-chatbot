from llm.model import init_llm_with_tool_calling, init_llm
from tools.parse_tool_call import parse_tool_call

from urllib.parse import urlparse
from agent.agent_context import AgentContext

from tools.select_agent import select_current_agent
from datetime import datetime

tools = [select_current_agent]
tools_names = {t.name: t for t in tools}

class RootClient:
    async def send_task(self, payload):
        llm = init_llm()

        query = payload["message"]["parts"][-1]["text"]

        response = llm.invoke(query)

        response = {
            "result": {
                        "id": payload["sessionId"],
                        "status": {"state": "completed", "timestamp": datetime.now().timestamp()},
                        "artifacts":[{"parts": [{"text": response.content}]}]
                      }
            }

        return response

class RootAgent:
    def __init__(self):
        self.model = init_llm_with_tool_calling()
   
    def select_agent(self, request: str):
        agent_context = AgentContext()
        
        prompt = f"""
        You are a expert delegator that can delegate the user request to the appropriate remote agents. The request from the users is {request}.

        Make sure to use the tool called select_current_agent to select a single agent, based on the agent descriptions, that will best serve the request.

        Here are the agents to chose from {agent_context.agent_summary}. If you are unable to pick an appropriate agent based on the agent descriptions, please respond select the option "root_agent".

        """

        result = self.model.invoke(prompt)

        tool_call= {}
        tool_call["tool_call_raw"] = result.content

        tool_details = parse_tool_call(tool_call)
        tool_details["user_query"] = request

        agent_name = tool_details["tool_argument"]["current_agent"]

        if agent_name == "root_agent":
            client = RootClient()
        else:
            print("*********************************************************************************************************************")
            print(f"I have determined that this can best be answered by external agent {agent_name}. Hang on while I reach out over A2A")
            print("*********************************************************************************************************************")
            client = tools_names[tool_details["tool_name"]].invoke(tool_details["tool_argument"]) 

        return client
      