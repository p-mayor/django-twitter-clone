from django.contrib import admin
from django.urls import path, include
from twitterclone.twitterusers import views as user_views
from twitterclone.tweets import views as tweet_views
from twitterclone.authentication import views as custom_auth_views
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='homepage'),
    path('tweetform/', views.add_tweet, name='add_tweet'),
    path('<int:tweet_id>/', views.detail, name='detail'),
    path('twitteruser/<int:twitteruser_id>/', views.Profile.as_view(), name='twitteruser'),
    path('follow/<int:twitteruser_id>/', views.Follow.as_view(), name='follow'),
    path('unfollow/<int:twitteruser_id>/', views.Unfollow.as_view(), name='unfollow'),
    path('signup/', views.Signup.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='login.html'),name='logout'),
]
