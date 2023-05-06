from django.db import models
from datetime import date

# Create your models here.

#Let a PatientData object represent one journal entry 
class PatientData(models.Model):
    fname = models.CharField(max_length=50) #Short answer
    lname = models.CharField(max_length=50) #Short answer
    entry = models.TextField(blank=True) #Long answer (required entry)
    date = models.DateField(default=date.today) #Date entry


    def __str__(self):
        return () 
