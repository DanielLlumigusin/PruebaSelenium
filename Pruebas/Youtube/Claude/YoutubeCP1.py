# "Generame un script de selenium en python en clases para este caso de prueba
# 1, Ingreso al Youtube
# 2. Seleccionar la caja de texto de Buscar
# 3. Ingresar texto(""""Pruebas Selenium"""")
# 4, Buscar un video que contenga la cadena de texto
# 5, Dar clic y reproducir el video""
# 6.Esperar 10 segundos
# 7.Salir"
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# class YoutubeTest:
#     def __init__(self):
#         self.driver = webdriver.Chrome()  # Asegúrate de tener el ChromeDriver instalado y en el PATH
#         self.wait = WebDriverWait(self.driver, 10)

#     def ingresar_youtube(self):
#         self.driver.get("https://www.youtube.com")

#     def buscar_video(self, texto):
#         search_box = self.wait.until(EC.presence_of_element_located((By.NAME, "search_query")))
#         search_box.send_keys(texto)
#         search_box.send_keys(Keys.RETURN)

#     def seleccionar_video(self, texto):
#         video = self.wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, texto)))
#         video.click()

#     def esperar_reproduccion(self, segundos):
#         time.sleep(segundos)

#     def cerrar_navegador(self):
#         self.driver.quit()

#     def ejecutar_prueba(self):
#         try:
#             self.ingresar_youtube()
#             self.buscar_video("Pruebas Selenium")
#             self.seleccionar_video("Pruebas Selenium")
#             self.esperar_reproduccion(10)
#         finally:
#             self.cerrar_navegador()

# if __name__ == "__main__":
#     prueba = YoutubeTest()
#     prueba.ejecutar_prueba()
    
#     DevTools listening on ws://127.0.0.1:44286/devtools/browser/43001dad-6337-47e0-893b-1b36e49840fe
# Traceback (most recent call last):
#   File "d:\PruebaSelenium\Pruebas\Youtube\Claude\YoutubeCP1.py", line 50, in <module>
#     prueba.ejecutar_prueba()
#   File "d:\PruebaSelenium\Pruebas\Youtube\Claude\YoutubeCP1.py", line 43, in ejecutar_prueba  
#     self.seleccionar_video("Pruebas Selenium")
#   File "d:\PruebaSelenium\Pruebas\Youtube\Claude\YoutubeCP1.py", line 30, in seleccionar_video
#     video = self.wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, texto)))    
#             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\DANIEL\AppData\Local\Programs\Python\Python312\Lib\site-packages\selenium\webdriver\support\wait.py", line 105, in until
#     raise TimeoutException(message, screen, stacktrace)
# selenium.common.exceptions.TimeoutException: Message:
# Stacktrace:
#         GetHandleVerifier [0x00007FF713D3B632+29090]
#         (No symbol) [0x00007FF713CAE6E9]
#         (No symbol) [0x00007FF713B6B1CA]
#         (No symbol) [0x00007FF713BBEFD7]
#         (No symbol) [0x00007FF713BBF22C]
#         (No symbol) [0x00007FF713C097F7]
#         (No symbol) [0x00007FF713BE672F]
#         (No symbol) [0x00007FF713C065D9]
#         (No symbol) [0x00007FF713BE6493]
#         (No symbol) [0x00007FF713BB09B1]
#         (No symbol) [0x00007FF713BB1B11]
#         GetHandleVerifier [0x00007FF71405881D+3294093]
#         GetHandleVerifier [0x00007FF7140A4403+3604339]
#         GetHandleVerifier [0x00007FF71409A2C7+3563063]
#         GetHandleVerifier [0x00007FF713DF6F16+797318]
#         (No symbol) [0x00007FF713CB986F]
#         (No symbol) [0x00007FF713CB5454]
#         (No symbol) [0x00007FF713CB55E0]
#         (No symbol) [0x00007FF713CA4A7F]
#         BaseThreadInitThunk [0x00007FFD2EA17374+20]
#         RtlUserThreadStart [0x00007FFD2F57CC91+33]


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# class YoutubeTest:
#     def __init__(self):
#         self.driver = webdriver.Chrome()
#         self.wait = WebDriverWait(self.driver, 20)  # Aumentamos el tiempo de espera a 20 segundos

#     def ingresar_youtube(self):
#         self.driver.get("https://www.youtube.com")

#     def buscar_video(self, texto):
#         search_box = self.wait.until(EC.presence_of_element_located((By.NAME, "search_query")))
#         search_box.send_keys(texto)
#         search_box.send_keys(Keys.RETURN)

#     def seleccionar_video(self, texto):
#         # Esperamos a que se cargue la página de resultados
#         self.wait.until(EC.presence_of_element_located((By.ID, "contents")))
        
#         # Buscamos el video por el título
#         video = self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//yt-formatted-string[contains(text(), '{texto}')]")))
#         self.driver.execute_script("arguments[0].scrollIntoView();", video)
#         video.click()

#     def esperar_reproduccion(self, segundos):
#         time.sleep(segundos)

#     def cerrar_navegador(self):
#         self.driver.quit()

#     def ejecutar_prueba(self):
#         try:
#             self.ingresar_youtube()
#             self.buscar_video("Pruebas Selenium")
#             self.seleccionar_video("Pruebas Selenium")
#             self.esperar_reproduccion(10)
#         finally:
#             self.cerrar_navegador()

# if __name__ == "__main__":
#     prueba = YoutubeTest()
#     prueba.ejecutar_prueba()
    
# Buscar video que contenga las palabras Pruebas Selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class YoutubeTest:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 20)

    def ingresar_youtube(self):
        self.driver.get("https://www.youtube.com")

    def buscar_video(self, texto):
        search_box = self.wait.until(EC.presence_of_element_located((By.NAME, "search_query")))
        search_box.clear()
        search_box.send_keys(texto)
        search_box.send_keys(Keys.RETURN)

    def seleccionar_video(self, palabras_clave):
        # Esperamos a que se cargue la página de resultados
        self.wait.until(EC.presence_of_element_located((By.ID, "contents")))
        
        # Buscamos un video que contenga las palabras clave
        xpath = f"//yt-formatted-string[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '{palabras_clave.lower()}')]"
        video = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        self.driver.execute_script("arguments[0].scrollIntoView();", video)
        video.click()

    def esperar_reproduccion(self, segundos):
        time.sleep(segundos)

    def cerrar_navegador(self):
        self.driver.quit()

    def ejecutar_prueba(self):
        try:
            self.ingresar_youtube()
            self.buscar_video("Pruebas Selenium")
            self.seleccionar_video("pruebas selenium")
            self.esperar_reproduccion(10)
        finally:
            self.esperar_reproduccion(10)
            self.cerrar_navegador()

if __name__ == "__main__":
    prueba = YoutubeTest()
    prueba.ejecutar_prueba()