from pydantic import Field

def select_current_agent(current_agent = Field(description="The most appropriate agent to use for the assigned task")):
    return current_agent