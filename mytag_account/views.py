from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
# Create your views here.
from django.template.loader import render_to_string
from django.urls import reverse_lazy, reverse
from django.utils.encoding import force_text, force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from mytag import settings
from mytag_account.forms import LoginForm, RegisterForm
from mytag_account.tokens import account_activation_token


def user_login_page(request):
    if request.user.is_authenticated:
        return redirect('userpanel:user-home-page')

    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        user_name = login_form.cleaned_data.get('user_name')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request, username=user_name, password=password)
        email_confirm = User.objects.filter(username=user_name).first()
        if email_confirm.email_confirm == 'False':
            mail_subject = 'فعال سازی حساب دی جی تگ'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email_confirm.email, ]
            message = render_to_string('mytag_account/acc_active_email.html', {
                'user': user,
                'domain': get_current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            send_mail(mail_subject, message, email_from, recipient_list)
            return render(request, 'mytag_account/active_email_done.html')
        if user is not None:
            login(request, user)
            return redirect('starting_page')
    context = {
        'login_form': login_form
    }
    return render(request, 'mytag_account/user_login_page.html', context)


def user_register_page(request):
    if request.user.is_authenticated:
        return redirect('userpanel:user-home-page')
    register_form = RegisterForm(request.POST or None)

    if register_form.is_valid():
        user_name = register_form.cleaned_data.get('user_name')
        password = register_form.cleaned_data.get('password')
        email = register_form.cleaned_data.get('email')
        user = User.objects.create_user(username=user_name, email=email, password=password)
        user.first_name = register_form.cleaned_data.get('first_name')
        user.last_name = register_form.cleaned_data.get('last_name')
        user.save()
        subject = 'خوش آمد گویی'
        message = f'سلام به دی جی تگ خوش امدید'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail(subject, message, email_from, recipient_list)
        mail_subject = 'فعال سازی حساب دی جی تگ'
        message = render_to_string('mytag_account/acc_active_email.html', {
            'user': user,
            'domain': get_current_site,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        send_mail(mail_subject, message, email_from, recipient_list)
        return render(request, 'mytag_account/active_email_done.html')

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


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')


def logout_user(request):
    e = logout(request)
    return render(request, 'mytag_account/user_login_page.html')
