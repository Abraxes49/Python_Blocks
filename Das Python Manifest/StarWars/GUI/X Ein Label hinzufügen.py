
import tkinter as tk
from tkinter import messagebox


def hallo_sagen():                      #das hier ist obsolet
    messagebox.showinfo(
        "Begrüßung",
        "Hallo Welt!"
    )

def add_label():                              # das hier ist die neue Funktion
    label.config(text="Du hast den Button gedrückt!")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Hallo Tkinter!")
    root.geometry("1000x500")

    button = tk.Button(
    root,
    text="Drück mich!",
    command=add_label,                      #deswegen muss das Command auch geänder werden
    width = 10,
    height = 5,

    )

    label = tk.Label(root, text="", font=("Arial", 14))         #Leeres Label
    label.pack(pady=20)                                         #abstand nach unten



    button.pack()
    button.place(x=100,y=200)
    root.mainloop()







