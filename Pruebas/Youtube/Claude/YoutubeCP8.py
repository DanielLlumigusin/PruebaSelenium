from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

class YouTubeUploadTest:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def open_youtube(self):
        self.driver.get("https://www.youtube.com")

    def click_create_video(self):
        create_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "ytd-topbar-menu-button-renderer.style-scope:nth-child(3)")))
        create_button.click()

    def click_upload_video(self):
        upload_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//yt-formatted-string[text()='Subir vídeo']")))
        upload_option.click()

    def create_channel_if_needed(self):
        try:
            create_channel_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//tp-yt-paper-button[contains(text(), 'Crear canal')]")))
            create_channel_button.click()
            create_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//tp-yt-paper-button[contains(text(), 'Crear')]")))
            create_button.click()
        except:
            print("El canal ya existe o no se requiere creación.")

    def select_video(self, file_path):
        select_file_input = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
        select_file_input.send_keys(file_path)

    def set_audience_for_kids(self):
        kids_radio = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//tp-yt-paper-radio-button[@name='VIDEO_MADE_FOR_KIDS_MFK']")))
        kids_radio.click()

    def click_next(self):
        next_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//ytcp-button[@id='next-button']")))
        next_button.click()

    def set_visibility_hidden(self):
        hidden_radio = self.wait.until(EC.element_to_be_clickable((By.NAME, "UNLISTED")))
        hidden_radio.click()

    def click_save(self):
        save_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//ytcp-button[@id='done-button']")))
        save_button.click()

    def click_continue(self):
        continue_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//ytcp-button[contains(@id, 'close-button')]")))
        continue_button.click()

    def click_uploaded_video(self):
        video_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/watch?v=')]")))
        video_link.click()

def main():
    driver = webdriver.Chrome()  # Asegúrate de tener el ChromeDriver instalado y en el PATH
    driver.maximize_window()
    youtube_test = YouTubeUploadTest(driver)

    try:
        youtube_test.open_youtube()
        youtube_test.click_create_video()
        youtube_test.click_upload_video()
        youtube_test.create_channel_if_needed()

        # Asegúrate de reemplazar 'ruta/a/tu/video.mp4' con la ruta real de tu video
        file_path = os.path.abspath('../Videos/F122.mp4')
        youtube_test.select_video(file_path)

        youtube_test.set_audience_for_kids()
        youtube_test.click_next()  # Detalles
        youtube_test.click_next()  # Elementos del video
        youtube_test.click_next()  # Comprobaciones
        youtube_test.set_visibility_hidden()
        youtube_test.click_save()
        
        # Esperar a que se complete la subida
        time.sleep(10)  # Ajusta este tiempo según el tamaño de tu video

        youtube_test.click_continue()
        youtube_test.click_uploaded_video()

        print("Prueba completada con éxito")
    except Exception as e:
        print(f"Error durante la prueba: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()