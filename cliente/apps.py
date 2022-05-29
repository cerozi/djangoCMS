from django.apps import AppConfig


class ClienteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cliente'

    def ready(self):
        from . import creating_groups

        creating_groups.group_create()
        return super().ready()
