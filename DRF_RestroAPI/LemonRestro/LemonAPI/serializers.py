from dataclasses import fields
from decimal import Decimal
from unittest.util import _MAX_LENGTH
from rest_framework import serializers

# from Learn_APIs.DRF_RestroAPI.LemonRestro.LemonAPI.views import menu_items
from .models import MenuItem , Category

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


# Model Serializer for function based views

# for @api_view() decorator

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'slug','title']

# for menu items @pi_view() decorator

class MenuItemSerializer2(serializers.ModelSerializer):
    #  change the name of the field
    stock = serializers.IntegerField(source='inventory')
    # after method add field
    total_price = serializers.SerializerMethodField(method_name='calculate_tax')

# for string related filed
    # category=serializers.StringRelatedField()
    # directly using 
    #category = CategorySerializer()

# for the HyperlinkRelatedField:
    category = serializers.HyperlinkedRelatedField(
        queryset = Category.objects.all(),
        view_name = 'category-detail'
    ) # add the context in the menu-items function

    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'stock', 'total_price','category']
        # depth=1

    def calculate_tax(self, product:MenuItem):
        return product.price * Decimal('1.1')
    

#-------------------------------------------------------------------------------#
# MenuItemSerializer extends the serializers.HyperlinkedModelSerializer class instead 
#-------------------------------------------------------------------------------#

# class MenuItemSerializer2(serializers.HyperlinkedModelSerializer):
#     stock = serializers.IntegerField(source='inventory')
#     total_price = serializers.SerializerMethodField(method_name='calculate_tax')

#     class Meta:
#         model = MenuItem
#         fields = ['id', 'title', 'price', 'stock', 'total_price','category']
#         # depth=1

#     def calculate_tax(self, product:MenuItem):
#         return product.price * Decimal('1.1')
    
