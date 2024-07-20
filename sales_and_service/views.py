from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from sales_and_service.models import profile, service, sales
from sales_and_service.serializers import ProfileSerializer, ServiceSerializer, SalesSerializer

class profile_op(APIView):
    def fetch_profile(self, pk):
        return profile.objects.filter(mobile_number=pk).first()
    
    def get(self,request, pk=None, format=None):
        if pk is not None:
            single_profile=self.fetch_profile(pk)
            if single_profile:
                serializer=ProfileSerializer(single_profile)
                return Response(serializer.data)
            else:
                return Response({'message': 'Profile not found'}, status=404)
        
        else:
            profiles=profile.objects.all()
            serializer=ProfileSerializer(profiles, many=True)
            return Response(serializer.data)
            
    
    
    def post(self, request, format=None):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class service_op(APIView):
    def fetch_services(self, pk):
        return service.objects.filter(mobile_number=pk).first()
    
    def get(self,request, pk=None, format=None):
        if pk is not None:
            profile_services=self.fetch_services(pk)
            if profile_services:
                serializer=ServiceSerializer(profile_services)
                return Response(serializer.data)
            else:
                return Response({'message': 'No services found for the profile'}, status=404)
        
        else:
            services=service.objects.all()
            serializer=ServiceSerializer(services, many=True)
            return Response(serializer.data)
        
    def post(self, request, format=None):
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class sales_op(APIView):
    def fetch_sales(self, pk):
        return sales.objects.filter(mobile_number=pk).first()
    
    def get(self,request, pk=None, format=None):
        if pk is not None:
            profile_sales=self.fetch_sales(pk)
            if profile_sales:
                serializer=SalesSerializer(profile_sales)
                return Response(serializer.data)
            else:
                return Response({'message': 'No sales found for the profile'}, status=404)
        
        else:
            saless=sales.objects.all()
            serializer=SalesSerializer(saless, many=True)
            return Response(serializer.data)
        
    def post(self, request, format=None):
        serializer = SalesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

        

    


