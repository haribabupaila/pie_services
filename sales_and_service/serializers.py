from rest_framework import serializers
from sales_and_service.models import sales,service,profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta: 
        model = profile
        fields = ['first_name','last_name','gender','mobile_number','email','address']

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = service
        fields = ['type_of_gadget','model_number','serial_number','specifications', 'Recieved_on',
                  'estimated_date','issue_description','remarks','service_charge','mobile_number']
        
class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = sales
        fields = ['type_of_gadget','model_number','serial_number','specifications', 'date_of_sale',
                  'remarks','price','warrenty_period','mobile_number']