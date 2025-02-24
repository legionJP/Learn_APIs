#
# Importance Of Data Validation

- Data validation is an important step in every web application because it ensures that user data is valid and sufficient. Explore different validation techniques in DRF.

# Validation
- Validation is the process of ensuring that user-submitted data is in the correct format, meets the requirements and is safe to add to the database.
- The serializers in DRF provide different features which you can use to validate these data while building your APIs.

# Examine some user inputs for API 
| Field  | Value           | Status                                                                 |
|--------|-----------------|-----------------------------------------------------------------------|
| Price  | 0               | Invalid, because the price of a menu item cannot be 0                 |
| Stock  | Negative value  | Invalid, because stock of a menu item cannot be lower than 0          |
| Title  | Duplicate values| Invalid, because there should not be more than one menu item with the same name or title |

- Besides these common validations, every project has additional requirements.like price can't be less than 10

# Validation in DRF

- There are two serializers in the serializers.py file, MenuItemSerializer and CategorySerializer. 
### Serializers.py
```py
from rest_framework import serializers
from decimal import Decimal
from .models import MenuItem, Category
 
class CategorySerializer (serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','slug','title']
 
class MenuItemSerializer(serializers.ModelSerializer):
    stock =  serializers.IntegerField(source='inventory')
    price_after_tax = serializers.SerializerMethodField(method_name = 'calculate_tax')
    category_id = serializers.IntegerField(write_only=True)
    category = CategorySerializer(read_only=True)
    class Meta:
        model = MenuItem
        fields = ['id','title','price','stock', 'price_after_tax','category','category_id']
    
    def calculate_tax(self, product:MenuItem):
        return product.price * Decimal(1.1)
```

# Ways to Modify and Validate the Data in Serializers 

# Method 1: Conditions in the field
- Code before the Meta class in the MenuItemSerializer.
- price = serializers.DecimalField(max_digits=6, decimal_places=2, min_value=2)

For Post Request 1, DRF will display the error that the price should be greater than or equal to 2. The validation works. 

# Method 2: Using keyword arguments in the Meta class

If the field is not declared above the Meta field, you can still validate it using keyword arguments in the Meta class. For this method, you need to remove the line you added in the previous section. Add an extra_kwargs section in the Meta class with below codes

```py
class Meta:
        model = MenuItem
        fields = ['id','title','price','stock', 'price_after_tax','category','category_id']
        extra_kwargs = {
            'price': {'min_value': 2},
        }
```

# Final Code for MenuitemSerializer Class

```py
class MenuItemSerializer(serializers.ModelSerializer):
    price_after_tax = serializers.SerializerMethodField(method_name = 'calculate_tax')
    category_id = serializers.IntegerField(write_only=True)
    category = CategorySerializer(read_only=True)
    class Meta:
        model = MenuItem
        fields = ['id','title','price','stock', 'price_after_tax','category','category_id']
        extra_kwargs = {
            'price': {'min_value': 2},
            'stock':{'source':'inventory', 'min_value': 0}
        }
    
    def calculate_tax(self, product:MenuItem):
        return product.price * Decimal(1.1)
```

# Method:3 Using validate_field() method 

Serializers in DRF provide you with another clean way of validating user input by writing valid_field() methods, where you replace the field with an actual field name. If the field name is price, the method name has to be validate_price(). If the field name is stock, then the method name has to be validate_stock().

Add the following two methods above the Meta class in the MenuItemSerializer. 

```py
def validate_price(self, value):
        if (value < 2):
            raise serializers.ValidationError('Price should not be less than 2.0')
    
def validate_stock(self, value):
        if (value < 0):
            raise serializers.ValidationError('Stock cannot be negative')
```

- As the API developer you need to check if the value meets the requirement, otherwise, raise the ValidationError with a message. 

# Method 4: Using the validate() method 

- You can add a validate() method in the serializer and validate multiple field values at once. DRF will pass all input values to this method. 

- Note: To follow this method you need to remove the previous two methods validate_stock and validate_price in the serializer.

- Add the following code above the Meta class in the MenuItemSerializer.
```py
def validate(self, attrs):
        if(attrs['price']<2):
            raise serializers.ValidationError('Price should not be less than 2.0')
        if(attrs['inventory']<0):
            raise serializers.ValidationError('Stock cannot be negative')
        return super().validate(attrs)
```

# Unique validation
```markdown
To make sure that there is no duplicate entry made by the clients. In such cases, unique validators become useful. Using this validator, you can ensure the uniqueness of a single field or combination of fields. Let’s examine how to use this validator. For a single field, use UniqueValidator class and for the combination of fields, use UniqueTogetherValidator.
```
# UniqueValidator
First, import the classes. 

```py
from rest_framework.validators import UniqueValidator
# OR
from rest_framework.validators import UniqueTogetherValidator
```
- To make sure that the title field remains unique in the MenuItems table, you can add the following code in the extra_kwargs section in the Meta class. Here's an example of using UniqueValidator for the title field.   

```py
extra_kwargs = {
            'title': {
                'validators': [
                    UniqueValidator(
                        queryset=MenuItem.objects.all()
                    )
                ]
            }
        }  

# Or you can add it when declaring a field above Meta class, like this.

title = serializers.CharField(
        max_length=255,
        validators=[UniqueValidator(queryset=MenuItem.objects.all())]
    )
```
# UniqueTogetherValidator

- When you want to use UniqueTogetherValidator validator, the code will be a little different. Here’s a sample code that will make the combination of title and price field unique. With this validation, there will be no duplicate entry of an item with the same price. This code goes directly inside the Meta class.

```py
validators = [
            UniqueTogetherValidator(
                queryset=MenuItem.objects.all(),
                fields=['title', 'price']
            ),
        ]
```
