# from email.policy import HTTP
# import stat
# from turtle import title
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status 
from rest_framework.decorators import api_view
from rest_framework.views import APIView

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


# Class Based Views

class BookList(APIView):
    # def get(self, request):
    #     return Response({"message":"list of books"}, status=status.HTTP_200_OK)
    
    
    # using the query str parameter 
    def get(self, request):
        author = request.GET.get('author')
        if(author):
            return Response({"message":"list of books by " +author}, status=status.HTTP_200_OK)

        return Response({"message":"list of books"}, status=status.HTTP_200_OK)

    def post(self, request):
        return  Response({"message": "New book added"}, status=status.HTTP_201_CREATED)    

# Accepting the primary key in api

class Book(APIView):
    def get(self,request, pk):
        return Response({"message": "single book with id "} + str(pk), status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        return Response({"title": request.data.get('title')}, status=status.HTTP_200_OK)
    
