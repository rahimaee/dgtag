from django.shortcuts import render, redirect
from home_newsletters.models import Newsletters


# Create your views here.

def save_email(request, *args, **kwargs):
    if request.POST:
        email = kwargs.get('Email')
        News_letters = Newsletters()
        News_letters.Email = email
        News_letters.save()
    return redirect('/')
