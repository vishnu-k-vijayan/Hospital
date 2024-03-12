from django.shortcuts import render
from .models import Doctor_table,Department_table
# Create your views here.
def Base_fn(request):
    return render(request,'Base.html')

def Home_fn(request):
    return render(request,'Home.html')   

def Department_fn(request):
    ob=Department_table.objects.all()
    return render(request,'Department.html',{'Department_list':ob})      

def Doctor_fn(request):
    ob1=Doctor_table.objects.all()
    return render(request,'Doctor.html',{'Doctor_list':ob1})      

def Booking_fn(request):
    return render(request,'Booking.html')

def About_fn(request):
    return render(request,'About.html')

def Contact_fn(request):
    return render(request,'Contact.html')