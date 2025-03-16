from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def init_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-notifications')
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-blink-features=AutomationControlled")

    # Éviter l'erreur WebGL
    options.add_argument("--enable-unsafe-swiftshader")
    options.add_argument("--disable-software-rasterizer")

    # Empêcher la fermeture automatique de Chrome
    options.add_experimental_option("detach", True)

    # Réutiliser le profil Chrome existant
    options.add_argument("--user-data-dir=C:/Users/Abdelmajid/AppData/Local/Google/Chrome/User Data")
    options.add_argument("--profile-directory=Default")

    # Instancier le WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    return driver
