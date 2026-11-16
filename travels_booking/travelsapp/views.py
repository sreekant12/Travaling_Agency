from django.shortcuts import render
from . models import Travel_car
from . models import Travel_bus
from . models import travel_minibus
from . models import Employee
from . models import Car_Booking
from . models import Bus_Booking
from . models import MiniBus_Booking




def home(request):
    return render(request,"home.html")
def bus(request):
    
    data=Travel_bus.objects.filter(is_activate=True)
    return render(request,"bus.html",context={"data":data})

def car(request):
    data=Travel_car.objects.filter(is_activate=True)
    return render(request,"car.html",context={"data":data})
def minibus(request):
    data=travel_minibus.objects.filter(is_activate=True)
    return render(request,"minibus.html",context={"data":data})

def Car_Booking(request):
    form=Car_Booking_form()
    if request.method=='POST':
        form=Car_Booking_form(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return render(request,"car.html",context={"form":form})

def Bus_Booking(request):
    form=Bus_Booking_form()
    if request.method=='POST':
        form=Bus_Booking_form(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return render(request,"car.html",context={"form":form})

def MiniBus_Booking(request):
    form=MiniBus_Booking_form()
    if request.method=='POST':
        form=MiniBus_Booking_form(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return render(request,"car.html",context={"form":form})

# Create your views here.
