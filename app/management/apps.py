from django.apps import AppConfig


class ManagementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app.management'

    def ready(self):
        import app.management.translation  # Импортируйте файл перевода