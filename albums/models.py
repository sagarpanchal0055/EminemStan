from django.db import models
from django.urls import reverse

# Create your models here.
# class for album MTBMB

class Album(models.Model):
    song_name = models.CharField(max_length = 100)
    release_date = models.CharField(max_length = 100)
    content1 = models.TextField()
    content2= models.TextField(blank = True)
    content3 = models.TextField(blank = True)
    about_song1 = models.TextField(blank = True)
    about_song2 = models.TextField(blank = True)

    def get_absolute_url(self):
        return reverse("albums:album-detail", kwargs = {"id":self.id})


# class for Kamikaze
class Kamikaze(models.Model):
    song_name = models.CharField(max_length = 100)
    release_date = models.CharField(max_length = 100)
    content1 = models.TextField()
    content2= models.TextField(blank = True)
    content3 = models.TextField(blank = True)
    about_song1 = models.TextField(blank = True)
    about_song2 = models.TextField(blank = True)

    # @property
    # def sorted_instance_set(self):
    #     return self.instance_set.order_by('song_name')

    def get_absolute_url(self):
        return reverse("albums:kamikaze-detail", kwargs = {"id":self.id})


# class for revival
class Revival(models.Model):
    song_name = models.CharField(max_length = 100)
    release_date = models.CharField(max_length = 100)
    content1 = models.TextField()
    content2= models.TextField(blank = True)
    content3 = models.TextField(blank = True)
    about_song1 = models.TextField(blank = True)
    about_song2 = models.TextField(blank = True)

    def get_absolute_url(self):
        return reverse("albums:revival-detail", kwargs = {"id":self.id})