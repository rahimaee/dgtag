from django.db import models


# Create your models here.

class Comments(models.Model):
    FullName = models.CharField(max_length=150, verbose_name='نام کامل')
    Email = models.EmailField(verbose_name='ایمیل')
    Comment = models.TextField(verbose_name='دیدگاه')
    IsRead = models.BooleanField(default=False, verbose_name='خوانده شده/خوانده نشده')
    IsActive = models.BooleanField(default=False, verbose_name='فعال/غیر فعال')
