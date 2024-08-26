from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

class FacebookUploader:
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def login(self, email, password):
        self.driver.get("https://www.facebook.com/")
        email_field = self.driver.find_element_by_id("email")
        password_field = self.driver.find_element_by_id("pass")
        login_button = self.driver.find_element_by_name("login")

        email_field.send_keys(email)
        password_field.send_keys(password)
        login_button.click()

    def upload_photo_or_video(self, file_path):
        # Assuming you're already logged in
        self.driver.get("https://www.facebook.com/")
        time.sleep(2)  # Wait for page to load

        # Click on "Photo/Video" button
        photo_video_button = self.driver.find_element_by_xpath("//span[text()='Photo/Video']")
        photo_video_button.click()

        # Click on "Add Photo/Video" button
        add_button = self.driver.find_element_by_xpath("//span[text()='Add Photo/Video']")
        add_button.click()

        # Select the file
        file_input = self.driver.find_element_by_xpath("//input[@type='file']")
        file_input.send_keys(file_path)

        # Click on "Post" button
        post_button = self.driver.find_element_by_xpath("//span[text()='Post']")
        post_button.click()

if __name__ == "__main__":
    fb_uploader = FacebookUploader()
    fb_uploader.login("0996085369", "mk8yjyqkd")
    fb_uploader.upload_photo_or_video("../imagenes/carro.jpg")
