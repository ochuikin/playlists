from django.shortcuts import render
from django.shortcuts import resolve_url
from django.views.generic import ListView, DetailView, CreateView
from .forms import PlaylistCreateForm
from .models import Playlist


class PlaylistView(DetailView):

    model = Playlist
    template_name = 'playlist/playlist.html'
    context_object_name = 'playlist'


class PlaylistList(ListView):

    model = Playlist
    template_name = 'playlist/playlists.html'


class PlaylistCreateView(CreateView):

    model = Playlist
    fields = ('name', 'is_private')
    template_name = 'playlist/playlist_create.html'

    def dispatch(self, request, *args, **kwargs):
        self.form = PlaylistCreateForm(request.POST or None)
        self.form.is_valid()
        return super(PlaylistCreateView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PlaylistCreateView, self).form_valid(form)

    def get_success_url(self):
        return resolve_url('playlist:playlist_detail', pk=self.object.pk)


    # def dispatch(self, request, *args, **kwargs):
    #     self.sort_field = request.GET.get('sort_field')
    #     return super(PlaylistList, self).dispatch(request, *args, **kwargs)
    #
    # def get_queryset(self):
    #     return Playlist.objects.all().order_by(self.sort_field)[:10]