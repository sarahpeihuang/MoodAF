from django.shortcuts import render
from django.http import HttpResponse
from .models import PatientData
from .forms import PatientForm
from django.contrib import messages
from django.db.models import Q


# Create your views here.

def home(request):
    return render(request, 'index.html', {})

#TODO: function that allows patient to access their journal entries (should be saved under their name)

#TODO: submit form function, if all the entires are valid in the journal entry, allows the form to be saved into database

#TODO: function(s) COHERE API - summarize and classify journal entry inputs 

#TODO: function display summarized and mood of journal entry on webpage - could be any sort of display
