from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from .models import *
from rest_framework import viewsets
# from . import serializers
# from django_api.serializers import RegisterSerializer


#Create your views here.
@api_view(['POST'])
def index(request):
	data = request.data
	new_register=Register_api(name=data['name'],address=data['address'],contact=data['contact'],gender=data['gender'],email=data['email'])
	new_register.save()
	return Response("product added successfully")
@api_view(['GET'])
def getdata(request):
	queryset = Register_api.objects.all()
	data = [{'id': blog.id, 'name': blog.name,'address':blog.address,'contact':blog.contact,'gender':blog.gender,'email':blog.email} for blog in queryset]
	return JsonResponse({'data':data})
@api_view(['delete'])
def deldata(request):
	data = request.data
	Register_api.objects.get(id=data['id']).delete()
	# print(data['id'])

	return Response("product Deleted successfully")


# class RegisterViewSet(viewsets.ModelViewSet):
# 	queryset = Register_api.objects.all()
# 	serializer_class = serializers.RegisterSerializer