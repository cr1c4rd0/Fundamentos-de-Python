from tkinter import *
from tkinter import ttk

root = Tk()
root.title("05 Numbers")
root.iconbitmap("name.ico")
frm = ttk.Frame(root, padding=10)
frm.grid()

# entero
lives = 3 

# Decimal
temperatura = 15.12

ttk.Label(frm, text= type(lives)).grid(column=0, row=0)

# El metodo loop siempre al final
root.mainloop()
