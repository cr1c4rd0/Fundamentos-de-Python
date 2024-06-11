from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Hola Mundo")
root.iconbitmap("name.ico")
frm = ttk.Frame(root, padding=10)
frm.grid()

text = "Ella sabe programar en Python"
text2 = "este es un titulo"

# Verifica si la palabra está dentro del texto si está devuelve 1 si no 0
verifica1 = ("JavaScript" in text)
verifica2 = ("Python" in text)

# Cuenta la cantidad de caracteres que hay en la cadena de texto
size = len(text)

# upper(), pasa todo el string a mayusculas
text_upper = text.upper()

# lower(), pasa todo el string a minisculas
text_lower = text.lower()

# Contar el número de apareciones de una letra en especifico
text_count = text.count("a")

# Pregunta si el texto inicia con algo en especifico si es correcto devuelve 1 si no 0
text_start = text.startswith("Ella")

# Pregunta si el texto finaliza con algo en especifico si es correcto devuelve 1 si no 0
text_end = text.endswith("Python")

# Reemplaza un texto especifico por otro
text_replace = text.replace("Python", "Go")

# Pone letra capital al texto
text2_capital = text2.capitalize()

# Valida si un texto es un digito si es correcto devuelve 1 si no 0
text2_digit = text2.isdigit()

ttk.Label(frm, text=verifica2).grid(column=0, row=0)
ttk.Label(frm, text=size).grid(column=0, row=1)
ttk.Label(frm, text=text_upper).grid(column=0, row=2)
ttk.Label(frm, text=text_lower).grid(column=0, row=3)
ttk.Label(frm, text=text_count).grid(column=0, row=4)
ttk.Label(frm, text=text_start).grid(column=0, row=5)
ttk.Label(frm, text=text_end).grid(column=0, row=6)
ttk.Label(frm, text=text_replace).grid(column=0, row=7)
ttk.Label(frm, text=text2_capital).grid(column=0, row=8)
ttk.Label(frm, text=text2_digit).grid(column=0, row=9)

# El metodo loop siempre al final
root.mainloop()
