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
class OrderAdd(CheckDealerMixin, View):
    error_message = 'Sipariş oluşturulamadı lütfen tekrar deneyiniz.'
    success_message = 'Sipariş başarıyla oluşturuldu'

    # listeleme sayfasından sepete ekleme
    def get(self, request):
        try:
            with transaction.atomic():

                # sipariş kaydını oluşturalım
                new_order = Order(dealer_id=self.role_id, order_cancelled=False, order_transfered=False)
                new_order.save()

                # shopping karttaki ürünleri sipariş kaydına ekleyelim
                # Ürünler işlem yapan bayi tarafından alınabilmi kontrol edilmesi lazım.
                # Bayiler sadece yetki verilen distibütörlerin ürünlerini alabilmeli.
                dealer = Dealer.objects.prefetch_related('distributors').get(pk=self.role_id)
                distributor_list = dealer.distributors.values_list('id', flat=True)

                cart = Cart(request)

                for item in cart:
                    product = Product.objects.get(pk=item['id'])

                    # ürünün distribütörü bayiye yetki vermişmi bakalım
                    # vermediyse hata verelim.
                    if product.distributor_id not in distributor_list:
                        permission_error_message = "%s ürünün sahibi satım alımı için size yetki verrmemiş. " \
                                                   "Ürün listenizden çıkartıldı." % (item['name'])
                        raise PermissionDenied(permission_error_message)

                    # sipariş edilen ürünleri ekleyelim
                    order_item = OrderItem(order=new_order, product=product, item_count=item['quantity'],
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
                return redirect(reverse('project:detail-order', kwargs={"pk": new_order.id}))

        # eğer stok yeterli değilse hatayı yakalayalım
        except ValidationError as e:
            messages.error(self.request, e)

        # eğer veritabanı hatası oluştuysa hatayı yakalayalım
        except IntegrityError:
            messages.error(self.request, self.error_message)

        # eğer distributor yetkisi yoksa hatayı yakalayalım ve ürünü listeden çıkartalım
        except PermissionDenied as e:
            cart.remove(product)
            messages.warning(self.request, e)

        # eğer başkabir hata varsa hatayı yakalayalım
        except Exception as e:
            messages.error(self.request, self.error_message)

        # eğer hata yoksa success_message ekleyelim ve detail-cart sayfasına yönlendirelim
        return redirect('project:detail-cart')


