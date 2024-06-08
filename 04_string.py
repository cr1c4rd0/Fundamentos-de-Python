from tkinter import *
from tkinter import ttk

root = Tk()
root.title("03 - String")
root.iconbitmap("name.ico")
frm = ttk.Frame(root, padding=10)
frm.grid()

# String
my_name = "Cristian:"
ttk.Label(frm, text=my_name).grid(column=0, row=0)
ttk.Label(frm, text=type(my_name)).grid(column=1, row=0)

# ttk.Button(frm, text="Salir", command=root.destroy).grid(column=0, row=3)

# El metodo loop siempre al final
root.mainloop()
