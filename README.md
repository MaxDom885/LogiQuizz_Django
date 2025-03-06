# Logi'Quizz

Logi'Quizz is a web application for a guessing game developed with Django. Users can register, log in, choose categories of riddles, play, ask for clues, and view a scoreboard.

## Features

- User registration and login
- Choice of riddle categories
- Riddle game with the option to ask for clues
- Scoreboard
- User profile with profile photo

## Prerequisites

- Python 3.12.3
- Django 5.0.6

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/logiquizz.git
    cd logiquizz
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Apply the migrations:
    ```sh
    python manage.py migrate
    ```

5. Create a superuser to access the admin interface:
    ```sh
    python manage.py createsuperuser
    ```

6. Start the development server:
    ```sh
    python manage.py runserver
    ```

7. Access the application in your browser at `http://127.0.0.1:8000`.
