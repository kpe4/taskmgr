from doctest import master
from tkinter import Button

class AppButton(Button):
    def __init__(self,text,command):
        super().__init__(master,
                         text=text,
                         command=lambda x=command:x)
        self.text =text
        self.command =command
        self.master= master
