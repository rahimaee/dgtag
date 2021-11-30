from django.db import models


# Create your models here.

class ContactNumbersType(models.Model):
    Name = models.CharField(max_length=50, verbose_name='نام')
    Icon = models.CharField(max_length=100, verbose_name='نام ایکون')

    class Meta:
        verbose_name = 'نوع شماره'
        verbose_name_plural = 'انواع شمارها'

    def __str__(self):
        return self.Name
