import asyncio
from graph.bot_graph import bot_graph
from uuid import uuid4

async def chat_loop():
    while True:
        try:
            user_input = input("User: ")
            if user_input.lower() in ["quit", "exit", "q"]:
                print("Goodbye!")
                break

            payload = {
            "id": uuid4().hex,
            "sessionId": uuid4().hex,
            "acceptedOutputModes": ["text"],
            "message": {
                "role": "user",
                "parts": [
                    {
                        "type": "text",
                        "text": user_input,
                    }
                ],
                },
            }

            graph = bot_graph()
            result = await graph.ainvoke({"query": user_input, "payload": payload})
            print(f"Bot: {result["result"]}")
        except Exception as e:
            print(f"Error: {e}")
            break

if __name__ == "__main__":
    asyncio.run(chat_loop())