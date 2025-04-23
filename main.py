import asyncio
from graph.bot_graph import bot_graph

async def chat_loop():
    while True:
        try:
            user_input = input("User: ")
            if user_input.lower() in ["quit", "exit", "q"]:
                print("Goodbye!")
                break

            graph = bot_graph()
            result = await graph.ainvoke({"query": user_input})
            print(f"Bot: {result["result"]}")
        except Exception as e:
            print(f"Error: {e}")
            break

if __name__ == "__main__":
    asyncio.run(chat_loop())