import json

def parse_tool_call(res):
    start_index = res["tool_call_raw"].find("{")
    end_index = res["tool_call_raw"].rfind("}") + 1
    json_str = res["tool_call_raw"][start_index:end_index]

    data = json.loads(json_str)
    
    tool_call = {}

    tool_call["tool_name"] = data.get("name")
    categories = data.get("arguments", {}).get("res_categories")
    tool_call["tool_argument"] = {"res_categories": categories}

    return tool_call