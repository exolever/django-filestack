from django.apps import AppConfig


class FilesConfig(AppConfig):
    name = 'files'

    def ready(self):
        from .signals import setup_signals
        setup_signals()
