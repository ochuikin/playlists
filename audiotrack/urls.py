"""application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from .views import AudiotrackList, AudiotrackView, AudiotrackCreateView, AudiotrackModifyView

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', AudiotrackView.as_view(), name="detail"),
    url(r'^(?P<pk>\d+)/modify$', AudiotrackModifyView.as_view(), name="modify"),
    url(r'^create/$', AudiotrackCreateView.as_view(), name='audiotrack_create'),
    url(r'^$', AudiotrackList.as_view(), name="audiotrack_list"),
]
