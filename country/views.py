from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import*

@api_view(['GET'])
def home(request):
    country_obj = Country.objects.all()
    serializer = CountrySerializer(country_obj, many= True)
    return Response({'status':'Success', 'payload': serializer.data})

@api_view(['POST'])
def post(request):
    data = request.data
    serializer = CountrySerializer(data=request.data)
    if not serializer.is_valid():
        return Response({'status':'Error' ,  'msg':'Sorry , Something went wrong'})
    
    serializer.save()
    return Response({'status':'Success' , 'payload':'data', 'msg':'Data saved sucessfully'})

@api_view(['PUT'])
def put(request, id):
    country_obj= Country.objects.get(id = id)
    serializer = CountrySerializer(country_obj, data=request.data)
    if not serializer.is_valid():
        return Response({'status':'Error', 'msg':'Sorry , Something went wrong'})
    
    serializer.save()
    return Response({'status':'Success' , 'payload':'data', 'msg':'Data updated sucessfully'})

@api_view(['PATCH'])
def patch(request, id):
    country_obj= Country.objects.get(id = id)
    serializer = CountrySerializer(country_obj, data=request.data, partial= True)
    if not serializer.is_valid():
        return Response({'status':'Error', 'msg':'Sorry , Something went wrong'})
    
    serializer.save()
    return Response({'status':'Success' , 'payload':'data', 'msg':'Data updated sucessfully'})
    
@api_view(['DELETE'])
def delete(request, id):
    country_obj = Country.objects.get(id = id )
    country_obj.delete()
    return Response({'status':'Success' , 'payload':'data', 'msg':'Data deleted sucessfully'})
    
    