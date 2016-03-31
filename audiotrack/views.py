from django.shortcuts import render, resolve_url
from django.views.generic import DetailView, CreateView, UpdateView
from django.views.generic import ListView
from .forms import AudiotrackListForm, AudiotrackCreateForm, AudiotrackModifyForm
from .models import Audiotrack


class AudiotrackCreateView(CreateView):
    model = Audiotrack
    fields = ('name', 'url')
    template_name = 'audiotrack/create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(AudiotrackCreateView, self).form_valid(form)

    def get_success_url(self):
        return resolve_url('audiotrack:detail', pk=self.object.pk)


class AudiotrackView(DetailView):
    model = Audiotrack
    template_name = 'audiotrack/audiotrack.html'
    context_object_name = 'audiotrack'


class AudiotrackModifyView(UpdateView):
    model = Audiotrack
    template_name = 'audiotrack/modify.html'
    context_object_name = 'audiotrack'

    # def dispatch(self, request, *args, **kwargs):
    #
    #     post = Audiotrack.objects.get(id=self.get_object().pk)
    #     self.modify_form = AudiotrackModifyForm(data=request.POST or None, instance=post)
    #
    #     if request.POST:
    #         if self.modify_form.is_valid():
    #             post = self.modify_form.save(commit=False)
    #             post.author = request.user
    #             post.save()
    #
    #     return super(AudiotrackModifyView, self).dispatch(request, *args, **kwargs)

    fields = ('name', 'url')

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
