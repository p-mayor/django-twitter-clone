from django.db import models
from twitterclone.twitterusers.models import TwitterUser
from django.core.validators import MaxLengthValidator
# Create your models here.

class Tweet(models.Model):
    twitter_user = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    body = models.TextField("Body", null=True, blank=True, validators=[MaxLengthValidator(140)])
    time = models.DateTimeField(auto_now_add=True)