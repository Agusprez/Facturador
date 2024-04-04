import tkinter as tk
from tkinter import filedialog
import pandas as pd

def abrir_excel():
    # Mostrar el diálogo de selección de archivos
    archivo_excel = filedialog.askopenfilename(filetypes=[("Archivos Excel", "*.xlsx"), ("Todos los archivos", "*.*")])
    
    # Verificar si se seleccionó un archivo
    if archivo_excel:
        # Leer el archivo Excel utilizando Pandas
        df = pd.read_excel(archivo_excel, sheet_name="Contribuyente")
        CUIT = df.iloc[0,0]
        CLAVE = df.iloc[0,1]
        RAZON_SOCIAL = df.iloc[0,2]

        df_comprobantes = pd.read_excel(archivo_excel, sheet_name="Comprobantes")
        df_comprobantes["Fecha"] = df_comprobantes["Fecha"].dt.strftime("%d/%m/%Y")
        datos = {
            "CUIT":CUIT,
            "CLAVE":CLAVE,
            "RAZON_SOCIAL":RAZON_SOCIAL,
            "Comprobantes":df_comprobantes
        }

        return datos