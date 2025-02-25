from django.apps import AppConfig

class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        # Importe les signaux pour qu'ils soient enregistrés
        import users.signals