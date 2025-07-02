import sys
from lib.tasks import load_tasks, save_tasks, add_task, view_tasks, complete_task, delete_task

def main():
    tasks = load_tasks()
    while True:
        print("\nTo-do List Application")
        print("1. View Task")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            description = input("Enter task description: ")
            add_task(tasks, description)
            save_tasks(tasks)
            print("Task added successfully.")
        elif choice == "3":
            view_tasks(tasks)
            try:
                index = int(input("Enter task number to mark as complete: ")) - 1
                complete_task(tasks, index)
                save_tasks(tasks)
                print("Task marked as complete.")
            except (ValueError, IndexError):
                print("Invalid task number. Please try again.")
        elif choice == "4":
            view_tasks(tasks)
            try:
                index = int(input("Enter task number to delete: ")) - 1
                delete_task(tasks, index)
                save_tasks(tasks)
                print("Task deleted successfully.")
            except (ValueError, IndexError):
                print("Invalid task number. Please try again.")
        elif choice == "5":
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()