from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class FacebookAddFriendTest:
    def __init__(self, email, password, friend_name):
        self.email = email
        self.password = password
        self.friend_name = friend_name
        self.driver = webdriver.Chrome()

    def login(self):
        driver = self.driver
        driver.get("https://www.facebook.com")
        time.sleep(3)

        # Localizar el campo de email y contraseña para iniciar sesión
        email_input = driver.find_element(By.ID, "email")
        password_input = driver.find_element(By.ID, "pass")

        # Ingresar las credenciales
        email_input.send_keys(self.email)
        password_input.send_keys(self.password)

        # Iniciar sesión
        password_input.send_keys(Keys.RETURN)
        time.sleep(7)

    def search_friend(self):
        driver = self.driver

        # Click en la barra de búsqueda
        search_box = driver.find_element(By.XPATH, "//input[@type='search' and @placeholder='Search Facebook']")
        search_box.click()

        # Ingresar el nombre del amigo/amiga en la barra de búsqueda y presionar Enter
        search_box.send_keys(self.friend_name)
        search_box.send_keys(Keys.RETURN)
        time.sleep(7)

    def click_on_friend_profile(self):
        driver = self.driver

        # Seleccionar el perfil del amigo/amiga (ajustar XPATH según resultados)
        profile = driver.find_element(By.XPATH, "//a[contains(text(), '{}')]".format(self.friend_name))
        profile.click()
        time.sleep(7)

    def click_add_friend(self):
        driver = self.driver

        # Clic en el botón de "Agregar amigo" (Ajustar XPATH si es necesario)
        add_friend_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Add Friend')]")
        add_friend_button.click()
        time.sleep(7)

    def run_test(self):
        try:
            self.login()
            self.search_friend()
            self.click_on_friend_profile()
            self.click_add_friend()
        finally:
            self.driver.quit()


if __name__ == "__main__":
    email = ""  # Tu email o número de teléfono
    password = ""  # Tu contraseña de Facebook
    friend_name = "Alejandro Daniel"  # Nombre del amigo/a a buscar

    # Crear instancia de la clase y ejecutar la prueba
    facebook_test = FacebookAddFriendTest(email, password, friend_name)
    facebook_test.run_test()
