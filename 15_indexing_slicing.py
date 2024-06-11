from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Hola Mundo")
root.iconbitmap("name.ico")
frm = ttk.Frame(root, padding=10)
frm.grid()

text = "Ella sabe programar en Python"


# Slicing


ttk.Label(frm, text="").grid(column=0, row=0)

# El metodo loop siempre al final
root.mainloop()
