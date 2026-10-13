import tkinter as tk

root = tk.Tk()
root.geometry('400x400')
root.title("Tasker")

collection = [
    "task1 create menu",
    "task2 create menu",
    "task3 create menu",
    "task4 create menu"
]

frame_menu = None
frame_tasks = None

def main():
    global frame_menu, frame_tasks

    frame_menu = tk.Frame(root, background="#000000", width=300, height=300)
    frame_tasks = tk.Frame(root, background="#000000", width=300, height=300)

    frame_menu.pack_propagate(False)
    frame_tasks.pack_propagate(False)

    button_show_tasks = tk.Button(
        frame_menu,
        text="view tasks",
        command=show_all_tasks
    )
    button_show_tasks.pack()

    button_exit = tk.Button(
        frame_menu,
        text="exit",
        command=root.destroy
    )
    button_exit.pack()

    frame_menu.pack()

def show_all_tasks():
    frame_menu.pack_forget()
    frame_tasks.pack()

    tasks = tk.Listbox(frame_tasks)
    for task in collection:
        tasks.insert(tk.END, task)
    tasks.pack()

    button_back = tk.Button(
        frame_tasks,
        text="back to menu",
        command=create_menu
    )
    button_back.pack()

def create_menu():
    frame_tasks.pack_forget()
    frame_menu.pack()

main()
root.mainloop()