import ingresoAFIP
import datosExcel
from ingresoAFIP import ingresoAFIP
from selenium import webdriver
import tkinter as tk
from tkinter import ttk, messagebox
from datosExcel import abrir_excel
import time

def proceso():
    tiempo_inicio = time.time()

    datos = abrir_excel()
    cuit = datos["CUIT"]
    cuit = str(cuit)
    clave = datos["CLAVE"] 
    comprobantes = datos["Comprobantes"]
    print(comprobantes)
    razonSocial = datos["RAZON_SOCIAL"]


    modificar_etiqueta(info, razonSocial)
    ingresoAFIP(cuit, clave, comprobantes, actualizar_progreso, modificar_etiqueta)
    modificar_etiqueta(info_progreso,"Proceso completado")
    time.sleep(2)
    mostrar_resumen()
    ventanaPrincipal.quit()

def mostrar_resumen():
    tiempo_fin = time.time()
    tiempo_transcurrido = tiempo_fin - tiempo_inicio
    tiempo_transcurrido_formateado = time.strftime("%H:%M:%S", time.gmtime(tiempo_transcurrido))

    mensaje = f"\nTiempo empleado: {tiempo_transcurrido_formateado}\n"


    messagebox.showinfo("Resumen del Proceso", mensaje)
    tiempo_inicio = 0

def actualizar_progreso(porcentaje):
    progressbar["value"] = porcentaje
    label_progreso.config(text=f"{porcentaje}%")
    ventanaPrincipal.update_idletasks()
    ventanaPrincipal.update()
    
def modificar_etiqueta(etiqueta, nuevo_texto):
    if etiqueta == "info_progreso":
        etiqueta = info_progreso
    etiqueta.config(text=nuevo_texto)
    ventanaPrincipal.update_idletasks()
    ventanaPrincipal.update()

ventanaPrincipal = tk.Tk()
ventanaPrincipal.geometry("600x300")
ventanaPrincipal.title("Facturador")

#Label
info = tk.Label(ventanaPrincipal, text="Seleccione un archivo Excel para iniciar el proceso:", font=("Arial",16))
info.pack(pady=20)

#Label
info_progreso = tk.Label(ventanaPrincipal, text="", font=("Arial",14))
info_progreso.pack(pady=5)
# Barra de carga
progressbar = ttk.Progressbar(ventanaPrincipal, orient="horizontal", length=400, mode="determinate")
progressbar.pack(pady=10)
label_progreso = tk.Label(ventanaPrincipal, text="0%", font=("Arial", 12))
label_progreso.pack()

# Botón para simular un proceso
boton_simular = tk.Button(ventanaPrincipal, text="Procesar Excel", command=proceso)
boton_simular.pack(pady=14)

boton_salir = tk.Button(ventanaPrincipal,text="Salir", command=quit)
boton_salir.pack(pady=14)

ventanaPrincipal.mainloop()
#ingresoAFIP(20293208477,"Lobianco#2023#", "LOBIANCO CARLOS DAVID")


