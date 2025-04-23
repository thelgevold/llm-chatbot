import asyncio
from uuid import uuid4
from agent.root_agent import RootAgent
from A2A.samples.python.common.client.client import A2AClient
from A2A.samples.python.common.types import TaskState, Task

async def completeTask(taskId, sessionId, streaming = False, use_push_notifications = False, notification_receiver_host = None, notification_receiver_port = 5000):
    prompt = input("User: ")

    if prompt == ":q" or prompt == "quit":
        return False

    root_agent = RootAgent()
    client = root_agent.select_agent(prompt)   
  
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
    }

    if use_push_notifications:
        payload["pushNotification"] = {
            "url": f"http://{notification_receiver_host}:{notification_receiver_port}/notify",            
            "authentication": {
                "schemes": ["bearer"],
            },
        }

    taskResult = None
    if streaming:
        response_stream = client.send_task_streaming(payload)
        async for result in response_stream:
            print(f"stream event => {result.model_dump_json(exclude_none=True)}")
        taskResult = await client.get_task({"id": taskId})
    else:
        taskResult = await client.send_task(payload)
        print(f"\n{taskResult.model_dump_json(exclude_none=True)}")

    ## if the result is that more input is required, loop again.
    state = TaskState(taskResult.result.status.state)
    if state.name == TaskState.INPUT_REQUIRED.name:
        return await completeTask(
            streaming,
            use_push_notifications,
            notification_receiver_host,
            notification_receiver_port,
            taskId,
            sessionId
        )
    else:
        ## task is complete
        return True


async def chat_loop():
    continue_loop = True

    while continue_loop:
        try:
            task_id = uuid4().hex    
            session_id = uuid4().hex

            continue_loop = await completeTask(taskId=task_id, sessionId=session_id)

            

        except Exception as e:
            print(f"Error: {e}")
            break

if __name__ == "__main__":
    asyncio.run(chat_loop())