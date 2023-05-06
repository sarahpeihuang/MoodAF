from django.db import models

# Create your models here.

#Let a PatientData object represent one journal entry 
class PatientData(models.Model):
    #TODO: define the type of input for each of the fields specified in forms
    #must include NAME (required form input) because that is how the patient will be able to access all the entries they've made

    def __str__(self):
        return () 
