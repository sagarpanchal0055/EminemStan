from django import forms
from .models import Album, Kamikaze, Revival

class AlbumModelForm(forms.ModelForm):
    class Meta:
        model = Album
        
        fields = [
            'song_name',
            'release_date',
            'content1',
            'content2',
            'content3',
            'about_song1',
            'about_song2',
        ]


class KamikazeModelForm(forms.ModelForm):
    class Meta:
        model = Kamikaze
        fields = [
            'song_name',
            'release_date',
            'content1',
            'content2',
            'content3',
            'about_song1',
            'about_song2',
        ]
        


class RevivalModelForm(forms.ModelForm):
    class Meta:
        model = Revival
        fields = [
            'song_name',
            'release_date',
            'content1',
            'content2',
            'content3',
            'about_song1',
            'about_song2',
        ]