import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login_facebook(driver, email, password):
    driver.get("https://www.facebook.com")

    # Vérifier si on est déjà connecté en cherchant le bouton du profil utilisateur
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@href, 'profile.php')]"))
        )
        print("✅ Déjà connecté à Facebook !")
        return  # On quitte la fonction
    except:
        print("🔄 Connexion nécessaire, tentative d'authentification...")

    # Remplir le formulaire de connexion si nécessaire
    try:
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        email_input.send_keys(email)

        password_input = driver.find_element(By.NAME, "pass")
        password_input.send_keys(password)

        login_button = driver.find_element(By.NAME, "login")
        login_button.click()

        print("✅ Connexion en cours...")

        # Vérifier si la connexion a réussi
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@href, 'profile.php')]"))
        )
        print("✅ Connecté à Facebook !")

    except Exception as e:
        print(f"⚠️ Erreur de connexion : {e}")
