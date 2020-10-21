from django import forms
from .models import Song

class SongCreate(forms.ModelForm):
    class Meta:
        model = Song
        fields = '__all__'
        fields = ("artist", "name")
