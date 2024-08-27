from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyperclip

class YouTubeClipTest:
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

    def select_first_video(self):
        first_video = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "ytd-video-renderer")))
        first_video.click()

    def click_three_dots(self):
        three_dots = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "ytd-menu-renderer.ytd-video-primary-info-renderer")))
        three_dots.click()

    def select_clip_option(self):
        clip_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//yt-formatted-string[contains(text(), 'Clip')]")))
        clip_option.click()

    def add_clip_title(self, title):
        title_input = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input#textarea")))
        title_input.clear()
        title_input.send_keys(title)

    def share_clip(self):
        share_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//yt-formatted-string[contains(text(), 'Compartir clip')]")))
        share_button.click()

    def copy_link(self):
        copy_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//yt-formatted-string[contains(text(), 'Copiar')]")))
        copy_button.click()
        time.sleep(1)  # Esperar a que se copie el enlace

    def paste_and_search(self):
        # Abrir una nueva pestaña
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[-1])
        
        # Ir a una página en blanco
        self.driver.get("about:blank")
        
        # Pegar el enlace y navegar
        body = self.driver.find_element(By.TAG_NAME, "body")
        body.send_keys(Keys.CONTROL + 'v')
        body.send_keys(Keys.RETURN)

def main():
    driver = webdriver.Chrome()  # Asegúrate de tener el ChromeDriver instalado y en el PATH
    youtube_test = YouTubeClipTest(driver)

    try:
        youtube_test.open_youtube()
        youtube_test.search_video("trailer")
        youtube_test.select_first_video()
        youtube_test.click_three_dots()
        youtube_test.select_clip_option()
        youtube_test.add_clip_title("clip de prueba")
        youtube_test.share_clip()
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