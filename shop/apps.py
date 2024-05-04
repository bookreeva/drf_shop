from django.apps import AppConfig


class ShopConfig(AppConfig):
    """ Конфигурационные данные приложения. """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shop'
    verbose_name = 'Магазин'
