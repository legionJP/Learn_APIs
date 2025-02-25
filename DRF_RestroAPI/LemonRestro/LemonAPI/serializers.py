from dataclasses import fields
from decimal import Decimal
from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from rest_framework.validators import UniqueValidator , UniqueTogetherValidator
import bleach

# from Learn_APIs.DRF_RestroAPI.LemonRestro.LemonAPI.views import menu_items
from .models import MenuItem , Category

#---------------------------------------------------------------------------------------------------#
# serializers  for class based views
#---------------------------------------------------------------------------------------------------#
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

#---------------------------------------------------------------------------------------------------#
# Model Serializer for function based views , for @api_view() decorator
#---------------------------------------------------------------------------------------------------#

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'slug','title']

###------------------------------------------------------------------------###
# for menu items @api_view() decorator

class MenuItemSerializer2(serializers.ModelSerializer):
    #  change the name of the field
    stock = serializers.IntegerField(source='inventory')
    # after method add field
    total_price = serializers.SerializerMethodField(method_name='calculate_tax')

#-------------------------------------------------------------------------------#
# for string related filed
    # category=serializers.StringRelatedField()
    # directly using 
    #category = CategorySerializer()

#-------------------------------------------------------------------------------#
# for the HyperlinkRelatedField:
#-------------------------------------------------------------------------------#
#     category = serializers.HyperlinkedRelatedField(
#         queryset = Category.objects.all(),
#         view_name = 'category-detail'
#     ) # add the context in the menu-items function
#-------------------------------------------------------------------------------#
# for Deserilization 
    category = CategorySerializer(read_only = True)
    category_id = serializers.IntegerField(write_only=True)
#-------------------------------------------------------------------------------#

#-------------------------------------------------------------------------------#
# Using the Bleach for validate_field
#-------------------------------------------------------------------------------#
    def validate_title(self, value):
        return bleach.clean(value)
#     # Using the validate() method  
#     def validate(self,attrs):
#         attrs['price'] =bleach.clean(attrs['price'])
#         if(attrs['price'])<Decimal('10'):
#             raise serializers.ValidationError("The Price Must be at least $10")
# # the bleach can  be used to validate the below fileds for sql injection
#         attrs['title'] = bleach.clean(attrs['title'])
#         attrs['price'] = bleach.clean(attrs['price'])
# # limit = request.GET.get('limit')
# # MenuItem.objects.raw('SELECT * FROM LittleLemonAPI_menuitem LIMIT %s', [limit])

#-------------------------------------------------------------------------------#

# # Method:3 Using validate_field() method 

#     def validate_price(self, value):
#         if value < Decimal('10'):
#             raise serializers.ValidationError('The Price Must be at least $10')
    
#     def validate_stock(self, value):
#         if value <0:
#             raise serializers.ValidationError('The Stock Must be at least 0')
   

    
# Method 4 : Using the validate() method
    def vlaidate(self, attrs):
        if attrs['price'] < Decimal('10'):
            raise serializers.ValidationError('The Price Must be at least $10')
        if attrs['stock'] <0:
            raise serializers.ValidationError('The Stock Must be at least 0')


    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'stock', 'total_price','category', 'category_id']
        # depth=1  # for the nested serializer

# API Data Validation:
    #Method:1. Using the Keyword Arguments in the Meta class
        # extra_kwargs = {
        #     'price': {'min_value': Decimal('10')},
        #     'stock' : {'source':'inventory', 'min_value':0}
        # }
# #1.1 UniqueValidator using the extra_kwargs
#         extra_kwargs= {
#             'title':{
#                 'validators':[UniqueValidator(queryset=MenuItem.objects.all())]
#             }
#         }
#     # Or using above the meta class 
#     # title = serializers.CharField(validators=[UniqueValidator(queryset=MenuItem.objects.all()),message='Ttile Must be Unique'])
# #1.2 UniqueTogetherValidator
#     validators = [UniqueTogetherValidator(
#                         queryset=MenuItem.objects.all(), 
#                         fields=['title','price']),
#                 ]

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
    
