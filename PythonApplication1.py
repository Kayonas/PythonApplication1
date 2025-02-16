# task_manager.py
# -*- coding: utf-8 -*-

# ����� �������� ��� ���
print("������ ��������� � �������������� ��������� UTF-8")
def add_task(task):
    """��������� ������."""
    pass

def list_tasks():
    """������� ������ �����."""
    return "�������"

def complete_task(task_id):
    """�������� ������ ��� �����������."""
    pass

def delete_task(task_id):
    """������� ������."""
    pass

def main():
    """������� �������."""
    print("����� ���������� � �������� �����")

if __name__ == "__main__":
    main()

    # task_manager.py

tasks = []

def add_task(task):
    """��������� ������ � ������."""
    tasks.append(task)
    print(f"������ '{task}' ���������.")

def list_tasks():
    """������� ������ �����."""
    if not tasks:
        return "��� �����."
    return "\n".join(f"{i + 1}. {tasks[i]}" for i in range(len(tasks)))

def complete_task(task_id):
    """�������� ������ ��� �����������."""
    try:
        completed_task = tasks.pop(task_id - 1)
        print(f"������ '{completed_task}' ���������.")
    except IndexError:
        print("������ �� �������.")

def delete_task(task_id):
    """������� ������."""
    try:
        deleted_task = tasks.pop(task_id - 1)
        print(f"������ '{deleted_task}' �������.")
    except IndexError:
        print("������ �� �������.")

def get_user_choice():
    """�������� ����� ������������."""
    return input("�������� �������� (add/list/complete/delete/exit): ")

def main():
    """������� �������."""
    print("����� ���������� � �������� �����")
    while True:
        choice = get_user_choice()
        if choice == "add":
            task = input("������� ������: ")
            add_task(task)
        elif choice == "list":
            print(list_tasks())
        elif choice == "complete":
            task_id = int(input("������� ����� ������ ��� ����������: "))
            complete_task(task_id)
        elif choice == "delete":
            task_id = int(input("������� ����� ������ ��� ��������: "))
            delete_task(task_id)
        elif choice == "exit":
            print("����� �� ���������.")
            break
        else:
            print("�������� �����. ����������, ���������� �����.")

if __name__ == "__main__":
    main()


