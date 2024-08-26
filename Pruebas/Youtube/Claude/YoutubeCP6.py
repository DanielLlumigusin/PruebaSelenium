# "Generame un script de selenium en python en clases para este caso de prueba
# 1, Ingreso al Youtube
# 2. Clic en Configuración
# 3,Clic en  Aspecto
# 4, Clic en Modo Oscuro"

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class YoutubeTest:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 20)

    def ingresar_youtube(self):
        self.driver.get("https://www.youtube.com")
        print("Ingreso a YouTube completado")

    def clic_configuracion(self):
        config_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//yt-icon-button[@id='avatar-btn']")))
        config_button.click()
        print("Clic en Configuración completado")

    def clic_aspecto(self):
        aspecto_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//yt-multi-page-menu-section-renderer[contains(@class, 'style-scope ytd-multi-page-menu-renderer')]//yt-formatted-string[contains(text(), 'Aspecto')]")))
        aspecto_button.click()
        print("Clic en Aspecto completado")

    def clic_modo_oscuro(self):
        modo_oscuro_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//tp-yt-paper-item[@id='dark-theme-item']")))
        modo_oscuro_button.click()
        print("Clic en Modo Oscuro completado")

    def cerrar_navegador(self):
        self.driver.quit()
        print("Navegador cerrado")

    def ejecutar_prueba(self):
        try:
            self.ingresar_youtube()
            self.clic_configuracion()
            self.clic_aspecto()
            self.clic_modo_oscuro()
            time.sleep(5)  # Espera para ver el cambio
        finally:
            self.cerrar_navegador()

if __name__ == "__main__":
    prueba = YoutubeTest()
    prueba.ejecutar_prueba()