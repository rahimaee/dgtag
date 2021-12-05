from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from userpanel_profile.forms import UserForm, UserViewForm


def Profile(request):
    context = {

    }
    if request.method == "GET":
        User_Form = UserForm(request.POST or None, initial={
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'PhoneNumber': request.user.PhoneNumber,
            'profile': request.user.profile,

        })
        context['User_Form'] = User_Form
    if request.method == "POST":
        User_Form = UserForm(request.POST or None, request.FILES, initial={
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'PhoneNumber': request.user.PhoneNumber,
            'profile': request.user.profile,

        })
        if User_Form.is_valid():
            User_edit = User.objects.filter(id=request.user.id).first()
            first_name = User_Form.cleaned_data.get('first_name')
            last_name = User_Form.cleaned_data.get('last_name')
            PhoneNumber = User_Form.cleaned_data.get('PhoneNumber')
            profile = User_Form.cleaned_data.get('profile')
            User_edit.profile = profile
            User_edit.first_name = first_name
            User_edit.last_name = last_name
            User_edit.PhoneNumber = PhoneNumber
            User_edit.save()
        return redirect(reverse('userpanel_profile:views'))

    return render(request, 'userpanel_profile/user_panel_profile_update.html', context)


def profile_view(request):
    user = User.objects.filter(pk=request.user.pk).first()
    context = {
        'user': user
    }
    return render(request, 'userpanel_profile/user_panel_profile_view.html', context)
