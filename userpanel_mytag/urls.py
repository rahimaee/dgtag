from django.urls import path, include
from .views import HomepageView, MyTagDetailView, MyTagCreate, MyTagUpdate, MyTagDelete

app_name = 'userpanel_mytag'
urlpatterns = [
    path('mytag/', HomepageView.as_view(), name='homepage'),
    path('mytag/<int:pk>/', MyTagDetailView.as_view(), name='detail'),
    path('mytag/create/', MyTagCreate, name='create'),
    path('mytag/update/<int:pk>/', MyTagUpdate.as_view(), name='update'),
    path('mytag/delete/<int:pk>/', MyTagDelete.as_view(), name='delete'),
]
