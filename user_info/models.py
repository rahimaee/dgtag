import os
from random import randint

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_name = randint(1, 100000)
    name, ext = get_filename_ext(filename)
    final_name = f"{new_name}{ext}"
    return f"UserProfile/{final_name}"


class UserInfo(models.Model):
    ProfileImg = models.ImageField(upload_to=upload_image_path, verbose_name='پروفایل')
    PhoneNumber = models.CharField(max_length=15, verbose_name='موبایل')
    user = models.FileField(User, verbose_name='کاربر')
