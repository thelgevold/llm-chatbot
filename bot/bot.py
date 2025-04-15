while True:
    try:
        user_input = input("User: ")
        if user_input.lower() in ["quit", "exit", "q"]:
            print("Goodbye!")
            break
        #stream_graph_updates(user_input)
    except Exception as e:
        print(e)
        break