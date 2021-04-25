import datetime

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template.defaultfilters import title

from Prescription.forms import Prescription_Views_Form


class Prescription_Views:

    def home1(self, request):
        return render(request,'home.html',{'title': 'Home'})

    def create1(self, request):
        #print(request.POST)
        addform = Prescription_Views_Form(request.POST)
        if addform.is_valid():
            var0 = request.POST.get('Patient_Name', '')
            var1 = request.POST.get('Patient_Age', 0)
            var2 = request.POST.get('Patient_Gender', 'Male')
            var3= request.POST.get('Patient_Allergies', '')
            var4 = request.POST.get('Prescription_Date', datetime.date.today())
            var5 = request.POST.get('Patient_Weight', 0.0)
            var6 = request.POST.get('Patient_Height', 0.0)
            var7 = request.POST.get('Is_Patient_Admitted', False)
            var8 = request.POST.get('Patient_Mobile_No', 000000000)
            var9 = request.POST.get('Patient_Image', '')
            var10 = request.POST.get('Patient_Condition_Description', '')
            var11 = request.POST.get('Patient_Medicine', '')
            add = Prescription_Views(Patient_Name =var0,Patient_Age=var1,Patient_Gender=var2,
                                     Patient_Allergies=var3,Prescription_Date=var4,Patient_Weight=var5,
                                     Patient_Height=var6,Is_Patient_Admitted=var7,Patient_Mobile_No=var8,
                                     Patient_Image = var9,Patient_Condition_Description = var10,Patient_Medicine = var11)
            add.save()
        else:
            addform = Prescription_Views_Form()
            add = Prescription_Views()

        return render(request,'create.html',{'title': 'Create'})


    def read1(self, request):
        return render(request,'read.html',{'title': 'Read'})

    def update1(self,request):
        return render(request,'update.html',{'title': 'Update'})

    def delete1(self,request):
        return render(request,'delete.html',{'title': 'Delete'})

    def create_status1(self,request):
        #var0 = request.get('Prescription_Date')
        print(request.GET)
        return render(request,'create_status.html')

    def read_status1(self,request):
        return render(request,'read_status.html')

    def update_status1(self,request):
        return render(request,'update_status.html')

    def delete_status1(self,request):
        return render(request,'delete_status.html')