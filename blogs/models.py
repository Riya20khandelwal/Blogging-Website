from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

# Create your models here.


class CustomUser(AbstractUser):
    username = None
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    user_bio = models.CharField(max_length=200)
    user_profile_image = models.ImageField(upload_to="profile")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.email
