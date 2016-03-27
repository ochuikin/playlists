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


    # def dispatch(self, request, *args, **kwargs):
    #     self.sort_field = request.GET.get('sort_field')
    #     return super(PlaylistList, self).dispatch(request, *args, **kwargs)
    #
    # def get_queryset(self):
    #     return Playlist.objects.all().order_by(self.sort_field)[:10]