from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class FacebookBlockUserTest:
    def __init__(self, email, password, profile_name):
        self.email = email
        self.password = password
        self.profile_name = profile_name
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

    def block_user(self):
        driver = self.driver

        # Dar click en la barra de búsqueda
        search_bar = driver.find_element(By.XPATH, "//input[@aria-label='Search Facebook']")
        search_bar.click()
        time.sleep(2)

        # Escribir el nombre del perfil y presionar Enter
        search_bar.send_keys(self.profile_name)
        search_bar.send_keys(Keys.ENTER)
        time.sleep(3)

        # Dar click en el perfil de la lista de resultados
        profile_link = driver.find_element(By.XPATH, f"//span[contains(text(), '{self.profile_name}')]")
        profile_link.click()
        time.sleep(3)

        # Dar click en los tres puntos horizontales
        options_button = driver.find_element(By.XPATH, "//div[@aria-label='Actions for this profile']")
        options_button.click()
        time.sleep(2)

        # Dar click en 'Block'
        block_button = driver.find_element(By.XPATH, "//span[text()='Block']")
        block_button.click()
        time.sleep(2)

        # Confirmar el bloqueo
        confirm_block_button = driver.find_element(By.XPATH, "//span[text()='Confirm']")
        confirm_block_button.click()
        time.sleep(2)

        # Cerrar el cuadro de diálogo
        close_button = driver.find_element(By.XPATH, "//span[text()='Close']")
        close_button.click()
        time.sleep(2)

    def run_test(self):
        try:
            self.login()
            self.block_user()
        finally:
            # Cerrar el navegador al finalizar
            self.driver.quit()

if __name__ == "__main__":
    # Credenciales de Facebook y nombre del perfil que se desea bloquear
    email = "elbandidoarmas@gmail.com"  # Reemplazar con tu correo registrado en Facebook
    password = "kespar02"       # Reemplazar con tu contraseña de Facebook
    profile_name = "Alejandro Daniel"  # Reemplazar con el nombre del perfil que se desea bloquear

    # Ejecutar el test de bloqueo de usuario
    facebook_test = FacebookBlockUserTest(email, password, profile_name)
    facebook_test.run_test()
