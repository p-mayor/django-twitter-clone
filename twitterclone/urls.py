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
    path('tweetform/', views.tweetform, name='tweetform'),
    path('<int:tweet_id>/', views.detail, name='detail'),
    path('twitteruser/<int:twitteruser_id>/', views.twitteruser, name='twitteruser'),
    path('signup/', custom_auth_views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='recipe/login.html'),name='login'),
]
