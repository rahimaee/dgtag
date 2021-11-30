from django.db import models


# Create your models here.

class SocialNetworkType(models.Model):
    Name = models.CharField(max_length=100, verbose_name='نام شبکه')
    Icon = models.CharField(max_length=120, verbose_name='نام ایکون')
    IsActive = models.BooleanField(default=False, verbose_name='فعال/غیرفعال')

    class Meta:
        verbose_name = 'شبکه'
        verbose_name_plural = 'شبکه ها'

    def __str__(self):
        return self.Name
