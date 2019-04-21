from django.db import models

# MATEMATİKSEL FONKSİYONLAR

class Vector(models.Model):
    x = models.FloatField()
    y = models.FloatField()

vector = Vector.objects.annotate(new_x=Abs('x')).get() # Abs() : mutlak değer
vector = Vector.objects.annotate(new_x=Ceil('x')).get() # Ceil() : yukarı yuvarlama
vector = Vector.objects.annotate(new_x=Floor('x')).get() # Floor() : aşağı yuvarlama
vector = Vector.objects.annotate(new_x=Round('x')).get() # Round() : en yakın değere yuvarlama
vector = Vector.objects.annotate(new_value=Power('x','y')).get() # Power() : x üzeri y
vector = Vector.objects.annotate(new_value=Sqrt('x')).get() # Sqrt() : kare kök


# bunlar filter içerisinde kullanılabilecek şekilde ayarlanabilir.
FloatField.register_lookup(Ceil)
FloatField.register_lookup(Abs)
vectors = Vector.objects.filter(x__abs__lt=1) # mutlak değeri birden büyük olanlar

# TEXT FONKSİYONLARI

# name alanının ilk harfinin unicode sayı karşılığını verir.
author = Author.objects.annotate(name_code_point=Ord('name')).get() # author.name_code_point = 77

# Chr unicode sayı ile arama yapar. M harfi ile başlayan kayıtları getirir
author = Author.objects.filter(name__startswith=Chr(ord('M'))).get()

# alanları birleştirir. screen_name için name ve goes by alanları birleşir.
author = Author.objects.annotate(
    screen_name=Concat(
        'name', V(' ('), 'goes_by', V(')'),
        output_field=CharField()
    )
).get()

# soldaki 1. harfi verir
author = Author.objects.annotate(first_initial=Left('name', 1)).get()

# sağdaki 1. harfi verir
author = Author.objects.annotate(last_letter=Right('name', 1)).get()

# name alanının karakter sayısını verir. register edip filterda kullanabiliriz.
author = Author.objects.annotate(name_length=Length('name')).get()

# küçük harf yapar
author = Author.objects.annotate(name_lower=Lower('name')).get()

# büyük harf yapar
author = Author.objects.annotate(name_upper=Upper('name')).get()

# 8 karakter olana kadar sola abc ekler. 4 hafta ekleyeceği için abcaJohn
Author.objects.update(name=LPad('name', 8, Value('abc')))

# 8 karakter olana kadar sağa abc ekler. 4 hafta ekleyeceği için Johnabca
Author.objects.update(name=LPad('name', 8, Value('abc')))

# soldaki boşlukları temizleme
Author.objects.update(name=LTrim('name'))

# sağdaki boşlukları temizleme
Author.objects.update(name=RTrim('name'))

# sağ ve soldaki boşlukları temizleme
Author.objects.update(name=Trim('name'))

# name alanının 1. harfinden başlayıp 5. harfa kadar alır ve alias kaydeder
Author.objects.update(alias=Lower(Substr('name', 1, 5)))

# eğer name içerisinde Smith geçiyorsa smith_index 1 atar. ve smith_index 1 den büyük olanları listeler
authors = Author.objects.annotate(smith_index=StrIndex('name', V('Smith'))).filter(smith_index__gt=0)

# name ters çevirir
author = Author.objects.annotate(backward=Reverse('name')).get()

# name alanındaki Margaret'i Margareth olarak değiştirir
Author.objects.update(name=Replace('name', Value('Margaret'), Value('Margareth')))

# name alanındaki değer 3 kere yan yana yazar ve kayıt eder.
Author.objects.update(name=Repeat('name', 3))

