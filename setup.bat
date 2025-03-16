@echo off
echo 🚀 Création de l'environnement virtuel...
python -m venv venv
call venv\Scripts\activate

echo 🔄 Installation des dépendances...
pip install --upgrade pip
pip install selenium webdriver-manager pandas pyperclip

echo ✅ Environnement prêt ! Exécutez `python main.py` pour démarrer.
