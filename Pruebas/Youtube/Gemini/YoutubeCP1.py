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
from time import sleep

class YoutubeTest:
    def __init__(self):
        self.driver = webdriver.Chrome()  # Ajusta esto según el navegador que uses (Chrome, Firefox, etc.)

    def test_youtube_search(self):
        self.driver.get("https://www.youtube.com")
        search_box = self.driver.find_element(By.NAME, "search_query")
        search_box.send_keys("Pruebas Selenium")
        search_box.submit()

        # Aquí puedes implementar una lógica más robusta para buscar el video específico
        # Por ejemplo, puedes buscar por título, descripción o canal
        first_video = self.driver.find_element(By.ID, "video-title")
        first_video.click()

        sleep(10)

    def tear_down(self):
        self.driver.quit()

if __name__ == "__main__":
    test = YoutubeTest()
    test.test_youtube_search()
    test.tear_down()
