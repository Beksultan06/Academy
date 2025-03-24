from django.apps import AppConfig


class MainpageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app.mainpage'
    verbose_name = 'Главная страница'
    
    def ready(self):
        import app.mainpage.translation