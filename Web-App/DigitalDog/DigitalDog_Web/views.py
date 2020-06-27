from django.shortcuts import render
from django.http import HttpResponse
from .forms import CreateUserForm
from django.contrib import auth, admin

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def login(request):
    return render(request,'login.html')     

def register(request):
    form = CreateUserForm()
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password1')
        email = request.POST.get('email')
        print (username + ":" + password + " -> " + email)
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
       
    return render(request, 'register.html', {'form': form})
        