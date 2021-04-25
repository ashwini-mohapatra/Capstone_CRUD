from datetime import date

from django.db import models


# Create your models here.
class Prescription(models.Model):
    Patient_No = models.BigAutoField(primary_key=True, unique=True)
    Patient_Name = models.CharField(max_length=100)
    Patient_Age = models.IntegerField()
    Patient_Gender = models.CharField(max_length=1)
    Patient_Allergies = models.CharField(max_length=200)
    Prescription_Date = models.DateField(default=date.today)
    Patient_Weight = models.FloatField(max_length=10)
    Patient_Height = models.FloatField(max_length=10)
    Is_Patient_Admitted = models.BooleanField(default=False)
    Patient_Mobile_No = models.BigIntegerField()
    Patient_Image = models.ImageField(upload_to='./Images')
    Patient_Condition_Description = models.TextField(max_length=200)
    Patient_Medicine = models.TextField(max_length=300)

    #class Meta:
    #    db_table = u'Prescription'

    #def __unicode__(self):
    #    return "{0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11}".format(self,self.Patient_Name,self.Patient_Age,self.Patient_Gender,self.Patient_Allergies,self.Prescription_Date,self.Patient_Weight,self.Patient_Height,self.Is_Patient_Admitted,self.Patient_Mobile_No,self.Patient_Image,self.Patient_Condition_Description,self.Patient_Medicine)
