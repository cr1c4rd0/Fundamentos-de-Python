from tkinter import *
from tkinter import ttk

root = Tk()
root.title("07 Transformación de tipos")
root.iconbitmap("name.ico")
frm = ttk.Frame(root, padding=10)
frm.grid()


name = "Cristian"
age = 36
complete = name + " " + str(age)


ttk.Label(frm, text=complete).grid(column=0, row=0)

# El metodo loop siempre al final
root.mainloop()
