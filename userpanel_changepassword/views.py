from django.contrib.auth import authenticate
from django.http import Http404
from django.shortcuts import render

# Create your views here.
from userpanel_changepassword.forms import ChangePasswordForm


def changepassword(request):
    context = {

    }
    MyChangePasswordForm = ChangePasswordForm(request.POST or None)
    context['ChangePasswordForm'] = MyChangePasswordForm
    if request.method == "POST":
        if MyChangePasswordForm.is_valid():
            user = request.user
            check = authenticate(username=user.username,
                                 password=MyChangePasswordForm.cleaned_data.get('old_password'))
            if check == request.user:
                if MyChangePasswordForm.data.get('new_password') == MyChangePasswordForm.data.get('password_config'):
                    user.set_password(MyChangePasswordForm.data.get('new_password'))
                    user.save()
                    context['success'] = 1
                else:
                    context['success'] = 3
            else:
                context['success'] = 2

    return render(request, 'userpanel_changepassword/userpanel_changepassword.html', context)
