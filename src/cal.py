import tkinter as tk

root = tk.Tk()
root.geometry("500x500")
texts = ""
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["C", "<"]
]
def button_click(value: str):
    global texts
    print(value)
    if value == "=":
        calk =str(eval(texts))
        texts += f"={calk}"
        text1.config(text=texts)
        print(texts)
        return
    if value == "<":
        texts= texts[:-1]
        text1.config(text=texts)
        print(texts)
        return
    if value == "C":
        texts= ""
        text1.config(text=texts)
        print(texts)
        return
    texts += value
    text1.config(text=texts)

text1 = tk.Label(root, height=5, width=30)
text1.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

for row, button_row in enumerate(buttons, start=1):
    for column, text in enumerate(button_row):
        button = tk.Button(
            root,
            text=text,
            font=("Arial", 18),
            command=lambda value=text: button_click(value)
        )
        button.grid(
            row=row,
            column=column,
            padx=5,
            pady=5,
            sticky="nsew"
        )

root.mainloop()
