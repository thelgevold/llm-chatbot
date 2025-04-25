import asyncio
from uuid import uuid4
from agent.root_agent import RootAgent
from A2A.samples.python.common.client.client import A2AClient
from A2A.samples.python.common.types import TaskState, Task
from A2A.samples.python.hosts.cli.push_notification_listener import PushNotificationListener
from A2A.samples.python.common.utils.push_notification_auth import PushNotificationReceiverAuth
import json

async def completeTask(client, prompt, taskId, sessionId, resume):
  
    payload = {
        "id": taskId,
        "sessionId": sessionId,
        "acceptedOutputModes": ["text"],
        "message": {
            "role": "user",
            "parts": [
                {
                    "type": "text",
                    "text": prompt,
                }
            ],
        },
        "resume": resume
    }

    taskResult = await client.send_task(payload)
    result = json.loads(taskResult.model_dump_json(exclude_none=True))
        
    if result["result"]["status"]["state"] == "input-required":
        for p in result["result"]["status"]["message"]["parts"]:
            print(p["text"])

    if result["result"]["status"]["state"] == "completed":
        for a in result["result"]["artifacts"]:
            for p in a["parts"]:
                print(p["text"])
  
    state = TaskState(taskResult.result.status.state)
    if state.name == TaskState.INPUT_REQUIRED.name:
        prompt = input("User: ")
        return await completeTask(client=client, prompt=prompt, taskId=taskId, sessionId=sessionId, resume=True)
        
    else:
        ## task is complete
        return True


async def chat_loop():
    continue_loop = True
    root_agent = RootAgent()
    
    while continue_loop:
        try:
            task_id = uuid4().hex    
            session_id = uuid4().hex

            prompt = input("User: ")

            if prompt == ":q" or prompt == "quit":
                return False
            
            client, host, port = root_agent.select_agent(prompt) 

            continue_loop = await completeTask(client=client, prompt=prompt, resume=False, taskId=task_id, sessionId=session_id)

        except Exception as e:
            print(f"Error: {e}")
            break

if __name__ == "__main__":
    asyncio.run(chat_loop())