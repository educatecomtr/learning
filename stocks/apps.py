from django.apps import AppConfig


class StocksConfig(AppConfig):
    name = 'stocks'  # proje adı ile aynı olmalıdır

    def ready(self):
        import stocks.signals # sinyallerin çalışmasını sağlar.
