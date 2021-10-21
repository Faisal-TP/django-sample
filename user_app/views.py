from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from user_app.forms import CustomeUserCreationForm
from user_app.forms import AddressForm

# Create your views here.
@login_required()
def dashboard(request):
    return render(request,'accounts/profile.html')
def createFn(request):
    if request.method=='POST':
        # form = UserCreationForm(request.POST)
        form = CustomeUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('create'))

    # form = UserCreationForm()
    form = CustomeUserCreationForm()
    return render(request,'registration/create.html',{'form':form})

def createaccount(request):
    form = AddressForm()
    return render(request,'registration/addressform.html',{'form':form})


