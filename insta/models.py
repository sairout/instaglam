from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class InstaUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    profilepic = models.ImageField(upload_to='')
    followers = models.PositiveIntegerField(default=0)
    following = models.PositiveIntegerField(default=0)


class Photo(models.Model):
    photo = models.ImageField(upload_to='')
    caption = models.CharField(max_length=256, blank=True, null=True)
    likes = models.PositiveIntegerField(default=0)
    comments = models.PositiveIntegerField(default=0)
    owner = models.CharField(max_length=200)
    date_uploaded = models.DateTimeField(auto_now=True)
    owner_profilepic = models.ImageField()


class Follower(models.Model):
    username = models.CharField(max_length=200)
    follower = models.CharField(max_length=200)


class Likes(models.Model):
    postid = models.IntegerField()
    liker = models.CharField(max_length=256)
    date = models.DateTimeField(auto_now=True)


class Comments(models.Model):
    postid = models.IntegerField()
    comment = models.CharField(max_length=500)
    commenter = models.CharField(max_length=256)
    date = models.DateTimeField(auto_now=True)
