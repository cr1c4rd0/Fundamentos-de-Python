from tkinter import *
from tkinter import ttk

root = Tk()
root.title("09 Comparadores")
root.iconbitmap("name.ico")
frm = ttk.Frame(root, padding=10)
frm.grid()

logic = True and False

ttk.Label(frm, text=logic).grid(column=0, row=0)

# El metodo loop siempre al final
root.mainloop()