from django.urls import path
from .views import *

app_name = 'products_order'
urlpatterns = [
    path('add-user-order', add_user_order, name='add-user-order'),
    path('add-order/<product_id>', add_shop_on_home, name='add-order'),
    path('open-order', user_open_order, name='list_order'),
    path('remove_order_detail/<detail_id>', remove_order_detail, name='remove-item_order'),
    path('order-item-update/<detail_id>/<count>', update_count, name='update-item_order'),
    path('order-address/', add_address_order, name='order-address'),
]
