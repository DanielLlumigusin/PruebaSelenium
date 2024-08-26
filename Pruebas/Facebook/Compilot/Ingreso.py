from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

class FacebookLogin:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.driver.get("https://www.facebook.com/")

    def login(self):
        email_input = self.driver.find_element_by_id("email")
        password_input = self.driver.find_element_by_id("pass")
        login_button = self.driver.find_element_by_name("login")

        email_input.send_keys(self.email)
        password_input.send_keys(self.password)
        login_button.click()

if __name__ == "__main__":
    email = ""
    password = ""

    fb_login = FacebookLogin(email, password)
    fb_login.login()
    # Puedes agregar más acciones después de iniciar sesión si lo necesitas
    time.sleep(5)  # Espera 5 segundos para ver el resultado
    fb_login.driver.quit()
