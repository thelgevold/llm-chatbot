from langchain_ollama import ChatOllama

from tools.select_agent import select_current_agent

model_llm_tools = None
model_llm = None
 
def init_llm_with_tool_calling(): 
    global model_llm_tools

    if model_llm_tools == None:
        model_llm_tools = ChatOllama(model="qwen2.5", base_url = "http://localhost:11439")
        model_llm_tools = model_llm_tools.bind_tools([select_current_agent])

    return model_llm_tools

def init_llm(): 
    global model_llm

    if model_llm == None:
        model_llm = ChatOllama(model="llama3.2", base_url = "http://localhost:11438", num_ctx=3000)
       
    return model_llm



