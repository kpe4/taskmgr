import tkinter as tk
from tkinter import ttk


class TaskList(ttk.Frame): # список задач
    def __init__(self, master, on_select=None): # конструктор
        super().__init__(master)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.listbox = tk.Listbox(self, exportselection=False)
        self.listbox.grid(row=0, column=0, sticky="nsew")

        if on_select is not None:
            self.listbox.bind("<<ListboxSelect>>", on_select)

    def refresh(self, tasks): # обновление списка задач
        self.listbox.delete(0, tk.END)
        for task in tasks:
            self.listbox.insert(tk.END, task.get("title") or "(без названия)")

    def selected_index(self): # получение индекса выбранной задачи
        sel = self.listbox.curselection()
        return sel[0] if sel else None
