from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now, localtime
import uuid


def photo_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4().hex[:16]}.{ext}'
    return f'user/photos/{instance.user.id}_{filename}'


class UserProfile(models.Model):
    # Links to Django's built-in User (already has username, email, password)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Extra profile fields not in User
    photo = models.ImageField(default='user/photos/default.png', upload_to=photo_upload_path)
    profile = models.TextField(default='thanks for interesting in my profile!', max_length=500)
    create_time = models.DateTimeField(default=now)
    update_time = models.DateTimeField(default=now)

    def __str__(self):
        return f'{self.user.username} - {localtime(self.create_time).strftime("%Y-%m-%d %H:%M:%S")}'
