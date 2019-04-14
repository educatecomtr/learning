from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):

    name = models.CharField(max_length=200)
    content = models.TextField()

    # learnings_bookcompanys_related, learnings_gamecompanys_related
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="%(app_label)s_%(class)s_related"
                               )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ['name']


class BookCompany(Company):
    publisher_name = models.CharField(max_length=50)

    class Meta(Company.Meta):
        db_table = 'company_alt_sinifi_book'


class GameCompany(Company):
    platform = models.CharField(max_length=50)


class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    page_count = models.PositiveSmallIntegerField()


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    comment_content = models.TextField()


class Intro(Book, Comment):
    intro_comment = models.TextField()


class NewManager(models.Manager):
    # yapılacak işlemler
    pass


class ProxyBook(Book):

    objects = NewManager()

    class Meta:
       proxy = True
       ordering = ['name']

    @property
    def short_name(self):
        return self.name[:10]




