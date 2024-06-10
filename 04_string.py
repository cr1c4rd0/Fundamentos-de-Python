from tkinter import *
from tkinter import ttk

root = Tk()
root.title("03 - String")
root.iconbitmap("name.ico")
frm = ttk.Frame(root, padding=10)
frm.grid()

# String
my_name = "Cristian"
last_name = "Ricardo"

#concatenación de strings
complete_name = my_name + " " + last_name

# format opción 1
template1 = "Hola, mi nombre es " + my_name + "y mi apellido es " + last_name

# format opción 2
template2 = "Hola, mi nombre es {} y mi apellido es {}".format(my_name, last_name)

# format opción 3
template3 = f"Hola, mi nombre es {my_name} y mi apellido es {last_name}"

ttk.Label(frm, text=complete_name).grid(column=0, row=0)
ttk.Label(frm, text=template1).grid(column=0, row=1)
ttk.Label(frm, text=template2).grid(column=0, row=2)
ttk.Label(frm, text=template2).grid(column=0, row=3)

# ttk.Button(frm, text="Salir", command=root.destroy).grid(column=0, row=3)

# El metodo loop siempre al final
root.mainloop()
