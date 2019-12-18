from django.contrib import admin
from django.urls import path, include
from twitterclone.tweets import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.tweetlist, name='tweetlist'),
]
