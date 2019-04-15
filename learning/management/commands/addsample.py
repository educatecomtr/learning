from django.core.management.base import BaseCommand
from learning.models import UserDetail, Product, Category
from django.contrib.auth.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Command Çalıştı')
