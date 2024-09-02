from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configura la ruta del ChromeDriver
chrome_driver_path = "/path/to/chromedriver"  # Cambia esta ruta a la de tu ChromeDriver
service = Service(chrome_driver_path)

# Inicializa el navegador
driver = webdriver.Chrome(service=service)

# Abre Facebook
driver.get("https://www.facebook.com")

# Espera a que el campo de email esté presente e ingresa tus credenciales
email_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "email"))
)
email_field.send_keys("tu_correo@example.com")  # Cambia esto por tu correo

# Ingresa la contraseña
password_field = driver.find_element(By.ID, "pass")
password_field.send_keys("tu_contraseña")  # Cambia esto por tu contraseña
password_field.send_keys(Keys.RETURN)

# Espera a que la página cargue
time.sleep(5)

# Busca la primera publicación en el feed
first_post = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "(//div[@aria-label='Me gusta'])[1]"))
)

# Coloca el cursor sobre el botón de "Me gusta" para que se desplieguen las reacciones
webdriver.ActionChains(driver).move_to_element(first_post).perform()

# Espera a que se desplieguen las opciones de reacción
time.sleep(2)

# Selecciona la reacción deseada (por ejemplo, "Me gusta", "Me encanta", etc.)
# Puedes cambiar el número al final para elegir diferentes reacciones
reaction_button = driver.find_element(By.XPATH, "(//div[@aria-label='Me gusta'])[1]")
reaction_button.click()

# Espera un poco para asegurarse de que la reacción se registre
time.sleep(3)

# Cierra el navegador
driver.quit()
