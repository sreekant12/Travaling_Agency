from django.db import models
import uuid

class Employee(models.Model):
    Employee_id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name=models.CharField(max_length=45)
    phone=models.CharField(max_length=10,unique=True)
    adress=models.TextField()
    photo=models.ImageField(upload_to='employee_images')
    role_choice=(("owner","owner"),("employee","employee"),("driver","driver"),("admin","admin"))
    role=models.CharField(max_length=50,choices=role_choice)
    experience=models.CharField()
    def __str__(self): 
        return f"{self.name}"

class Travel_bus(models.Model):
    Travels_id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    primary_driver=models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name='primary_driver')
    secondary_driver=models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name='secondary_driver')
    bus_number=models.CharField(max_length=15)
    bus_company=models.CharField(max_length=30)

    couch_choice=(('AC','AC'),('Non-AC','Non-AC'))
    couch_type=models.CharField(max_length=8,choices=couch_choice)
    seats=models.PositiveIntegerField()
    seat_type=models.CharField(max_length=15,choices=(('normal','normal'),('Pushback','Pushback'),('Semi_Sleeper','Semi_Sleeper'),('Sleeper_Berth','Sleeper_Berth')))
    luggage_choice=(('small','small'),('medium','medium'),('large','large'))
    luggage=models.CharField(max_length=7,choices=luggage_choice)
    Entertainment_choice=(('yes','yes'),('no','no'))
    Entertainment=models.CharField(max_length=3,choices=Entertainment_choice)
    front_photo=models.ImageField(upload_to='bus_images')
    left_photo=models.ImageField(upload_to='bus_images')
    right_photo=models.ImageField(upload_to='bus_images')
    back_photo=models.ImageField(upload_to='bus_images')
    inner_photo=models.ImageField(upload_to='bus_images')

class Travel_car(models.Model):
    Travels_id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    driver_name=models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    
    car_number=models.CharField(max_length=15)
    car_company=models.CharField(max_length=30)
    couch_choice=(('AC','AC'),('Non-AC','Non-AC'))
    couch_type=models.CharField(max_length=8,choices=couch_choice)
    seats=models.PositiveIntegerField()
    seat_type=models.CharField(max_length=15,choices=(('normal','normal'),('Pushback','Pushback'),('Semi_Sleeper','Semi_Sleeper'),('Sleeper_Berth','Sleeper_Berth')))
    luggage_choice=(('small','small'),('medium','medium'),('large','large'))
    luggage=models.CharField(max_length=7,choices=luggage_choice)
   
    front_photo=models.ImageField(upload_to='car_images')
    left_photo=models.ImageField(upload_to='car_images')
    right_photo=models.ImageField(upload_to='car_images')
    back_photo=models.ImageField(upload_to='car_images')
    inner_photo=models.ImageField(upload_to='car_images')
    

class travel_minibus(models.Model):
    Travels_id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    driver_name=models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    minibus_number=models.CharField(max_length=15)
    minibus_company=models.CharField(max_length=30)
    couch_choice=(('AC','AC'),('Non-AC','Non-AC'))
    couch_type=models.CharField(max_length=8,choices=couch_choice)
    seats=models.PositiveIntegerField()
    seat_type=models.CharField(max_length=15,choices=(('normal','normal'),('Pushback','Pushback'),('Semi_Sleeper','Semi_Sleeper'),('Sleeper_Berth','Sleeper_Berth')))
    luggage_choice=(('small','small'),('medium','medium'),('large','large'))
    luggage=models.CharField(max_length=7,choices=luggage_choice)
    Entertainment_choice=(('yes','yes'),('no','no'))
    Entertainment=models.CharField(max_length=3,choices=Entertainment_choice)
    front_photo=models.ImageField(upload_to='bus_images')
    left_photo=models.ImageField(upload_to='bus_images')
    right_photo=models.ImageField(upload_to='bus_images')
    back_photo=models.ImageField(upload_to='bus_images')
    inner_photo=models.ImageField(upload_to='bus_images')
    