
from django.urls import path

from rango import views # load view from rango app

app_name='rango'

urlpatterns = [
    path('', views.index, name='index'), # view from rango app, at first line for first display
    #path('', views.hello_world, name='hello'),
    path('about/', views.about, name='about'),
    path('category/<slug:category_name_slug>/',
        views.show_category, name='show_category'),
    path('add_category/', views.add_category, name='add_category'),
    path('category/<slug:category_name_slug>/add_page/', views.add_page, name='add_page'),



]
