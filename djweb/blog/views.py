from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
# Create your views here.

def home(request):
    response = HttpResponse("Okay boy you are about to get your legs wet!!!\n\t")
    response.write(request.path)
    response.write('<h1>Appsecco testing</h1>')
    return response

def about(request):
    return HttpResponse('<h1>about us</h1>')

