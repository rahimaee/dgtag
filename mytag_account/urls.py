from django.urls import path

from mytag_account.views import user_login_page, user_register_page, ResetPasswordView
from django.contrib.auth import views as auth_views

app_name = 'account'

urlpatterns = [
    path('login', user_login_page, name='login'),
    path('register', user_register_page, name='register'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='mytag_account/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
]
