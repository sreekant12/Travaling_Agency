from django.contrib import admin
from travelsapp.models import Employee
from travelsapp.models import Travel_bus
from travelsapp.models import Travel_car
from travelsapp.models import travel_minibus
from travelsapp.models import Booking

# Register your models here.

class Employee_admin(admin.ModelAdmin):
    list_display=['Employee_id','name','phone','adress','photo','role','experience']
admin.site.register(Employee,Employee_admin)
class Travel_bus_admin(admin.ModelAdmin):
    list_display=['Travels_id','primary_driver','secondary_driver','bus_number','bus_company','couch_type','seats','seat_type','luggage','Entertainment','front_photo','left_photo','right_photo','back_photo','inner_photo']
admin.site.register(Travel_bus,Travel_bus_admin)
class Travel_car_admin(admin.ModelAdmin):
    list_display=['Travels_id','driver_name','car_number','car_company','couch_type','seats','seat_type','luggage','front_photo','left_photo','right_photo','back_photo','inner_photo']
admin.site.register(Travel_car,Travel_car_admin)
class travel_minibus_admin(admin.ModelAdmin):
    list_display=['Travels_id','driver_name','minibus_number','minibus_company','couch_type','seats','seat_type','luggage','Entertainment','front_photo','left_photo','right_photo','back_photo','inner_photo']
admin.site.register(travel_minibus,travel_minibus_admin)
class Booking_admin(admin.ModelAdmin):
    list_display=['booking_id','Full_Name','Mobile_Number','Gmail_Address','Pickup_Date','Landmark','Village_City','PIN_Code','State','car','minibus','bus']
admin.site.register(Booking,Booking_admin)
    
