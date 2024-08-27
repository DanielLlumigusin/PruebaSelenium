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

    def search_video(self, search_text):
        search_box = self.driver.find_element(By.NAME, "search_query")
        search_box.send_keys(search_text)
        search_box.send_keys(Keys.RETURN)
        time.sleep(2)

    def play_video(self):
        video = self.driver.find_element(By.XPATH, "//a[@id='video-title' and contains(@title, 'Pruebas Selenium')]")
        video.click()
        time.sleep(5)

    def subscribe_channel(self):
        subscribe_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Suscribirme')]")
        subscribe_button.click()
        time.sleep(2)

    def run_test(self):
        self.open_youtube()
        self.search_video("Pruebas Selenium")
        self.play_video()
        self.subscribe_channel()
        self.driver.quit()

if __name__ == "__main__":
    test = YouTubeTest()
    test.run_test()
