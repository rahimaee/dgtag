from django.urls import path, include

from mytag_account.views import user_login_page, user_register_page, ResetPasswordView, activate
from django.contrib.auth import views as auth_views

app_name = 'account'

urlpatterns = [
    path('login', user_login_page, name='login'),
    path('register', user_register_page, name='register'),
    path('activate/<uidb64>/<token>', activate, name='activate'),
]
