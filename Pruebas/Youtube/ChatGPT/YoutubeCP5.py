from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class YouTubeAutomationTest:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def open_youtube(self):
        driver = self.driver

        # Ingresar a YouTube
        driver.get("https://www.youtube.com")
        time.sleep(3)

    def search_video(self, search_query):
        driver = self.driver

        # Seleccionar la caja de texto de Buscar
        search_box = driver.find_element(By.NAME, "search_query")
        search_box.click()

        # Ingresar el texto a buscar y dar Enter
        search_box.send_keys(search_query)
        search_box.send_keys(Keys.ENTER)
        time.sleep(3)

    def play_video(self):
        driver = self.driver

        # Buscar el primer video que contiene la cadena de texto y dar clic
        video = driver.find_element(By.XPATH, "//a[@id='video-title']")
        video.click()
        time.sleep(5)

    def save_video(self):
        driver = self.driver

        # Hacer clic en el botón "Guardar" (Añadir a lista de reproducción)
        try:
            save_button = driver.find_element(By.XPATH, "//button[@aria-label='Guardar en una lista de reproducción']")
            save_button.click()
            time.sleep(3)

            # Seleccionar una lista de reproducción predeterminada o nueva
            playlist_option = driver.find_element(By.XPATH, "//yt-formatted-string[contains(text(),'Ver más tarde')]")
            playlist_option.click()
            time.sleep(3)
        except:
            print("No se encontró el botón de 'Guardar' o no se pudo añadir el video a la lista de reproducción.")

    def run_test(self, search_query):
        try:
            self.open_youtube()
            self.search_video(search_query)
            self.play_video()
            self.save_video()
        finally:
            # Cerrar el navegador al finalizar
            self.driver.quit()

if __name__ == "__main__":
    search_query = "Pruebas Selenium"

    # Ejecutar el test de YouTube
    youtube_test = YouTubeAutomationTest()
    youtube_test.run_test(search_query)
