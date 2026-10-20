from view import *
from utils import *
def task_add(tasks):
    print("ведите задачу")
    tasks.append(input(">>> "))
    task_print(tasks)
    return tasks
def task_red(tasks):
    task_print(tasks)
    print("ведите номер")
    a = input(">>> ")
    print("ведите задачу")
    if check(tasks, a):
        tasks[int(a) - 1] = input(">>> ")
        task_print(tasks)
        return tasks
    print("неправельный номер");input("нажмите Enter чтобы продолжить")
def task_delete(tasks):
    print("ведите номер задачи")
    task_print(tasks,False)
    a = input(">>> ")
    if check(tasks, a):
        tasks.pop(1 - int(a))
        task_print(tasks)
        return tasks
    print("неправельный номер");input("нажмите Enter чтобы продолжить")