from dataclasses import fields
from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from .models import MenuItem

# serializers  for class based views

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'inventory']
        

class MenuItemSerializer1(serializers.ModelSerializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price']