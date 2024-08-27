from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class YouTubeTrendingTest:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def open_youtube(self):
        driver = self.driver

        # Ingresar a YouTube
        driver.get("https://www.youtube.com")
        time.sleep(3)

    def select_trending(self):
        driver = self.driver

        # Buscar el botón de "Explorar" en el menú lateral
        try:
            explore_button = driver.find_element(By.XPATH, "//tp-yt-paper-item[@title='Explore']")
            explore_button.click()
            time.sleep(3)

            # Seleccionar la opción de "Tendencias"
            trending_button = driver.find_element(By.XPATH, "//yt-formatted-string[text()='Trending']")
            trending_button.click()
            time.sleep(5)
        except Exception as e:
            print(f"Error al seleccionar 'Tendencias': {str(e)}")

    def verify_trending_videos(self):
        driver = self.driver

        # Verificar que los videos en tendencia se desplieguen correctamente
        try:
            trending_videos = driver.find_elements(By.XPATH, "//ytd-video-renderer")
            if len(trending_videos) > 0:
                print(f"Se encontraron {len(trending_videos)} videos en tendencia.")
            else:
                print("No se encontraron videos en la sección de 'Tendencias'.")
        except Exception as e:
            print(f"Error al verificar los videos en tendencia: {str(e)}")

    def run_test(self):
        try:
            self.open_youtube()
            self.select_trending()
            self.verify_trending_videos()
        finally:
            # Cerrar el navegador al finalizar
            self.driver.quit()

if __name__ == "__main__":
    # Ejecutar el test de YouTube Tendencias
    youtube_test = YouTubeTrendingTest()
    youtube_test.run_test()
