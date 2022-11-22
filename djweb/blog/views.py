from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
# Create your views here.

posts = [
    {
        'name':'srush',
        'age':21,
        'education':'b.tech',
        'interest':'abhhi'
    },
    {
        'name':'abhhi',
        'age':21,
        'education':'b.tech',
        'interest':'srushti'
    }
]

def home(request):
    context = {
        'title':'Home page baby'
    }
    return render(request, 'blog/home.html', context)

def about(request):
    context = {
        'title': 'Blogging using template',
        'post' : posts
    }
    return render(request, 'blog/about.html', context)

