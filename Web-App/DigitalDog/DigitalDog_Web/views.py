from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def login(request):
    return render(request,'login.html')     

def register(request):
    return render(request,'register.html')
        