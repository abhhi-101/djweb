from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='blog-home'),
    path('users/', views.searchusers, name='search_users'),
    #path('nosql/', views.nosql, name='nosql'),
    path('ssrf/', views.ssrf, name='ssrf'),
    path('nosql/', views.nosql, name='nosql'),
]