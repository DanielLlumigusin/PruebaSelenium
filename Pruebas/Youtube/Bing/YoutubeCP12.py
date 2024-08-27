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

    def search_trailer(self):
        search_box = self.driver.find_element(By.NAME, "search_query")
        search_box.send_keys("trailer")
        search_box.send_keys(Keys.RETURN)
        time.sleep(2)

    def select_first_video(self):
        first_video = self.driver.find_element(By.XPATH, "//a[@id='video-title']")
        first_video.click()
        time.sleep(5)

    def create_clip(self):
        more_options = self.driver.find_element(By.XPATH, "//button[@aria-label='Más opciones']")
        more_options.click()
        time.sleep(1)
        clip_option = self.driver.find_element(By.XPATH, "//yt-formatted-string[text()='Clip']")
        clip_option.click()
        time.sleep(2)
        title_box = self.driver.find_element(By.XPATH, "//input[@id='clip-title']")
        title_box.send_keys("clip de prueba")
        share_clip_button = self.driver.find_element(By.XPATH, "//button[text()='Compartir clip']")
        share_clip_button.click()
        time.sleep(2)

    def copy_and_paste_link(self):
        copy_link_button = self.driver.find_element(By.XPATH, "//button[text()='Copiar enlace']")
        copy_link_button.click()
        time.sleep(1)
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get("https://www.google.com")
        search_box = self.driver.find_element(By.NAME, "q")
        search_box.send_keys(Keys.CONTROL + 'v')
        search_box.send_keys(Keys.RETURN)
        time.sleep(5)

    def run_test(self):
        self.open_youtube()
        self.search_trailer()
        self.select_first_video()
        self.create_clip()
        self.copy_and_paste_link()
        self.driver.quit()

if __name__ == "__main__":
    test = YouTubeTest()
    test.run_test()
