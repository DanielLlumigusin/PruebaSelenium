from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class YouTubePlaylistTest:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open_youtube(self):
        self.driver.get("https://www.youtube.com")

    def search_playlists(self, search_term):
        search_box = self.wait.until(EC.presence_of_element_located((By.NAME, "search_query")))
        search_box.clear()
        search_box.send_keys(search_term)
        search_box.send_keys(Keys.RETURN)

    def select_first_playlist(self):
        first_playlist = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "ytd-playlist-renderer")))
        first_playlist.click()

    def click_three_dots(self):
        three_dots = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "yt-icon-button.ytd-playlist-header-renderer")))
        three_dots.click()

    def save_playlist(self):
        save_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//yt-formatted-string[contains(text(), 'Guardar lista de reproducción')]")))
        save_button.click()

    def reload_page(self):
        self.driver.refresh()

    def click_logo(self):
        logo = self.wait.until(EC.element_to_be_clickable((By.ID, "logo")))
        logo.click()

    def open_playlists_section(self):
        playlists_section = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//yt-formatted-string[text()='Listas de reproducción']")))
        playlists_section.click()

    def click_saved_playlist(self):
        saved_playlist = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "ytd-playlist-renderer")))
        saved_playlist.click()

def main():
    driver = webdriver.Chrome()  # Asegúrate de tener el ChromeDriver instalado y en el PATH
    youtube_test = YouTubePlaylistTest(driver)

    try:
        youtube_test.open_youtube()
        youtube_test.search_playlists("Listas de reproducción")
        youtube_test.select_first_playlist()
        youtube_test.click_three_dots()
        youtube_test.save_playlist()
        
        # Opción 1: Recargar la página
        youtube_test.reload_page()
        
        # Opción 2: Hacer clic en el logo (descomenta si prefieres esta opción)
        # youtube_test.click_logo()
        
        youtube_test.open_playlists_section()
        youtube_test.click_saved_playlist()
        
        print("Prueba completada con éxito")
        
        # Esperamos un poco para ver el resultado
        time.sleep(5)
    except Exception as e:
        print(f"Error durante la prueba: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()