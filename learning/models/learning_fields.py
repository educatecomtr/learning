from django.db import models


class LearningFields(models.Model):

    # alan özellikleri - aldıkları bazı genel parametreler
    tamsayi = models.IntegerField(verbose_name='Tam Sayı', null=True, blank=True, default=5, unique=True,
                                  primary_key=False, editable=True, help_text='Buraya girilen sayı tam sayı olmalıdır',
                                  db_index=True, db_column='tam_sayi')

    # alan türleri

    '''
    Small Integer   : -32.768 – 32.767 arası tam sayı alabilir.
    Integer         : -2.147.483.648 – 2.147.483.647 arası tam sayı alabilir.
    Big Integer     : -9.223.372.036.854.775.808 - 9.223.372.036.854.775.807 arası tam sayı alabilir.
    CharField       : En fazla 255 karakter alabilir.
    '''

    # id = models.AutoField(primary_key=True)

    #id = models.BigAutoField(primary_key=True)

    small_integer_field = models.SmallIntegerField()

    integer_field = models.IntegerField()

    big_integer_field = models.BigIntegerField(default=1)

    positive_integer_field = models.PositiveIntegerField()

    positive_small_integer_field = models.PositiveSmallIntegerField()

    float_field = models.FloatField()

    decimal_field = models.DecimalField(max_digits=10, decimal_places=5)

    boolean_field = models.BooleanField()

    char_field = models.CharField(max_length=50)

    text_field = models.TextField()

    date_field = models.DateField(auto_now_add=True)

    date_time_field = models.DateTimeField(auto_now=True)

    time_field = models.TimeField()

    email_field = models.EmailField()

    ip_address_field = models.GenericIPAddressField(protocol='both', unpack_ipv4=True)

    slug_field = models.SlugField()

    url_field = models.URLField()

    uuid_field = models.UUIDField()

    binary_field = models.BinaryField(default='')

    # file_field = models.FileField()
    # file_path_field = models.FilePathField()
    # image_field = models.ImageField() # Pillow kurulumu gerekli.
