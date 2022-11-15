from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model



class User(AbstractUser):
    mobileNumber = models.IntegerField(null=True,blank=True)
    cityname = models.CharField(max_length=200,null=True,blank=True)
    statename = models.CharField(max_length=200,null=True,blank=True)
    countryname = models.CharField(max_length=250,null=True,blank=True)

    
    def __str__(self):
        return self.username


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username
      