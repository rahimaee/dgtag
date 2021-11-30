from django.contrib import admin

from mytag_cards_contactnumbers.models import ContactNumbers
from .models import Card
from mytag_cards_socialnetworks.models import SocialNetwork


# Register your models here.
class ContactNumbersInline(admin.TabularInline):
    model = ContactNumbers


class SocialNetworkInline(admin.TabularInline):
    model = SocialNetwork


class CardAdmin(admin.ModelAdmin):
    list_display = ['__str__']
    inlines = [
        ContactNumbersInline,
        SocialNetworkInline,
    ]

    class Meta:
        model = Card


admin.site.register(Card, CardAdmin)
