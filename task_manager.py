tasks = []

def show_menu():
    print("\nTask Manager")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Mark Task as Done")
    print("5. Exit")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks):
            status = "Done" if task["done"] else "Pending"
            print(f"{i + 1}. {task['task']} - {status}")

def add_task():
    task_name = input("Enter the task: ")
    tasks.append({"task": task_name, "done": False})
    print("Task added.")

def remove_task():
    view_tasks()
    try:
        index = int(input("Enter the number of the task to remove: ")) - 1
        removed = tasks.pop(index)
        print(f"Removed task: {removed['task']}")
    except (IndexError, ValueError):
        print("Invalid task number.")

def mark_done():
    view_tasks()
    try:
        index = int(input("Enter the number of the task to mark as done: ")) - 1
        tasks[index]["done"] = True
        print(f"Marked as done: {tasks[index]['task']}")
    except (IndexError, ValueError):
        print("Invalid task number.")

while True:
    show_menu()
    choice = input("Choose an option (1–5): ")
    
    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        mark_done()
    elif choice == "5":
        print("Exiting Task Manager.")
        break
    else:
        print("Invalid choice. Please select a number from 1 to 5.")
