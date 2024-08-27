from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class YouTubeShareAutomation:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def open_youtube(self):
        driver = self.driver
        driver.get("https://www.youtube.com/")
        time.sleep(3)

    def select_video(self):
        driver = self.driver
        # Seleccionar el primer video de la página principal o de una búsqueda
        video = driver.find_element(By.XPATH, "(//a[@id='video-title'])[1]")
        video.click()
        time.sleep(5)  # Esperar a que el video cargue y comience

    def share_video_and_copy_link(self):
        driver = self.driver
        # Hacer clic en el botón de "Compartir"
        share_button = driver.find_element(By.XPATH, "//yt-icon-button[@id='button' and @aria-label='Share']")
        share_button.click()
        time.sleep(2)
        
        # Hacer clic en el botón de "Copiar enlace"
        copy_link_button = driver.find_element(By.XPATH, "//yt-formatted-string[text()='Copy link']")
        copy_link_button.click()
        time.sleep(2)
        
        # Obtener el enlace del video copiado
        link_field = driver.find_element(By.XPATH, "//div[@id='copy-input']/input")
        copied_link = link_field.get_attribute("value")
        return copied_link

    def paste_link_in_browser(self, copied_link):
        driver = self.driver
        # Abrir una nueva pestaña en el navegador
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        
        # Pegar el enlace en la barra de búsqueda y presionar Enter
        driver.get(copied_link)
        time.sleep(5)  # Esperar a que la página cargue

    def run(self):
        try:
            self.open_youtube()
            self.select_video()
            copied_link = self.share_video_and_copy_link()
            self.paste_link_in_browser(copied_link)
        finally:
            time.sleep(5)
            self.driver.quit()

if __name__ == "__main__":
    youtube_automation = YouTubeShareAutomation()
    youtube_automation.run()
