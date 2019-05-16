'''
Arkadaşlar merhaba, önceki derslerimizde django ile ilgili bilgiler öğrendik ve bunları ufak uygulamalar ile
pekiştirdik. Bilgi bakımından uygulama yazılımına geçebilecek kadar bilgi birikimi sağladık. Uygulamamızı
yazarken de Django hakkında farklı bilgileri öğrenmeye devam edeceğiz. Kod yazma işlemine başlamadan önce yapacağımız
yazılımı biraz detaylandıralım. Projenin detayları kafamızda otursun. Önemli bir noktayı atlarsak daha sonra düzeltmek
için çok zaman harcayabiliriz.

Aslında ihtiyaç ve proje analizinin uzun uzun düşünülmesi gerekli. Veritabanı diyagramlarının vs. kurulması gerekli.
Fakat biz çok detaylı bir örnek yapmayacağımız için bu kadar detaylı bir çalışma yapmayacağız.

Distribütörler için bayilerinin online olarak sipariş verecebilecekleri bir stok uygulaması yapacağız.

Bu uygulama da hem django yönetici sayfasından hem de bizim kendi oluşturacağımız yönetim sayfalarından distribütör
ve bayiler için farklı işlemler yapılabilecek. Ben kursu anlatmaya başlamadan önce sizlerin zamanını fazla almamak
ve daha akıcı bir anlatım olması nedeniyle uygulamayı öncelikle kendim yazdım. Şimdi bu uygulama üzerinden kontrol
ederek yapılacak listesini çıkartalım.

Distribütörler sadece django yönetici panelinden eklenebilecek. Yani distribütör eklenebilmesi için super admin
yetkisine sahip olmak gerekecek.

Distribütör oluşturulurken seçilen yetkili distributor için super-admin benzeri bir yetki seviyesine sahip olacak
ve distribütör ile ilgili tüm işlemleri yetkisine bakılmadan yapabilecektir. Aynı durum bayi oluşturulurken seçilen
kullanıcı için de geçerlidir. Fakat bayiler hem django yönetici panelinden hem de hazırladığımız yönetici panelinden
eklenebilecektir.

Distribütör ve Bayilerin personel ekleyebileceği, ilişkilendirebileceği ve yetkilerini ayarlayabileceği bir yapı
olacaktır. Personeller sadece yetkili oldukları bölümler için işlem gerçekleştirebilecektir.

Personel bölümü sadece distribütör ve bayi de ana yetkili kullanıcı tarafından yönetilebilecektir. Diğer bölümler
için personel yetkisi kontrol edilecektir.

Distribütörler sisteme ürünler ekleyecek ve mevcut ve stoklarını ayarlayacaktır. Distribütörlerin yetki vermiş
oldukları bayiler bu ürünleri listeleyebilecek ve sipariş verebilecektir. Bu siparişler distribütör tarafından
onaylanmadan bayi tarafından iptal edilebilir olacaktır. Onaylandığında ise distribütör ve bayi tarafından iptal
edilemeyecektir.

Bayiler yapmış oldukları ödemeleri sistemden giriş yapacak ve distribütör onayına düşecektir. Distribütör onay veya
red işlemi yapmadan önce iptal edebilecektir.

Distribütörler diğer bayilerin borç / alacak tutarını izleyebilecektir. Aynı durum bayiler için de geçerlidir.

Evet şimdi projemize yeni bir uygulama ekleyelim. Uygulama adımız project olsun.

python manage.py startapp project

views ve modellerimiz için klasörlerimizi  ve __init__.py dosyalarını oluşturalım. views.py ve models.py yi silelim.



'''

default_app_config = 'project.apps.ProjectConfig'