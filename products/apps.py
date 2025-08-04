from django.apps import AppConfig


class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'


    def ready(self):
        import products.signals  # yoo line add garnu parxa sabai ko apps.py ma