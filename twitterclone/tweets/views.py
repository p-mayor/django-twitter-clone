from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test

from .models import Tweet
from .forms import TweetForm

# Create your views here.
def tweetlist(request):
    latest_tweet_list = Tweet.objects.order_by('time')
    context = {'latest_tweet_list': latest_tweet_list}
    return render(request, 'tweetlist.html', context)

@login_required
def tweetform(request):
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = TweetForm()
    return render(request, 'tweetform.html', {'form':form})