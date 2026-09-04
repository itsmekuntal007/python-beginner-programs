import os

FILE_NAME = "tasks.txt"


def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        return [line.strip() for line in file if line.strip()]


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")


def show_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")


tasks = load_tasks()

while True:
    print("\n===== TO-DO LIST V2 =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter a task: ").strip()

        if task:
            tasks.append(task)
            save_tasks(tasks)
            print("✅ Task added successfully.")
        else:
            print("❌ Task cannot be empty.")

    elif choice == "2":
        show_tasks(tasks)

    elif choice == "3":
        show_tasks(tasks)

        if tasks:
            try:
                task_number = int(input("Enter the task number to remove: "))

                if 1 <= task_number <= len(tasks):
                    removed_task = tasks.pop(task_number - 1)
                    save_tasks(tasks)
                    print(f"🗑️ Removed: {removed_task}")
                else:
                    print("❌ Invalid task number.")

            except ValueError:
                print("❌ Please enter a valid number.")

    elif choice == "4":
        print("👋 Exiting To-Do List V2. Goodbye!")
        break

    else:
        print("❌ Invalid choice. Please choose 1-4.")