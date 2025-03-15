
import tkinter as tk
from tkinter import messagebox  #jo für die messagbox


def hallo_sagen():
    messagebox.showinfo(
        "Begrüßung",
        "Hallo Welt!"

    )


if __name__ == "__main__":
    root = tk.Tk()          # Haupfenster root tk ist der Konstruktor
    root.title("Hallo Tkinter!")
    root.geometry("1000x500")  # merke x

    button = tk.Button(     #KOnstruktor Button
    root,
    text="Drück mich!",
    command=hallo_sagen,     # mit funktion siehe oben
    width = 50,
    height = 12,
    )
    button.pack()
    button.place(x=100,y=20)
    root.mainloop()






