# facebook_bot.py
import pandas as pd
from utils.config_loader import load_config
from utils.selenium_driver import init_driver
from utils.fb_login import login_facebook
from utils.fb_comment import comment_posts

class FacebookAutoComment:
    def __init__(self, config_file):
        self.config = load_config(config_file)
        self.driver = init_driver()
        self.email = self.config['facebook']['email']
        self.password = self.config['facebook']['password']
        self.input_file = self.config['settings']['input_file']
        self.message = self.config['settings']['message']
        self.comment_delay = int(self.config['settings']['comment_delay'])

    def run(self):
        df = pd.read_csv(self.input_file)
        login_facebook(self.driver, self.email, self.password)
        
        for _, row in df.iterrows():
            comment_posts(self.driver, row["url"], self.message, self.comment_delay)
        
        input("🔴 Appuyez sur 'Entrée' pour fermer le navigateur...")
        self.driver.quit()
        print("✅ Automatisation terminée avec succès !")