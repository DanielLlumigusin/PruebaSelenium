from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

class FacebookBot:
    def __init__(self, email, password):
        self.driver = webdriver.Chrome()  # Cambia 'Chrome' por tu navegador si es necesario
        self.email = email
        self.password = password

    def login(self):
        self.driver.get("https://www.facebook.com/")
        # Encuentra los campos de email y contraseña y los rellena
        email_field = self.driver.find_element(By.ID, 'email')
        email_field.send_keys(self.email)
        password_field = self.driver.find_element(By.ID, 'pass')
        password_field.send_keys(self.password)
        # Hace clic en el botón de login
        login_button = self.driver.find_element(By.NAME, 'login')
        login_button.click()

    def search_friend(self, friend_name):
        # Encuentra la barra de búsqueda y escribe el nombre del amigo
        search_bar = self.driver.find_element(By.XPATH, "//input[@placeholder='Buscar en Facebook']")
        search_bar.send_keys(friend_name)
        search_bar.send_keys(Keys.ENTER)

    def add_friend(self):
        # Encuentra el botón de "Agregar amigo" y hace clic
        add_friend_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Agregar amigo')]")
        add_friend_button.click()

    def close_browser(self):
        self.driver.quit()

# Reemplaza con tu email y contraseña
email = ""
password = ""
friend_name = "Alejandro Daniel"

# Crea una instancia del bot
bot = FacebookBot(email, password)

# Ejecuta las acciones
bot.login()
bot.search_friend(friend_name)
bot.add_friend()

# Cierra el navegador
bot.close_browser()