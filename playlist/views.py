from django.http import HttpResponse
try:
    from django.utils import simplejson as json
except ImportError:
    import json
from django.shortcuts import resolve_url
from django.views.generic import ListView, DetailView, CreateView
from .forms import PlaylistCreateForm
from .models import Playlist
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404


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


@login_required
@require_POST
def like(request):
    if request.method == 'POST':
        user = request.user
        slug = request.POST.get('slug', None)
        playlist = get_object_or_404(Playlist, slug=slug)

        if playlist.likes.filter(id=user.id).exists():
            playlist.likes.remove(user)
            message = 'You disliked this'
        else:
            playlist.likes.add(user)
            message = 'You liked this'

    ctx = {'likes_count': playlist.total_likes, 'message': message}
    # use mimetype instead of content_type if django < 5
    return HttpResponse(json.dumps(ctx), content_type='application/json')