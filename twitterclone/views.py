from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test

from twitterclone.twitterusers.models import TwitterUser
from twitterclone.tweets.models import Tweet

@login_required
def tweet(request):
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = TweetForm()
    return render(request, 'twitterclone/tweets/tweet.html', {'form':form})

def index(request):
    latest_tweet_list = Tweet.objects.order_by('time')
    context = {'latest_tweet_list': latest_tweet_list}
    return render(request, 'twitterclone/tweets/tweetlist.html', context)

# def detail(request, recipe_id):
#     recipe = get_object_or_404(Recipe, pk=recipe_id)
#     return render(request, 'recipe/detail.html', {'recipe': recipe})

# def author(request, author_id):
#     author = get_object_or_404(Author, pk=author_id)
#     author_recipe_list = Recipe.objects.filter(author=author_id)
#     return render(request, 'recipe/author.html', 
#         {'author': author, 'author_recipe_list':author_recipe_list}
#     )

# # ref: https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html

# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return HttpResponseRedirect('/')
#     else:
#         form = UserCreationForm()
#     return render(request, 'recipe/signup.html', {'form': form})


# def logout_view(request):
#     logout(request)
#     return HttpResponseRedirect('/')
