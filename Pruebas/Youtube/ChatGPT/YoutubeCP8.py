from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

class YouTubeVideoUpload:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login_youtube(self, email, password):
        driver = self.driver
        driver.get("https://www.youtube.com")
        time.sleep(3)

        # Click en 'Iniciar sesión'
        login_button = driver.find_element(By.XPATH, "//tp-yt-paper-button[@aria-label='Sign in']")
        login_button.click()
        time.sleep(2)

        # Ingresar el email
        email_input = driver.find_element(By.XPATH, "//input[@type='email']")
        email_input.send_keys(email)
        email_input.send_keys(Keys.ENTER)
        time.sleep(3)

        # Ingresar la contraseña
        password_input = driver.find_element(By.XPATH, "//input[@type='password']")
        password_input.send_keys(password)
        password_input.send_keys(Keys.ENTER)
        time.sleep(5)

    def create_video(self, video_path):
        driver = self.driver

        # Click en el ícono de la cámara para crear
        camera_icon = driver.find_element(By.XPATH, "//yt-icon-button[@aria-label='Create']")
        camera_icon.click()
        time.sleep(2)

        # Click en 'Subir un video'
        upload_video_button = driver.find_element(By.XPATH, "//yt-formatted-string[text()='Upload video']")
        upload_video_button.click()
        time.sleep(3)

        # Crear canal si es la primera vez
        try:
            create_channel_button = driver.find_element(By.XPATH, "//ytcp-button[@id='create-channel-button']")
            create_channel_button.click()
            time.sleep(2)

            # Confirmar creación de canal
            confirm_create_button = driver.find_element(By.XPATH, "//ytcp-button[@id='done-button']")
            confirm_create_button.click()
            time.sleep(2)
        except Exception as e:
            print("Canal ya creado o no es necesario crear canal.")

        # Subir video desde el explorador de archivos
        select_video_input = driver.find_element(By.XPATH, "//input[@type='file']")
        select_video_input.send_keys(video_path)
        time.sleep(5)

    def set_video_details(self):
        driver = self.driver

        # Seleccionar audiencia - video creado para niños
        audience_section = driver.find_element(By.XPATH, "//ytcp-dropdown-trigger[contains(@aria-label,'Audience')]")
        audience_section.click()
        time.sleep(2)

        for_kids_option = driver.find_element(By.XPATH, "//tp-yt-paper-item[@id='text-item-0']")
        for_kids_option.click()
        time.sleep(2)

    def set_video_visibility(self):
        driver = self.driver

        # Dar clic en siguiente hasta llegar a visibilidad
        for _ in range(3):
            next_button = driver.find_element(By.XPATH, "//ytcp-button[@id='next-button']")
            next_button.click()
            time.sleep(2)

        # Seleccionar 'Oculto' en visibilidad
        visibility_dropdown = driver.find_element(By.XPATH, "//ytcp-button[@aria-label='Visibility options']")
        visibility_dropdown.click()
        time.sleep(2)

        hidden_option = driver.find_element(By.XPATH, "//tp-yt-paper-item[@id='text-item-1']")
        hidden_option.click()
        time.sleep(2)

    def save_and_finish(self):
        driver = self.driver

        # Guardar el video
        save_button = driver.find_element(By.XPATH, "//ytcp-button[@id='done-button']")
        save_button.click()
        time.sleep(5)

        # Clic en continuar
        continue_button = driver.find_element(By.XPATH, "//ytcp-button[@id='done-button']")
        continue_button.click()
        time.sleep(5)

    def play_uploaded_video(self):
        driver = self.driver

        # Seleccionar el video recién subido
        video_thumbnail = driver.find_element(By.XPATH, "//ytd-thumbnail[@id='thumbnail']")
        video_thumbnail.click()
        time.sleep(5)

    def run(self, email, password, video_path):
        try:
            self.login_youtube(email, password)
            self.create_video(video_path)
            self.set_video_details()
            self.set_video_visibility()
            self.save_and_finish()
            self.play_uploaded_video()
        finally:
            self.driver.quit()


if __name__ == "__main__":
    email = "danielalejandroarmasrobles@gmail.com"
    password = "Blackheart"
    video_path = os.path.abspath("../Videos/F122.mp4")

    uploader = YouTubeVideoUpload()
    uploader.run(email, password, video_path)