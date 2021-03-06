"""cloudtest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib.auth.views import logout
from django.urls import path
from django.conf.urls import url
from cloudtest import views, settings

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^rooms-tariff', views.room, name='room-tariff'),
    url(r'^home', views.home, name='home'),
    url(r'^introduction', views.introduction, name='introduction'),
    url(r'^gallery', views.gallery, name='gallery'),
    url(r'^contact', views.contact, name='contact'),
    url(r'^room-details', views.roomdet, name='room-details'),
    url(r'^login', views.loginp, name='login'),
    url(r'^signup', views.signup, name='signup'),
    url(r'^profile', views.profile, name='profile'),
    url(r'^logout/$', logout, {'next_page': '/login'}, name='logout'),
]
