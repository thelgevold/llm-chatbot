from pydantic import Field
from langchain_core.tools import tool

@tool
def select_current_agent(current_agent = Field(description="The most appropriate agent to use for the assigned task")):
    """Selects the best agent for the task at hand"""

    return current_agent