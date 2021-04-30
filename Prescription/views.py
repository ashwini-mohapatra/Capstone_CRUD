import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.template.defaultfilters import title

from Prescription.models import Prescription


class Prescription_Views:

    def home1(self, request):
        return render(request, 'home.html', {'title': 'Home'})

    def create1(self, request):
        var0 = request.POST.get('Patient_Name', '')
        var4 = request.POST.get('Prescription_Date', datetime.date.today())
        var5 = request.POST.get('Patient_Weight', 0.0)
        var6 = request.POST.get('Patient_Height', 0.0)
        var7 = request.POST.get('Is_Patient_Admitted', "off")
        if var7 == "on":
            var71 = True
        else:
            var71 = False
        var8 = request.POST.get('Patient_Mobile_No', 000000000)
        var9 = request.POST.get('Patient_Image','')
        # var9 = request.FILES['Patient_Image']
        var10 = request.POST.get('Patient_Condition_Description', '')
        if var0 != "":
            add = Prescription(Patient_Name=var0, Prescription_Date=var4, Patient_Weight=var5,
                               Patient_Height=var6, Is_Patient_Admitted=var71, Patient_Mobile_No=var8,
                               Patient_Image=var9, Patient_Condition_Description=var10)
            add.save()
            return redirect('/read')
        return render(request, 'create.html', {'title': 'Create'})

    def handle_uploaded_file(self,f):
        x = './Images/' + f.name, 'wb+'
        with open(x) as destination:
            for chunk in f.chunks():
                destination.write(chunk)
        return x

    def read1(self, request):
        queryset = Prescription.objects.all()
        return render(request, 'read.html', {'title': 'Read', 'Prescriptions': queryset})

    def update1(self, request, pid):
        updatequery = Prescription.objects.filter(Patient_Id=pid)
        if request.method == 'POST':
            var0 = request.POST.get('Patient_Name', '')
            var4 = request.POST.get('Prescription_Date', datetime.date.today())
            var5 = request.POST.get('Patient_Weight', 0.0)
            var6 = request.POST.get('Patient_Height', 0.0)
            var7 = request.POST.get('Is_Patient_Admitted', "off")
            if var7 == "on":
                var71 = True
            else:
                var71 = False
            var8 = request.POST.get('Patient_Mobile_No', 000000000)
            var9 = request.POST.get('Patient_Image', '')
            # var9 = request.FILES['Patient_Image']
            var10 = request.POST.get('Patient_Condition_Description', '')
            if var0 != "":
                add = Prescription(Patient_No=pid, Patient_Name=var0, Prescription_Date=var4, Patient_Weight=var5,
                                   Patient_Height=var6, Is_Patient_Admitted=var71, Patient_Mobile_No=var8,
                                   Patient_Image=var9, Patient_Condition_Description=var10)
                add.save()
                return redirect('/read')
        return render(request, 'update.html', {'title': 'Update', 'Prescriptions': updatequery})

    def delete1(self, request, id):
        Prescription.objects.filter(Patient_No=id).delete()
        return redirect('/read')
