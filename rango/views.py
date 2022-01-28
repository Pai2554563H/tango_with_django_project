from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Rango says hey there partner!" +
                        "<a href='/rango/about/'>About</a>")# must return HttpResponse

def hello_world(request):
    return HttpResponse("Hello world, hi Pai!")

def about(request):
    return HttpResponse("Rango says here is the about page." +
                        "<a href='/rango/'>Index</a>")




