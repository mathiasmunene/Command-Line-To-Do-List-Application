def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = [line.strip().split("|") for line in file]
            return [{"description": task[0], "completed": task[1] == "True"} for task in tasks]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(f"{task['description']}|{task['completed']}\n")

def add_task(tasks, description):
    tasks.append({"description": description, "completed": False})

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    for i, task in enumerate(tasks, 1):
        status = "✔" if task["completed"] else " "
        print(f"{i}. [{status}] {task['description']}")

