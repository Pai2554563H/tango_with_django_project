
from django.urls import path

from rango import views # load view from rango app

app_name='rango'

urlpatterns = [
    path('', views.index, name='index'), # view from rango app, at first line for first display
    #path('', views.hello_world, name='hello'),

]
