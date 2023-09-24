from rest_framework import serializers
from sales_and_service.models import sales,service,profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta: 
        model = profile
        fields = ['first_name','last_name','gender','mobile_number','email','address']