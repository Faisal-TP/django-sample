from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.http.response import JsonResponse
from django.core import serializers
# Create your views here.

def home(request):
	#return HttpResponse("hiiiiii")
	return render(request,'createac.html')

def add(request):
	name = request.POST['name']
	address = request.POST['address']
	contact = request.POST['contact']
	gender = request.POST['gender']
	email = request.POST['email']
	username = request.POST['username']
	password = request.POST['password']
	new_register=Registerajax(name=name,address=address,contact=contact,gender=gender,email=email,username=username,password=password)
	new_register.save()
	# return render(request,'createac.html')
	return JsonResponse({'message':'Inserted'})

def loadfun(request):
	return render(request,'display.html')

def displaydata(reuest):
	queryset = Registerajax.objects.all()
	data = [{'id': blog.id, 'name': blog.name,'address':blog.address,'contact':blog.contact,'gender':blog.gender} for blog in queryset]
	# product_list = []
	# for obj in queryset:
	# 	product_list.append(obj)
	return JsonResponse({'data':data})

def deletedata(request):
	id = request.POST['key_id']
	Registerajax.objects.get(id=id).delete()
	return JsonResponse({'message':'Data Deleted'})

def fnviewsingle(request):
	id = request.POST['single_id']
	blog = Registerajax.objects.get(id=id)
	# sdata = [{'id': blog.id, 'name': blog.name,'address':blog.address,'contact':blog.contact,'gender':blog.gender} for blog in singleobj]
	sdata = [{'id': blog.id, 'name': blog.name,'address':blog.address,'contact':blog.contact,'gender':blog.gender}]
	return JsonResponse({'sdata':sdata})
def fnfileupload(request):
	 if(request.method == "POST"):
		 print("hiiiiiii")
		 name = request.POST['name']
		 file = request.FILES['file']
		 print(name)
		 print(file.name)
		 return JsonResponse({'message':'Data Uploaded'})
	 else:
		 return render(request,'fileupd.html')