# "Generame un script de selenium en python en clases para este caso de prueba
# 1, Ingreso al Youtube
# 2. Seleccionar la caja de texto de Buscar
# 3. Ingresar texto(""""Pruebas Selenium"""")
# 4, Buscar un video que contenga la cadena de texto
# 5, Dar clic y reproducir el video""
# 6.Esperar 10 segundos
# 7.Salir"

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class YouTubeTestCase(unittest.TestCase):

    def setUp(self):
        # Inicializa el navegador (puedes usar Chrome o Firefox, asegúrate de tener el driver adecuado)
        self.browser = webdriver.Chrome()  # O usa webdriver.Firefox() si prefieres Firefox
        self.browser.maximize_window()

    def test_search_and_play_video(self):
        # Paso 1: Ingreso a YouTube
        self.browser.get('https://www.youtube.com')
        time.sleep(2)  # Espera para asegurarse de que la página cargue completamente

        # Paso 2: Seleccionar la caja de texto de Buscar
        search_box = self.browser.find_element(By.NAME, 'search_query')
        
        # Paso 3: Ingresar texto "Pruebas Selenium"
        search_box.send_keys('Pruebas Selenium')
        
        # Paso 4: Buscar un video que contenga la cadena de texto
        search_box.send_keys(Keys.RETURN)
        time.sleep(2)  # Espera para que se carguen los resultados de búsqueda

        # Paso 5: Dar clic y reproducir el video (primer resultado)
        first_video = self.browser.find_element(By.XPATH, '(//a[@id="video-title"])[1]')
        first_video.click()
        
        # Paso 6: Esperar 10 segundos para que se reproduzca el video
        time.sleep(10)

    def tearDown(self):
        # Paso 7: Salir
        self.browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
