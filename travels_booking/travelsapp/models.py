from django.db import models
import uuid
class Travel_Agency(models.Model):
    Agency_id=models.UUIDField(primary_key=True,editable=True,default=uuid.uuid4)
    name=models.CharField(max_length=50)
    address=models.TextField()
    pincode=models.PositiveBigIntegerField()
    logo=models.ImageField(upload_to=r"\Agency_logos",blank=True,null=True)
    def __str__(self):
        return f"{name}"
  
    