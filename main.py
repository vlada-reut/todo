# main.py
from tasks import TaskManager
from storage import load_tasks, save_tasks

def print_menu():
    print("\nДобро пожаловать!\n📋 Меню задач:")
    print("1. Показать задачи")
    print("2. Добавить задачу")
    print("3. Удалить задачу по номеру")
    print("4. ✍️Редактировать задачу")
    print("5. Сохранить задачу и выйти")

def main():
    tasks = load_tasks()
    manager = TaskManager(tasks)

    while True:
        print_menu()
        user_choice = input("Выберите действие (1-5): ")

        if choice == "1":
            manager.display_tasks()
        elif choice == "2":
            title = input("Введите заголовок задачи: ")
            desc = input("Введите описание задачи: ")
            manager.add_task(title, desc)
        elif choice == "3":
            index = input("Введите номер задачи для удаления: ")
            manager.delete_task(index)
        elif choice == "4":
            index = input("Введите номер задачи для редактирования: ")
            new_title = input("Новый заголовок (оставьте пустым, если не менять): ")
            new_desc = input("Новое описание (оставьте пустым, если не менять): ")
            manager.edit_task(index, new_title, new_desc)
        elif choice == "5":
            save_tasks(manager.tasks)
            print("✅ Задачи сохранены. До свидания!")
            break
        else:
            print("❌ Неверный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()
