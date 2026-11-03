from django.shortcuts import render
def home(request):
    return render(request,"home.html")
def bus(request):
    return render(request,"bus.html")
def car(request):
    return render(request,"car.html")
def minibus(request):
    return render(request,"minibus.html")

# Create your views here.
