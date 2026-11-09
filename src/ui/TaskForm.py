import tkinter as tk
from tkinter import ttk


class TaskForm(ttk.Frame): # форма задачи
    def __init__(self, master): # конструктор
        super().__init__(master)
        self.rowconfigure(3, weight=1)
        self.columnconfigure(0, weight=1)

        ttk.Label(self, text="Title").grid(row=0, column=0, sticky="w")
        self.title_entry = ttk.Entry(self)
        self.title_entry.grid(row=1, column=0, sticky="ew", pady=(0, 5))

        ttk.Label(self, text="Description").grid(row=2, column=0, sticky="w")
        self.desc_text = tk.Text(self, wrap="word", height=8)
        self.desc_text.grid(row=3, column=0, sticky="nsew")

    def get(self): # получение данных из формы
        return self.title_entry.get().strip(), self.desc_text.get("1.0", tk.END).strip()

    def set(self, title, description): # установка данных в форму
        self.clear()
        self.title_entry.insert(0, title or "")
        self.desc_text.insert("1.0", description or "")

    def clear(self): # очистка формы
        self.title_entry.delete(0, tk.END)
        self.desc_text.delete("1.0", tk.END)
