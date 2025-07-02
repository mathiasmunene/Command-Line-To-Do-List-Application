import sys
from lib.tasks import load_taks, save_tasks, add_task, view_tasks,
    complete_task, delete_task

def main():
    tasks = load_taks()

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
        
