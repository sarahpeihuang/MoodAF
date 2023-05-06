from django import forms
from .models import PatientData


class PatientForm(forms.ModelForm):
    class Meta:
        model = PatientData

        #TODO: Define the fields of the database (eg. fields associated with the journal entry)
        fields = []
        #The "names" of the fields here should be the same as the name specified in form.html