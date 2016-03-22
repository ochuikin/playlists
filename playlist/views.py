from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import Playlist


class PlaylistView(DetailView):

    model = Playlist
    template_name = 'playlist/playlist.html'
    context_object_name = 'playlist'


class PlaylistList(ListView):

    model = Playlist
    template_name = 'playlist/playlists.html'