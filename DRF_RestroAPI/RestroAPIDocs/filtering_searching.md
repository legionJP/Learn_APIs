# Searching and filtering in the API Endpoints 

## 1. By Managing and Filtering Data at the Client site
![alt text](image-14.png)

- It can take less time to develop
- #### Tradeoff
    - It will fetch every or all records frmo the database and it can not be sustainable 
    when there is lot of data and can create the load on server 


## 2. By Prcessing the Conditions on the Server Side
![alt text](image-15.png)

- #### Benifits : 
    - When using the Server Process Conditions it will take less time for the loading and fetching
    - bcz only required  the data is fetched after the process of filtering 

# Code for filtering 
```python
def menu_items1(request):
    if request.method == 'GET':
        items = MenuItem.objects.select_related('category').all()
        #------------------------------------------------------------------#
        # for filtering the items based on category and price: 
        #------------------------------------------------------------------#
        catgeory_name = request.query_params.get('category')
        to_price = request.query_params.get('max_price')
        if catgeory_name:
            items = items.filter(category__title=catgeory_name)
        if to_price:
            items = items.filter(price__lte=to_price) #  price_lte ==> less than or equal to price
        #------------------------------------------------------------------#
        serialized_items = MenuItemSerializer2(items, many=True) # to covert the all the items to json 
        # return Response(items.values()) # for models without serializer
        return Response(serialized_items.data)

# query : http://127.0.0.1:8000/api/menu-items/?max_price=10
```
# Searching 