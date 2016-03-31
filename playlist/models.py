# coding: utf-8

from __future__ import unicode_literals
from django.db import models


class Playlist(models.Model):

    name = models.CharField(verbose_name=u'Название плейлиста', max_length=255)

    audiotracks = models.ManyToManyField('audiotrack.Audiotrack', verbose_name=u'Список треков', related_name="playlists")

    created_at = models.DateTimeField(verbose_name=u'Дата создания', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name=u'Дата последнего изменения', auto_now_add=True)

    is_private = models.BooleanField(default=True, verbose_name=u'Закрытый плейлист')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'Плейлист'
        verbose_name_plural = u'Плейлисты'
        ordering = ('-name', )
