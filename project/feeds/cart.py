from project.models import Product
from django.core import serializers


class TryIter:
    def __init__(self):
        self.deneme = [1, 2, 3, 4]

    def __iter__(self):
        for i in self.deneme:
            yield i*2

    def __len__(self):
        return len(self.deneme)


# Shopping cart nesnemizi oluşturalım.
# Shopping carta ekleme, silme, sıfırlama ve güncelleme işlemleri yapılabilsin.
# Bunun için add, remove ve clear metodlarını oluşturalım. İçerini daha sonra dolduracağız.
class Cart(object):

    # Shopping Cartımızı sessionda tutacağız.
    # Bu nedenle kart çağırıldığında daha önce bu kart için bir session oluşturulmuşmu kontrol edelim.
    # Ürünleri tutacağımız session adı shopping_cart olsun.
    # Eğer oluşturulmamış ise yeni bir session oluşturalım.
    # self.cart session bilgilerini aktaralım.
    def __init__(self, request):

        self.session = request.session

        cart = self.session.get('shopping_cart')
        distributors = self.session.get('shopping_distributors')

        if not cart:
            cart = self.session['shopping_cart'] = {}
            distributors = self.session['shopping_distributors'] = {}
        else:
            if not distributors:
                cart = self.session['shopping_cart'] = {}

        self.cart = cart
        self.distributors = distributors

    # ürünlerimiz benzersiz olduğu için kartımızda ürün id ile tutabiliriz.
    # dict lerin keyleri string olarak tutulduğu için product_id yi stringe çevirelim.
    # cart içerisinde ürün varmı diye bakalım. Eğer yoksa carta ekleyelim.
    # Eğer varsa ürün adedini güncelleyelim.
    # Kart bilgilerini sessiona aktarmadık. Aktarmak için bir save metodu oluşturalım ve
    # Session kaydını gerçekleştirelim.
    def add(self, product, quantity=1):
        product_id = str(product.id)
        distributor_id = str(product.distributor_id)

        if product_id not in self.cart:
            if product.stock_count < quantity:
                return False

            if distributor_id not in self.distributors:

                self.distributors[distributor_id] = 1;

            self.cart[product_id] = {'id': product.id, 'quantity': quantity, 'price': product.price, 'name': product.name}
        else:
            if product.stock_count < self.cart[product_id]['quantity'] + quantity:
                return False

            if distributor_id not in self.distributors:
                self.distributors[distributor_id] += 1;

            self.cart[product_id]['quantity'] += quantity

        self.save()
        return True

    def save(self):
        self.session['shopping_cart'] = self.cart
        self.session['shopping_distributors'] = self.distributors
        # self.session.modified = True

    # Ürünü karttan silmek için öncelikle cart içerisinde ürün varmı bakalım.
    # Eğer varsa cart içerisinde çıkartalım ve sessionı güncelleyelim.
    def remove(self, product):

        product_id = str(product.id)
        distributor_id = str(product.distributor_id)

        if product_id in self.cart:

            if self.distributors[distributor_id] > 1:
                self.distributors[distributor_id] -= -1
            else:
                del self.distributors[distributor_id]

            del self.cart[product_id]
            self.save()

    # Kartı temizlemek için tüm session bilgisini silelim.
    def clear(self):
        del self.session['shopping_distributors']
        del self.session['shopping_cart']
        # self.session.modified = True

    # kart nesnesini __iter__ metodu ile yinelenebilir olmasını sağlayabiliriz.
    # bu sayede kartta yer alan her ürünü view ve template dosyalarımızda alabiliriz.
    # bunu basit bir örnek ile gösterelim. (class TryIter)
    # kartımızı yineenebilir yaparken ürün bilgilerini ve toplam fiyatları karta ekleyelim.

    def __iter__(self):
        for item in self.cart.values():
            item['total_price'] = item['price'] * item['quantity']
            yield item

    # kart nesnesindeki ürün sayısını hesaplamak için yine bir sihirli method olan
    # __len__ den yararlanılır. Fakat biz ürün sayısını değil toplam sipariş sayısını döndüreceğiz.
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    # toplam tutarı hesaplamak içinde kendi methodumuzu yazalım.
    # her ürün için ürün adedi ve fiyatı çarpalım ve hepsini toplayalım.
    def get_total_price(self):
        return sum(item['price'] * item['quantity'] for item in self.cart.values())





