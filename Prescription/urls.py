from django.urls import path
from . import views
from .views import Prescription_Views

urlpatterns=[
    path('',Prescription_Views().home,name='home'),
    path('create',Prescription_Views().create,name='Add'),
    path('read',Prescription_Views().read,name='Read'),
    path('update',Prescription_Views().update,name='Update'),
    path('delete',Prescription_Views().delete,name='Delete'),
    # path('create.html',Prescription_Views().create,name='Add'),
    # path('read.html',Prescription_Views().read,name='Read'),
    # path('update.html',Prescription_Views().update,name='Update'),
    # path('delete.html','../templates/create',name='Delete'),
]