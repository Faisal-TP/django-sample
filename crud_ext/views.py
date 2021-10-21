from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import Template,loader
from .models import *
from django.contrib.auth.models import User, auth
from django.core.files.storage import FileSystemStorage
from random import random
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

def index(request):
     return render(request,'index.html')

def register(request):
    if(request.method == "POST"):
        name = request.POST['name']
        address = request.POST['address']
        contact = request.POST['contact']
        gender = request.POST['gender']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        chkuser=Register.objects.filter(username = username).exists()
        if chkuser==True:
            return HttpResponse("Username Allredy Exist")
        else:
            new_register=Register(name=name,address=address,contact=contact,gender=gender,email=email,username=username,password=password)
            new_register.save()
    return render(request,'register.html')

def viewrecords(request):
    display_obj = Register.objects.all()
    return render(request,'view.html',{'datas':display_obj})
def delete(request,id):
    Register.objects.get(id=id).delete()
    return redirect('viewrecords')

def viewsingle(request,id):
    singleobj = Register.objects.get(id=id)
    return render(request,'update.html',{'data':singleobj})

def update(request,id):
    name = request.POST['name']
    address = request.POST['address']
    contact = request.POST['contact']
    gender = request.POST['gender']
    email = request.POST['email']
    Register.objects.filter(id=id).update(name=name,address=address,contact=contact,gender=gender,email=email)
    return redirect('viewrecords')

def login(request):
    if(request.method == "POST"):
        username = request.POST['username']
        password = request.POST['password']
        try:
            log = Register.objects.get(username=username)
            if log.username==username and log.password==password:
                #Create Session
                request.session['user_id']=log.id 
                #close create session
                return redirect('home')
            else:
                return render(request,'login.html',{'error':'Incorrect Username'})
            
        except Register.DoesNotExist:
            return render(request,'login.html',{'error':'Incorrect Password'})
    else:
        return render(request,'login.html')

def home(request):
    userId=request.session['user_id']
    profileobj = Register.objects.get(id=userId)
    profileobj.pic= Profile.objects.get(user_id_id = userId)
    #objStock = Register.objects.select_related('Profile')
    #print (objStock[0].profile.image)
    #my_dict = {"profile": profileobj,'file':profilepicbj}
    # for a in objStock:
    #     print('hhhhhhhhhhhhhhh')
    #     print(a.name)
    return render(request,'userhome.html',{'res':profileobj})

    
def profile(request):
    if(request.method == "POST"):
        # profile = request.POST['name']
        userId=request.session['user_id']
        #file upload
        myFile = request.FILES['image']
        file_name = str(random())+ myFile.name
        fs = FileSystemStorage()
        fs.save(file_name, myFile)
        #close file upload
        chkid=Profile.objects.filter(user_id_id = userId).exists()
        if chkid==True:
            Profile.objects.filter(user_id_id=userId).update(image=file_name)
            return redirect('home')
        else:
            file_upload=Profile(image=file_name,user_id_id=userId)
            file_upload.save()
            return redirect('home')
        return redirect('home')
def FnBase(request):
    return render(request,'base.html')

@api_view(['GET'])
def index(request):
    message = 'congratulations , you have created an API'
    return Response(message)