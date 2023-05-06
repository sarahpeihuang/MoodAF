from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home')
    #TODO: define the different paths (different web 'pages') associated with the website
]