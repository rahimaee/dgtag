from django.urls import path
from .views import *

app_name = 'userpanel_map'
urlpatterns = [
    path('map', all_map_user, name='all_map'),
    path('map/add', add_map_user, name='add_map'),
    path('map/update/<MapId>', update_map_user, name='update_map'),
    path('map/detail/<MapId>', view_map_user, name='detail_map'),

]
