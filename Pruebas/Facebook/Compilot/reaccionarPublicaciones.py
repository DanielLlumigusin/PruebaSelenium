from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Configura la ubicación del ChromeDriver
driver_path = 'ruta/al/chromedriver'
driver = webdriver.Chrome(driver_path)

# Abre Facebook e inicia sesión
driver.get('https://www.facebook.com/')
time.sleep(2)

# Encuentra y completa los campos de inicio de sesión
email_input = driver.find_element(By.ID, 'email')
password_input = driver.find_element(By.ID, 'pass')
login_button = driver.find_element(By.NAME, 'login')

email_input.send_keys('tu_correo@ejemplo.com')
password_input.send_keys('tu_contraseña')
login_button.click()

time.sleep(5)  # Espera a que la página cargue completamente

# Navega a la publicación específica (puedes ajustar el XPATH según sea necesario)
post = driver.find_element(By.XPATH, "//div[contains(text(), 'Texto de la publicación')]")
post.click()

time.sleep(2)

# Encuentra el botón de "Me gusta" y mantén presionado para ver otras reacciones
like_button = driver.find_element(By.XPATH, "//div[@aria-label='Me gusta']")
webdriver.ActionChains(driver).move_to_element(like_button).perform()

time.sleep(2)

# Selecciona la reacción deseada (por ejemplo, "Me encanta")
love_reaction = driver.find_element(By.XPATH, "//div[@aria-label='Me encanta']")
love_reaction.click()

time.sleep(2)

# Cierra el navegador
driver.quit()
