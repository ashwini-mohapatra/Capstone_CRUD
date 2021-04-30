from datetime import date

from django.db import models


# Create your models here.
class Prescription(models.Model):
    Patient_No = models.BigAutoField(primary_key=True, unique=True)
    Patient_Name = models.CharField(max_length=100)
    Prescription_Date = models.DateField(default=date.today)
    Patient_Weight = models.FloatField(max_length=10)
    Patient_Height = models.FloatField(max_length=10)
    Is_Patient_Admitted = models.BooleanField(default=False)
    Patient_Mobile_No = models.BigIntegerField()
    Patient_Image = models.ImageField(upload_to='./Images')
    Patient_Condition_Description = models.TextField(max_length=200)
