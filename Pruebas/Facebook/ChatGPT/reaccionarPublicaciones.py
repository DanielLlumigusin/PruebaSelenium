from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time

class FacebookReactionBot:
    def __init__(self, driver_path, user_email, user_password):
        # Configuración del navegador
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(service=Service(driver_path), options=chrome_options)
        self.user_email = user_email
        self.user_password = user_password

    def login(self):
        self.driver.get('https://www.facebook.com/')
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'email')))
        
        # Ingresar correo electrónico
        email_input = self.driver.find_element(By.ID, 'email')
        email_input.send_keys(self.user_email)

        # Ingresar contraseña
        password_input = self.driver.find_element(By.ID, 'pass')
        password_input.send_keys(self.user_password)

        # Hacer clic en el botón de inicio de sesión
        login_button = self.driver.find_element(By.NAME, 'login')
        login_button.click()

    def search_and_react(self, search_text, reaction_type):
        # Esperar a que la barra de búsqueda esté disponible y hacer clic
        search_box = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@type="search"]')))
        search_box.click()

        # Ingresar el texto de búsqueda y presionar Enter
        search_box.send_keys(search_text)
        search_box.send_keys(Keys.RETURN)

        # Esperar a que los resultados de búsqueda se carguen
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@role="feed"]')))

        # Localizar el primer post en el feed
        first_post = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '(//div[@role="article"])[1]')))

        # Localizar el botón de reacción
        reaction_button = first_post.find_element(By.XPATH, './/div[@aria-label="Like"]')

        # Usar ActionChains para mantener presionado el botón de reacción
        actions = ActionChains(self.driver)
        actions.move_to_element(reaction_button).click_and_hold().perform()

        # Esperar un momento para que se desplieguen las reacciones
        time.sleep(1)

        # Seleccionar la reacción especificada
        reaction_xpath = f'//div[@aria-label="{reaction_type.capitalize()}"]'
        reaction = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, reaction_xpath)))
        reaction.click()

        # Soltar el botón de reacción
        actions.release().perform()

    def close_browser(self):
        self.driver.quit()

if __name__ == "__main__":
    # Parámetros del script
    driver_path = 'path_to_chromedriver'
    user_email = 'your_email@example.com'
    user_password = 'your_password'
    search_text = 'formula 1'
    reaction_type = 'like'  # Cambia a 'love', 'care', 'haha', 'wow', 'sad', 'angry' según lo necesites

    # Crear una instancia de la clase y ejecutar los métodos
    fb_bot = FacebookReactionBot(driver_path, user_email, user_password)
    fb_bot.login()
    fb_bot.search_and_react(search_text, reaction_type)
    fb_bot.close_browser()
