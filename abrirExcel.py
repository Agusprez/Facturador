import pandas as pd
import tkinter as tk
from tkinter import filedialog

def abrir_excel():
    archivo_excel = filedialog.askopenfilename(filetypes=[("Archivos Excel", "*.xlsx"), ("Todos los archivos", "*.*")])
    
    if archivo_excel:
        df = pd.read_excel(archivo_excel, sheet_name=1)
        CUIT = df.iloc[0,0]
        CLAVE = df.iloc[0,1]
        print(f"CUIT: {CUIT}")
        print(f"Clave: {CLAVE}")
