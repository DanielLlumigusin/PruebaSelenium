from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class YouTubeBot:
    def __init__(self, search_term):
        self.driver = webdriver.Chrome()  # Puedes cambiar Chrome por Firefox, Edge, etc.
        self.search_term = search_term

    def search_and_play(self):
        self.driver.get("https://www.youtube.com/")

        # Encuentra la barra de búsqueda y escribe el término
        search_bar = self.driver.find_element(By.ID, "search")
        search_bar.send_keys(self.search_term)
        search_bar.send_keys(Keys.ENTER)

        # Encuentra el primer video y hace clic
        first_video = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "video-title"))
        )
        first_video.click()

        # Espera a que el video se cargue
        video = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.TAG_NAME, "video"))
        )
        video.click()  # Hace clic en el video para reproducirlo

    def save_video(self):
        # Encuentra el botón de "Guardar" (el XPath puede variar según la interfaz)
        save_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//ytd-toggle-button-renderer[@aria-label='Guardar']"))
        )
        save_button.click()

    def close_browser(self):
        self.driver.quit()

# Reemplaza con tu término de búsqueda
search_term = "Pruebas Selenium"

# Crea una instancia de la clase y ejecuta las acciones
bot = YouTubeBot(search_term)
bot.search_and_play()
bot.save_video()
bot.close_browser()