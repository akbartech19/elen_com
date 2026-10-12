from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index-2/', views.index2, name='index2'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('fashion/', views.fashion, name='fashion'),
    path('photography/', views.photography, name='photography'),
    path('travel/', views.travel, name='travel'),
]