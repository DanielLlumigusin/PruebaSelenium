# "Generame un script de selenium en python en clases para este caso de prueba
# 1, Ingreso al Youtube
# 2. Clic en Configuración
# 3,Clic en  Aspecto
# 4, Clic en Modo Oscuro"

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class YoutubeAutomation:
    def __init__(self):
        # Inicializar el navegador (puedes usar Chrome o Firefox)
        self.driver = webdriver.Chrome(executable_path='/ruta/a/tu/chromedriver')

    def ingresar_a_youtube(self):
        self.driver.get('https://www.youtube.com')

    def clic_configuracion(self):
        config_btn = self.driver.find_element(By.XPATH, '//button[@aria-label="Configuración"]')
        config_btn.click()

    def clic_aspecto(self):
        aspecto_btn = self.driver.find_element(By.XPATH, '//a[contains(text(), "Aspecto")]')
        aspecto_btn.click()

    def clic_modo_oscuro(self):
        modo_oscuro_btn = self.driver.find_element(By.XPATH, '//label[contains(text(), "Modo oscuro")]')
        modo_oscuro_btn.click()

    def ejecutar_caso_de_prueba(self):
        self.ingresar_a_youtube()
        self.clic_configuracion()
        self.clic_aspecto()
        self.clic_modo_oscuro()

    def cerrar_navegador(self):
        self.driver.quit()

# Crear una instancia de la clase y ejecutar el caso de prueba
if __name__ == '__main__':
    youtube_automation = YoutubeAutomation()
    youtube_automation.ejecutar_caso_de_prueba()
    youtube_automation.cerrar_navegador()
