from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Audiotrack(models.Model):



    name = models.CharField(max_length=255)

    url = models.CharField(max_length=255)
