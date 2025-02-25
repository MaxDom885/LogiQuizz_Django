# Logi'Quizz

Logi'Quizz est une application web de jeu de devinettes développée avec Django. Les utilisateurs peuvent s'inscrire, se connecter, choisir des catégories de devinettes, jouer, demander des indices, et consulter un tableau des scores.

## Fonctionnalités

- Inscription et connexion des utilisateurs
- Choix de catégories de devinettes
- Jeu de devinettes avec possibilité de demander des indices
- Tableau des scores
- Profil utilisateur avec photo de profil

## Prérequis

- Python 3.12.3
- Django 5.0.6

## Installation

1. Clonez le dépôt :
    ```sh
    git clone https://github.com/votre-utilisateur/logiquizz.git
    cd logiquizz
    ```

2. Créez et activez un environnement virtuel :
    ```sh
    python -m venv env
    source env/bin/activate  # Sur Windows, utilisez `env\Scripts\activate`
    ```

3. Installez les dépendances :
    ```sh
    pip install -r requirements.txt
    ```

4. Appliquez les migrations :
    ```sh
    python manage.py migrate
    ```

5. Créez un superutilisateur pour accéder à l'interface d'administration :
    ```sh
    python manage.py createsuperuser
    ```

6. Lancez le serveur de développement :
    ```sh
    python manage.py runserver
    ```

7. Accédez à l'application dans votre navigateur à l'adresse `http://127.0.0.1:8000`.



