import sys
from lib.tasks import load_taks, save_tasks, add_task, view_tasks,
    complete_task, delete_task

def main():
    tasks = load_taks()

    