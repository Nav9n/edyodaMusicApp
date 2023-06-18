from django import forms
from .models import Song

class UploadSongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'artist', 'audio_file', 'privacy_access', 'allowed_emails']
