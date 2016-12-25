from __future__ import unicode_literals

from django.db import models
# The model is the blueprint for a database
# Create your models here.
class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = model.CharField(max_length=500)
    genre = model.CharField(max_length=100)
    album_logo = models.CharField(max_length=100)

class Song():
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    
