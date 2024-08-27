from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class YouTubeBot:
    def __init__(self, search_term, comment):
        self.driver = webdriver.Chrome()  # Puedes cambiar Chrome por Firefox, Edge, etc.
        self.search_term = search_term
        self.comment = comment

    def search_and_play(self):
        self.driver.get("https://www.youtube.com/")

        # Encuentra la barra de búsqueda y escribe el término
        search_bar = self.driver.find_element(By.ID, "search")
        search_bar.send_keys(self.search_term)
        search_bar.send_keys(Keys.ENTER)

        # Encuentra el primer video y hace clic
        first_video = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "video-title"))
        )
        first_video.click()

        # Espera a que el video se cargue
        video = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.TAG_NAME, "video"))
        )
        video.click()  # Hace clic en el video para reproducirlo

    def add_comment(self):
        # Encuentra el campo de comentarios y escribe el comentario
        comment_box = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "contenteditable-root"))
        )
        comment_box.send_keys(self.comment)

        # Encuentra el botón de enviar comentario y hace clic
        send_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "submit-button"))
        )
        send_button.click()

    def close_browser(self):
        self.driver.quit()

# Reemplaza con tu término de búsqueda y el comentario
search_term = "Pruebas Selenium"
comment = "Comentario desde Selenium"

# Crea una instancia de la clase y ejecuta las acciones
bot = YouTubeBot(search_term, comment)
bot.search_and_play()
bot.add_comment()
bot.close_browser()