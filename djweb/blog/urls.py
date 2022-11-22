from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about-us', views.about, name='blog-about')
]
