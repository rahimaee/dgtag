from django.db import models


# Create your models here.

class Category(models.Model):
    FnName = models.CharField(max_length=50, verbose_name='نام فارسی')
    EnName = models.CharField(max_length=50, verbose_name='نام در url')
    IsActive = models.BooleanField(default=False, verbose_name='فعال/غیرفعال')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'همه دسته ها'

    def __str__(self):
        return self.FnName
