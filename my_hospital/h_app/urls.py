from django.urls import path
from .import views


urlpatterns=[
    path('',views.Base_fn,name='Base'),
    path('Home',views.Home_fn,name='Home'),
    path('Department',views.Department_fn,name='Department'),
    path('Doctor',views.Doctor_fn,name='Doctor'),
    path('Booking',views.Booking_fn,name='Booking'),
    path('About',views.About_fn,name='About'),
    path('Contact',views.Contact_fn,name='Contact'),
]
