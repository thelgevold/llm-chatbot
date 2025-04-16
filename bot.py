from graph.bot_graph import bot_graph

while True:
    try:
        user_input = input("User: ")
        if user_input.lower() in ["quit", "exit", "q"]:
            print("Goodbye!")
            break
        
        graph = bot_graph()
        graph.invoke({"query": user_input})
    except Exception as e:
        print(e)
        break