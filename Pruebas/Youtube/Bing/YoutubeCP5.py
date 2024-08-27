from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class YouTubeTest:
    def __init__(self):
        # Inicializar el navegador (asegúrate de tener ChromeDriver en tu PATH o especifica su ubicación)
        self.driver = webdriver.Chrome()

    def run_test(self):
        try:
            # 1. Ingreso a YouTube
            self.driver.get("https://www.youtube.com/")

            # 2. Seleccionar la caja de texto de búsqueda
            search_box = self.driver.find_element_by_name("search_query")

            # 3. Ingresar texto ("Pruebas Selenium")
            search_box.send_keys("Pruebas Selenium")
            search_box.send_keys(Keys.RETURN)  # Presionar Enter

            # Esperar a que carguen los resultados
            time.sleep(3)

            # 4. Buscar un video que contenga la cadena de texto
            video_link = self.driver.find_element_by_css_selector("a#video-title")
            video_link.click()  # Hacer clic en el primer video de la lista

            # Esperar a que cargue el video
            time.sleep(5)

            # 5. Reproducir el video (puedes ajustar esto según tus necesidades)
            video_player = self.driver.find_element_by_css_selector("video.html5-main-video")
            video_player.click()  # Hacer clic en el reproductor de video

            # Esperar a que se reproduzca el video (puedes ajustar esto según tus necesidades)
            time.sleep(10)

            # 6. Dar clic en el botón "Guardar"
            save_button = self.driver.find_element_by_css_selector("button.ytd-menu-renderer")
            save_button.click()

            print("Caso de prueba completado con éxito.")

        except Exception as e:
            print(f"Error: {str(e)}")

        finally:
            # Cerrar el navegador
            self.driver.quit()

if __name__ == "__main__":
    test = YouTubeTest()
    test.run_test()
