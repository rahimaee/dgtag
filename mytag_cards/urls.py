from django.urls import path
from .views import my_tag_home

app_name = 'cards'
urlpatterns = [
    path('u/<card>', my_tag_home, name='my_tag_home'),
]
