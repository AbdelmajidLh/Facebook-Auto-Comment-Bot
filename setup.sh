#!/bin/bash
echo "🚀 Création de l'environnement virtuel..."
python3 -m venv venv
source venv/bin/activate

echo "🔄 Installation des dépendances..."
pip install --upgrade pip
pip install selenium webdriver-manager pandas pyperclip

echo "✅ Environnement prêt ! Exécutez 'python main.py' pour démarrer."
