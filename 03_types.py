from tkinter import *
from tkinter import ttk

root = Tk()
root.title("02 - Tipos de datos")
root.iconbitmap("name.ico")
frm = ttk.Frame(root, padding=10)
frm.grid()

# String
my_name = "Cristian:"
ttk.Label(frm, text=my_name).grid(column=0, row=0)
ttk.Label(frm, text=type(my_name)).grid(column=1, row=0)

# Int
my_age = 36
ttk.Label(frm, text="Mi edad:").grid(column=0, row=1)
ttk.Label(frm, text=my_age).grid(column=1, row=1)

# Boolean
is_single = False
if is_single == False:
    single = "Comprometido"
else:
     single = "Soltero"

ttk.Label(frm, text="Estado civil:").grid(column=0, row=2)
ttk.Label(frm, text=single).grid(column=1, row=2)

#ttk.Button(frm, text="Salir", command=root.destroy).grid(column=0, row=3)

# El metodo loop siempre al final
root.mainloop()
