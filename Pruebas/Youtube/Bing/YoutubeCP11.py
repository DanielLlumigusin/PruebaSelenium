from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

class YouTubeTest:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    def open_youtube(self):
        self.driver.get("https://www.youtube.com")
        time.sleep(2)

    def search_playlist(self, search_text):
        search_box = self.driver.find_element(By.NAME, "search_query")
        search_box.send_keys(search_text)
        search_box.send_keys(Keys.RETURN)
        time.sleep(2)

    def select_first_playlist(self):
        first_playlist = self.driver.find_element(By.XPATH, "//a[@id='video-title']")
        first_playlist.click()
        time.sleep(5)

    def save_playlist(self):
        more_options = self.driver.find_element(By.XPATH, "//button[@aria-label='Más opciones']")
        more_options.click()
        time.sleep(1)
        save_button = self.driver.find_element(By.XPATH, "//yt-formatted-string[text()='Guardar lista de reproducción en la biblioteca']")
        save_button.click()
        time.sleep(2)

    def reload_page(self):
        self.driver.find_element(By.XPATH, "//yt-icon[@id='logo-icon']").click()
        time.sleep(2)

    def open_playlists_section(self):
        playlists_section = self.driver.find_element(By.XPATH, "//yt-formatted-string[text()='Listas de reproducción']")
        playlists_section.click()
        time.sleep(2)

    def open_saved_playlist(self):
        saved_playlist = self.driver.find_element(By.XPATH, "//a[@title='Listas de reproducción guardadas']")
        saved_playlist.click()
        time.sleep(2)

    def run_test(self):
        self.open_youtube()
        self.search_playlist("Listas de reproducción")
        self.select_first_playlist()
        self.save_playlist()
        self.reload_page()
        self.open_playlists_section()
        self.open_saved_playlist()
        self.driver.quit()

if __name__ == "__main__":
    test = YouTubeTest()
    test.run_test()
