from django.urls import path, include
from main import views

urlpatterns = [
    path('', views.home, name='home') #when there is no path specified, run the home function in views.py 

    #TODO: define the different paths (different web 'pages') associated with the website
]