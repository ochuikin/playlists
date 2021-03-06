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
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import logout, login
from playlist.views import PlaylistList
from core.views import RegisterFormView

urlpatterns = [
    url(r'^$', PlaylistList.as_view(), name="playlist_list"),
    url(r'^admin/', admin.site.urls),
    url(r'^audiotrack/', include('audiotrack.urls', namespace="audiotrack")),
    url(r'^playlists/', include('playlist.urls', namespace="playlist")),
    url(r'^login/$', login, {'template_name': 'registration/login.html'}, name="login"),
    url(r'^logout/$', logout, {'template_name': 'registration/logged.html'}, name="logout"),
    url(r'^register/$', RegisterFormView.as_view()),
    # url('^', include('django.contrib.auth.urls'))
]
