# from storege import *
# from core import *
# from config import *
# def main():
#     task = []
#     task = load(task,NAME_FILES_SAVES)
#     is_start = True
#     while is_start:
#         clear()
#         save(task,NAME_FILES_SAVES)
#         menu()
#         a = input(">>> ")
#         match a:
#             case "1":
#                 task_print(task)
#             case "2":
#                 task=task_add(task)
#             case "3":
#                 task=task_red(task)
#             case "4":
#                 task=task_delete(task)
#             case "5":
#                 is_start = False
#             case _:
#                 print("такого пункта нет");input("нажмите Enter чтобы продолжить")
# if __name__ == '__main__':
#     main()

from ui.Interface import Interface
if __name__ == '__main__':
    i = Interface()
    i.root.mainloop()