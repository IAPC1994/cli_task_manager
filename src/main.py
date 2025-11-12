import os
from .task_manager import list_tasks, add_task, complete_task, delete_task


def clear_console():
    # cls in Windows, clear in Linux/Mac
    os.system("cls" if os.name == "nt" else "clear")


def show_menu():
    print("==== Task Manager ====")
    print("1. List tasks")
    print("2. Add task")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Exit")


def main():
    while True:
        clear_console()
        show_menu()

        option = input("\nChoose an option: ")

        match option:
            case "1":
                list_tasks()
            case "2":
                add_task()
            case "3":
                complete_task()
            case "4":
                delete_task()
            case "5":
                clear_console()
                print("\nGoodbye!👋")
                break
            case _:
                print("\nInvalid option, please try again.")
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
