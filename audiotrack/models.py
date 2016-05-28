# coding: utf-8

from __future__ import unicode_literals

from django.db import models
from django.conf import settings

class Audiotrack(models.Model):

    name = models.CharField(verbose_name=u'Название трека', max_length=255)

    url = models.CharField(blank=True, verbose_name=u'Адрес трека', max_length=255)
    audio_file = models.FileField(null=True, blank=True, upload_to='uploads/')

    tags = models.ManyToManyField("tags.Tag", verbose_name=u'Теги')

    length = models.FloatField(blank=True)

    created_at = models.DateTimeField(verbose_name=u'Дата создания', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name=u'Дата последнего изменения', auto_now_add=True)

    author = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'Аудиотрек'
        verbose_name_plural = u'Аудиотреки'
        ordering = ('-name', )
