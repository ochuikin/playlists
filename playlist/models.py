from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Playlist(models.Model):

    name = models.CharField(max_length=255)

    audiotracks = models.ManyToManyField('audiotrack.Audiotrack', related_name="playlists")

    def __unicode__(self):
        return self.name