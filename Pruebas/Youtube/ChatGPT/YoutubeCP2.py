from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class YouTubeLoginTest:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.driver = webdriver.Chrome()

    def login_to_youtube(self):
        driver = self.driver

        # Ingresar a YouTube
        driver.get("https://www.youtube.com")
        time.sleep(3)

        # Seleccionar el botón "Acceder"
        sign_in_button = driver.find_element(By.XPATH, "//yt-formatted-string[text()='Acceder']")
        sign_in_button.click()
        time.sleep(3)

    def enter_credentials(self):
        driver = self.driver

        # Escribir el correo registrado
        email_input = driver.find_element(By.XPATH, "//input[@type='email']")
        email_input.send_keys(self.email)
        next_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Siguiente')]")
        next_button.click()
        time.sleep(3)

        # Escribir la contraseña
        password_input = driver.find_element(By.XPATH, "//input[@type='password']")
        password_input.send_keys(self.password)
        next_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Siguiente')]")
        next_button.click()
        time.sleep(3)

    def skip_welcome(self):
        driver = self.driver

        # Seleccionar la opción "Ahora no" en el cuadro "Accediste a tu cuenta"
        try:
            skip_button = driver.find_element(By.XPATH, "//button[text()='Ahora no']")
            skip_button.click()
            time.sleep(2)
        except:
            print("No se mostró el cuadro de bienvenida")

    def open_profile(self):
        driver = self.driver

        # Dar clic en el botón de perfil
        profile_button = driver.find_element(By.XPATH, "//button[@id='avatar-btn']")
        profile_button.click()
        time.sleep(2)

    def run_test(self):
        try:
            self.login_to_youtube()
            self.enter_credentials()
            self.skip_welcome()
            self.open_profile()
        finally:
            # Cerrar el navegador al finalizar
            self.driver.quit()

if __name__ == "__main__":
    # Credenciales de YouTube
    email = "danielalejandroarmasrobles@gmail.com"  # Reemplazar con tu correo registrado en YouTube
    password = "Blackheart"    # Reemplazar con tu contraseña

    # Ejecutar el test de inicio de sesión en YouTube
    youtube_test = YouTubeLoginTest(email, password)
    youtube_test.run_test()

