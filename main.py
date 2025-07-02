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
