from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status 
from rest_framework.decorators import api_view

# Create your views here.

# Accepting the POST and Get from DRF APIs
@api_view(['POST','GET'])
def books(request):
    return Response('List of the Books ', status=status.HTTP_200_OK)

