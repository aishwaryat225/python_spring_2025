import json
import os

# File to store tasks persistently
TASKS_FILE = "tasks.json"

def load_tasks():
    """Load tasks from the JSON file."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks, task_name):
    """Add a new task to the list."""
    tasks.append({"task": task_name, "completed": False})
    save_tasks(tasks)
    print(f'Task "{task_name}" added.')

def view_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("No tasks found.")
    else:
        for idx, task in enumerate(tasks, 1):
            status = "[✓]" if task["completed"] else "[ ]"
            print(f"{idx}. {status} {task['task']}")

def mark_task_completed(tasks, task_index):
    """Mark a task as completed."""
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        save_tasks(tasks)
        print(f'Task "{tasks[task_index]["task"]}" marked as completed.')
    else:
        print("Invalid task number.")

def remove_task(tasks, task_index):
    """Remove a task from the list."""
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        save_tasks(tasks)
        print(f'Task "{removed_task["task"]}" removed.')
    else:
        print("Invalid task number.")

def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Remove Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            task_name = input("Enter task: ").strip()
            add_task(tasks, task_name)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            view_tasks(tasks)
            task_index = int(input("Enter task number to mark as completed: ")) - 1
            mark_task_completed(tasks, task_index)

        elif choice == "4":
            view_tasks(tasks)
            task_index = int(input("Enter task number to remove: ")) - 1
            remove_task(tasks, task_index)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
