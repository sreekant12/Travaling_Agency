from django.shortcuts import render,redirect
from . models import Travel_car
from . models import Travel_bus
from . models import Travel_Minibus
from . models import Employee
from . models import Car_Booking
from . models import Bus_Booking
from . models import MiniBus_Booking
from . forms import Car_Booking_form
from . forms import Bus_Booking_form
from . forms import MiniBus_Booking_form
from django.core.cache import cache

import logging
import re
import secrets
import hmac
import requests

from django.conf import settings
from django.core.cache import cache
from django.http import JsonResponse
from django.views.decorators.http import require_POST

logger = logging.getLogger(__name__)



def home(request):
    return render(request,"home.html")
def bus(request):
    
    data=Travel_bus.objects.filter(is_activate=True)
    return render(request,"bus.html",context={"data":data})

def car(request):
    data=Travel_car.objects.filter(is_activate=True)
    return render(request,"car.html",context={"data":data})
def minibus(request):
    data=Travel_Minibus.objects.filter(is_activate=True)
    return render(request,"minibus.html",context={"data":data})

def Car_Booking(request):
    form=Car_Booking_form()
    if request.method=='POST':
        form=Car_Booking_form(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print("helo")
            print(form.cleaned_data)
            return redirect('home')
    return render(request,"car.html",context={"form":form})

def Bus_Booking(request):
    form=Bus_Booking_form()
    if request.method=='POST':
        form=Bus_Booking_form(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('home')
        return render(request,"car.html",context={"form":form})

def MiniBus_Booking(request):
    form=MiniBus_Booking_form()
    if request.method=='POST':
        form=MiniBus_Booking_form(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('home')
        return render(request,"car.html",context={"form":form})




@require_POST
def generate_otp(request):
    phone = request.POST.get("Mobile_Number")
    print(f"Received phone number for OTP: {phone}")  # Debugging statement
    if not phone:
        return JsonResponse({
            "success": False,
            "message": "Enter a valid 10-digit Indian mobile number."
        }, status=400)

    api_key = settings.TEXTBEE_API_KEY

    if not api_key:
        return JsonResponse({
            "success": False,
            "message": "TextBee API key is not configured."
        }, status=500)

    # Prevent repeated OTP requests within 5 minutes.
    lock_key = f"otp_send_lock_{phone}"

    if not cache.add(lock_key, True, timeout=300):
        return JsonResponse({
            "success": False,
            "message": "Please wait 5 minutes before requesting another OTP."
        }, status=429)

    otp = f"{secrets.randbelow(1000000):06d}"
    print(f"Generated OTP for {phone}: {otp}")  # For debugging; remove in production.
    mobile_number = "+91" + phone

    cache.set(f"otp_{phone}", otp, timeout=300)
    url = "https://api.textbee.dev/api/v1/gateway/send-sms"

    headers = {
        "x-api-key": api_key,
        "Content-Type": "application/json",
    }

    payload = {
        "recipients": [mobile_number],
        "message": (
            f"Your TravelGo verification OTP is {otp}. "
            "It is valid for 5 minutes. "
            "Do not share this code."
        ),
    }

    try:
        response = requests.post(
            url,
            headers=headers,
            json=payload,
            timeout=15
        )

        try:
            result = response.json()
        except ValueError:
            result = {}

        if (
            response.status_code == 200
            and result.get("data", {}).get("success") is True
        ):
            cache.set(f"otp_{phone}", otp, timeout=300)
            

            return JsonResponse({
                "success": True,
                "message": "OTP request accepted. Please check your SMS."
            })

        logger.error(
            "TextBee error: HTTP %s - %s",
            response.status_code,
            response.text[:500]
        )

        

        return JsonResponse({
            "success": False,
            "message": (
                f"TextBee returned HTTP {response.status_code}. "
                "Check the Django terminal for details."
            )
        }, status=502)

    except requests.RequestException:
        logger.exception("TextBee connection failed")
        cache.delete(lock_key)

        return JsonResponse({
            "success": False,
            "message": "Could not connect to TextBee."
        }, status=502)


@require_POST
def verify_otp(request):

    phone = (request.POST.get("Mobile_Number") or "").strip()
    entered_otp = (request.POST.get("otp") or "").strip()

    if not re.fullmatch(r"[6-9][0-9]{9}", phone):
        return JsonResponse({
            "success": False,
            "message": "Invalid mobile number."
        }, status=400)

    if not re.fullmatch(r"\d{6}", entered_otp):
        return JsonResponse({
            "success": False,
            "message": "Enter a valid 6-digit OTP."
        }, status=400)

    otp_key = f"otp_{phone}"
    attempts_key = f"otp_attempts_{phone}"

    cached_otp = cache.get(otp_key)

    if cached_otp is None:
        return JsonResponse({
            "success": False,
            "message": "OTP expired. Please request a new OTP."
        }, status=400)

    attempts = cache.get(attempts_key, 0)

    if attempts >= 5:
        return JsonResponse({
            "success": False,
            "message": "Too many attempts. Request a new OTP."
        }, status=429)

    if hmac.compare_digest(str(cached_otp), entered_otp):

        cache.delete(otp_key)
        cache.delete(attempts_key)
        return JsonResponse({
            "success": True,
            "message": "Mobile number verified successfully!"
        })

    cache.set(attempts_key, attempts + 1, timeout=300)

    return JsonResponse({
        "success": False,
        "message": "Incorrect OTP. Please try again."
    }, status=400)



#car booking email
def car_booking_email(request):
    Booking=Car_Booking.objects.all()   