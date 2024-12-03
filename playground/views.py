from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def calculate():
    x=1
    y=1
    return x


def say_hello(request):
    x= calculate()
    return render(request,'hello.html',{'name':'ALi'})

def dog(request):
    return render(request,'base.html',{'name':'max'})