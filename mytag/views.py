from django.shortcuts import render, redirect, Http404
from django.core.mail import send_mail


# home page
from mytag import settings


def home_page(request):
    context = {}
    return render(request, 'home_page.html', context)
