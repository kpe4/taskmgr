from tkinter import *
import tkinter as tk


collection = ["task_1 create menu", "task_2 add main"]




frame_memu =None
frame_tasks =None
tasks = None
def init():
    global frame_tasks,frame_memu,tasks
    frame_memu = tk.Frame(root, background="#000000", width=400, height=400)

    frame_tasks = tk.Frame(root, background="#000000", width=400, height=400)
    button_exit = tk.Button(frame_tasks, text="Exit", command=create_menu)
    button_exit.pack()
    button_exit1 = tk.Button(frame_tasks, text="show", command=show)
    button_exit1.pack()
    frame_memu.pack_propagate(False)
    frame_tasks.pack_propagate(False)
    tasks = tk.Listbox(frame_tasks, width=400, height=400)
    tasks.pack()

def show():
    print(tasks.curselection())
def show_all_tasks():
    frame_memu.pack_forget()
    frame_tasks.pack()
    tasks.delete(0, tk.END)
    for tack in collection:
        tasks.insert(tk.END, tack)



def create_menu():
    frame_memu.pack()
    frame_tasks.pack_forget()




init()
create_menu()
root.mainloop()