from django.db import models
from django.utils import timezone
from enum import Enum 

class genderenum(Enum):
    a1="Male"
    a2="Female"


class profile(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    gender=models.CharField(
        max_length=20,
        choices=[(e.value, e.name) for e in genderenum],
        default=genderenum.a1.value,
    )
    mobile_number=models.CharField(max_length=11, primary_key=True)
    email=models.CharField(max_length=25, unique=True)
    address=models.TextField()

class service(models.Model):
    type_of_gadget=models.CharField(max_length=50)
    model_number=models.CharField(max_length=50)
    serial_number=models.CharField(max_length=50, null=True)
    specifications=models.TextField(null=True)
    Recieved_on = models.DateField(null=True, blank=True)
    estimated_date=models.DateField()
    issue_description=models.TextField(null=True)
    remarks=models.TextField(null=True)
    service_charge=models.CharField(max_length=50)
    mobile_number=models.ForeignKey(profile, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.Recieved_on:  # If Recieved_on is not set
            self.Recieved_on = timezone.now().date()  # Set it to current date
        super().save(*args, **kwargs)

    
class sales(models.Model):
    type_of_gadget=models.CharField(max_length=50)
    model_number=models.CharField(max_length=50)
    serial_number=models.CharField(max_length=50, null=True)
    specifications=models.TextField(null=True)
    date_of_sale = models.DateField(null=True, blank=True)
    remarks=models.TextField(null=True)
    price=models.CharField(max_length=50)
    warrenty_period=models.CharField(max_length=50)
    mobile_number=models.ForeignKey(profile, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.date_of_sale:  # If date_of_sale is not set
            self.date_of_sale = timezone.now().date()  # Set it to current date
        super().save(*args, **kwargs)