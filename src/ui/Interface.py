import tkinter as tk

from PIL import Image, ImageTk
from pathlib import Path

from logger import name_file
from ui.Frame import AppFrame

class Interface:
    def __init__(self,windows_w=400,windows_h=400):
        self.root = tk.Tk()
        
        self.root.title("Task Manager")
        self.root_w = windows_w
        self.root_h = windows_h
        
        self.root.geometry(f"{self.root_w}x{self.root_h}")
        
        base_path = Path(__file__).resolve().parent.parent
        icon_path = base_path / "assets" / "icon.ico"
        
        try:
            img = Image.open(icon_path)
            icon = ImageTk.PhotoImage(img)
            self.root.iconphoto(True, icon)
        except FileNotFoundError:
            print(f"Иконка не найдена по пути: {icon_path}")

        self.frame = {}
        self.buttons = []

        self.create_interface()
        
        self.root.mainloop()

    def create_interface(self):
        self.create_frames(["menu", "task"])
        self.create_buttons()

    def create_frames(self, mane_frame):
        for i,r in enumerate(mane_frame):
            frame = AppFrame(self.root,"#000000",self.root_w, self.root_h)
            if r == "menu":
                frame.hide(False)
            self.frame[r] = frame
        print(self.frame)

    def create_buttons(self):
        button_show_task = tk.Button(self.frame["menu"], text="посмотреть задачи",command=lambda :self.frame["menu"].hide(True))
        button_show_task.pack()

if __name__ == "__main__":
    app = Interface()
