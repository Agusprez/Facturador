from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time




def ingresoAFIP(CUIT, clave, comprobantes, actualizar_progreso, modificar_etiqueta):

    # Configurar las opciones de Chrome para que se ejecute en modo headless
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')  # Ejecutar en modo headless
    chrome_options.add_argument('--disable-gpu')  # Deshabilitar la GPU (recomendado para ejecución en servidor)
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
        modificar_etiqueta("info_progreso", "Ingreso a la AFIP correcto")
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
        cantidadComprobantes = len(comprobantes)
        modificar_etiqueta("info_progreso", "Facturando...")

        for index, comprobante in comprobantes.iterrows():
            try:
                generarComprobantes_button = driver.find_element(By.XPATH, "/html/body/div[2]/table/tbody/tr[1]/td/a")
                generarComprobantes_button.click()

                elegirPtoVenta = driver.find_element(By.ID, "puntodeventa")
                selectPV = Select(elegirPtoVenta)
                selectPV.select_by_index(1) 
                time.sleep(3)

                elegirComprobante = driver.find_element(By.ID,"universocomprobante")
                selectComp = Select(elegirComprobante)
                nombreComp = comprobante["Tipo"]
                selectComp.select_by_visible_text(nombreComp)
                #selectComp.select_by_index(4)
                #Aca en realidad, se deberia elegir By Value
                time.sleep(3)

                continuar_button = driver.find_element(By.XPATH, "/html/body/div[2]/form/input[2]")
                continuar_button.click()
                
                modificar_etiqueta("info_progreso", "Facturando... Paso 1 de 4")

                
                input_fecha = driver.find_element(By.XPATH,"/html/body/div[2]/form/div/div/table/tbody/tr[1]/td/input[1]")
                
                input_fecha.clear()
                #Va a venir en el excel
                fecha_comprobante = comprobante["Fecha"]
                ################################
                input_fecha.send_keys(fecha_comprobante)

                elegirConcepto = driver.find_element(By.ID, "idconcepto")
                selectConcepto = Select(elegirConcepto)
                selectConcepto.select_by_index(3)
                #selectConcepto.select_by_visible_text(" Consumidor Final")
                time.sleep(2)

                continuar_button_2  = driver.find_element(By.XPATH, "/html/body/div[2]/form/input[2]")
                continuar_button_2.click()

                modificar_etiqueta("info_progreso", "Facturando... Paso 2 de 4")


                elegirCondicion = driver.find_element(By.ID, "idivareceptor")
                selectCondicion = Select(elegirCondicion)
                #selectCondicion.select_by_index(2)
                selectCondicion.select_by_visible_text(" Consumidor Final")

                checkbox_condicion = driver.find_element(By.ID, "formadepago4")
                checkbox_condicion.click()
                time.sleep(2)

                continuar_button_3  = driver.find_element(By.XPATH, "/html/body/div[2]/form/input[2]")
                continuar_button_3.click()

                modificar_etiqueta("info_progreso", "Facturando... Paso 3 de 4")


                input_detalle = driver.find_element(By.ID, "detalle_descripcion1")
                detalle = comprobante["Descripcion"]
                input_detalle.send_keys(detalle)
                #Va a venir en el excel
                #precio_aleatorio = random.randint(1500,1900)
                #precio = round(precio_aleatorio * 100,-2 )
                precio = comprobante["Importe"]
                ######################
                input_precio = driver.find_element(By.ID, "detalle_precio1")
                input_precio.send_keys(precio)
                if nombreComp == "Factura B":
                    elegirAlicuota = driver.find_element(By.ID, "detalle_tipo_iva1")
                    selectAlicuota = Select(elegirAlicuota)
                    selectAlicuota.select_by_index(7)
                time.sleep(3)

                continuar_button_4  = driver.find_element(By.XPATH, "/html/body/div[2]/form/input[8]")
                continuar_button_4.click()

                modificar_etiqueta("info_progreso", "Facturando... Paso 4 de 4")


                generarComprobante_button_final = driver.find_element(By.ID, "btngenerar")
                #generarComprobante_button_final.click()
                alertaDeComprobante = WebDriverWait(driver, 10).until(EC.alert_is_present())
                alertaDeComprobante.accept()
                time.sleep(1)
                menuPrincipal_button = driver.find_element(By.XPATH, "/html/body/div[2]/table/tbody/tr[2]/td/input")
                menuPrincipal_button.click()


                time.sleep(5)
            except Exception as e:
                print(e)
            finally:
                modificar_etiqueta("info_progreso", "Facturando...")
                porcentajeProgreso = (index + 1) * 100 /cantidadComprobantes
                porcentajeProgreso = int(porcentajeProgreso)
                actualizar_progreso(porcentajeProgreso)
    except Exception as e:
        print(e)
    finally:
        driver.quit()

#ingresoAFIP(20293208477,"Lobianco#2023#")