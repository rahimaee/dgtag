from django.contrib import admin
from .models import Newsletters, NewslettersSend

# Register your models here.
admin.site.register(Newsletters)
admin.site.register(NewslettersSend)
