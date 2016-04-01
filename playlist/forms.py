# -*- coding: utf-8 -*-

from django import forms
from .models import Playlist


class PlaylistCreateForm(forms.Form):

    #name = forms.CharField(max_length=255)
    is_private = forms.BooleanField(required=False)

