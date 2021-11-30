from django.shortcuts import render


# Create your views here.

def user_panel_home_page(request):
    context = {}
    return render(request, 'userpanel/user_panel_home_page.html', context)
