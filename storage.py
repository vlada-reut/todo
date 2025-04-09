# storage.py

import json
import os

TASKS_DB = "tasks.json"  # Файл для хранения задач

def load_tasks():
    """Загружает задачи из файла, если он существует."""
    if not os.path.exists(TASKS_DB):
        return []
    try:
        with open(TASKS_DB, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    except json.JSONDecodeError:
        print("⚠️ Ошибка при чтении файла задач. Начинаем с пустого списка.")
        return []

def save_tasks(task_list):
    """Сохраняет задачи в файл."""
    with open(TASKS_DB, "w", encoding="utf-8") as file:
        json.dump([t.to_dict() for t in task_list], file, indent=4, ensure_ascii=False)
    print("💾 Задачи успешно сохранены.")
