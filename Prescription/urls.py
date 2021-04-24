from django.urls import path
from . import views
from .views import Prescription_Views

urlpatterns=[
    path('',Prescription_Views().home,name='home'),
    path('create',Prescription_Views().create,name='Add'),
    path('read',Prescription_Views().read,name='Read'),
    path('update',Prescription_Views().update,name='Update'),
    path('delete',Prescription_Views().delete,name='Delete'),
    path('create_status.html',Prescription_Views().create_status,name='Add Status'),
    path('read_status.html',Prescription_Views().read_status,name='Read Status'),
    path('update_status.html',Prescription_Views().update_status,name='Update Status'),
    path('delete_status.html',Prescription_Views().delete_status,name='Delete Status'),
]