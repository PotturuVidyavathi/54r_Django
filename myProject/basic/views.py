from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.db import connection

from django.views.decorators.csrf import csrf_exempt
# from basic.models import StudentNew,Users
from django.contrib.auth.hashers import make_password,check_password
from django.conf import settings
import json
# import jwt

# Create your views here.
def sample(request):
    return HttpResponse("Hello World")

def sample1(request):
    return HttpResponse("Welcome to Django")

def sampleInfo(request):

    # data = {"name":"Abc","age":22,"city":"Hyd"}
    data = [1,2,3,4,5,6,7,8,9]
    return JsonResponse(data)

#to get the dynamic response as passing through the url called as query parameters(?x=)

# query params ---> used to pass extra information throught url while making request.

def dynamicResponse(request):
    name = request.GET.get("name"," ") 
    city=request.GET.get("city",'hyd')
    return HttpResponse(f'hello {name} from {city}')


    

# to test database connection through api
def health(request):

    try:
        with connection.cursor() as c:
            c.execute("sELECT 1")
        return JsonResponse({"status":"ok","db":"connected"})
    except Exception as e:
        return JsonResponse({"status":"error","db":str(e)})


def addStudent(request):

    # if request.method=="POST":
    #     pass
    # return JsonResponse({"error":"use post method"}) 
    if request.method == 'POST':
        data = json.load(request.body)



@csrf_exempt
def login(request):
    if request.method=="POST":
        data=request.POST
        print(data)
        username=data.get('username')
        password=data.get("password")        
        try:
            user=Users.objects.get(username=username)
            if check_password(password,user.password):
                payload={"username":username,"email":user.email,"id":user.id}
                token=jwt.encode(payload,settings.SECRET_KEY,algorithm="HS256")

                return JsonResponse({"status":'successfully loggedin','token':token},status=200)
            else:
                return JsonResponse({"status":'failure','message':'invalid password'},status=400)
        except Users.DoesNotExist:
            return JsonResponse({"status":'failure','message':'user not found'},status=400)







# ==========templates ===========

def home(request):
    return render(request,'home.html')

def aboutus(request):
    return render(request,'aboutus.html')

def welcome(request):
    return render(request,'welcome.html')