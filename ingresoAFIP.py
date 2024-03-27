from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time




def ingresoAFIP(CUIT, clave, nombreRCEL):
    # Configurar las opciones de Chrome para que se ejecute en modo headless
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')  # Ejecutar en modo headless
    # chrome_options.add_argument('--disable-gpu')  # Deshabilitar la GPU (recomendado para ejecución en servidor)
    chrome_options.add_argument("--enable-logging")  # Habilitar el registro de la consola

    # Inicializar el navegador con las opciones configuradas
    driver = webdriver.Chrome(options=chrome_options)

    try:
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

        verTodos_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Ver todos')]"))
        )

        # Desplazar el cursor hasta el elemento
        actions = ActionChains(driver)
        actions.move_to_element(verTodos_button).perform()

        # Hacer clic en el botón "Ver todos"
        verTodos_button.click()

        # Esperar implícitamente 5 segundos para que aparezcan los elementos después de hacer clic
        driver.implicitly_wait(5)
        
        comprobanteEnLinea_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(., 'COMPROBANTES EN LÍNEA') and contains(., 'Sistema de emisión de comprobantes electrónicos')]"))
        )
        actions = ActionChains(driver)
        actions.move_to_element(comprobanteEnLinea_button).perform()
        comprobanteEnLinea_button.click()
        driver.implicitly_wait(5)
        time.sleep(5)

        # Obtener los identificadores de todas las ventanas abiertas
        handles = driver.window_handles

        # Cambiar el enfoque a la nueva ventana
        for handle in handles:
            if handle != driver.current_window_handle:
                driver.switch_to.window(handle)
                break

        empresa_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//html/body/div[2]/form/table/tbody/tr[4]/td/input[2]")))
        empresa_button.click()

        #Desde aca se deberia iterar

        generarComprobantes_button = driver.find_element(By.XPATH, "/html/body/div[2]/table/tbody/tr[1]/td/a")
        generarComprobantes_button.click()

        elegirPtoVenta = driver.find_element(By.ID, "puntodeventa")
        selectPV = Select(elegirPtoVenta)
        selectPV.select_by_index(1) 
        time.sleep(3)

        elegirComprobante = driver.find_element(By.ID,"universocomprobante")
        selectComp = Select(elegirComprobante)
        selectComp.select_by_index(4)
        time.sleep(3)

        continuar_button = driver.find_element(By.XPATH, "/html/body/div[2]/form/input[2]")
        continuar_button.click()

    
        time.sleep(5)
    except Exception as e:
        print(e)
    finally:
        driver.quit()

# Llamar a la función para completar la declaración jurada
#completar_declaracion_jurada(5937,20341095698, 2024, 2, 1258.20, "Capozzuca Jeronimo", "Febrero 2024")
#ingresoAFIP(20293208477,"Lobianco#2023#")