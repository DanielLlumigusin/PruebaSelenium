from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os

class FacebookPostPhotoVideoTest:
    def __init__(self, email, password, file_path):
        self.email = email
        self.password = password
        self.file_path = file_path
        self.driver = webdriver.Chrome()

    def login(self):
        driver = self.driver

        # Ingresar a Facebook
        driver.get("https://www.facebook.com")
        time.sleep(3)

        # Localizar el campo de correo y contraseña
        email_input = driver.find_element(By.ID, "email")
        password_input = driver.find_element(By.ID, "pass")

        # Ingresar el correo y la contraseña
        email_input.send_keys(self.email)
        password_input.send_keys(self.password)

        # Hacer clic en el botón de iniciar sesión
        login_button = driver.find_element(By.NAME, "login")
        login_button.click()
        time.sleep(10)

    def post_photo_or_video(self):
        driver = self.driver

        # Dar click en el botón "Foto/Video"
        photo_video_button = driver.find_element(By.XPATH, "//span[text()='Photo/video']")
        photo_video_button.click()
        time.sleep(10)

        # Dar click en agregar foto o video
        add_photo_video_input = driver.find_element(By.XPATH, "//input[@type='file']")
        add_photo_video_input.send_keys(self.file_path)
        time.sleep(10)

        # Dar click en Post
        post_button = driver.find_element(By.XPATH, "//div[@aria-label='Post']")
        post_button.click()
        time.sleep(10)

    def run_test(self):
        try:
            self.login()
            self.post_photo_or_video()
        finally:
            # Cerrar el navegador al finalizar
            self.driver.quit()

if __name__ == "__main__":
    # Credenciales de Facebook y ruta de archivo
    email = ""  # Reemplazar con tu correo registrado en Facebook
    password = ""       # Reemplazar con tu contraseña de Facebook
    file_path = os.path.abspath("../imagenes/carro.jpg")  # Reemplazar con la ruta completa de la foto o video

    # Ejecutar el test de publicar foto/video
    facebook_test = FacebookPostPhotoVideoTest(email, password, file_path)
    facebook_test.run_test()
