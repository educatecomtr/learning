from django.db import models
from django.contrib.auth.models import User


class UserDetail(models.Model):
    address = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username + ' detail'

