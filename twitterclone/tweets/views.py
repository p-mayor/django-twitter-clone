from django.shortcuts import render
from .models import Tweet

# Create your views here.
def tweetlist(request):
    latest_tweet_list = Tweet.objects.order_by('time')
    context = {'latest_tweet_list': latest_tweet_list}
    return render(request, 'tweetlist.html', context)