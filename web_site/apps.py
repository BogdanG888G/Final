from django.apps import AppConfig


class WebSiteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'web_site'

    def ready(self):
        import web_site.signals