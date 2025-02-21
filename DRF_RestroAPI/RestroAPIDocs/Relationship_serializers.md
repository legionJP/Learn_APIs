# Relationship Serializers

```markdown
# Relationship Serializers

- convert the related model into json and display them correctly.

```
![alt text](image-5.png)

# Serializers.py


```python
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

    # category=serializers.StringRelatedField()
    # directly using 
    category = CategorySerializer()

    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'stock', 'total_price','category']

    def calculate_tax(self, product:MenuItem):
        return product.price * Decimal('1.1')
    
```
# Views.py

```python

# Single menu item view 

@api_view()
def single_menu_item(request, id):
    item = MenuItem.objects.get(pk=id)
    serialized_item = MenuItemSerializer1(item)
    return Response(serialized_item.data)

# Model Serializer
@api_view()
def menu_items1(request):
    # items= MenuItem.objects.all()
    items = MenuItem.objects.select_related('category').all()
    serialized_items = MenuItemSerializer2(items, many=True) # to covert the all the items to json 
    # return Response(items.values()) # for models without serializer
    return Response(serialized_items.data)
'''
Changing your view files to load the related model in a single SQL call will make your API more efficient by
not running a separate SQL query for every item to load the related data.
'''

@api_view()
def single_menu_item1(request, id):
    item = MenuItem.objects.get(pk=id)
    serialized_item = MenuItemSerializer2(item)
    return Response(serialized_item.data)
```