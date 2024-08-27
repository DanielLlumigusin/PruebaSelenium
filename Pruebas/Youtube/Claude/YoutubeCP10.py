from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyperclip

class YouTubeShareTest:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open_youtube(self):
        self.driver.get("https://www.youtube.com")

    def select_video(self):
        # Selecciona el primer video de la página principal
        first_video = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "ytd-rich-item-renderer")))
        first_video.click()

    def click_share(self):
        share_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Compartir']")))
        share_button.click()

    def copy_link(self):
        copy_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//tp-yt-paper-button[contains(., 'Copiar')]")))
        copy_button.click()
        
        # Esperar un momento para asegurarse de que el enlace se haya copiado
        time.sleep(1)

    def paste_and_search(self):
        # Abrir una nueva pestaña
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[-1])
        
        # Ir a una página en blanco
        self.driver.get("about:blank")
        
        # Encontrar el cuerpo de la página y pegar el enlace
        body = self.driver.find_element(By.TAG_NAME, "body")
        body.send_keys(Keys.CONTROL + 'v')
        
        # Obtener el enlace pegado
        pasted_link = pyperclip.paste()
        
        # Ir al enlace pegado
        self.driver.get(pasted_link)

def main():
    driver = webdriver.Chrome()  # Asegúrate de tener el ChromeDriver instalado y en el PATH
    youtube_test = YouTubeShareTest(driver)

    try:
        youtube_test.open_youtube()
        youtube_test.select_video()
        youtube_test.click_share()
        youtube_test.copy_link()
        youtube_test.paste_and_search()
        
        print("Prueba completada con éxito")
        
        # Esperamos un poco para ver el resultado
        time.sleep(5)
    except Exception as e:
        print(f"Error durante la prueba: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()