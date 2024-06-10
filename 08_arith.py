from tkinter import *
from tkinter import ttk

root = Tk()
root.title("07 Transformación de tipos")
root.iconbitmap("name.ico")
frm = ttk.Frame(root, padding=10)
frm.grid()

ttk.Label(frm, text=10 + 10).grid(column=0, row=0)
ttk.Label(frm, text=10 - 5).grid(column=0, row=1)
ttk.Label(frm, text=10 * 2).grid(column=0, row=2)
ttk.Label(frm, text=10 / 2).grid(column=0, row=3)
ttk.Label(frm, text=10 % 2).grid(column=0, row=4)
# Muestra el valor entero de una división
ttk.Label(frm, text=10 // 2).grid(column=0, row=5)
# Exponente
ttk.Label(frm, text=2 ** 3).grid(column=0, row=6)



# El metodo loop siempre al final
root.mainloop()
