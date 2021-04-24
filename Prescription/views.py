from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template.defaultfilters import title


class Prescription_Views:

    def home(self,request):
        return render(request,'home.html',{'title': 'Home'})

    def create(self,request):

        return render(request,'create.html',{'title': 'Create'})

    def read(self,request):
        val1=request.GET['']
        return render(request,'read.html',{'title': 'Read'})

    def update(self,request):
        return render(request,'update.html',{'title': 'Update'})

    def delete(self,request):
        return render(request,'delete.html',{'title': 'Delete'})

    def create_status(self,request):
        # val0 = request.GET['Prescription_Date']
        # val1 = request.GET['Patient_Name']
        # val2 = request.GET['Patient_Mobile_No']
        # val3 = request.GET['Patient_Is_Admitted']
        # val4 = request.GET['Patient_Weight']
        # val5 = request.GET['Patient_Height']
        # val6 = request.GET['Patient_Image']
        return render(request,'create_status.html')

    def read_status(self,request):
        return render(request,'read_status.html')

    def update_status(self,request):
        return render(request,'update_status.html')

    def delete_status(self,request):
        return render(request,'delete_status.html')