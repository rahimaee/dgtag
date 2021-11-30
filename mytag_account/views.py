from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy

from mytag import settings
from mytag_account.forms import LoginForm, RegisterForm


def user_login_page(request):
    if request.user.is_authenticated:
        return redirect('/')

    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        user_name = login_form.cleaned_data.get('user_name')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request, username=user_name, password=password)
        if user is not None:
            login(request, user)
            return redirect('starting_page')
    context = {
        'login_form': login_form
    }
    return render(request, 'mytag_account/user_login_page.html', context)


def user_register_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    register_form = RegisterForm(request.POST or None)

    if register_form.is_valid():
        user_name = register_form.cleaned_data.get('user_name')
        password = register_form.cleaned_data.get('password')
        email = register_form.cleaned_data.get('email')
        User.objects.create_user(username=user_name, email=email, password=password)
        subject = 'خوش آمد گویی'
        message = f'سلام به دی جی تگ خوش امدید'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail(subject, message, email_from, recipient_list)
        return redirect('account:login')

    context = {
        'register_form': register_form
    }
    return render(request, 'mytag_account/user_register_page.html', context)


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'mytag_account/user_password_reset.html'
    email_template_name = 'mytag_account/password_reset_email.html'
    subject_template_name = 'mytag_account/email.html'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('account:login')

