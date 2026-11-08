import json
import os
from uuid import UUID, uuid4
from pathlib import Path


def _get_db_path(): # получение пути сохранений
    project_root = Path(__file__).parent.parent
    return project_root / "saves.json"

def load_task(task_id): # загрузка задачи
    db_path = _get_db_path()
    if not db_path.exists():
        return None
    
    with open(db_path, 'r', encoding='utf-8') as f:
        tasks = json.load(f)
    
    for task in tasks['tasks']:
        if task.get('id') == task_id:
            return task
    return None

def create_task(title, description): # создание задачи
    db_path = _get_db_path()
    
    if not db_path.exists():
        with open(db_path, 'w', encoding='utf-8') as f:
            json.dump({
                "version": 1,
                "created_at": None,
                "tasks": []
            }, f, ensure_ascii=False, indent=2)
    
    with open(db_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    task = {
        "id": str(uuid4()),
        "title": title,
        "description": description,
        "completed": False,
        "completed_at": None,
        "created_at": data.get("created_at"),
        "due_date": None
    }
    
    if not data.get("created_at"):
        data["created_at"] = task["created_at"]
    
    data["tasks"].append(task)
    
    with open(db_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    return task

def delete_task(task_id): # удаление задачи
    db_path = _get_db_path()
    if not db_path.exists():
        return False
    
    with open(db_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    original_task_count = len(data["tasks"])
    if isinstance(original_task_count, int):
        data["tasks"] = [t for t in data["tasks"] if t.get("id") != task_id]
        
    if len(data["tasks"]) < original_task_count:
        with open(db_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    
    return False

def update_task(task_id, title=None, description=None, completed=None): # обновление задачи
    db_path = _get_db_path()
    if not db_path.exists():
        return None
    with open(db_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    for task in data["tasks"]:
        if task.get("id") == task_id:
            if title is not None:
                task["title"] = title
            if description is not None:
                task["description"] = description
            if completed is not None:
                task["completed"] = completed
                task["completed_at"] = completed
                
            with open(db_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            
            return task
            
    return None

def get_all_tasks(): # получение всех задач
    db_path = _get_db_path()
    if not db_path.exists():
        return []
    
    with open(db_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    return data.get("tasks", [])

def get_tasks_as_dict_list():
    return get_all_tasks()


def store_task(task_id, title, description): # сохранение задачи
    try:
        task = create_task(title, description)
        return {'success': True, 'task': task}
    except Exception as e:
        return {'success': False, 'error': str(e)}
