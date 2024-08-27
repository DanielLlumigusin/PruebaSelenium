from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class YouTubeBot:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='/path/to/chromedriver')  # Cambia la ruta al ejecutable de ChromeDriver

    def login_and_navigate(self, email, password):
        self.driver.get("https://www.youtube.com")
        
        # Encuentra y haz clic en el botón "Acceder"
        login_button = self.driver.find_element(By.XPATH, "//yt-formatted-string[text()='Acceder']")
        login_button.click()

        # Ingresa el correo registrado
        email_input = self.driver.find_element(By.ID, "identifierId")
        email_input.send_keys(email)
        email_input.send_keys(Keys.RETURN)

        # Espera hasta que aparezca el campo de contraseña
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))

        # Ingresa la contraseña
        password_input = self.driver.find_element(By.NAME, "password")
        password_input.send_keys(password)
        password_input.send_keys(Keys.RETURN)

        # Espera hasta que aparezca la opción "ahora no"
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[text()='ahora no']")))

        # Haz clic en "ahora no"
        no_option = self.driver.find_element(By.XPATH, "//span[text()='ahora no']")
        no_option.click()

        # Haz clic en "Perfil"
        profile_button = self.driver.find_element(By.ID, "avatar-btn")
        profile_button.click()

    def close(self):
        self.driver.quit()

# Uso del bot
if __name__ == "__main__":
    bot = YouTubeBot()
    bot.login_and_navigate("danielalejandroarmasrobles@gmail.com", "Blackheart")
    bot.close()

