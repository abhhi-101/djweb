from django.contrib import admin
from .models import *

# Register your models here.

from .models import Profile
from blog.models import Posts
admin.site.register(Profile)
admin.site.register(Posts)
admin.site.register(demousers)
admin.site.register(Users)
admin.site.register(login)