from django.apps import AppConfig


class StocksConfig(AppConfig):
    name = 'stocks'  # proje adı ile aynı olmalıdır

    def ready(self):
        import stocks.templatetags.tags
        import stocks.signals.user_management

