import json

def add_task():

    with open("tasks.json", "r") as f:
        data = json.load(f)

    for i, task in enumerate(data["tasks"], start = 1):
        print(f"{i}, {task['text']}")

    task = input("What task do you want to add? ")


    data["tasks"]. append({"text": task, "done": False})

    with open("tasks.json", "w") as f:
        json.dump(data,f, indent = 4)
    

def complete_task():
    with open ("tasks.json", "r") as f:
        data = json.load(f)

    print("Your current tasks: ")
    for i, task in enumerate(data["tasks"], start = 1):
        checkbox = "[X]" if task ["done"] else "[ ]"
        print(f"{i}, {task['text']}, {checkbox}")
    
    user_input = input("What task have you completed? ")
    done_index = int(user_input)

    task_idx = done_index - 1
    data ["tasks"] [task_idx] ["done"] = True
    print(f"✅ Marked '{data['tasks'][task_idx]['text']}' as done.")

    with open("tasks.json", "w") as f:
        json.dump(data, f, indent= 4)


def view_tasks():
    with open("tasks.json", "r") as f:
        data = json.load(f)

        for i, task in enumerate(data["tasks"], start=1):
            checkbox = "[x]" if task["done"] else "[ ]"
            print(f"{i}. {checkbox} {task['text']}")

def remove_task():
    with open("tasks.json", "r") as f:
        data = json.load(f)

    for i, task in enumerate(data["tasks"], start=1):
        checkbox = "[x]" if task["done"] else "[ ]"
        print(f"{i}. {checkbox} {task['text']}")

    del_data = input("what task do you wanna delete?")

    if del_data.isdigit():
        index = int(del_data) - 1
        if 0 <= index < len(data["tasks"]):
            removed = data["tasks"].pop(index)
            print(f"🗑️ Removed: {removed['text']}")
        else:
            print("Invalid task number.")
    else:
        print("Please enter a valid number.")

    with open("tasks.json", "w") as f:
        json.dump(data, f, indent=4)

while True:
    command = input("What do you want to do? (add, complete, view, remove, quit): ").lower()
    
    if command == "add":
        add_task()
    elif command == "complete":
        complete_task()
    elif command == "remove":
        remove_task()
    elif command == "view":
        view_tasks()
    elif command == "quit":
        print("Bye!")
        break
    else:
        print("Unknown command.")
