from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView
from django.views.generic import ListView
from .models import Audiotrack


class AudiotrackView(DetailView):

    model = Audiotrack
    template_name = 'audiotrack/audiotrack.html'
    context_object_name = 'audiotrack'

class AudiotrackList(ListView):

    model = Audiotrack
    template_name = 'audiotrack/audiotracks.html'

#def show_audiotrack(request, audiotrack_id=0):
#    return render(request, 'audiotrack/audiotrack.html', {"audiotrack_id": audiotrack_id})

#def show_audiotracks(request):
#    return render(request, 'audiotrack/audiotracks.html')