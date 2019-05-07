from django import forms


# Ürünü shopping cart eklemek için formumuzu oluşturalım.
class AddProductToShoppingCartForm(forms.Form):
    # Bunu dışarda da yazabilirdik
    PRODUCT_QUANTITY = [(i, str(i)) for i in range(1, 6)]

    # Ürün adedi için 1-5 den beşe kadar seçim yaptıralım. Bunun için seçim kutusu oluşturalım.
    # Bu kutu sadece int dönüş yapabilsin.
    # Bu nedenle TypedChoiceField oluşturup coerce argümanı olarak int verelim.
    # coerce quantity alanının int olarak dönmeye zorlar.
    # Değer olarak birden beşe kadar sayı oluşturalın bir liste yapalım ve choices argümanı olarak atayalım.
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY, coerce=int)

