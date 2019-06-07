from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    avatar = models.ImageField(upload_to='image/avatar', default='image/avatar/default_avatar.jpg')
    