import tkinter as tk

root = tk.Tk()
root.geometry('300x300')
root.iconbitmap("")

frame_menu = None
frame_tasks = None

def main():
    global frame_menu, frame_tasks
    frame_menu = tk.Frame(root, background="#000000", width=300, height=300)
    frame_tasks = tk.Frame(root, background="#000000", width=300, height=300)

    button_show_tasks = tk.Button(frame_menu, text="view tasks", command=show_all_tasks())
    button_show_tasks.pack()

    button_exit = tk.Button(frame_menu, text="exit", command=create_menu())
    button_exit.pack()

def show_all_tasks():
    frame_menu.pack_forget()
    frame_menu.pack(expand=True, fill="both")


def create_menu():
    frame_tasks.pack_forget()
    frame_menu.pack(expand=True, fill="both")

root.mainloop()