from django.db import models
from datetime import date

# Create your models here.

#Let a PatientData object represent one journal entry 
class PatientData(models.Model):
    fname = models.CharField(max_length=50) #Short answer
    lname = models.CharField(max_length=50) #Short answer
    entryBox = models.TextField(blank=False) #Long answer (required entry)
    date = models.DateField(default=date.today) #Date entry
    mood = models.CharField(blank=True, max_length=100, default="No mood") #Short answer
    feedback = models.TextField(blank=True, default="No feedback")

    def __str__(self):
        return (self.fname + " " + self.lname) 
