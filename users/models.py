from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):
    user_image = models.ImageField(upload_to='users/')
    phone = models.CharField(max_length=13)
    Ismingiz = models.CharField(max_length=150, blank=True)
    Sharifingiz = models.CharField(max_length=150, blank=True)
    Qayerdansiz = models.CharField(max_length=150, blank=True)
