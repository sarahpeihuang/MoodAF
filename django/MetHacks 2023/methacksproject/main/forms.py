from django import forms
from .models import PatientData


class PatientForm(forms.ModelForm):
    class Meta:
        model = PatientData

        #TODO: Define the fields of the database (eg. fields associated with the journal entry)
        fields = []
        #First Name, Last Name, Actual Journal Text Entry, Highlights of their day, etc...