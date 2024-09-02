from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class FacebookLoginTest:
    def __init__(self, email, password):
        self.email = email
        self.password = password
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
        time.sleep(5)

    def run_test(self):
        try:
            self.login()
        finally:
            # Cerrar el navegador al finalizar
            self.driver.quit()

if __name__ == "__main__":
    # Credenciales de Facebook
    email = "elbandidoarmas@gmail.com"  # Reemplazar con tu correo registrado en Facebook
    password = "kespar02"       # Reemplazar con tu contraseña de Facebook

    # Ejecutar el test de inicio de sesión
    facebook_test = FacebookLoginTest(email, password)
    facebook_test.run_test()

