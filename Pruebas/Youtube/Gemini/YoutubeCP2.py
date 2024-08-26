# "Generame un script de selenium en python en clases para este caso de prueba
# ""1. Ingresar a YouTube
# 2. Seleccionar el botón """"Acceder""""
# 3. Escribir un correo registrado.
# 4. Dar clic en siguiente.
# 5. Ingresar contraseña
# 6. De nuevo dar clic en siguiente.
# 7. Seleccionar en la opcion """"ahora no"""" en el cuadro 
# """"Accediste a tu cuenta""""
# 8. Dar clic en """"Perfil"""""""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

class YouTubeLoginAutomation:
    def __init__(self, driver_path, email, password):
        self.driver_path = driver_path
        self.email = email
        self.password = password
        self.driver = None

    def setup_driver(self):
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        service = Service(self.driver_path)
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

    def login_to_youtube(self):
        # Step 1: Ingresar a YouTube
        self.driver.get("https://www.youtube.com")
        time.sleep(2)

        # Step 2: Seleccionar el botón "Acceder"
        sign_in_button = self.driver.find_element(By.XPATH, '//yt-formatted-string[text()="Acceder"]')
        sign_in_button.click()
        time.sleep(2)

        # Step 3: Escribir un correo registrado
        email_input = self.driver.find_element(By.XPATH, '//input[@type="email"]')
        email_input.send_keys(self.email)
        time.sleep(1)

        # Step 4: Dar clic en siguiente
        next_button = self.driver.find_element(By.XPATH, '//span[text()="Siguiente"]')
        next_button.click()
        time.sleep(2)

        # Step 5: Ingresar contraseña
        password_input = self.driver.find_element(By.XPATH, '//input[@type="password"]')
        password_input.send_keys(self.password)
        time.sleep(1)

        # Step 6: De nuevo dar clic en siguiente
        next_button = self.driver.find_element(By.XPATH, '//span[text()="Siguiente"]')
        next_button.click()
        time.sleep(5)

        # Step 7: Seleccionar en la opción "ahora no" en el cuadro "Accediste a tu cuenta"
        try:
            now_not_button = self.driver.find_element(By.XPATH, '//button[text()="Ahora no"]')
            now_not_button.click()
            time.sleep(2)
        except:
            pass  # Si el botón no aparece, continuar sin errores

        # Step 8: Dar clic en "Perfil"
        profile_button = self.driver.find_element(By.XPATH, '//button[@id="avatar-btn"]')
        profile_button.click()
        time.sleep(2)

    def close_driver(self):
        if self.driver:
            self.driver.quit()

if __name__ == "__main__":
    # Configura el path de tu WebDriver (por ejemplo, 'chromedriver.exe')
    DRIVER_PATH = 'path/to/chromedriver'
    
    # Credenciales de usuario
    EMAIL = 'tu_correo@gmail.com'
    PASSWORD = 'tu_contraseña'

    # Crear instancia y ejecutar el caso de prueba
    yt_test = YouTubeLoginAutomation(DRIVER_PATH, EMAIL, PASSWORD)
    yt_test.setup_driver()
    yt_test.login_to_youtube()
    yt_test.close_driver()
