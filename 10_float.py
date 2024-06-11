from tkinter import *
from tkinter import ttk

root = Tk()
root.title("09 Comparadores")
root.iconbitmap("name.ico")
frm = ttk.Frame(root, padding=10)
frm.grid()

x = 3.3
y = 1.1 + 2.2
roundy = round(y, 2)

if x == roundy:
    resul = "son iguales"
else:
    resul = "No son iguales"

ttk.Label(frm, text=resul).grid(column=0, row=0)

# El metodo loop siempre al final
root.mainloop()
