from django.core.management.base import BaseCommand
from learning.models import UserDetail, Product, Category
from django.contrib.auth.models import User


class Command(BaseCommand):

    def handle(self, *args, **kwargs):


        User.objects.bulk_create([
            User(id=1, username='admin'),
            User(id=2, username='user1'),
            User(id=3, username='user2'),
            User(id=4, username='user3'),
            User(id=5, username='user4')
        ])

        UserDetail.objects.bulk_create([
            UserDetail(user_id=1, address='address 1'),
            UserDetail(user_id=2, address='address 2'),
            UserDetail(user_id=3, address='address 3'),
            UserDetail(user_id=4, address='address 4'),
            UserDetail(user_id=5, address='address 5')
        ])

        Product.objects.bulk_create([
            Product(id=1, name='Tencere', author_id=2, slug='tencere'),
            Product(id=2, name='Çatal', author_id=2, slug='catal'),
            Product(id=3, name='Bıçak', author_id=2, slug='bicak'),
            Product(id=4, name='Kaşık', author_id=2, slug='kasik'),
            Product(id=5, name='Yatak', author_id=2, slug='yatak'),
            Product(id=6, name='Koltuk', author_id=3, slug='koltuk'),
            Product(id=7, name='Masa', author_id=3, slug='masa'),
        ])

        Category.objects.bulk_create([
            Category(id=1, name='Mutfak'),
            Category(id=2, name='Yatak Odası'),
            Category(id=3, name='Oturma Odası'),
            Category(id=4, name='Mobilyalar')
        ])

