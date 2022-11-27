from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from users.models import Users
# Create your views here.

def home(request):
    context = {
        'title':'Home page baby'
    }
    return render(request, 'blog/home.html', context)

def about(request):
    context = {
        'title': 'Blogging using template',
        'post' : 'posts'
    }
    return render(request, 'blog/about.html', context)


def searchusers(request):
    if request.user.is_authenticated:
        q=request.GET.get('q','')
        f = Users.objects.all().filter(user=q)
        if f:
            args={"user_searched":f[0].user,"firstname":f[0].first_name,"lastname":f[0].last_name}
            return render(request,'blog/users.html',args)
        else:
            return render(request,'blog/users.html', {'query': q})
    else:
        return redirect('login')

