from django.contrib.auth.decorators import login_required
try:
    from django.utils import simplejson as json
except ImportError:
    import json
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, resolve_url
from django.views.decorators.http import require_POST
from django.views.generic import DetailView, CreateView, UpdateView
from django.views.generic import ListView
from playlist.models import Playlist
from .forms import AudiotrackListForm, AudiotrackCreateForm, AudiotrackModifyForm
from .models import Audiotrack


class AudiotrackCreateView(CreateView):
    model = Audiotrack
    fields = ('name', 'url', 'audio_file')
    template_name = 'audiotrack/create.html'

    def dispatch(self, request, *args, **kwargs):
        self.form = AudiotrackCreateForm(request.POST or None)
        self.form.is_valid()
        return super(AudiotrackCreateView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.length = 0

        # img = self.get_form_kwargs().get('files')['audio_file']
        # form.instance.audio_file = img;

        obj = Audiotrack(
            name = form.instance.name,
            url = form.instance.url,
            audio_file = self.get_form_kwargs().get('files').get('audio_file'),
            length = 0,
            author = self.request.user)
        obj.save()
        self.id = obj.id
        return HttpResponseRedirect(self.get_success_url())
        # return super(AudiotrackCreateView, self).form_valid(form)

    def get_success_url(self):
        return resolve_url('audiotrack:detail', pk=self.id)


class AudiotrackView(DetailView):
    model = Audiotrack
    template_name = 'audiotrack/audiotrack.html'
    context_object_name = 'audiotrack'

    def get_context_data(self, **kwargs):
        context = super(AudiotrackView, self).get_context_data(**kwargs)

        context['playlists'] = Playlist.objects.all()
        return context


class AudiotrackModifyView(UpdateView):
    model = Audiotrack
    template_name = 'audiotrack/modify.html'
    context_object_name = 'audiotrack'

    # fields = ('name', 'url', 'tags')
    form_class = AudiotrackModifyForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(AudiotrackModifyView, self).form_valid(form)

    # def get_context_data(self, **kwargs):
    #     context = super(AudiotrackModifyView, self).get_context_data(**kwargs)
    #     context['modify_form'] = self.modify_form
    #     return context

    def get_success_url(self):
        return resolve_url('audiotrack:detail', pk=self.object.pk)


class AudiotrackList(ListView):
    model = Audiotrack
    template_name = 'audiotrack/audiotracks.html'

    def dispatch(self, request, *args, **kwargs):
        self.form = AudiotrackListForm(request.GET)
        self.form.is_valid()
        self.create_form = AudiotrackCreateForm(request.POST or None)
        return super(AudiotrackList, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        #exception when logout
        queryset = Audiotrack.objects.filter(author=self.request.user)
        if self.form.cleaned_data.get('search'):
            # queryset = queryset.filter(name=self.form.cleaned_data['search'])
            queryset = queryset.filter(name__contains=self.form.cleaned_data['search'])
        if self.form.cleaned_data.get('sort_field'):
            queryset = queryset.order_by(self.form.cleaned_data['sort_field'])[:10]
        return queryset

    def get_context_data(self, **kwargs):
        context = super(AudiotrackList, self).get_context_data(**kwargs)
        context['form'] = self.form
        context['create_form'] = self.create_form
        return context

@login_required
@require_POST
def add(request):
    if request.method == 'POST':
        user = request.user
        track_id = request.POST.get('track_id', None)
        playlist_id = request.POST.get('playlist_id', None)
        print "track_id", track_id
        print "playlist_id", playlist_id
        Playlist.objects.get(id=playlist_id).audiotracks.add(Audiotrack.objects.get(id=track_id))
    ctx = {'message':'completed'}
    return HttpResponse(json.dumps(ctx), content_type='application/json')