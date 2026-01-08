FILE_NAME = "tasks.txt"


def load_tasks():
    """Load tasks from file"""
    try:
        with open(FILE_NAME, "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    """Save tasks to file"""
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")


def view_tasks(tasks):
    """Display all tasks"""
    if not tasks:
        print("\nNo tasks available.")
        return

    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def add_task(tasks):
    """Add a new task"""
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("Task added successfully.")
    else:
        print("Task cannot be empty.")


def delete_task(tasks):
    """Delete a task by index"""
    view_tasks(tasks)

    if not tasks:
        return

    try:
        task_num = int(input("Enter task number to delete: "))
        removed_task = tasks.pop(task_num - 1)
        save_tasks(tasks)
        print(f"Task '{removed_task}' deleted.")
    except (ValueError, IndexError):
        print("Invalid task number.")


def show_menu():
    print("\n===== TO-DO APP =====")
    print("1. View tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Exit")


def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice. Please select 1-4.")


if __name__ == "__main__":
    main()
