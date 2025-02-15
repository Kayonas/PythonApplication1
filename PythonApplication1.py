# task_manager.py
# -*- coding: utf-8 -*-

# çäåñü íà÷íåòñÿ âàø êîä
print("Ïðèìåð ïðîãðàììû ñ èñïîëüçîâàíèåì êîäèðîâêè UTF-8")
def add_task(task):
    """Äîáàâëÿåò çàäà÷ó."""
    pass

def list_tasks():
    """Âûâîäèò ñïèñîê çàäà÷."""
    return "Îáðàçåö"

def complete_task(task_id):
    """Îòìå÷àåò çàäà÷ó êàê âûïîëíåííóþ."""
    pass

def delete_task(task_id):
    """Óäàëÿåò çàäà÷ó."""
    pass

def main():
    """Ãëàâíàÿ ôóíêöèÿ."""
    print("Äîáðî ïîæàëîâàòü â ìåíåäæåð çàäà÷")

if __name__ == "__main__":
    main()

    # task_manager.py

tasks = []

def add_task(task):
    """Äîáàâëÿåò çàäà÷ó â ñïèñîê."""
    tasks.append(task)
    print(f"Çàäà÷à '{task}' äîáàâëåíà.")

def list_tasks():
    """Âûâîäèò ñïèñîê çàäà÷."""
    if not tasks:
        return "Íåò çàäà÷."
    return "\n".join(f"{i + 1}. {tasks[i]}" for i in range(len(tasks)))

def complete_task(task_id):
    """Îòìå÷àåò çàäà÷ó êàê âûïîëíåííóþ."""
    try:
        completed_task = tasks.pop(task_id - 1)
        print(f"Çàäà÷à '{completed_task}' âûïîëíåíà.")
    except IndexError:
        print("Çàäà÷à íå íàéäåíà.")

def delete_task(task_id):
    """Óäàëÿåò çàäà÷ó."""
    try:
        deleted_task = tasks.pop(task_id - 1)
        print(f"Çàäà÷à '{deleted_task}' óäàëåíà.")
    except IndexError:
        print("Çàäà÷à íå íàéäåíà.")

def get_user_choice():
    """Ïîëó÷àåò âûáîð ïîëüçîâàòåëÿ."""
    return input("Âûáåðèòå äåéñòâèå (add/list/complete/delete/exit): ")




