from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User

from twitterclone.twitterusers.models import TwitterUser
from twitterclone.tweets.models import Tweet

from .forms import TweetForm

def detail(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id)
    return render(request, 'detail.html', {'tweet': tweet})

@login_required
def index(request):
    user_data = TwitterUser.objects.filter(user=request.user)
    current_user = TwitterUser.objects.get(user=request.user)
    followers = user_data[0].followers.all()
    follower_tweet_list = Tweet.objects.filter(twitter_user=current_user)
    for follower in followers:
        follower_tweet_list = follower_tweet_list | Tweet.objects.filter(twitter_user=follower)
    follower_tweet_list = follower_tweet_list.order_by('-time')
    context = {'follower_tweet_list': follower_tweet_list}
    return render(request, 'base.html', context)

def tweetlist(request):
    return render(request, 'tweetlist.html')

@login_required
def add_tweet(request):
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            body = form.cleaned_data.get('body')
            user = get_object_or_404(TwitterUser, pk=request.user.id)
            a = Tweet(body=body, twitter_user=user)
            a.save()
            return HttpResponseRedirect('/')
    else:
        form = TweetForm()
    return render(request, 'tweetform.html', {'form':form})


def profile(request, twitteruser_id):
    twitteruser = get_object_or_404(TwitterUser, pk=twitteruser_id)
    twitteruser_tweet_list = Tweet.objects.filter(twitter_user=twitteruser_id)
    return render(request, 'twitteruser.html', 
        {'twitteruser': twitteruser, 'twitteruser_tweet_list':twitteruser_tweet_list}
    )

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)

            a = TwitterUser(name=username,bio='', user=user, tweet_count=0, follower_count=0)
            a.save()
            
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def follow(request, twitteruser_id):
    current_user = TwitterUser.objects.get(user=request.user)
    user_to_follow = TwitterUser.objects.get(user=twitteruser_id)
    current_user.followers.add(user_to_follow)
    return HttpResponseRedirect('/')

def unfollow(request, twitteruser_id):
    current_user = TwitterUser.objects.get(user=request.user)
    user_to_unfollow = TwitterUser.objects.get(user=twitteruser_id)
    current_user.followers.remove(user_to_unfollow)
    return HttpResponseRedirect('/')