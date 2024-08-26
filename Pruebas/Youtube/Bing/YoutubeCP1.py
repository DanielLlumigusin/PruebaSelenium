# "Generame un script de selenium en python en clases para este caso de prueba
# 1, Ingreso al Youtube
# 2. Seleccionar la caja de texto de Buscar
# 3. Ingresar texto(""""Pruebas Selenium"""")
# 4, Buscar un video que contenga la cadena de texto
# 5, Dar clic y reproducir el video""
# 6.Esperar 10 segundos
# 7.Salir"
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class YouTubeTest:
    def __init__(self):
        self.driver = webdriver.Chrome()  # Asegúrate de tener el driver de Chrome instalado y en tu PATH

    def open_youtube(self):
        self.driver.get("https://www.youtube.com")

    def search_video(self, search_query):
        search_box = self.driver.find_element(By.NAME, "search_query")
        search_box.send_keys(search_query)
        search_box.send_keys(Keys.RETURN)

    def play_video(self):
        time.sleep(2)  # Esperar a que se carguen los resultados
        video = self.driver.find_element(By.XPATH, '//*[@id="video-title"]')
        video.click()

    def wait_and_quit(self, wait_time):
        time.sleep(wait_time)
        self.driver.quit()

    def run_test(self):
        self.open_youtube()
        self.search_video("Pruebas Selenium")
        self.play_video()
        self.wait_and_quit(10)

if __name__ == "__main__":
    test = YouTubeTest()
    test.run_test()
