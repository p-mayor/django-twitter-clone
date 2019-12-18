from django.db import models

from django.contrib.auth.models import User


class TwitterUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,)
    name = models.CharField(max_length=20)
    bio = models.TextField("Bio", null=True, blank=True)
    tweet_count = models.IntegerField()
    follower_count = models.IntegerField()

    def __str__(self):
        return self.name
