from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from sales_and_service.models import profile
from sales_and_service.serializers import ProfileSerializer

class profileList(APIView):
    def get(self,request, format=None):
        profiles=profile.objects.all()
        serializer=ProfileSerializer(profiles, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProfileDetail(APIView):
    def fetch_profile(self, pk):
        try:
            return profile.objects.get(mobile_number=pk)
        except profile.DoesNotExist:
            return Http404
        
    def get(self,request, pk, format=None):
        profile=self.fetch_profile(pk)
        serializer=ProfileSerializer(profile)
        return Response(serializer.data)

    

        

    


