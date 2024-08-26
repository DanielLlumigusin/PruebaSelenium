from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import os

class FacebookPostPhoto:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def login_to_facebook(self, email, password):
        self.driver.get("https://www.facebook.com")
        email_field = self.wait.until(EC.presence_of_element_located((By.ID, "email")))
        email_field.send_keys(email)
        password_field = self.driver.find_element(By.ID, "pass")
        password_field.send_keys(password)
        login_button = self.driver.find_element(By.NAME, "login")
        login_button.click()

    def click_photo_video_button(self):
        photo_video_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Photo/video']")))
        photo_video_button.click()

    def click_add_photo_button(self):
        add_photo_button = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
        return add_photo_button

    def select_photo(self, file_path):
        add_photo_button = self.click_add_photo_button()
        add_photo_button.send_keys(file_path)

    def click_post_button(self):
        post_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Publicar']")))
        post_button.click()

def main():
    driver = webdriver.Chrome()  # Asegúrate de tener el ChromeDriver instalado y en el PATH
    fb_post = FacebookPostPhoto(driver)

    try:
        fb_post.login_to_facebook("0996085369", "mk8yjyqkd")
        fb_post.click_photo_video_button()
        
        # Asegúrate de reemplazar 'ruta/a/tu/foto.jpg' con la ruta real de tu foto
        file_path = os.path.abspath('../imagenes/carro.jpg')
        fb_post.select_photo(file_path)
        
        fb_post.click_post_button()
        
        print("Foto publicada exitosamente")
    except Exception as e:
        print(f"Error durante la publicación de la foto: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()