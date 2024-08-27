from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class YouTubeAutomation:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def open_youtube(self):
        driver = self.driver
        driver.get("https://www.youtube.com/")
        time.sleep(3)

    def search_video(self, search_text):
        driver = self.driver
        # Seleccionar la caja de texto de búsqueda
        search_box = driver.find_element(By.NAME, "search_query")
        search_box.click()
        time.sleep(1)
        # Ingresar el texto de búsqueda
        search_box.send_keys(search_text)
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)

    def play_video(self):
        driver = self.driver
        # Buscar un video que contenga la cadena de texto y reproducirlo
        video = driver.find_element(By.XPATH, "(//a[@id='video-title'])[1]")
        video.click()
        time.sleep(5)  # Esperar a que el video cargue y empiece a reproducirse

    def subscribe_to_channel(self):
        driver = self.driver
        try:
            # Dar clic en el botón "Suscribirme"
            subscribe_button = driver.find_element(By.XPATH, "//tp-yt-paper-button[@aria-label='Subscribe']")
            subscribe_button.click()
            time.sleep(2)
        except Exception as e:
            print("Ya estás suscrito o no se encontró el botón de suscripción.")

    def run(self, search_text):
        try:
            self.open_youtube()
            self.search_video(search_text)
            self.play_video()
            self.subscribe_to_channel()
        finally:
            self.driver.quit()

if __name__ == "__main__":
    search_text = "Pruebas Selenium"
    youtube_automation = YouTubeAutomation()
    youtube_automation.run(search_text)
