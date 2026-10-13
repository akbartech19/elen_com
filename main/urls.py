from django.urls import path
from .views import (
    index_view, 
    index2_view, 
    about_view, 
    contact_view, 
    fashion_view, 
    photography_view, 
    travel_view
)

urlpatterns = [
    path('', index_view, name='index'),
    path('index-2/', index2_view, name='index_2'),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    path('fashion/', fashion_view, name='fashion'),
    path('photography/', photography_view, name='photography'),
    path('travel/', travel_view, name='travel'),
]
