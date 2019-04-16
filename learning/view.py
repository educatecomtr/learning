from django.contrib.auth.models import User
from learning.models import Product


product = Product.objects.first()

print(product.author.name)