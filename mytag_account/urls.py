from django.urls import path, include, reverse_lazy

from mytag_account.views import user_login_page, user_register_page, ResetPasswordView, activate, logout
from django.contrib.auth import views as auth_views

app_name = 'account'

urlpatterns = [
    path('login', user_login_page, name='login'),
    path('register', user_register_page, name='register'),
    path('account/activate/<uidb64>/<token>', activate, name='activate'),
    path('account/password_reset/',
         auth_views.PasswordResetView.as_view(template_name='mytag_account/password_reset_form.html',
                                              email_template_name='mytag_account/password_reset_email.html',
                                              success_url=reverse_lazy('account:password_reset_done')),
         name='password_reset'),

    path('account/password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='mytag_account/password_reset_done.html'),
         name='password_reset_done'),

    path('account/reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="mytag_account/password_reset_confirm.html",
                                                     success_url=reverse_lazy('account:password_reset_complete')),
         name='password_reset_confirm'),
    path('account/reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='mytag_account/password_reset_complete.html'),
         name='password_reset_complete'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
]
