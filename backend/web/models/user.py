from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profile_pics/', default='photos/default.png', blank=True, null=True)
    username = models.CharField(max_length=128, unique=True)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=256, blank=True, null=True)
    phone = models.CharField(max_length=32, blank=True, null=True)
    
    