from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def profile(request):
 return render(request,'profile.html',)


def forgetPwd(request):
 return render(request,'forget_pwd.html',)


def login(request):
 return render(request,'login.html',)


def register(request):
 return render(request,'register.html',)