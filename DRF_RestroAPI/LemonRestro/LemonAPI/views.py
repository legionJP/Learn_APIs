from django.shortcuts import render

from rest_framework import generics
from .models import MenuItem
from .serializers import MenuItemSerializer, MenuItemSerializer1, MenuItemSerializer2
# Create your views here.

# using the genric view 
class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

# using the single menu item or id to delete 
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset= MenuItem.objects.all()
    serializer_class = MenuItemSerializer

# Using the api_view decorator
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()
def menu_items(request):
    items= MenuItem.objects.all()
    serialized_items = MenuItemSerializer1(items, many=True) # to covert the all the items to json 
    # return Response(items.values()) # for models without serializer
    return Response(serialized_items.data)

# Single menu item view 

@api_view()
def single_menu_item(request, id):
    item = MenuItem.objects.get(pk=id)
    serialized_item = MenuItemSerializer1(item)
    return Response(serialized_item.data)

# Model Serializer
@api_view()
def single_menu_item1(request, id):
    item = MenuItem.objects.get(pk=id)
    serialized_item = MenuItemSerializer2(item)
    return Response(serialized_item.data)