"""react URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from miniBond.views import *
from django.views.generic.base import RedirectView
#,areaType,target,propertyData):
app_name = 'miniBond'
urlpatterns = [
    url(r'^$', index),
    url(r'^hello/', hello),
    url(r'^favicon.ico$', RedirectView.as_view(url=r'staticaaa/favicon.ico')),
    url(r'^refreshCache/', refreshCache),
    url(r'^myname/(\d{1,2})/$', myname),
    url(r'^index/', index, name='index'),
    url(r'^log/(?P<areaType>.+)/(?P<target>.+)/(?P<propertyData>.+)/$', logTrace),
    url(r'^towx/(?P<uuid>[^/]+)/$', toWx)
]
