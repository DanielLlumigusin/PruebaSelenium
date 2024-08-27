from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class YouTubeAutomationTest:
    def __init__(self, comment_text):
        self.driver = webdriver.Chrome()
        self.comment_text = comment_text

    def login_to_youtube(self):
        driver = self.driver

        # Ingresar a YouTube
        driver.get("https://www.youtube.com")
        time.sleep(3)

    def search_video(self, search_query):
        driver = self.driver

        # Seleccionar la caja de texto de buscar
        search_box = driver.find_element(By.NAME, "search_query")
        search_box.click()
        time.sleep(1)

        # Ingresar el texto a buscar y dar Enter
        search_box.send_keys(search_query)
        search_box.send_keys(Keys.ENTER)
        time.sleep(3)

    def play_video(self):
        driver = self.driver

        # Buscar el primer video que contiene la cadena de texto y dar clic
        video = driver.find_element(By.XPATH, "//a[@id='video-title']")
        video.click()
        time.sleep(5)

    def comment_on_video(self):
        driver = self.driver

        # Hacer scroll hacia abajo para que aparezca la caja de comentarios
        driver.execute_script("window.scrollTo(0, 600);")
        time.sleep(3)

        # Seleccionar la caja de comentarios
        comment_box = driver.find_element(By.XPATH, "//ytd-commentbox[@id='placeholder-area']")
        comment_box.click()
        time.sleep(2)

        # Ingresar el texto del comentario
        comment_area = driver.find_element(By.XPATH, "//yt-formatted-string[@id='contenteditable-root']")
        comment_area.send_keys(self.comment_text)
        time.sleep(2)

        # Publicar el comentario
        post_button = driver.find_element(By.XPATH, "//yt-button-renderer[@id='submit-button']")
        post_button.click()
        time.sleep(3)

    def run_test(self, search_query):
        try:
            self.login_to_youtube()
            self.search_video(search_query)
            self.play_video()
            self.comment_on_video()
        finally:
            # Cerrar el navegador al finalizar
            self.driver.quit()

if __name__ == "__main__":
    # Texto del comentario
    comment_text = "Comentario desde Selenium"
    search_query = "Pruebas Selenium"

    # Ejecutar el test de YouTube
    youtube_test = YouTubeAutomationTest(comment_text)
    youtube_test.run_test(search_query)
