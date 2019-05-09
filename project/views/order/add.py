from django.views import View
from django.shortcuts import redirect, reverse
from project.feeds import Cart
from project.models import Product, Order, OrderItem, Dealer
from django.contrib import messages
from django.db import transaction
from django.db import IntegrityError
from django.core.exceptions import ValidationError, PermissionDenied
from stocks.mixins import CheckDealerMixin


# Sipariş oluşturma
# CheckDealerMixin ile sadece bayilerin giriş yapmasını sağlayalım.
class OrderAddView(CheckDealerMixin, View):
    error_message = 'Sipariş oluşturulamadı lütfen tekrar deneyiniz.'
    success_message = 'Sipariş başarıyla oluşturuldu'

    # listeleme sayfasından sepete ekleme
    def get(self, request):
        try:
            with transaction.atomic():

                cart = Cart(request)
                new_order = {}
                for distributor_id in cart.distributors.keys():
                    # sipariş kaydını oluşturalım
                    new_order[distributor_id] = Order(distributor_id=distributor_id, dealer_id=self.role_id, order_cancelled=False, order_transfered=False)
                    new_order[distributor_id].save()

                # shopping karttaki ürünleri sipariş kaydına ekleyelim
                # Ürünler işlem yapan bayi tarafından alınabilirmi kontrol edilmesi lazım.
                # Bayiler sadece yetki verilen distibütörlerin ürünlerini alabilmeli.

                dealer = Dealer.objects.prefetch_related('distributors').get(pk=self.role_id)
                distributor_list = list(dealer.distributors.values_list('id', flat=True))

                for item in cart:
                    product = Product.objects.get(pk=item['id'])

                    str_distributor_id = str(product.distributor_id)

                    # ürünün distribütörü bayiye yetki vermişmi bakalım
                    # vermediyse hata verelim.

                    if str_distributor_id not in cart.distributors or product.distributor_id not in distributor_list:
                        permission_error_message = "%s ürünün sahibi satım alımı için size yetki verrmemiş. " \
                                                   "Ürün listenizden çıkartıldı." % (item['name'])
                        raise PermissionDenied(permission_error_message)

                    # sipariş edilen ürünleri ekleyelim
                    order_item = OrderItem(order=new_order[str_distributor_id], product=product, item_count=item['quantity'],
                                           item_price=item['price'])
                    order_item.save()

                    # ünün stok miktarını düşelim
                    product.stock_count = product.stock_count - item['quantity']

                    # eğer yeterli stok yoksa siparişi durduralım
                    if product.stock_count < 0:
                        item['quantity'] = product.stock_count + item['quantity']
                        validation_error_message = "%s ürünü için yeterli stok bulunamadı. " \
                                                   "Ürün adedi kalan stok kadar güncellendi." % (item['name'])

                        raise ValidationError(validation_error_message)

                    product.save()

                # shpping kartı temizleyelim
                cart.clear()

                # eğer hata yoksa success_message ekleyelim
                messages.success(self.request, self.success_message)

                # detail-order sayfasına yönlendirelim
                return redirect('project:list-order')

        # eğer stok yeterli değilse hatayı yakalayalım
        except ValidationError as e:
            messages.error(self.request, e)

        # eğer veritabanı hatası oluştuysa hatayı yakalayalım
        except IntegrityError as e:
            print(str(e))
            messages.error(self.request, self.error_message)

        # eğer distributor yetkisi yoksa hatayı yakalayalım ve ürünü listeden çıkartalım
        except PermissionDenied as e:
            cart.remove(product)
            messages.warning(self.request, e)

        # eğer başkabir hata varsa hatayı yakalayalım
        except Exception as e:
            print(str(e))
            messages.error(self.request, self.error_message)

        # eğer hata yoksa success_message ekleyelim ve detail-cart sayfasına yönlendirelim
        return redirect('project:detail-cart')


