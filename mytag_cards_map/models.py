import os
from random import randint

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from mytag_cards.models import Card


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_name = randint(1, 100000)
    name, ext = get_filename_ext(filename)
    final_name = f"{new_name}{ext}"
    return f"UserMap/{final_name}"


class Map(models.Model):
    Name = models.CharField(max_length=100, verbose_name='نام')
    Country = models.CharField(max_length=50, verbose_name='کشور')
    Province = models.CharField(max_length=50, verbose_name='استان')
    City = models.CharField(max_length=50, verbose_name='شهر')
    Address = models.TextField(verbose_name='ادرس')
    Lat = models.CharField(max_length=100, verbose_name='lat')
    Lng = models.CharField(max_length=100, verbose_name='lat')
    MapZoom = models.CharField(max_length=20, verbose_name='زوم نقشه', default='16')
    MapImg = models.ImageField(upload_to=upload_image_path, verbose_name='عکس برای نشقه')
    MapText = models.CharField(max_length=150, verbose_name='متن نشقه')
    IsActive = models.BooleanField(default=True, verbose_name='فعال/غیرفعال')
    By_User = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    DgTag = models.ForeignKey(Card, on_delete=models.CASCADE, verbose_name='کارت')

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = 'نشقه'
        verbose_name_plural = 'نقشه ها'
