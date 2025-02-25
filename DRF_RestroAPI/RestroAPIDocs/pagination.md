#
# Paginations 

- Paginations are uised to chunk the results and save the server resources

### Request for the many records and can be limit by the certain numbers 

Limit= 10 per page
Request = 20 Records 
Total call = 2

# If the Limit exteds send the 404 error 

# Views.py

```py

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

```
