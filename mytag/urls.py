"""mytag URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

# my import
from django.conf import settings
from django.conf.urls.static import static

from home_comments.views import comment_partial_view
from home_newsletters.views import news_letters_partial_view
from .views import home_page
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home_page, name='starting_page'),
    path('', include('mytag_cards.urls', namespace='mytag_cards')),
    path('', include('mytag_account.urls', namespace='account')),
    path('comment', comment_partial_view, name='comment'),
    path('newsletters', news_letters_partial_view, name='newsletters'),
    path('userpanel', include('userpanel.urls', namespace='userpanel')),
    path('userpanel/', include('userpanel_mytag.urls', namespace='userpanel_mytag')),
    path('userpanel/', include('userpanel_profile.urls', namespace='userpanel_profile')),
    path('userpanel/', include('userpanel_changepassword.urls', namespace='userpanel_changepassword')),

    path('admin/', admin.site.urls),

]
if settings.DEBUG:
    # add root static files
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # add media static files
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
