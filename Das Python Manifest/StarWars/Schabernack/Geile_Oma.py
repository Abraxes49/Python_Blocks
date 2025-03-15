import tkinter as tk
from tkinter import messagebox

def text_ändern():
    label.config(text="Du hast den Button gedrückt!")  # Ändert den Text des Labels

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Hallo Tkinter!")
    root.geometry("500x300")

    label = tk.Label(root, text="", font=("Arial", 14))  # Leeres Label
    label.pack(pady=20)  # Abstand nach unten

    button = tk.Button(
        root,
        text="Drück mich!",
        command=text_ändern,
        width=20,
        height=2,
    )
    button.pack()

    root.mainloop()
