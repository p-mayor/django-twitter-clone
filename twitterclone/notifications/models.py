from django.db import models

from twitterclone.tweets.models import Tweet
from twitterclone.twitterusers.models import TwitterUser

# Create your models here.
class Notification(models.Model):
     tweet = models.ForeignKey(Tweet,on_delete=models.CASCADE)
     tweetfor = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
     
     def __str__(self):
        return f"{self.tweetfor}{self.id}"