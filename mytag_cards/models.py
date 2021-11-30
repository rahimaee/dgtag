import os
from random import randint

from django.contrib.auth.models import User
from django.db import models
from mytag_type.models import CardType
from django.db.models import Q


# Create your models here.

# image name on  server
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_name = randint(1, 100000)
    name, ext = get_filename_ext(filename)
    final_name = f"{new_name}{ext}"
    return f"Card/{final_name}"


class CardManager(models.Manager):
    def card_by_user_name(self, UserName):
        card = self.get_queryset().filter(IsActive=True, IsActiveUserName=True, UserName=UserName).first()
        if card is not None:
            return card
        else:
            return None

    def card_by_card_id(self, CardID):
        card = self.get_queryset().filter(IsActive=True, CardId=CardID).first()
        if card is not None:
            return card
        else:
            return None

    def get_ContactNumbers(self):
        return self.get_queryset().filter(IsActive=True).all()


class Card(models.Model):
    ProfileImg = models.ImageField(upload_to=upload_image_path, null=True, blank=True, verbose_name='عکس پروفایل')
    FirstName = models.CharField(max_length=150, verbose_name='نام')
    LastName = models.CharField(max_length=150, verbose_name='نام خانوادگی')
    Company = models.CharField(max_length=120, verbose_name='نام کمپانی')
    WorkName = models.CharField(max_length=100, verbose_name='شغل')
    Bio = models.TextField(verbose_name='بایوگرافی')
    UserName = models.CharField(max_length=150, verbose_name='نام کاربری')
    IsActive = models.BooleanField(default=True, verbose_name='فعال/غیرفعال')
    Views = models.IntegerField(default=0, verbose_name='بازدید')
    TypeOfCard = models.ForeignKey(CardType, models.CASCADE, verbose_name='نوع کارت')
    Pro = models.BooleanField(default=False, verbose_name='پرو')
    IsActiveUserName = models.BooleanField(default=False, verbose_name='فعال/غیرفعال بودن نام کاربری')
    verification = models.BooleanField(default=False, verbose_name='تایید هویت')
    CardId = models.IntegerField(verbose_name='ایدی کاربر در url')
    BuildTime = models.DateTimeField(verbose_name='زمان ساخت کارت')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = CardManager()

    class Meta:
        verbose_name = 'کارت'
        verbose_name_plural = 'کارت ها'

    def __str__(self):
        return self.FirstName + self.LastName

    def get_name(self):
        if self.LastName is None or self.FirstName is None:
            return self.Company
        else:
            return self.FirstName + " " + self.LastName
