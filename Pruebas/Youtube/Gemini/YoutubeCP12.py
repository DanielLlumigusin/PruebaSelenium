from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyperclip

class YouTubeClipCreator:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(driver_path)

    def create_and_share_clip(self, search_term, clip_title):
        self.driver.get("https://www.youtube.com/")

        # Buscar el video
        search_bar = self.driver.find_element(By.ID, "search")
        search_bar.send_keys(search_term)
        search_bar.send_keys(Keys.ENTER)

        # Seleccionar el primer video
        first_video = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "video-title"))
        )
        first_video.click()

        # Hacer clic en los tres puntos y seleccionar "Clip"
        more_actions_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//ytd-menu-renderer[@aria-label='Más acciones']"))
        )
        more_actions_button.click()

        clip_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//yt-formatted-string[text()='Clip']"))
        )
        clip_button.click()

        # Agregar el título al clip
        clip_title_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Título del clip']"))
        )
        clip_title_input.send_keys(clip_title)

        # Hacer clic en "Compartir clip"
        share_clip_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//yt-formatted-string[text()='Compartir clip']"))
        )
        share_clip_button.click()

        # Copiar el enlace del clip
        copy_link_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Copiar']"))
        )
        copy_link_button.click()

        # Obtener el enlace copiado (opcional, para verificación)
        copied_link = pyperclip.paste()
        print("Enlace del clip copiado:", copied_link)

        # Abrir una nueva pestaña y pegar el enlace
        self.open_new_tab_and_paste_link(copied_link)

    def open_new_tab_and_paste_link(self, link):
        # Abrir una nueva pestaña en el navegador
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[-1])

        # Pegar el enlace en la barra de direcciones
        address_bar = self.driver.find_element(By.TAG_NAME, "input")
        address_bar.send_keys(link)
        address_bar.send_keys(Keys.ENTER)

    def close_browser(self):
        self.driver.quit()

# Reemplaza con la ruta a tu chromedriver
driver_path = "ruta/a/tu/chromedriver"
search_term = "trailer"
clip_title = "clip de prueba"

# Crear una instancia de la clase y ejecutar las acciones
bot = YouTubeClipCreator(driver_path)
bot.create_and_share_clip(search_term, clip_title)
bot.close_browser()