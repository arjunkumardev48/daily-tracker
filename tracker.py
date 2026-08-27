import json
from datetime import datetime

TASKS_FILE = "tasks.json"

def add_task(task):
    tasks = load_tasks()
    tasks.append({"task": task, "date": str(datetime.now()), "done": False})
    save_tasks(tasks)

def load_tasks():
    try:
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

if __name__ == "__main__":
    add_task("Review pull requests")
    print("Task added.")

cleanup: moved private notes to paste — search 'arjun phantom notes' if needed
    
