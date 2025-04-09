# tasks.py

class Task: # Класс Task представляет одну задачу с заголовком и описанием
    def __init__(self, title, description):
        self.title = title
        self.description = description

    def to_dict(self):
        return {"title": self.title, "description": self.description}

    @staticmethod
    def from_dict(data):
        return Task(data["title"], data["description"])

class TaskManager:
    def __init__(self, task_list):
        self.tasks = [Task.from_dict(t) for t in task_list]

    def add_task(self, title, description):
        task = Task(title, description)
        self.tasks.append(new_task)
        print(f"✅ Задача \"{title}\" добавлена.")

    def delete_task(self, index_str):
        try:
            index = int(index_str) - 1
            removed = self.tasks.pop(index)
            print(f"🗑️ Задача \"{removed.title}\" удалена.")
        except (ValueError, IndexError):
            print("❌ Неверный номер задачи.")

    def edit_task(self, index_str, new_title, new_description):
        try:
            index = int(index_str) - 1
            task = self.tasks[index]
            if new_title:
                task.title = new_title
            if new_description:
                task.description = new_description
            print(f"✏️ Задача обновлена.")
        except (ValueError, IndexError):
            print("❌ Неверный номер задачи.")

    def display_tasks(self):
        if not self.tasks:
            print("📭 Список задач пуст.")
            return
        print("\n📋 Список задач:")
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task.title} — {task.description}")
