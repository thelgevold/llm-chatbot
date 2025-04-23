from typing import TypedDict

class State(TypedDict):
    tool_call: dict
    query: str
    client: any
    result: any
