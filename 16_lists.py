from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Hola Mundo")
root.iconbitmap("name.ico")
frm = ttk.Frame(root, padding=10)
frm.grid()

numbers = [1, 2 ,3 ,4]



ttk.Label(frm, text="").grid(column=0, row=0)

# El metodo loop siempre al final
root.mainloop()
