from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class FacebookUploader:
    def __init__(self, email, password, file_path):
        self.driver = webdriver.Chrome()  # Puedes cambiar Chrome por Firefox, Edge, etc.
        self.email = email
        self.password = password
        self.file_path = file_path

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

        # Espera a que el inicio de sesión se complete (ajusta el tiempo según sea necesario)
        time.sleep(5)

    def upload_media(self):
        # Encuentra el botón para crear una publicación (puede variar según la interfaz de Facebook)
        create_post_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@data-testid, 'create_post_button')]"))
        )
        create_post_button.click()

        # Encuentra el campo para seleccionar archivos y envía el archivo
        file_input = self.driver.find_element(By.XPATH, "//input[@type='file']")
        file_input.send_keys(self.file_path)

        # Encuentra el botón de publicar y hace clic
        post_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Publicar')]"))
        )
        post_button.click()

    def close_browser(self):
        self.driver.quit()

# Reemplaza con tu email, contraseña y la ruta del archivo
email = ""
password = ""
file_path = "../imagenes/carro.jpg"  # O la ruta de tu video

# Crea una instancia de la clase y ejecuta las acciones
bot = FacebookUploader(email, password, file_path)
bot.login()
bot.upload_media()
bot.close_browser()
