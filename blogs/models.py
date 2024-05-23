from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
from django.utils import timezone

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
    

class Blog(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    blog_name =  models.CharField(max_length=200, null=False, blank=False)
    title = models.CharField(max_length=200, null=False, blank=False)
    category = models.CharField(max_length=200)
    blog_image = models.ImageField(upload_to='blog_images', null=True, blank=True)
    content = models.TextField(null=False, blank=False)
    post_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.blog_name
