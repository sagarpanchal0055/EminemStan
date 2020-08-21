from django.db import models
from django.urls import reverse

# Create your models here.
class Lyrics(models.Model):
    album_id = models.CharField(max_length = 100)
    album_name = models.CharField(max_length = 100)

    def get_absolute_url(self):
        return reverse("lyrics:lyrics-detail", kwargs = {"album_id":self.album_id})
