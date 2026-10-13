"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from main.views import (
    index_view, 
    index2_view, 
    about_view, 
    contact_view, 
    fashion_view, 
    photography_view, 
    travel_view
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Bosh sahifa (http://127.0.0)
    path('', index_view, name='index'),
    
    # Qolgan ichki sahifalar
    path('index-2/', index2_view, name='index_2'),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    path('fashion/', fashion_view, name='fashion'),
    path('photography/', photography_view, name='photography'),
    path('travel/', travel_view, name='travel'),
]

