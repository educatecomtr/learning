from django.apps import AppConfig


class StocksConfig(AppConfig):
    name = 'stocks'  # must be the same with your project name

    def ready(self):
        import stocks.signals
