from django.db import models
from django.contrib.auth.models import User

class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    audio_file = models.FileField(upload_to='songs/')
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    privacy_access = models.CharField(max_length=20)
    allowed_emails = models.ManyToManyField(User, related_name='allowed_songs', blank=True)
