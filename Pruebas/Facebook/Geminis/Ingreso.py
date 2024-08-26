from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class FacebookLogin:
    def __init__(self, email, password):
        self.driver = webdriver.Chrome()  # Puedes cambiar Chrome por Firefox, Edge, etc.
        self.email = email
        self.password = password

    def login(self):
        self.driver.get("https://www.facebook.com/")

        # Encuentra los campos de email y contraseña y los rellena
        email_field = self.driver.find_element(By.ID, 'email')
        email_field.send_keys(self.email)
        password_field = self.driver.find_element(By.ID, 'pass')
        password_field.send_keys(self.password)

        # Encuentra el botón de login y hace clic
        login_button = self.driver.find_element(By.NAME, 'login')
        login_button.click()

        # Agrega una pausa opcional para que la página cargue completamente
        sleep(3)

    def cerrar_navegador(self):
        self.driver.quit()

# Reemplaza con tu email y contraseña
email = ""
password = ""

# Crea una instancia de la clase y ejecuta el login
bot = FacebookLogin(email, password)
bot.login()
bot.cerrar_navegador()