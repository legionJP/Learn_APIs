from queue import Empty
from re import search
from django.core.paginator import EmptyPage
from django.shortcuts import get_object_or_404, render

from rest_framework import generics
from .models import MenuItem
from .serializers import MenuItemSerializer, MenuItemSerializer1, MenuItemSerializer2

# Create your views here.
#---------------------------------------------------------------------------------------------------#
# using the genric view 
#---------------------------------------------------------------------------------------------------#
class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

# using the single menu item or id to delete 
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset= MenuItem.objects.all()
    serializer_class = MenuItemSerializer
#---------------------------------------------------------------------------------------------------#
# Using the api_view decorator
#---------------------------------------------------------------------------------------------------#
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

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


#----------------------------------------------------------------------------------------------#
# Model Serializer
#----------------------------------------------------------------------------------------------#

# @api_view()
# def menu_items1(request):
#     # items= MenuItem.objects.all()
#     items = MenuItem.objects.select_related('category').all()
#     #serialized_items = MenuItemSerializer2(items, many=True) 
#     serialized_items = MenuItemSerializer2(items, many=True, context={'request':request}) # for the hyperlinkedrelatedfield
#     return Response(serialized_items.data)     # return Response(items.values()) # for models without serializer to covert the all the items to json

'''
Changing your view files to load the related model in a single SQL call will make your API more efficient by
not running a separate SQL query for every item to load the related data.
'''

@api_view()
def single_menu_item1(request, id):
    item = MenuItem.objects.get(pk=id)
    serialized_item = MenuItemSerializer2(item)
    return Response(serialized_item.data)

# ---------------------------------------------------------------------------------------------------#
# Using the HyperlinkedRelatedField , view for category_detail
# ---------------------------------------------------------------------------------------------------#
from . serializers import CategorySerializer 
from .models import Category

@api_view()
def category_detail(request , pk):
    category = get_object_or_404(Category, pk=pk)
    serialized_category = CategorySerializer(category)
    return Response(serialized_category.data)
# map it in the urls.py

# ---------------------------------------------------------------------------------------------------#
# Views  For Deserialization and Validation
#---------------------------------------------------------------------------------------------------#
# Deserialization is the process of converting the JSON data into a Django object.
# Validation is the process of checking if the data is valid or not.

from rest_framework_csv.renderers import CSVRenderer
from django.core.paginator import Paginator
from rest_framework.decorators import renderer_classes

@api_view(['GET', 'POST'])
# @renderer_classes([CSVRenderer]) #for the csv renderer 

def menu_items1(request):
    if request.method == 'GET':
        items = MenuItem.objects.select_related('category').all()
        #------------------------------------------------------------------#
        # for filtering the items based on category and price: 
        #------------------------------------------------------------------#
        catgeory_name = request.query_params.get('category')
        to_price = request.query_params.get('max_price')
        search = request.query_params.get('search')
        ordering = request.query_params.get('ordering')
#------------------------------------------------------------------#
    # Query param for the pagination records
        page = request.query_params.get('page', default=1)
        perpage = request.query_params.get('per_page',default=2)
#------------------------------------------------------------------#
        if catgeory_name:
            items = items.filter(category__title=catgeory_name)
        if to_price:
            items = items.filter(price__lte=to_price) #  price_lte ==> less than or equal to price
        if search:
            items = items.filter(title__icontains=search) # title_icontains ==> case insensitive search
        if ordering:
            ordering_fields = ordering.split(',')
            #items = items.order_by(ordering)
            items = items.order_by(*ordering_fields) # for multiple ordering fields
#------------------------------------------------------------------#
        # Initializing the Paginator object
        paginator = Paginator(items, per_page=perpage)
        try:
            items = paginator.page(number=page)
        except EmptyPage:
            items =[]
#------------------------------------------------------------------#
        serialized_items = MenuItemSerializer2(items, many=True) # to covert the all the items to json 
        # return Response(items.values()) # for models without serializer
        return Response(serialized_items.data)
    elif request.method == 'POST':
        serialized_items = MenuItemSerializer2(data=request.data)
        #------------------------------------------------------------------#
        # data validation
        
        # if serialized_items.is_valid():
        #     serialized_items.save()
        #     return Response(serialized_items.data, status.HTTP_201_CREATED)
        # return Response(serialized_items.errors, status.HTTP_400_BAD_REQUEST)
    # OR
        serialized_items.is_valid(raise_exception=True)
        serialized_items.save()
        return Response(serialized_items.data, status.HTTP_201_CREATED)


# ---------------------------------------------------------------------------------------------------#
# Views:   HTML Template render 
#---------------------------------------------------------------------------------------------------#

from rest_framework.renderers import TemplateHTMLRenderer 
from rest_framework.decorators import renderer_classes

@api_view()
@renderer_classes([TemplateHTMLRenderer])
def menu(request):
    items = MenuItem.objects.select_related('category').all()

    # for filtering the items based on category and price: 
    #------------------------------------------------------------------#
    catgeory_name = request.query_params.get('category')
    to_price = request.query_params.get('to_price')
    if catgeory_name:
        items = items.filter(category__title=catgeory_name)
    if to_price:
        items = items.filter(price__lte=to_price) #  price_lte ==> less than or equal to price
    #------------------------------------------------------------------#
    serialized_items = MenuItemSerializer2(items, many=True)
    return Response({'items': serialized_items.data}, template_name='menu.html')

# ---------------------------------------------------------------------------------------------------#

# ---------------------------------------------------------------------------------------------------#
# Views  for Static HTML Template render
#---------------------------------------------------------------------------------------------------#
from rest_framework.renderers import  StaticHTMLRenderer

@api_view(['GET'])
@renderer_classes([StaticHTMLRenderer])
def welcome(request):
    data ='<html><body><h1><center>Welcome to Lemon Restro </center></h1></body></html>'
    return Response(data)



# ---------------------------------------------------------------------------------------------------#
# Views for the Filerting and Pagination using the DjangoFilterBackend and OrderingFilter, ModelViewSet
#---------------------------------------------------------------------------------------------------#

from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer2
    # throttling
   # from rest_framework.throttling import AnonRateThrottle , UserRateThrottle
   # throttle_classes = [UserRateThrottle, AnonRateThrottle]

    # condition throttling 
    def get_throttles(self):
        if self.action=='create':
            throttle_classes=[UserRateThrottle] # or use custom TenCallsPerMinute
        else:
            throttle_classes=[]
        return [throttle() for throttle in throttle_classes]

    ordering_fields = ['price', 'inventory'] # specify the fields for ordering other than the default ordering fields
    search_fields = ['title']
    filter_fields = ['category']


# ---------------------------------------------------------------------------------------------------#
# Views for the API auth token genration
# ---------------------------------------------------------------------------------------------------#
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def secret(request):
    return Response({'message': 'This is a secret message'}, status=status.HTTP_200_OK)


# ---------------------------------------------------------------------------------------------------#
# manager View: To check the authorization Layer
# ---------------------------------------------------------------------------------------------------#

@api_view()
@permission_classes([IsAuthenticated])
def manager_view(request):
    if request.user.groups.filter(name='Manager').exists():
        return Response({'message': 'This is Manager Auth Class'}, status=status.HTTP_200_OK)
    else:
        return Response({'message':'You are not authorizeed'},status=status.HTTP_404_NOT_FOUND)

# ---------------------------------------------------------------------------------------------------#
# Views for the Throttle Check 
# ---------------------------------------------------------------------------------------------------#
from rest_framework.throttling import AnonRateThrottle , UserRateThrottle
from rest_framework.decorators import throttle_classes
from .throttles import TenCallsPerMinute
@api_view()
@throttle_classes([AnonRateThrottle])
def throttle_check(request):
    return Response({'message': "Successful"})

# fro the authenticated user
@api_view()
@permission_classes([IsAuthenticated])
# @throttle_classes([UserRateThrottle])
@throttle_classes([TenCallsPerMinute]) # custom throttle rate limit

def throttle_check_auth(request):
    return Response({'message': "Successful"})

# ---------------------------------------------------------------------------------------------------#
