from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def profile(request):
 return render(request,'profile.html',)

