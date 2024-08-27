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

    def like_video(self):
        # Esperar a que el botón "Me gusta" sea clickeable
        like_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//yt-icon-button[@id='segmented-like-button']")))
        
        # Verificar si el botón ya está activado
        aria_pressed = like_button.get_attribute("aria-pressed")
        
        if aria_pressed == "false":
            like_button.click()
            print("Se dio 'Me gusta' al video")
        else:
            print("El video ya tenía 'Me gusta'")

def main():
    driver = webdriver.Chrome()  # Asegúrate de tener el ChromeDriver instalado y en el PATH
    youtube_test = YoutubeTest(driver)

    try:
        youtube_test.open_youtube()
        youtube_test.search_video("Pruebas Selenium")
        youtube_test.click_video("Pruebas Selenium")
        
        # Esperamos un poco para que el video comience a reproducirse
        time.sleep(5)
        
        youtube_test.like_video()
        
        print("Prueba completada con éxito")
        
        # Esperamos un poco más para ver el resultado
        time.sleep(5)
    except Exception as e:
        print(f"Error durante la prueba: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()