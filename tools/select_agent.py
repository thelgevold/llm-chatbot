from pydantic import Field
from langchain_core.tools import tool
from agent.agent_context import AgentContext

@tool
def select_current_agent(current_agent = Field(description="The most appropriate agent to use for the assigned task")):
    """Selects the best agent for the task at hand"""

    agent_context = AgentContext()

    a2a_client = agent_context.clients[current_agent]

    return a2a_client