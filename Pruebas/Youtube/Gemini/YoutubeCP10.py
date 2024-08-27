from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyperclip

class YouTubeLinkCopier:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(driver_path)

    def search_and_copy_link(self, search_term):
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

        # Hacer clic en compartir
        share_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//ytd-menu-renderer[@aria-label='Compartir']"))
        )
        share_button.click()

        # Copiar el enlace
        copy_link_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Copiar']"))
        )
        copy_link_button.click()

        # Obtener el enlace copiado (opcional, para verificación)
        copied_link = pyperclip.paste()
        print("Enlace copiado:", copied_link)

    def open_new_tab(self):
        # Abrir una nueva pestaña en el navegador
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def paste_link_and_search(self):
        # Pegar el enlace en la barra de direcciones
        address_bar = self.driver.find_element(By.TAG_NAME, "input")
        address_bar.send_keys(Keys.CONTROL + 'v')  # Ctrl+v para pegar en Windows
        address_bar.send_keys(Keys.ENTER)

    def close_browser(self):
        self.driver.quit()

# Reemplaza con la ruta a tu chromedriver y el término de búsqueda
driver_path = "ruta/a/tu/chromedriver"
search_term = "Pruebas Selenium"

# Crear una instancia de la clase y ejecutar las acciones
bot = YouTubeLinkCopier(driver_path)
bot.search_and_copy_link(search_term)
bot.open_new_tab()
bot.paste_link_and_search()
bot.close_browser()