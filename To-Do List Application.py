tasks = []

while True:
    action = input("Add/View/Remove/Quit: ").lower()
    if action == "add":
        task = input("Enter task: ")
        tasks.append(task)
    elif action == "view":
        for i, t in enumerate(tasks):
            print(f"{i + 1}. {t}")
    elif action == "remove":
        index = int(input("Enter task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            tasks.pop(index)
    elif action == "quit":
        break
    else:
        print("Unknown command.")
