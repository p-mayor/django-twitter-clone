from django.contrib import admin

# Register your models here.
from .models import TwitterUser

admin.site.register(TwitterUser)