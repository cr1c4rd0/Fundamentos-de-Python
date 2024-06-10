from tkinter import *
from tkinter import ttk

root = Tk()
root.title("06 Booleans")
root.iconbitmap("name.ico")
frm = ttk.Frame(root, padding=10)
frm.grid()


single = False
if single == True:
    estado = "Soltero"
else:
    estado = "Casado"

ttk.Label(frm, text=estado).grid(column=0, row=0)

# El metodo loop siempre al final
root.mainloop()
