from django.urls import path
from .views import *

app_name = 'home_products'

urlpatterns = [
    path('', ProductsList.as_view(), name='starting_page'),
    path('<productId>/<name>', products_detail, name='detail'),
]
