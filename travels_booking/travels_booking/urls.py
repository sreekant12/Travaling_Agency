"""
URL configuration for travels_booking project.

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
from travelsapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("", views.home, name="home"),
    path("admin/", admin.site.urls),
    path("car/", views.car, name="car"),
    path("bus/", views.bus, name="bus"),
    path("minibus/", views.minibus, name="minibus"),

    path("generate_otp/", views.generate_otp, name="generate_otp"),

    path("verify_otp/", views.verify_otp, name="verify_otp"),

    path("Car_Booking/", views.Car_Booking, name="Car_Booking"),

    path("Bus_Booking/", views.Bus_Booking, name="Bus_Booking"),

    path("MiniBus_Booking/", views.MiniBus_Booking, name="MiniBus_Booking"),
    

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)