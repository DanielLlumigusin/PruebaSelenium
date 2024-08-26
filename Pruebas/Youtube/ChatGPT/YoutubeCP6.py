from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class YouTubeTest:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        # Asegúrate de especificar la ruta correcta al chromedriver o utilizar WebDriver Manager
        self.driver = webdriver.Chrome(service=Service("path/to/chromedriver"), options=chrome_options)
        self.wait = WebDriverWait(self.driver, 10)

    def open_youtube(self):
        self.driver.get("https://www.youtube.com/")
        time.sleep(2)  # Esperar un momento para que cargue la página

    def click_settings(self):
        settings_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Settings']")))
        settings_button.click()
        time.sleep(2)  # Esperar un momento para que cargue el menú de configuración

    def click_appearance(self):
        appearance_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Appearance')]")))
        appearance_option.click()
        time.sleep(2)  # Esperar un momento para que cargue el submenú de apariencia

    def enable_dark_mode(self):
        dark_mode_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Dark theme')]")))
        dark_mode_option.click()
        time.sleep(2)  # Esperar un momento para que se aplique el modo oscuro

    def close_browser(self):
        self.driver.quit()

if __name__ == "__main__":
    test = YouTubeTest()
    test.open_youtube()
    test.click_settings()
    test.click_appearance()
    test.enable_dark_mode()
    test.close_browser()
