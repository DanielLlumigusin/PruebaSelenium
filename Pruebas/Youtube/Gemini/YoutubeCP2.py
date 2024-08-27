from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class YouTubeLogin:
    def __init__(self, email, password):
        self.driver = webdriver.Chrome()  # Puedes cambiar Chrome por Firefox, Edge, etc.
        self.email = email
        self.password = password

    def login(self):
        self.driver.get("https://www.youtube.com/")

        # Encuentra el botón "Acceder" y hace clic
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "button"))
        )
        login_button.click()

        # Encuentra el campo de correo electrónico y escribe
        email_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "identifierId"))
        )
        email_field.send_keys(self.email)

        # Encuentra el botón "Siguiente" y hace clic
        next_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "identifierNext"))
        )
        next_button.click()

        # Encuentra el campo de contraseña y escribe
        password_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "password"))
        )
        password_field.send_keys(self.password)

        # Encuentra el botón "Siguiente" y hace clic
        next_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "passwordNext"))
        )
        next_button.click()

        # Maneja la opción "Ahora no" (puede variar según la interfaz)
        # Aquí asumimos un botón con el texto "Ahora no"
        try:
            no_thanks_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Ahora no')]"))
            )
            no_thanks_button.click()
        except:
            print("Opción 'Ahora no' no encontrada")

        # Encuentra el botón de perfil y hace clic
        profile_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "avatar-btn"))
        )
        profile_button.click()

    def close_browser(self):
        self.driver.quit()

# Reemplaza con tu correo electrónico y contraseña
email = "danielalejandroarmasrobles@gmail.com"
password = "Blackheart"

# Crea una instancia de la clase y ejecuta el login
bot = YouTubeLogin(email, password)
bot.login()
bot.close_browser()
