from llm.model import init_llm_with_tool_calling
from tools import parse_tool_call

class RootAgent:
    def __init__(self):
        self.model = init_llm_with_tool_calling()

    def select_agent(self, request: str):
        prompt = f"""
        You are a expert delegator that can delegate the user request to the appropriate remote agents. The request from the users is {request}.

        Use the tool called select_current_agent to select a single agent that based on the agent descriptions will best serve the request.

        """

        result = self.model.invoke(prompt)

        tool_details = parse_tool_call(result)