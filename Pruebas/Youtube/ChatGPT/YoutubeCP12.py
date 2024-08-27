from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class YouTubeClipAutomation:
    def __init__(self):
        # Inicialización del driver de Selenium
        self.driver = webdriver.Chrome()

    def open_youtube(self):
        # Abre la página principal de YouTube
        driver = self.driver
        driver.get("https://www.youtube.com/")
        time.sleep(3)

    def search_trailer(self):
        # Ingresa la cadena de búsqueda "trailer" en la barra de búsqueda de YouTube
        driver = self.driver
        search_box = driver.find_element(By.NAME, "search_query")
        search_box.send_keys("trailer")
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)

    def select_first_video(self):
        # Selecciona el primer video de los resultados de búsqueda
        driver = self.driver
        first_video = driver.find_element(By.XPATH, "(//a[@id='video-title'])[1]")
        first_video.click()
        time.sleep(5)

    def create_clip(self):
        # Crea un clip desde el video usando las opciones del reproductor
        driver = self.driver
        # Clic en los tres puntos suspensivos debajo del reproductor
        more_options_button = driver.find_element(By.XPATH, "//yt-icon-button[@aria-label='More actions']")
        more_options_button.click()
        time.sleep(2)
        
        # Seleccionar la opción "Clip"
        clip_option = driver.find_element(By.XPATH, "//yt-formatted-string[text()='Clip']")
        clip_option.click()
        time.sleep(3)
        
        # Añadir un título para el clip
        title_box = driver.find_element(By.XPATH, "//input[@id='clip-title-input']")
        title_box.send_keys("clip de prueba")
        time.sleep(1)
        
        # Dar clic en "Compartir clip"
        share_clip_button = driver.find_element(By.XPATH, "//yt-formatted-string[text()='Compartir clip']")
        share_clip_button.click()
        time.sleep(2)

    def copy_and_paste_clip_link(self):
        driver = self.driver
        # Copiar el link generado
        clip_link_input = driver.find_element(By.XPATH, "//input[@class='clip-share-url']")
        clip_link = clip_link_input.get_attribute("value")
        time.sleep(1)

        # Abrir una nueva pestaña y pegar el enlace en la barra de búsqueda
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get(clip_link)
        time.sleep(3)

    def run(self):
        try:
            self.open_youtube()
            self.search_trailer()
            self.select_first_video()
            self.create_clip()
            self.copy_and_paste_clip_link()
        finally:
            time.sleep(5)
            self.driver.quit()

if __name__ == "__main__":
    youtube_clip_automation = YouTubeClipAutomation()
    youtube_clip_automation.run()
