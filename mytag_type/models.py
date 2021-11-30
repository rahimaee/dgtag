from django.db import models


# Create your models here.

class CardType(models.Model):
    Name = models.CharField(max_length=100, verbose_name='نام')
    NameEn = models.CharField(max_length=100, verbose_name='نام انگلیسی')
    IsActive = models.BooleanField(default=False, verbose_name='فعال/غیرفعال')
