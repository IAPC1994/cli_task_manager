import json
import os

FILE_PATH = "tasks.json"  # File to store the tasks


def load_tasks():
    if not os.path.exists(FILE_PATH):
        return []

    # with safe way to manage files. Open the file and then close it.
    # Parameter 2 (Mode): "r" read - "w" write - "a" add at the end - "r+" read and write at the end
    with open(FILE_PATH, "r", encoding="utf-8") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []


def save_tasks(tasks):
    with open(FILE_PATH, "w", encoding="utf-8") as file:
        # Write a python object in the file with JSON format.
        json.dump(tasks, file, indent=4)
