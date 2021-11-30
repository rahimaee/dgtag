from django.urls import path, include
from .views import user_panel_home_page

app_name = 'userpanel'
urlpatterns = [
    path('', user_panel_home_page, name='user-home-page'),
]
