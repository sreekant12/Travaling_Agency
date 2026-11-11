from django.shortcuts import render
from . models import Travel_car
from . models import Travel_bus
from . models import travel_minibus
from . models import Employee




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


# Create your views here.
