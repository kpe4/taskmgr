import os
import sys
import tkinter as tk
from tkinter import ttk, messagebox

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from storage import create_task, delete_task, get_all_tasks, update_task
from ui.task_list import TaskList
from ui.task_form import TaskForm


class TaskManagerApp(tk.Tk): # интерфейс приложения
    def __init__(self): # конструктор
        super().__init__()
        self.title("Task Manager")
        self.geometry("800x600")
        self.minsize(560, 400)

        self.tasks = []
        self.task_id = None

        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)

        ttk.Label(self, text="Task Manager", font=("Arial", 14, "bold")).grid(
            row=0, column=0, sticky="w", padx=10, pady=10)

        body = ttk.Frame(self)
        body.grid(row=1, column=0, sticky="nsew", padx=10)
        body.rowconfigure(0, weight=1)
        body.columnconfigure(0, weight=1, uniform="c")
        body.columnconfigure(1, weight=1, uniform="c")

        self.task_list = TaskList(body, on_select=self.on_select)
        self.task_list.grid(row=0, column=0, sticky="nsew", padx=(0, 5))

        self.form = TaskForm(body)
        self.form.grid(row=0, column=1, sticky="nsew", padx=(5, 0))

        bar = ttk.Frame(self)
        bar.grid(row=2, column=0, sticky="ew", padx=10, pady=10)
        ttk.Button(bar, text="Add", command=self.on_add).pack(side="left", fill="x", expand=True, padx=3)
        ttk.Button(bar, text="Save", command=self.on_save).pack(side="left", fill="x", expand=True, padx=3)
        ttk.Button(bar, text="Delete", command=self.on_delete).pack(side="left", fill="x", expand=True, padx=3)

        self.refresh()

    def refresh(self): # обновление списка задач
        self.tasks = get_all_tasks() or []
        self.task_list.refresh(self.tasks)

    def on_select(self, event=None): # обработчик события выбора задачи

        index = self.task_list.selected_index()
        if index is None:
            return
        task = self.tasks[index]
        self.task_id = task.get("id")
        self.form.set(task.get("title", ""), task.get("description", ""))

    def on_add(self): # добавление задачи
        title, description = self.form.get()
        if not title and not description:
            messagebox.showwarning("Task Manager", "Введите название или описание.")
            return
        create_task(title, description)
        self.clear()

    def on_save(self): # сохранение задачи
        if self.task_id is None:
            messagebox.showwarning("Task Manager", "Выберите задачу.")
            return
        title, description = self.form.get()
        update_task(self.task_id, title=title, description=description)
        self.clear()

    def on_delete(self): # удаление задачи
        if self.task_id is None:
            messagebox.showwarning("Task Manager", "Выберите задачу.")
            return
        if messagebox.askyesno("Task Manager", "Удалить задачу?"):
            delete_task(self.task_id)
            self.clear()

    def clear(self): # очистка формы
        self.refresh()
        self.task_id = None
        self.form.clear()


if __name__ == "__main__":
    TaskManagerApp().mainloop()
