from django.contrib import admin
from travelsapp.models import Employee
from travelsapp.models import Travel_bus
# Register your models here.

class Employee_admin(admin.ModelAdmin):
    list_display=['Employee_id','name','phone','adress','photo','role','experience']
admin.site.register(Employee,Employee_admin)
class Travel_bus_admin(admin.ModelAdmin):
    list_display=['Travels_id','bus_number','bus_company','couch_type','seats','seat_type','luggage','Entertainment','front_photo','left_photo','right_photo','back_photo','inner_photo']
admin.site.register(Travel_bus,Travel_bus_admin)



 