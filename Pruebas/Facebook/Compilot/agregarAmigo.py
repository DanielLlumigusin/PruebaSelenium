from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FacebookFriendAdder:
    def __init__(self, email, password):
        self.driver = webdriver.Chrome()  # Cambia esto al driver que estés utilizando
        self.email = email
        self.password = password

    def login(self):
        self.driver.get("https://www.facebook.com/")
        email_input = self.driver.find_element(By.ID, "email")
        password_input = self.driver.find_element(By.ID, "pass")
        login_button = self.driver.find_element(By.NAME, "login")

        email_input.send_keys(self.email)
        password_input.send_keys(self.password)
        login_button.click()

    def search_friend(self, friend_name):
        search_bar = self.driver.find_element(By.NAME, "q")
        search_bar.send_keys(friend_name)
        search_bar.send_keys(Keys.RETURN)

    def visit_friend_profile(self):
        # Espera hasta que aparezcan los resultados de búsqueda
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "search-result"))
        )
        # Haz clic en el primer resultado (perfil de amigo/amiga)
        first_result = self.driver.find_element(By.CLASS_NAME, "search-result")
        first_result.click()

    def add_friend(self):
        # Espera hasta que aparezca el botón "Agregar a mis amigos"
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='Agregar a mis amigos']"))
        )
        # Haz clic en el botón "Agregar a mis amigos"
        add_friend_button = self.driver.find_element(By.XPATH, "//button[text()='Agregar a mis amigos']")
        add_friend_button.click()

    def close_browser(self):
        self.driver.quit()

# Ejemplo de uso
if __name__ == "__main__":
    email = ""
    password = ""
    friend_name = "Alejandro Daniel"

    fb_friend_adder = FacebookFriendAdder(email, password)
    fb_friend_adder.login()
    fb_friend_adder.search_friend(friend_name)
    fb_friend_adder.visit_friend_profile()
    fb_friend_adder.add_friend()
    fb_friend_adder.close_browser()
