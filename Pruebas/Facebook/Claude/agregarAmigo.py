from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FacebookFriendRequest:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open_facebook(self):
        self.driver.get("https://www.facebook.com/")

    def click_search_bar(self):
        search_bar = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[placeholder='Busca en Facebook']")))
        search_bar.click()

    def enter_friend_name(self, friend_name):
        search_input = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='search']")))
        search_input.send_keys(friend_name)

    def perform_search(self):
        search_input = self.driver.find_element(By.CSS_SELECTOR, "input[type='search']")
        search_input.send_keys(Keys.RETURN)

    def click_friend_profile(self):
        friend_profile = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[role='article'] a[role='link']")))
        friend_profile.click()

    def click_add_friend(self):
        add_friend_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[aria-label='Agregar a amigos']")))
        add_friend_button.click()

def main():
    driver = webdriver.Chrome()  # Asegúrate de tener el ChromeDriver instalado y en el PATH
    fb_friend_request = FacebookFriendRequest(driver)

    try:
        fb_friend_request.open_facebook()
        fb_friend_request.click_search_bar()
        fb_friend_request.enter_friend_name("Alejandro Daniel")
        fb_friend_request.perform_search()
        fb_friend_request.click_friend_profile()
        fb_friend_request.click_add_friend()
    finally:
        driver.quit()

if __name__ == "__main__":
    main()