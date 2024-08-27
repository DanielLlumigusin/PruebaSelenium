from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class YoutubeLogin:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open_youtube(self):
        self.driver.get("https://www.youtube.com")

    def click_sign_in_button(self):
        sign_in_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//tp-yt-paper-button[@aria-label='Acceder']")))
        sign_in_button.click()

    def enter_email(self, email):
        email_field = self.wait.until(EC.presence_of_element_located((By.ID, "identifierId")))
        email_field.send_keys(email)
        next_button = self.wait.until(EC.element_to_be_clickable((By.ID, "identifierNext")))
        next_button.click()

    def enter_password(self, password):
        password_field = self.wait.until(EC.presence_of_element_located((By.NAME, "password")))
        password_field.send_keys(password)
        next_button = self.wait.until(EC.element_to_be_clickable((By.ID, "passwordNext")))
        next_button.click()

    def skip_additional_step(self):
        try:
            skip_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Ahora no')]")))
            skip_button.click()
        except:
            print("No se encontró el botón 'Ahora no' o no fue necesario.")

    def click_profile(self):
        profile_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button#avatar-btn")))
        profile_button.click()

def main():
    driver = webdriver.Chrome()  # Asegúrate de tener el ChromeDriver instalado y en el PATH
    youtube_login = YoutubeLogin(driver)

    try:
        youtube_login.open_youtube()
        youtube_login.click_sign_in_button()
        youtube_login.enter_email("danielalejandroarmasrobles@gmail.com")
        youtube_login.enter_password("Blackheart")
        youtube_login.skip_additional_step()
        youtube_login.click_profile()
        
        print("Inicio de sesión y acceso al perfil completados con éxito")
    except Exception as e:
        print(f"Error durante el proceso: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()