from django.db import models
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
    mobile_number=models.CharField(max_length=11, unique=True)
    email=models.CharField(max_length=25, unique=True)
    address=models.TextField()

class service(models.Model):
    type_of_gadget=models.CharField(max_length=50)
    model_number=models.CharField(max_length=50)
    serial_number=models.CharField(max_length=50, null=True)
    specifications=models.TextField()
    Recieved_on=models.DateField(auto_now_add=True)
    estimated_date=models.DateField()
    issue_description=models.TextField()
    remarks=models.TextField(null=True)
    service_charge=models.CharField(max_length=50)
    mobile_number=models.ForeignKey(profile, on_delete=models.CASCADE)

    
class sales(models.Model):
    type_of_gadget=models.CharField(max_length=50)
    model_number=models.CharField(max_length=50)
    serial_number=models.CharField(max_length=50, null=True)
    specifications=models.TextField()
    date_of_sale=models.DateField(auto_now_add=True)
    remarks=models.TextField(null=True)
    price=models.CharField(max_length=50)
    warrenty_period=models.CharField(max_length=50)
    mobile_number=models.ForeignKey(profile, on_delete=models.CASCADE)


