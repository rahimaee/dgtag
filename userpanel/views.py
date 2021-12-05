from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import Http404


# Create your views here.

def user_panel_home_page(request):
    context = {}
    return render(request, 'userpanel/user_panel_home_page.html', context)


