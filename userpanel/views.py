from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import Http404


# Create your views here.
@login_required(login_url='/login')
def user_panel_home_page(request):
    context = {}
    return render(request, 'userpanel/user_panel_home_page.html', context)


