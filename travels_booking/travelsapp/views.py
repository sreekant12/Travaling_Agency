from django.shortcuts import render
from . models import Travel_car
from . models import Employee




def home(request):
    return render(request,"home.html")
def bus(request):
    return render(request,"bus.html")
def car(request):
    data=Travel_car.objects.filter(is_activate=True)
    return render(request,"car.html",context={"data":data})
def minibus(request):
    return render(request,"minibus.html")


# Create your views here.
