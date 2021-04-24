"""CapstoneCRUD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from CapstoneCRUD import settings

urlpatterns = [
    path('',include('Prescription.urls')),
    path('create', include('Prescription.urls')),
    path('read', include('Prescription.urls')),
    path('update', include('Prescription.urls')),
    path('delete', include('Prescription.urls')),
    path('create_status',include('Prescription.urls')),
    path('delete_status', include('Prescription.urls')),
    path('read_status', include('Prescription.urls')),
    path('update_status', include('Prescription.urls')),
    path('admin/', admin.site.urls),
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, directory_root=settings.MEDIA_ROOT)

