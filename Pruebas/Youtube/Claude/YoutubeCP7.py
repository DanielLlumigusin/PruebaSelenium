from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class YouTubeTrendsTest:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open_youtube(self):
        self.driver.get("https://www.youtube.com")

    def navigate_to_trends(self):
        # Esperar a que el botón de "Explorar" sea visible y hacer clic
        explore_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//yt-formatted-string[text()='Explorar']")))
        explore_button.click()

        # Esperar a que aparezca la opción "Tendencias" y hacer clic
        trends_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//yt-formatted-string[text()='Tendencias']")))
        trends_button.click()

    def check_trending_videos(self):
        # Esperar a que los videos en tendencia se carguen
        trending_videos = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//ytd-video-renderer")))

        print(f"Se encontraron {len(trending_videos)} videos en tendencia.")

        # Revisar los primeros 5 videos (o menos si hay menos de 5)
        for i, video in enumerate(trending_videos[:5]):
            title = video.find_element(By.ID, "video-title").text
            views = video.find_element(By.XPATH, ".//ytd-video-meta-block//span[2]").text
            print(f"Video {i+1}: Título: {title}, Vistas: {views}")

        # Hacer scroll para cargar más videos
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        # Esperar a que se carguen más videos
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//ytd-video-renderer[position() > 5]")))

        print("Se han cargado más videos después del scroll.")

def main():
    driver = webdriver.Chrome()  # Asegúrate de tener el ChromeDriver instalado y en el PATH
    driver.maximize_window()  # Maximizar la ventana para asegurar que todos los elementos sean visibles
    youtube_test = YouTubeTrendsTest(driver)

    try:
        youtube_test.open_youtube()
        youtube_test.navigate_to_trends()
        youtube_test.check_trending_videos()
        
        print("Prueba completada con éxito")
    except Exception as e:
        print(f"Error durante la prueba: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()