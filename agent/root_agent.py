from llm.model import init_llm_with_tool_calling
from tools.parse_tool_call import parse_tool_call
from urllib.parse import urlparse
from agent.agent_context import AgentContext

from tools.select_agent import select_current_agent

tools = [select_current_agent]
tools_names = {t.name: t for t in tools}

class RootAgent:
    def __init__(self):
        self.model = init_llm_with_tool_calling()
   
    def select_agent(self, request: str):
        agent_context = AgentContext()
        
        prompt = f"""
        You are a expert delegator that can delegate the user request to the appropriate remote agents. The request from the users is {request}.

        Make sure to use the tool called select_current_agent to select a single agent, based on the agent descriptions, that will best serve the request.

        Here are the agents to chose from {agent_context.agent_summary}.

        """

        result = self.model.invoke(prompt)
      
        tool_call= {}
        tool_call["tool_call_raw"] = result.content

        tool_details = parse_tool_call(tool_call)
        tool_details["user_query"] = request

        client = tools_names[tool_details["tool_name"]].invoke(tool_details["tool_argument"]) 

        url = next(agent["url"] for agent in agent_context.agent_summary if agent["name"] == tool_details["tool_argument"]["current_agent"])

        url_parts = urlparse(url)

        print(f"Found this url {url}")

        return client, url_parts.hostname, url_parts.port 
      