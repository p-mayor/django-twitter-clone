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
    path('twitteruser/<int:twitteruser_id>/', views.profile, name='twitteruser'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='login.html'),name='logout'),
]
