from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    #return HttpResponse("heloooooo")
    return HttpResponse("<h1>heloooooo</h1>")
def myhome(request):
    #return render(request,'home.html')
    return render(request,'home.html',{'name':'faisal'})

def add(request):
    return render(request,'sum.html')

def add2(request):
    return render(request,'sum2.html')

def addnos(request):
    value1 = request.GET['number1']
    value2 = request.GET['number2']
    sum = int(value1)+int(value2)
    print(sum)
    return render(request,'sum.html',{'sum':sum})

def addnos2(request):
    value1 = request.POST['number1']
    value2 = request.POST['number2']
    sum = int(value1)+int(value2)
    print(sum)
    return render(request,'sum2.html',{'sum':sum})