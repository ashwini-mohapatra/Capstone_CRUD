from datetime import date

from django import forms


class Prescription_Views_Form(forms.Form):
    Patient_Name = forms.CharField()
    Patient_Age = forms.IntegerField()
    Patient_Gender = forms.CharField()
    Patient_Allergies = forms.CharField()
    Prescription_Date = forms.DateField()
    Patient_Weight = forms.FloatField()
    Patient_Height = forms.FloatField()
    Is_Patient_Admitted = forms.BooleanField()
    Patient_Mobile_No = forms.IntegerField()
    Patient_Image = forms.ImageField()
    Patient_Condition_Description = forms.CharField()
    Patient_Medicine = forms.CharField()
