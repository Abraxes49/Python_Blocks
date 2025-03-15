import tkinter as tk

root = tk.Tk()

List = ["1", "+", "2"]
Rechnung = " ".join(List)

Ergebnis = eval(Rechnung)  # Ergebnis ist hier eine Zahl (int)

label = tk.Label(root, text=str(Ergebnis), font=("Arial", 550))  # Ergebnis als String übergeben
label.pack()

root.mainloop()
