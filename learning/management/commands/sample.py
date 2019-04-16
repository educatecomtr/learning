from django.core.management.base import BaseCommand

class Command(BaseCommand):

    help = 'Komut hakkında yardım bilgisi'

    def add_arguments(self, parser):
        # Zorunlu argüman
        parser.add_argument('user_id', type=int, help='user_id yardım bilgisi')
        parser.add_argument('product_id', type=int, help='product_id yardım bilgisi')

        # İsteğe Başlı Argüman
        parser.add_argument('--prefix', type=str, help='prefix yardım bilgisi')
        parser.add_argument('--admin', action='store_true', help='admin yardım bilgisi')
        parser.add_argument('-u', '--users', nargs='+', type=int, help='users yardım bilgisi')

    def handle(self, *args, **kwargs):

        user_id = kwargs['user_id']
        product_id = kwargs['product_id']
        prefix = kwargs['prefix']
        admin = kwargs['admin']
        users = kwargs['users']

        print('Positional user_id : ' + str(user_id))
        print('Positional product_id : ' + str(product_id))

        if prefix:
            print('Optional prefix : ' + prefix)

        if admin:
            print('Optional admin selected')

        if users:
            print('Optional list : ' + str(users))
