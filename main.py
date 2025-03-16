# main.py
from facebook_bot import FacebookAutoComment

def main():
    bot = FacebookAutoComment("config.ini")
    bot.run()
    input("🔴 Appuyez sur 'Entrée' pour fermer le navigateur...")

if __name__ == "__main__":
    main()