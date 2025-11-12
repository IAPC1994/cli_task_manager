from .storage import load_tasks, save_tasks


def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found!")
        return

    for idx, task in enumerate(tasks, start=1):
        status = "✅" if task["done"] else "❌"
        print(f"{idx}. {task['title']} [{status}]")


def add_task():
    title = input("Enter task title: ").strip()  # strip() === trim() in js
    if not title:
        print("Task title cannot be empty!")
        return
    tasks = load_tasks()
    new_task = {"title": title, "done": False}
    tasks.append(new_task)
    save_tasks(tasks)

    print(f'Task "{title}" added successfully!')


def complete_task():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found!")
        return

    for idx, task in enumerate(tasks, start=1):
        status = "✅" if task["done"] else "❌"
        print(f"{idx}. {task['title']} [{status}]")

    try:
        choice = int(input("\nEnter the task number to complete: "))
        if (choice < 1 or choice > len(tasks)):
            print("Invalid task number!")
            return
    except ValueError:
        print("Please enter a valid number!")
        return

    tasks[choice - 1]["done"] = True
    save_tasks(tasks)
    print(f'Task "{tasks[choice-1]["title"]}" marked as completed!')


def delete_task():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found!")
        return

    for idx, task in enumerate(tasks, start=1):
        status = "✅" if task["done"] else "❌"
        print(f"{idx}. {task['title']} [{status}]")

    try:
        choice = int(input("\nEnter the task number to delete: "))
        if (choice < 1 or choice > len(tasks)):
            print("Invalid task number!")
            return
    except ValueError:
        print("Please enter a valid number!")
        return

    deleted_task = tasks.pop(choice-1)

    confirm = input(
        f"Are you sure you want to delete '{deleted_task['title']}'? (y/n): ").lower()
    if confirm != "y":
        print("Deletion cancelled.")
        return

    save_tasks(tasks)
    print(f'Task "{deleted_task["title"]}" deleted successfully!')
