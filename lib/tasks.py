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



            