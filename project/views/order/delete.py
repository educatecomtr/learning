from django.views import View
from django.shortcuts import redirect
from project.feeds import Cart
from project.models import Product
from django.contrib import messages


# Sipariş silme
class OrderDelete(View):
    success_message = 'Ürün başarıyla karttan çıkartıldı.'
    error_message = 'Ürün karttan silinemedi.'

    def get(self, request, pk=None):
        try:
            cart = Cart(request)
            product = Product.objects.get(pk=pk)
            cart.remove(product)
            messages.success(self.request, self.success_message)
        except Exception as e:
            messages.error(self.request, self.error_message)

        return redirect('project:detail-cart')


