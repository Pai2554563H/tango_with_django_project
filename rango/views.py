from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Rango says hey there partner!")# must return HttpResponse

def hello_world(request):
    return HttpResponse("Hello world, hi Pai!")

def hello_world(request):
    return HttpResponse("Hello world, hi Pai!")




