from tkinter import *
from tkinter import ttk

root=Tk()
root.title("Hola Mundo")
root.iconbitmap("name.ico")
frm = ttk.Frame(root, padding=10)
frm.grid()
world = "Hola Mundo"
ttk.Label(frm, text=world).grid(column=0, row=0)
ttk.Button(frm, text="Salir", command=root.destroy).grid(column=1, row=0)

# El metodo loop siempre al final
root.mainloop()
