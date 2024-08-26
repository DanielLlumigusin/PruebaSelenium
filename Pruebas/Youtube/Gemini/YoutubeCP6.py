# "Generame un script de selenium en python en clases para este caso de prueba
# 1, Ingreso al Youtube
# 2. Clic en Configuración
# 3,Clic en  Aspecto
# 4, Clic en Modo Oscuro"
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class YoutubeDarkMode:
    def __init__(self):
        self.driver = webdriver.Chrome()  # Ajusta según tu navegador

    def activate_dark_mode(self):
        self.driver.get("https://www.youtube.com")
        
        # Esperar a que el elemento de configuración esté visible (puede variar según la estructura de YouTube)
        settings_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "yt-masthead-btn"))  # Reemplaza con el ID correcto
        )
        settings_button.click()

        # Similares acciones para encontrar y hacer clic en "Aspecto" y "Modo Oscuro"
        # ...

    def tear_down(self):
        self.driver.quit()

if __name__ == "__main__":
    test = YoutubeDarkMode()
    test.activate_dark_mode()
    test.tear_down()