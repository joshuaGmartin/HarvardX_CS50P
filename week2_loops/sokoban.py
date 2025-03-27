def main():
    history = []

    while True:
        action = input("Action: ").lower()
        if action == "undo":
            print(history.pop(), "undone")
        elif action == "restart":
            history.clear()
        else:
            history.append(action)
        print(history)


main()
