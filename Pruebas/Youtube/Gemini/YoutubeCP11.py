from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class YouTubePlaylistSaver:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(driver_path)

    def search_and_save_playlist(self, search_term):
        self.driver.get("https://www.youtube.com/")

        # Buscar la lista de reproducción
        search_bar = self.driver.find_element(By.ID, "search")
        search_bar.send_keys(search_term)
        search_bar.send_keys(Keys.ENTER)

        # Seleccionar la primera lista de reproducción
        first_playlist = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//ytd-playlist-renderer"))
        )
        first_playlist.click()

        # Hacer clic en los tres puntos y guardar
        more_actions_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//ytd-menu-renderer[@aria-label='Más acciones']"))
        )
        more_actions_button.click()

        save_playlist_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//yt-formatted-string[text()='Guardar lista de reproducción']"))
        )
        save_playlist_button.click()

        # Recargar la página o ir a la página principal
        self.driver.refresh()  # O puedes usar: self.driver.get("https://www.youtube.com/")

        # Ir a la sección de listas de reproducción
        library_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//yt-formatted-string[text()='Biblioteca']"))
        )
        library_button.click()

        # Hacer clic en la lista de reproducción guardada (ajusta el XPath según tu interfaz)
        saved_playlist = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//ytd-playlist-renderer[@aria-label='Tu lista de reproducción']"))
        )
        saved_playlist.click()

    def close_browser(self):
        self.driver.quit()

# Reemplaza con la ruta a tu chromedriver
driver_path = "ruta/a/tu/chromedriver"
search_term = "Listas de reproducción"

# Crear una instancia de la clase y ejecutar las acciones
bot = YouTubePlaylistSaver(driver_path)
bot.search_and_save_playlist(search_term)
bot.close_browser()