from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class YoutubeTest:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open_youtube(self):
        self.driver.get("https://www.youtube.com")

    def search_video(self, search_term):
        search_box = self.wait.until(EC.presence_of_element_located((By.NAME, "search_query")))
        search_box.clear()
        search_box.send_keys(search_term)
        search_box.send_keys(Keys.RETURN)

    def click_video(self, search_term):
        video = self.wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, search_term)))
        video.click()

    def subscribe(self):
        # Esperar a que el botón "Suscribirme" sea clickeable
        subscribe_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//tp-yt-paper-button[@aria-label='Suscribirse']")))
        
        # Verificar si ya está suscrito
        if subscribe_button.get_attribute("subscribed") != "true":
            subscribe_button.click()
            print("Te has suscrito al canal")
        else:
            print("Ya estabas suscrito a este canal")

def main():
    driver = webdriver.Chrome()  # Asegúrate de tener el ChromeDriver instalado y en el PATH
    youtube_test = YoutubeTest(driver)

    try:
        youtube_test.open_youtube()
        youtube_test.search_video("Pruebas Selenium")
        youtube_test.click_video("Pruebas Selenium")
        
        # Esperamos un poco para que el video comience a reproducirse
        time.sleep(5)
        
        youtube_test.subscribe()
        
        print("Prueba completada con éxito")
        
        # Esperamos un poco más para ver el resultado
        time.sleep(5)
    except Exception as e:
        print(f"Error durante la prueba: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()