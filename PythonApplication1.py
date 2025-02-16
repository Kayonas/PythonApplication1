# -*- coding: utf-8 -*-
# task_manager.py

tasks = []

def add_task(task):
    """Добавляет задачу в список."""
    tasks.append(task)
    print(f"Задача '{task}' добавлена.")

def list_tasks():
    """Выводит список задач."""
    if not tasks:
        return "Нет задач."
    return "\n".join(f"{i + 1}. {tasks[i]}" for i in range(len(tasks)))

def complete_task(task_id):
    """Отмечает задачу как выполненную."""
    try:
        completed_task = tasks.pop(task_id - 1)
        print(f"Задача '{completed_task}' выполнена.")
    except IndexError:
        print("Задача не найдена.")

def delete_task(task_id):
    """Удаляет задачу."""
    try:
        deleted_task = tasks.pop(task_id - 1)
        print(f"Задача '{deleted_task}' удалена.")
    except IndexError:
        print("Задача не найдена.")

def get_user_choice():
    """Получает выбор пользователя."""
    return input("Выберите действие (add/list/complete/delete/exit): ")

def main():
    """Главная функция."""
    print("Добро пожаловать в менеджер задач")
    while True:
        choice = get_user_choice()
        if choice == "add":
            task = input("Введите задачу: ")
            add_task(task)
        elif choice == "list":
            print(list_tasks())
        elif choice == "complete":
            task_id = int(input("Введите номер задачи для завершения: "))
            complete_task(task_id)
        elif choice == "delete":
            task_id = int(input("Введите номер задачи для удаления: "))
            delete_task(task_id)
        elif choice == "exit":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
<<<<<<< HEAD
    main()
=======
    main()
>>>>>>> 3fadb23c1d2f884034c424f6def737483f30563a
