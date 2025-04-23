from llm.model import init_llm_with_tool_calling
from tools.parse_tool_call import parse_tool_call

from agent.agent_service import AgentService

class RootAgent:
    def __init__(self):
        self.model = init_llm_with_tool_calling()
        self.agent_service = AgentService()

        self.agent_summary = self.agent_service.get_available_agents()

    def select_agent(self, request: str):
        prompt = f"""
        You are a expert delegator that can delegate the user request to the appropriate remote agents. The request from the users is {request}.

        Make sure to use the tool called select_current_agent to select a single agent, based on the agent descriptions, that will best serve the request.

        Here are the agents to chose from {self.agent_summary}.

        """

        result = self.model.invoke(prompt)
      
        tool_call= {}
        tool_call["tool_call_raw"] = result.content

        tool_details = parse_tool_call(tool_call)
        print(tool_details)