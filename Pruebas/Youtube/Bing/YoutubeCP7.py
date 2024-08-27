from selenium import webdriver
import time

class YouTubeTrendsTest:
    def __init__(self):
        # Inicializar el navegador (asegúrate de tener ChromeDriver en tu PATH o especifica su ubicación)
        self.driver = webdriver.Chrome()

    def run_test(self):
        try:
            # 1. Ingreso a YouTube
            self.driver.get("https://www.youtube.com/")

            # 2. En la sección "Explorar" del menú lateral, seleccionar "Tendencias"
            explore_button = self.driver.find_element_by_xpath("//a[contains(@href, '/feed/explore')]")
            explore_button.click()
            time.sleep(2)  # Esperar a que cargue la página de Tendencias

            # 3. Revisar el despliegue de los videos en tendencia
            trending_videos = self.driver.find_elements_by_css_selector("a#video-title")
            for video in trending_videos:
                print(f"Video en tendencia: {video.text}")

            print("Caso de prueba completado con éxito.")

        except Exception as e:
            print(f"Error: {str(e)}")

        finally:
            # Cerrar el navegador
            self.driver.quit()

if __name__ == "__main__":
    test = YouTubeTrendsTest()
    test.run_test()
