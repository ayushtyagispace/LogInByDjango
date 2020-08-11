from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
from .forms import CreateUserForm

def home(request):
    return render(request,'home.html')


def registerPage(request):
    #if request.user.is_valid:
     #   return redirect('home')
    #else:
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account was created for' + user)

            return redirect('login') 
    return render(request,'register.html',{'form':form})



def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return render(request,'index.html')
        else:
            messages.info(request,'Username OR Password is incorrect')
        
    return render(request,'login.html',{})

def logoutUser(request):
    logout(request)
    return redirect('login')