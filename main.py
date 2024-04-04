from ingresoAFIP import ingresoAFIP
from selenium import webdriver
import pandas as pd
import tkinter as tk
from tkinter import filedialog
from abrirExcel import abrir_excel



def cerrar_ventana():
    root.destroy()

root = tk.Tk()
root.geometry("400x200")
root.title("Seleccionar Archivo Excel")
info = tk.Label(root, text="Facturador", font=("Arial", 16))
info.pack(pady=10)


# Botón para abrir el archivo Excel
boton_abrir = tk.Button(root, text="Abrir Archivo", command=abrir_excel)
boton_abrir.pack(pady=8)  # Colocar el botón en la parte inferior con espacio adicional

# Botón para cerrar la ventana
boton_cerrar = tk.Button(root, text="Cerrar", command=cerrar_ventana)
boton_cerrar.pack(pady=8)

# Ejecutar el bucle principal de Tkinter
root.mainloop()

#ingresoAFIP(20293208477,"Lobianco#2023#", "LOBIANCO CARLOS DAVID")
