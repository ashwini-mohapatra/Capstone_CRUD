from django.urls import path
from . import views
from .views import Prescription_Views

urlpatterns=[
    path('',Prescription_Views().home1,name='home'),
    path('create',Prescription_Views().create1,name='Add'),
    path('read',Prescription_Views().read1,name='Read'),
    path('update/<int:pid>',Prescription_Views().update1,name='Update'),
    path('delete/<int:id>',Prescription_Views().delete1,name='Delete'),
    # path('create_status',Prescription_Views().create_status1,name='Add Status'),
    # path('read_status',Prescription_Views().read_status1,name='Read Status'),
    # path('update_status',Prescription_Views().update_status1,name='Update Status'),
    # path('delete_status',Prescription_Views().delete_status1,name='Delete Status'),
]