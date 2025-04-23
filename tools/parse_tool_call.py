import json

def parse_tool_call(res):
    start_index = res["tool_call_raw"].find("{")
    end_index = res["tool_call_raw"].rfind("}") + 1
    json_str = res["tool_call_raw"][start_index:end_index]
    data = json.loads(json_str)
    
    tool_call = {}

    tool_call["tool_name"] = data.get("name")
    current_agent = data.get("arguments", {}).get("current_agent")
    tool_call["tool_argument"] = {"current_agent": current_agent}

    return tool_call