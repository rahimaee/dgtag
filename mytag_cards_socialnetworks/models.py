from django.db import models

from mytag_cards.models import Card
from mytag_cards_socialnetworks_type.models import SocialNetworkType


# Create your models here.

class SocialNetwork(models.Model):
    Name = models.CharField(max_length=150, verbose_name='نام')
    Url = models.CharField(max_length=250, verbose_name='ادرس شبکه اجتماعی')
    Type = models.ForeignKey(SocialNetworkType, models.CASCADE, verbose_name='نوع شبکه')
    IsActive = models.BooleanField(default=False, verbose_name='فعال/غیرفعال')
    cards = models.ForeignKey(Card, models.CASCADE, verbose_name='کارت')

    class Meta:
        verbose_name = 'شبکه اجتماعی'
        verbose_name_plural = 'شبکه های اجتماعی'

    def __str__(self):
        return self.Name
