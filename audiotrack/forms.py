# -*- coding: utf-8 -*-

from django import forms
from .models import Audiotrack


class AudiotrackListForm(forms.Form):

    search = forms.CharField(required=False)
    sort_field = forms.ChoiceField(choices=(('name', 'Name'), ('id', 'ID'), ('created_at', u'Дата создания')), required=False)

    def clean_search(self):
        search = self.cleaned_data.get('search')
        # raise forms.ValidationError(u'Я неправильный поиск!')
        return search


class AudiotrackCreateForm(forms.Form):

    title = forms.CharField(max_length=255)
    url = forms.CharField(widget=forms.Textarea)


class AudiotrackModifyForm(forms.ModelForm):
    class Meta:
        model = Audiotrack
        fields = ('name', 'url')

