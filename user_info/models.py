from django.db import models


# Create your models here.


class UserInfo(models.Model):
    ProfileImg = models.ImageField()
    PhoneNumber = models.CharField(default=15, verbose_name='موبایل')
