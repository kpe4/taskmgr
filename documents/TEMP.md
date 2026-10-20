# старый участки файла
view
```
def task_print(tasks,pause=True):
    for i, key in enumerate(tasks, 1):
        print(i, "задача:", key)
    if pause:input("нажмите Enter чтобы продолжить")
def menu():
    print("менеджер задач")
    print("1 - посмотреть задачи")
    print("2 - добавить задачи")
    print("3 - редоктировать задачу")
    print("4 - удалить задачу")
    print("5 - выйти из приложени")
```