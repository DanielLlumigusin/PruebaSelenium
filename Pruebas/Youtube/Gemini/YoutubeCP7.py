from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class YouTubeTrendsChecker:
    def __init__(self):
        self.driver = webdriver.Chrome()  # Puedes cambiar Chrome por Firefox, Edge, etc.

    def check_trending_videos(self):
        self.driver.get("https://www.youtube.com/")

        # Encuentra el menú lateral (puede variar según la interfaz)
        menu_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Menú']"))
        )
        menu_button.click()

        # Encuentra la opción "Explorar" y hace clic
        explore_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//yt-formatted-string[text()='Explorar']"))
        )
        explore_button.click()

        # Encuentra la sección de "Tendencias" y verifica si los videos se cargan
        trending_section = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//yt-formatted-string[text()='Tendencias']"))
        )

        # Verifica si hay videos en la sección de tendencias (puedes personalizar esta verificación)
        video_list = trending_section.find_elements(By.xpath, "//ytd-video-renderer")
        if video_list:
            print("Videos en tendencia encontrados correctamente.")
        else:
            print("No se encontraron videos en tendencia.")

    def close_browser(self):
        self.driver.quit()

# Crea una instancia de la clase y ejecuta la verificación
checker = YouTubeTrendsChecker()
checker.check_trending_videos()
checker.close_browser()