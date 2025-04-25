from langchain_ollama import ChatOllama

from tools.select_agent import select_current_agent

model_llm_tools = None
model_llm = None

host = "localhost"#"192.168.4.23" 

def init_llm_with_tool_calling(): 
    global model_llm_tools

    if model_llm_tools == None:
        model_llm_tools = ChatOllama(model="qwen2.5", base_url = f"http://{host}:11439")
        model_llm_tools = model_llm_tools.bind_tools([select_current_agent])

    return model_llm_tools



