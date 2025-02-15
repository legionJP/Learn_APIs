from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status 
from rest_framework.decorators import api_view

# Create your views here.

# Accepting the POST and Get from DRF APIs
@api_view(['POST','GET'])
def books(request):
    return Response('List of the Books ', status=status.HTTP_200_OK)

#----------------------------------------------------------------------------------------
# API View Decorators 

# api view and response displays the better interface in browser
# It can also specify which method to appcept in the list of arguments
# Also can make the post request in the beowser itself

# Allows to implement the Trottling and Rate Limiting 
# Helps with the Authentication endpoints

#----------------------------------------------------------------------------------------

