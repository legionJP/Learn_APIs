from django.shortcuts import render

from rest_framework import generics
from .models import MenuItem
from .serializers import MenuItemSerializer
# Create your views here.

# using the genric view 


class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

# using the single menu item or id to delete 
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset= MenuItem.objects.all()
    serializer_class = MenuItemSerializer