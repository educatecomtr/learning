'''
Arkadaşlar merhaba, önceki derslerimizde django ile ilgili bilgiler öğrendik ve bunları ufak uygulamalar ile
pekiştirdik. Bilgi bakımından uygulama yazılımına geçebilecek kadar bilgi birikimi sağladık. Uygulamamızı
yazarken de Django hakkında farklı bilgileri öğrenmeye devam edeceğiz. Kod yazma işlemine başlamadan önce yapacağımız
yazılımı biraz detaylandıralım. Projenin detayları kafamızda otursun. Önemli bir noktayı atlarsak daha sonra düzeltmek
için çok zaman harcayabiliriz.

Aslında ihtiyaç ve proje analizinin uzun uzun düşünülmesi gerekli. Veritabanı diyagramlarının vs. kurulması gerekli.
Fakat biz çok detaylı bir örnek yapmayacağımız için bu kadar detaylı bir çalışma yapmayacağız.

Distribütörler için bayilerinin online olarak sipariş verecebilecekleri bir stok uygulaması yapacağız. Bu uygulama da
hem django yönetici sayfasından hem de bizim kendi oluşturacağımız yönetim sayfalarından distribütör ve bayiler için
farklı işlemler yapılabilecek.

Distribütörler sadece django yönetici panelinden eklenebilecek. Yani distribütör eklenebilmesi için super admin
yetkisine sahip olmak gerekecek.

Distribütör oluşturulurken seçilen yetkili distributor için super-admin benzeri bir yetki seviyesine sahip olacak
ve distribütör ile ilgili tüm işlemleri yetkisine bakılmadan yapabilecektir. Aynı durum bayi oluşturulurken seçilen
kullanıcı için de geçerlidir. Fakat bayiler hem django yönetici panelinden hem de hazırladığımız yönetici panelinden
eklenebilecektir.

Distribütörler :



Bayiler :






Ben kursu anlatmaya başlamadan önce sizlerin zamanını fazla almamak ve daha akıcı bir anlatım olması nedeniyle
uygulamayı öncelikle kendim yazdım. Şimdi bu uygulama üzerinden kontrol ederek yapılacak listesini çıkartalım.






Evet şimdi projemize yeni bir uygulama
ekleyelim. Uygulama adımız project olsun.

python manage.py startapp project

views ve modellerimiz için klasörlerimizi  ve __init__.py dosyalarını oluşturalım. views.py ve models.py yi silelim.





'''

default_app_config = 'project.apps.ProjectConfig'