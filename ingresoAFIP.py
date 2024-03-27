from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os
import sys
import tkinter as tk




def ingresoAFIP(CUIT, clave):
    # Configurar las opciones de Chrome para que se ejecute en modo headless
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')  # Ejecutar en modo headless
    # chrome_options.add_argument('--disable-gpu')  # Deshabilitar la GPU (recomendado para ejecución en servidor)
    chrome_options.add_argument("--enable-logging")  # Habilitar el registro de la consola

    # Inicializar el navegador con las opciones configuradas
    driver = webdriver.Chrome(options=chrome_options)

    # Navegar a la URL de inicio de sesión
    url = "https://auth.afip.gob.ar/"
    driver.get(url)
    driver.implicitly_wait(5)

    # Encontrar los campos de usuario y contraseña e ingresar las credenciales
    username_field = driver.find_element(By.ID, "F1:username")
    username_field.send_keys(CUIT)
    submit_button = driver.find_element(By.ID, "F1:btnSiguiente")
    submit_button.click()

    driver.implicitly_wait(5)

    password_field = driver.find_element(By.ID, "F1:password")
    password_field.send_keys(clave)
    submit_button = driver.find_element(By.ID, "F1:btnIngresar")
    submit_button.click()

    driver.implicitly_wait(5)

    # Enviar el formulario de inicio de sesión
    #password_field.send_keys(Keys.RETURN)

    # Esperar un momento para que la página se cargue completamente
    #driver.implicitly_wait(5)  # Esperar 5 segundos (puedes ajustar este valor según sea necesario)

    # Encontrar los campos de número de cuenta, CUIT, año y mes e ingresar datos
    #nro_de_cuenta_field = driver.find_element(By.ID, "id_ncuenta")
    #cuit_field = driver.find_element(By.ID, "id_cuit")
    #anio_field = driver.find_element(By.NAME, "anio_input")
    #mes_field = driver.find_element(By.NAME, "mes_input")

    #nro_de_cuenta_field.send_keys(nroCuenta)
    #cuit_field.send_keys(cuit)
    #anio_field.send_keys(year)
    #mes_field.send_keys(mes)

    
    #if nro_de_cuenta_field and cuit_field and anio_field and mes_field:
    #    print("Me meto a buscar el boton")
    #    submit_button = driver.find_element(By.XPATH, "//button[contains(text(),'Validar Datos')]")
    #    driver.implicitly_wait(5)  # Esperar 5 segundos (puedes ajustar este valor según sea necesario)
    #    submit_button.click()
    #else:
    #    print("Los campos no están completos. Por favor, asegúrate de llenar todos los campos necesarios antes de continuar.")
    #    raise Exception("Los campos no están completos. Por favor, asegúrate de llenar todos los campos necesarios antes de continuar.")
    #if imprimir_logs(driver):
    #    driver.quit()
    #    mostrar_alerta("Pagina de la Municipalidad CAÍDA")


    # Esperar un momento para que la página se cargue completamente
    #driver.implicitly_wait(5)  # Esperar 5 segundos (puedes ajustar este valor según sea necesario)

    # Seleccionar la casilla de verificación PYME
    #checkbox_mipime = driver.find_element(By.ID, "pyme")
    #driver.implicitly_wait(5)  # Esperar 5 segundos (puedes ajustar este valor según sea necesario)
    #checkbox_mipime.click()

    # Ingresar el valor en el campo de texto
    #item_comercio = driver.find_element(By.ID, "item4")
    #Si el importe es mayor a cero, escribe los datos del valor
    #if importe > 0:
    #    item_comercio.clear()  # Limpiar el campo de texto
    #    item_comercio.send_keys(importe)
    #    item_comercio.send_keys(Keys.TAB)

    # Mover el foco a otro elemento (por ejemplo, el botón "Validar Datos") después de ingresar el valor en el campo de texto

    # Encontrar el botón "Confirmar DDJJ e imprimir" y hacer clic en él
    #submit_button_DJ = driver.find_element(By.XPATH, "//button[contains(text(),'Confirmar DDJJ e imprimir')]")
    #time.sleep(5)
    #submit_button_DJ.click()
    # Esperar un momento para que la página se cargue completamente
    #driver.implicitly_wait(5)  # Esperar 5 segundos (puedes ajustar este valor según sea necesario)

    # Verificar si se muestra un mensaje de error
    #mensaje_error = driver.find_elements(By.XPATH, "//legend[contains(text(),'Error datos ingresados incorrectamente')]")

    # Si se encuentra un mensaje de error, imprimirlo y salir del proceso
    #if mensaje_error:
    #    print("Se ha encontrado un error: ", mensaje_error[0].text)
    #    driver.quit()  # Cerrar el navegador
    #    raise Exception('DJ no presentada')


    #Despues del submit, me cambia la pagina y aparece el boton de Imprimir boleta de pago, que en realidad es un enlace
    #enlace_imprimir_boleta = driver.find_element(By.XPATH, "//a[contains(text(),'Imprimir boleta de pago (PDF)')]")
    #url_pdf = enlace_imprimir_boleta.get_attribute("href")



    
    time.sleep(5)
    driver.quit()

# Llamar a la función para completar la declaración jurada
#completar_declaracion_jurada(5937,20341095698, 2024, 2, 1258.20, "Capozzuca Jeronimo", "Febrero 2024")
ingresoAFIP(20293208477,"Lobianco#2023#")