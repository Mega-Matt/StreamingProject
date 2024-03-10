from django.core.validators import FileExtensionValidator
from django.db import models


class Channel(models.Model):
    name = models.CharField(max_length=200, unique = True)
    description = models.TextField(max_length=2000)
    is_live = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    channel = models.ManyToManyField(Channel)
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Livestream(models.Model):
    title = models.CharField(max_length=500)
    video_recording = models.FileField(upload_to='videos_uploaded', null=True,
                                       validators=[FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    created_at = models.DateTimeField(auto_now_add=True)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
