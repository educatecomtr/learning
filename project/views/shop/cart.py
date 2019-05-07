from django.views import View
from django.shortcuts import render, redirect
from project.forms import AddProductToShoppingCartForm
from project.feeds import Cart
from project.models import Product
from django.contrib import messages


# Shopping Cart listeleme sayfası
class CartView(View):
    def get(self, request):
        cart = Cart(request)
        return render(request=request, template_name='project/shop/cart.html', context={'cart': cart})


# Shopping karta ürün ekleme
class CartAdd(View):
    success_message = 'Ürün başarıyla karta eklendi.'
    error_message = 'Ürün karta eklenemedi.'
    stock_message = 'Yeterli stok bulunamadı.'

    # listeleme sayfasından sepete ekleme
    def get(self, request, pk=None):
        try:
            product = Product.objects.get(pk=pk)
            cart = Cart(request)
            add = cart.add(product=product, quantity=1)

            if add:
                messages.success(self.request, self.success_message)
            else:
                messages.warning(self.request, self.stock_message)

        except Exception as e:
            messages.error(self.request, self.error_message)

        return redirect('project:detail-cart')

    # detay sayfasından sepete ekleme
    def post(self, request, pk=None):

        form = AddProductToShoppingCartForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            try:
                cart = Cart(request)
                product = Product.objects.get(pk=pk)
                add = cart.add(product=product, quantity=quantity)

                if add:
                    messages.success(self.request, self.success_message)
                else:
                    messages.warning(self.request, self.stock_message)

            except Exception as e:
                messages.error(self.request, self.error_message)
        else:
            messages.error(self.request, self.error_message)

        return redirect('project:detail-cart')


# Shopping karttan ürün silme
class CartDelete(View):
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


# Shopping kartı temizleme
class CartClear(View):
    success_message = 'Kart başarıyla temizlendi.'
    error_message = 'Kart temizlenemedi.'

    def get(self, request):
        try:
            cart = Cart(request)
            cart.clear()
            messages.success(self.request, self.success_message)
        except Exception as e:
            messages.error(self.request, self.error_message)

        return redirect('project:detail-cart')
