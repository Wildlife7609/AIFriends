from django.utils.timezone import now, localtime
from django.db import models
from web.models.user import UserProfile
import uuid


def photo_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4().hex[:10]}.{ext}'
    return f'character/photos/{instance.author.user_id}_{filename}'

def background_image_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4().hex[:10]}.{ext}'
    return f'character/background_image/{instance.author.user_id}_{filename}'

class Character(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to=photo_upload_path)
    prompt = models.TextField(max_length=100000)
    background_image = models.ImageField(upload_to=background_image_upload_path)
    create_time = models.DateTimeField(default=now)
    update_time = models.DateTimeField(default=now)
    is_public = models.BooleanField(default=False)
    greeting = models.TextField(max_length=500, blank=True, null=True)
    profile = models.TextField(max_length=100000)
    tags = models.CharField(max_length=500, blank=True, null=True)
    voice_id = models.CharField(max_length=100, blank=True, null=True)
    chat_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.author.user.username} - {self.name} - {localtime(self.create_time).strftime('%Y-%m-%d %H:%M:%S')}"
