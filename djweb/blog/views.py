from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from users.models import Users, login
import requests
import pymongo

## connecting to db for Pymongo
client = pymongo.MongoClient('mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.6.0')
dbname = client['inj']
db_users = dbname['users']

def nosql(request):
    user = request.GET.get('user')
    password = request.GET.get('pass')
    if user:
        result = bool(db_users.find_one({"$where": "this.name == '" + user + "' && this.type == '" + password + "' " }))
        if result == True:
            announce = "You are a valid user!"
        else:
            announce = "Who are you?"
        context = {
            "result" : announce
        }       
        return render(request, 'inj/nosql.html', context)
    else:
        return render(request, 'inj/nosql.html')



# Create your views here.
def home(request):
    context = {
        'title':'Home page baby'
    }
    return render(request, 'blog/home.html', context)

# vulnerable to XSS
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

# vulnerable to SSRF
def ssrf(request):
    if request.user.is_authenticated:
        url = request.POST.get('imgUrl')
        print(url)
        if url:
            url = request.POST.get('imgUrl')
            res = requests.get(url, stream = True)
            file_name = "image"
        else:
            return render(request, 'blog/ssrf.html')
        if res.status_code == 200:
            open("img", "wb").write(res.content)
            print(res.content)
            content = {
                'response' : res.content 
            }
            '''with open(file_name,'wb') as f:
                shutil.copyfileobj(res.raw, f)
            print('Image sucessfully Downloaded: ',file_name)
        else:
            print('Image Couldn\'t be retrieved')'''
        
    return render(request, 'blog/ssrf.html', content)


"""def nosql(request):
    if request.user.is_authenticated:
        name=request.POST.get('name')
        password=request.POST.get('pass')
        '''nosql_query = "db.users_login.insertOne({user:'"+str(name)+"',password:'"+str(password)+"'})"
        val=login.objects.raw("db.users_login.find({user:'abhhi'})")
        #user=val[0].user
        return render(request, 'blog/nosql.html',{"user1":str(val)})'''
        if name:
            if login.objects.all().filter(user=name):

                nosql_query = "db.users_login.find({user:'"+name+"'} && {password='"+password+"'})"
                #print(nosql_query)
                try:
                    print("\nin try\n")
                    login.objects.raw_query(nosql_query)
                except:
                    #print("\nin except\n")
                    login.objects.raw_query(nosql_query)
                    return render(
                        request, 
                        'blog/nosql.html',
                        {
                            "wrongpass":password,
                            "sql_error":"nosql_query"
                        })
            else:
                return render(request, 'blog/nosql.html',{"no": "User not found"})
        else:
            return render(request, 'blog/nosql.html')
    else:
        return redirect('login')"""