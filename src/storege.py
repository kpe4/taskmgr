import json
import os

def load(task,name_file):

    if not os.path.exists(name_file):
        save(task,name_file)
        return task
    with open(name_file, "r", encoding="utf-8") as f:
        task = json.load(f)
        return task
def save(task,name_file):
    with open(name_file, "w", encoding="utf-8") as f:
        json.dump(task, f, indent=4, ensure_ascii=False)