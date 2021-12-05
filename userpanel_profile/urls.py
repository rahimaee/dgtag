from django.urls import path
from .views import Profile, profile_view

app_name = 'userpanel_profile'
urlpatterns = [
    path('profile/update', Profile, name='Profile'),
    path('profile/', profile_view, name='views'),
]
