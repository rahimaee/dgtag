from django.urls import path
from .views import changepassword

app_name = 'ChangePassword'
urlpatterns = [
    path('changepassword', changepassword, name='changepassword'),
]
