
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class YouTubeUploadTest:
    def __init__(self):
        # Inicializar el navegador (asegúrate de tener ChromeDriver en tu PATH o especifica su ubicación)
        self.driver = webdriver.Chrome()

    def run_test(self):
        try:
            # 1. Ingreso a YouTube
            self.driver.get("https://www.youtube.com/")

            # 2. Seleccionar el icono de la cámara para crear un video
            camera_icon = self.driver.find_element_by_css_selector("yt-icon.style-scope.ytd-topbar-menu-button-renderer")
            camera_icon.click()

            # 3. Seleccionar "Subir un video"
            upload_button = self.driver.find_element_by_xpath("//span[contains(text(), 'Subir un video')]")
            upload_button.click()

            # 4. En caso de ser la primera vez, seleccionar "Crear canal"
            create_channel_button = self.driver.find_element_by_xpath("//span[contains(text(), 'Crear canal')]")
            create_channel_button.click()

            # 5. Dar clic en "Crear"
            create_button = self.driver.find_element_by_xpath("//span[contains(text(), 'Crear')]")
            create_button.click()

            # 6. Dar clic en "Seleccionar video"
            select_video_button = self.driver.find_element_by_xpath("//span[contains(text(), 'Seleccionar video')]")
            select_video_button.click()

            # 7. Subir el video desde el explorador de archivos (simulado aquí)
            # (Puedes ajustar esto según tus necesidades)

            # 8. En detalles, sección "Audiencia", seleccionar que el video está creado para niños
            kids_audience_checkbox = self.driver.find_element_by_css_selector("input#radioLabel1")
            kids_audience_checkbox.click()

            # 9. Dar clic en "Siguiente"
            next_button = self.driver.find_element_by_xpath("//span[contains(text(), 'Siguiente')]")
            next_button.click()

            # 10. En "Elementos del video", dar clic en "Siguiente"
            next_button.click()

            # 11. En "Comprobaciones", dar clic en "Siguiente"
            next_button.click()

            # 12. En "Visibilidad", seleccionar la opción "Oculto"
            visibility_dropdown = self.driver.find_element_by_css_selector("yt-dropdown-menu.style-scope.ytd-metadata-settings")
            visibility_dropdown.click()
            hidden_option = self.driver.find_element_by_xpath("//yt-formatted-string[contains(text(), 'Oculto')]")
            hidden_option.click()

            # 13. Dar clic en "Guardar"
            save_button = self.driver.find_element_by_xpath("//span[contains(text(), 'Guardar')]")
            save_button.click()

            # 14. Dar clic en "Continuar"
            continue_button = self.driver.find_element_by_xpath("//span[contains(text(), 'Continuar')]")
            continue_button.click()

            # 15. Dar clic en el video creado (puedes ajustar esto según tus necesidades)

            print("Caso de prueba completado con éxito.")

        except Exception as e:
            print(f"Error: {str(e)}")

        finally:
            # Cerrar el navegador
            self.driver.quit()

if __name__ == "__main__":
    test = YouTubeUploadTest()
    test.run_test()
