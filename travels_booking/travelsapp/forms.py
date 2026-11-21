from django import forms
from . models import Car_Booking
from . models import Bus_Booking
from . models import MiniBus_Booking


class Car_Booking_form(forms.ModelForm):
    class Meta:
        model=Car_Booking
        fields='__all__'


class Bus_Booking_form(forms.ModelForm):
    class Meta:
        model=Bus_Booking
        fields='__all__'

class MiniBus_Booking_form(forms.ModelForm):
    class Meta:
        model=MiniBus_Booking
        fields='__all__'