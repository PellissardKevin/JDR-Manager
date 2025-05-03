from django.apps import AppConfig


class Jdr_ManagerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'jdr_manager'
    
    def ready(self):
        import jdr_manager.signals
