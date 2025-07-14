import json
from colorama import Fore, Style, init
init(autoreset=True) 

def add_task():

    with open("tasks.json", "r") as f:
        data = json.load(f)

    for i, task in enumerate(data["tasks"], start = 1):
        print(f"{i}, {task['text']}")

    task = input("What task do you want to add? If none write 0 ").lower()

    if task == "0":
        view_tasks()
        return


    data["tasks"]. append({"text": task, "done": False})

    print(Fore.GREEN +"Task added succesuflly")

    with open("tasks.json", "w") as f:
        json.dump(data,f, indent = 4)
    

def complete_task():
    with open ("tasks.json", "r") as f:
        data = json.load(f)

    print("Your current tasks: ")
    for i, task in enumerate(data["tasks"], start = 1):
        checkbox = "[X]" if task ["done"] else "[ ]"
        print(f"{i}, {task['text']}, {checkbox}")
    
    user_input = input(Fore.GREEN +"What task have you completed? If none write 0 ")

    if user_input == "0":
        view_tasks()
        return

    if user_input not in data:
        print (Fore.RED +"Task does not exsist")
        return

    if not user_input .isdigit():
        print(Fore.RED +"please write a didget")
        return
    done_index = int(user_input)

    task_idx = done_index - 1
    data ["tasks"] [task_idx] ["done"] = True
    print(f" Marked '{data['tasks'][task_idx]['text']}' as done.")

    with open("tasks.json", "w") as f:
        json.dump(data, f, indent= 4)


def view_tasks():
    with open("tasks.json", "r") as f:
        data = json.load(f)

        for i, task in enumerate(data["tasks"], start=1):
            checkbox = "[x]" if task["done"] else "[ ]"
            print(Fore.YELLOW + f"{i}. {checkbox} {task['text']}")

def remove_task():
    with open("tasks.json", "r") as f:
        data = json.load(f)

    for i, task in enumerate(data["tasks"], start=1):
        checkbox = "[x]" if task["done"] else "[ ]"
        print(f"{i}. {checkbox} {task['text']}")

    del_data = input(Fore.RED +"what task do you wanna delete? If you don't want to delete any write 0. ")
    if del_data == "0":
        view_tasks()
        return


    if del_data.isdigit():
        index = int(del_data) - 1
        if 0 <= index < len(data["tasks"]):
            removed = data["tasks"].pop(index)
            print(Fore.RED +"Task deleted succesfully")
        else:
            print(Fore.RED +"Invalid task number.")
    else:
        print(Fore.RED +"Please enter a valid number.")



    with open("tasks.json", "w") as f:
        json.dump(data, f, indent=4)

while True:
    command = input(Fore.BLUE + Style.BRIGHT + """
-------------------------------------------------------------------------------------------------------------------------------------------
    What do you want to do? 

    Add a task (1) 
    Complete a task (2) 
    View your tasks (3) 
    Remove a task (4)
    Quit.(5):
-------------------------------------------------------------------------------------------------------------------------------------------
    """
                    
    ).lower()
    
    if command == "1":
        add_task()
    elif command == "2":
        complete_task()
    elif command == "4":
        remove_task()
    elif command == "3":
        view_tasks()
    elif command == "5":
        print(Fore.RED + "Bye!")
        break
    else:
        print(Fore.RED +"Unknown command.")

