from django.db import models

from mytag_cards.models import Card
from mytag_cards_contactnumbers_type.models import ContactNumbersType


# Create your models here.


class ContactNumbers(models.Model):
    Name = models.CharField(max_length=120, verbose_name='نام')
    Number = models.CharField(max_length=50, verbose_name='شماره')
    Type = models.ForeignKey(ContactNumbersType, models.CASCADE, verbose_name='نوع')
    IsActive = models.BooleanField(default=False, verbose_name='فعال/غیرفعال')
    cards = models.ForeignKey(Card, related_name='has_ContactNumbers', on_delete=models.CASCADE, verbose_name='کارت')
