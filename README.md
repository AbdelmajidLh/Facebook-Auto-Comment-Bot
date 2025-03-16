# Facebook Auto Comment Bot

## 📌 Description
Ce projet est un bot automatique en Python utilisant **Selenium** pour commenter des publications Facebook. Il peut être utilisé pour automatiser des commentaires sur des posts spécifiques en utilisant un fichier CSV contenant des liens de publications.

## 🛠️ Installation

### 1️⃣ **Cloner le projet**
```bash
git clone https://github.com/votre-repo/FB_autoComm.git
cd FB_autoComm
```

### 2️⃣ **Créer et activer un environnement virtuel**
```bash
python -m venv venv
source venv/bin/activate  # MacOS/Linux
venv\Scripts\activate    # Windows
```

### 3️⃣ **Installer les dépendances**
```bash
pip install -r requirements.txt
```

### 4️⃣ **Installer et configurer ChromeDriver**
Vérifie la version de **Google Chrome** installée :
```bash
chrome --version
```
Télécharge la version correspondante de **ChromeDriver** [ici](https://sites.google.com/chromium.org/driver/downloads).
Ensuite, place le fichier **chromedriver.exe** dans ce dossier :
```
C:/Program Files/Google/Chrome/Application/chromedriver-win64/
```
Ajoute ce chemin aux variables d’environnement pour qu’il soit accessible globalement.

### 5️⃣ **Configurer le fichier `config.ini`**
Dans le fichier `config.ini`, renseigne tes informations Facebook et paramètres du bot :
```ini
[facebook]
email = votremail@exemple.com
password = votremotdepasse

[settings]
input_file = groups_pages.csv
message = "Ceci est un commentaire automatique !"
comment_delay = 10
```

---

## 🚀 Utilisation

### 1️⃣ **Lancer le bot**
```bash
python main.py
```
### 2️⃣ **Format du fichier CSV** (`groups_pages.csv`)
Le fichier doit contenir une colonne `url` avec les liens des posts à commenter :
```csv
url
https://www.facebook.com/elhou.abdelmajid/posts/123456789
https://www.facebook.com/somegroup/posts/987654321
```

---

## 🔧 Dépannage

### 1️⃣ **ChromeDriver ne se lance pas ou plante ?**
- Vérifie que **Google Chrome** est bien installé et à jour.
- Vérifie que **ChromeDriver** est de la **même version** que ton Google Chrome.
- Essaie de le lancer manuellement pour voir s’il fonctionne :
  ```bash
  chromedriver --port=9515
  ```

### 2️⃣ **Le bot ne trouve pas la boîte de commentaire ?**
- Facebook met souvent à jour son HTML, donc il faut parfois adapter les **XPATH**.
- Vérifie avec **l’outil d’inspection** (`F12` → `Inspecter` → Chercher la boîte de commentaire).
- Mets à jour le fichier `fb_comment.py` avec les nouvelles classes CSS.

### 3️⃣ **Erreur `SessionNotCreatedException: DevToolsActivePort file doesn't exist`**
Ajoute ces options dans `selenium_driver.py` pour éviter les erreurs de session :
```python
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
```

---

## 🏆 Améliorations possibles
- ✅ Ajout d’un mode **headless** pour exécuter le bot sans afficher Chrome.
- ✅ Détection intelligente des erreurs et relance automatique.
- ✅ Ajout d’un mode **proxy** pour éviter les blocages Facebook.
- ✅ Génération de logs pour suivre les actions du bot.


## 📜 Licence
Ce projet est sous licence **MIT** - Vous pouvez le modifier et l’utiliser librement.


## 💡 Remerciements
Merci aux développeurs de Selenium et WebDriver Manager ! 🚀



🎯 **Profite bien du bot et bon automatisation !** 😊

