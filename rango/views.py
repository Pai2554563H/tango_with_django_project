from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage matches to {{ boldmessage }} in the template!
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    # boldmessage in index.html file

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.

    # Note that the first parameter is the template we wish to use.
    return render(request, 'rango/index.html', context=context_dict)

def hello_world(request):
    return HttpResponse("Hello world, hi Pai!")
    # must return HttpResponse

def about(request):
    #return HttpResponse("Rango says here is the about page." +
    #                    "<a href='/rango/'>Index</a>")

    #context_dict = {'boldmessage': 'Hello world!'}
    return render(request, 'rango/about.html')




