from selenium import webdriver
from selenium.webdriver.common.by import By
# ... (resto de las importaciones)

# ... (código para iniciar el navegador y loguearse)

# Encontrar la publicación a la que quieres reaccionar
# (el XPath puede variar según la estructura de la publicación)
post = driver.find_element(By.XPATH, "//div[contains(@data-testid, 'post_message')]")

# Encontrar el botón de reacción (por ejemplo, "Me gusta")
like_button = post.find_element(By.XPATH, ".//a[contains(@aria-label, 'Me gusta')]")
like_button.click()