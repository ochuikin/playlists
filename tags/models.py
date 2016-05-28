# coding=utf-8

from __future__ import unicode_literals
from django.db import models


class Tag(models.Model):
    name = models.CharField(verbose_name=u'Название Тега', max_length=255)

    class Meta:
        verbose_name = u'Тег'
        verbose_name_plural = u'Теги'
        ordering = ('-name',)

    def __unicode__(self):
        return self.name
