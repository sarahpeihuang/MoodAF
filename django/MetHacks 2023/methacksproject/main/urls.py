from django.urls import path, include
from main import views

#Specifies all the PATHS in the website

urlpatterns = [
    path('', views.home, name='home'), #when there is no path specified, run the home function in views.py 
    path('form', views.form, name='form')
    #TODO: define the different paths (different web 'pages') associated with the website
]