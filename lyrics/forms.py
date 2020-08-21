from django import forms
from .models import Lyrics

class LyricsModelForm(forms.ModelForm):
    class Meta:
        model = Lyrics
        fields = [
            'album_name',
            'album_id',
        ]