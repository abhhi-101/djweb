from django.contrib import admin

# Register your models here.

from .models import Profile
from blog.models import Posts
admin.site.register(Profile)
admin.site.register(Posts)
