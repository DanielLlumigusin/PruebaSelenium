from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class YouTubeBot:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='/path/to/chromedriver')  # Cambia la ruta al ejecutable de ChromeDriver

    def search_and_play_video(self, search_query, comment_text):
        self.driver.get("https://www.youtube.com")
        search_box = self.driver.find_element(By.NAME, "search_query")
        search_box.send_keys(search_query)
        search_box.send_keys(Keys.RETURN)

        # Espera hasta que aparezcan los resultados de búsqueda
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "video-title")))

        # Haz clic en el primer video de la lista
        first_video = self.driver.find_element(By.ID, "video-title")
        first_video.click()

        # Espera a que el video se cargue y luego reproduce
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "ytp-time-duration")))
        play_button = self.driver.find_element(By.CLASS_NAME, "ytp-play-button")
        play_button.click()

        # Ingresa el comentario
        comment_input = self.driver.find_element(By.ID, "contenteditable-root")
        comment_input.send_keys(comment_text)
        comment_input.send_keys(Keys.RETURN)

    def close(self):
        self.driver.quit()

# Uso del bot
if __name__ == "__main__":
    bot = YouTubeBot()
    bot.search_and_play_video("Pruebas Selenium", "Comentario desde Selenium")
    bot.close()
