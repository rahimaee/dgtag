from django.urls import path
from .views import *

app_name = 'userpanel_invoice'
urlpatterns = [
    path('invoice', all_invoice, name='invoice'),

]
