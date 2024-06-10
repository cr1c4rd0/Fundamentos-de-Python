from tkinter import *
from tkinter import ttk

root = Tk()
root.title("09 Comparadores")
root.iconbitmap("name.ico")
frm = ttk.Frame(root, padding=10)
frm.grid()

ttk.Label(frm, text=10 + 10).grid(column=0, row=0)

# El metodo loop siempre al final
root.mainloop()
