from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FacebookLogin:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open_facebook(self):
        self.driver.get("https://www.facebook.com")

    def enter_email(self, email):
        email_field = self.wait.until(EC.presence_of_element_located((By.ID, "email")))
        email_field.send_keys(email)

    def enter_password(self, password):
        password_field = self.driver.find_element(By.ID, "pass")
        password_field.send_keys(password)

    def click_login_button(self):
        login_button = self.driver.find_element(By.NAME, "login")
        login_button.click()

def main():
    driver = webdriver.Chrome()  # Asegúrate de tener el ChromeDriver instalado y en el PATH
    fb_login = FacebookLogin(driver)

    try:
        fb_login.open_facebook()
        fb_login.enter_email("")
        fb_login.enter_password("")
        fb_login.click_login_button()
        
        # Espera opcional para verificar el inicio de sesión exitoso
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[aria-label='Inicio']")))
        print("Inicio de sesión exitoso")
    except Exception as e:
        print(f"Error durante el inicio de sesión: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()