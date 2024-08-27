from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class YouTubePlaylistAutomation:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def open_youtube(self):
        driver = self.driver
        driver.get("https://www.youtube.com/")
        time.sleep(3)

    def search_playlist(self):
        driver = self.driver
        # Seleccionar la barra de búsqueda y escribir la cadena de texto
        search_box = driver.find_element(By.NAME, "search_query")
        search_box.send_keys("Listas de reproducción")
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)

    def select_first_playlist(self):
        driver = self.driver
        # Seleccionar la primera lista de reproducción en los resultados de búsqueda
        first_playlist = driver.find_element(By.XPATH, "(//a[@id='video-title'])[1]")
        first_playlist.click()
        time.sleep(3)

    def save_playlist(self):
        driver = self.driver
        # Hacer clic en los tres puntos del cuadro de reproducción de la lista de reproducción
        options_button = driver.find_element(By.XPATH, "//yt-icon-button[@id='button' and @aria-label='More actions']")
        options_button.click()
        time.sleep(2)
        
        # Hacer clic en "Guardar lista de reproducción en la biblioteca"
        save_button = driver.find_element(By.XPATH, "//yt-formatted-string[text()='Guardar en biblioteca']")
        save_button.click()
        time.sleep(2)

    def refresh_page(self):
        driver = self.driver
        # Recargar la página o hacer clic en el logotipo de YouTube para volver a la página principal
        driver.find_element(By.ID, "logo-icon").click()
        time.sleep(3)

    def go_to_playlists_section(self):
        driver = self.driver
        # En el menú lateral, hacer clic en "Listas de reproducción"
        playlists_button = driver.find_element(By.XPATH, "//a[@title='Biblioteca']")
        playlists_button.click()
        time.sleep(3)

    def select_saved_playlist(self):
        driver = self.driver
        # Seleccionar la lista de reproducción guardada
        saved_playlist = driver.find_element(By.XPATH, "(//a[@id='video-title'])[1]")
        saved_playlist.click()
        time.sleep(3)

    def run(self):
        try:
            self.open_youtube()
            self.search_playlist()
            self.select_first_playlist()
            self.save_playlist()
            self.refresh_page()
            self.go_to_playlists_section()
            self.select_saved_playlist()
        finally:
            time.sleep(5)
            self.driver.quit()

if __name__ == "__main__":
    youtube_automation = YouTubePlaylistAutomation()
    youtube_automation.run()
