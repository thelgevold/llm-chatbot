import json

def parse_tool_call(res):
    print("starting parsing")
    start_index = res["tool_call_raw"].find("{")
    print(start_index)
    end_index = res["tool_call_raw"].rfind("}") + 1
    print(end_index)
    json_str = res["tool_call_raw"][start_index:end_index]
    print(json_str)
    data = json.loads(json_str)
    
    tool_call = {}

    tool_call["tool_name"] = data.get("name")
    categories = data.get("arguments", {}).get("current_agent")
    tool_call["tool_argument"] = {"current_agent": categories}

    return tool_call