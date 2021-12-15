from django.db import models


# Create your models here.

class Tag(models.Model):
    Name = models.CharField(max_length=50, verbose_name='نام تگ')
    IsActive = models.BooleanField(default=False, verbose_name='فعال/غیرفعال')

    class Meta:
        verbose_name = 'برچسب'
        verbose_name_plural = 'برچسب ها'

    def __str__(self):
        return self.Name

