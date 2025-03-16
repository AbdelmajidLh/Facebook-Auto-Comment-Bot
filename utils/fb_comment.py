import time
import pyperclip
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def comment_posts(driver, url, message, delay):
    print(f"🔄 Accès au post : {url}")
    driver.get(url)
    time.sleep(5)  # Attendre le chargement de la page

    try:
        # Liste des XPATHs possibles pour la boîte de commentaire
        possible_xpaths = [
            "//div[@role='textbox']",  # Champ de commentaire standard
            "//div[contains(@class, 'x1i10hfl')]",  # Nouveau champ détecté
            "//div[contains(@class, 'notranslate')]",  # Ancienne classe utilisée par Facebook
        ]

        comment_box = None
        for xpath in possible_xpaths:
            try:
                comment_box = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, xpath))
                )
                print("✅ Champ de commentaire détecté !")
                break  # Dès qu'on trouve un élément, on arrête
            except:
                continue

        if not comment_box:
            print("⚠️ Aucun champ de commentaire détecté après plusieurs essais. Vérifie l'URL.")
            return

        # Essayer de poster un commentaire
        try:
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'})", comment_box)
            time.sleep(2)
            comment_box.click()

            pyperclip.copy(message)
            actions = ActionChains(driver)
            actions.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).send_keys(Keys.ENTER)
            actions.perform()

            print(f"✅ Commentaire posté sur {url} : {message}")
            time.sleep(delay)

        except Exception as e:
            print(f"⚠️ Erreur en postant le commentaire sur {url} : {e}")

    except Exception as e:
        print(f"⚠️ Erreur en accédant au post {url} : {e}")
