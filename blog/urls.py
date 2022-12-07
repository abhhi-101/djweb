from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='blog-home'),
    path('users/', views.searchusers, name='search_users'),
    path('ssrf/', views.ssrf, name='ssrf'),
    path('nosql/', views.nosql, name='nosql'),
    path('password-reset/', views.passwordreset, name='password-reset'),
]