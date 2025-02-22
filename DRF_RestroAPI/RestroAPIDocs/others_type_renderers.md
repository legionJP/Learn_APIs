# 
# Different types of renderers:
Renderers are the core classes in DRF that display the API output in different formats like JSON and XML.

# TemplateHTMLRenderer

```markdown
Sometimes, even in an API project, it might be required to display HTML output. For example, if you generate an invoicing API, you need to display the transaction and order details in a nicely formatted way using HTML and CSS. In such cases, DRF’s TemplateHTMLRenderer can help
```

- ## Step 1
Using the TemplateHTMLRenderer, you can pass the data to an HTML file and then display that data using Django’s native templating language called DT.

- import rest_framework.renderers module in the views.py file and renderer_classes decorator. 
```python
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.decorators import api_view, renderer_classes
```

- ## Step 2
- The second step is to create a new function called menu in the views.py file. 

```python
@api_view() 
@renderer_classes ([TemplateHTMLRenderer])
def menu(request):
    items = MenuItem.objects.select_related('category').all()
    serialized_item = MenuItemSerializer(items, many=True)
    return Response({'data':serialized_item.data}, template_name='menu-items.html')
```


Note how the serialized data is passed as context to the HTML template file named menu-items.html. You need to put this HTML file inside the templates directory in your Django app, so the path of this file is: LittleLemon/LittleLemonAPI/templates/menu-item.html

## Step 3
The third step is to add the following templating code to this HTML file. This code block accepts the template data and displays them in a HTML table. 


```html
<!DOCTYPE html> 
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Menu Items</title>
</head>
<body>
    <table width="100%" style="text-align: left;">
        <tr>
            <th>Item</th> <!-- item column heading -->
            <th>Price</th> <!-- price column heading -->
            <th>Price After Tax</th> <!-- price after tax column heading -->
            <th>Stock</th> <!-- stock column heading -->
        </tr>
        {% for item in data %}
        <tr>
            <td>{{ item.title }}</td>
            <td>{{ item.price }}</td>
            <td>{{ item.price_after_tax }}</td>
            <td>{{ item.stock }}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
```

## Step 4

The final step is to map this function to an API endpoint in the urls.py file so that it can be browsed as http://127.0.0.1:8000/api/menu.

```python
from django.urls import path 
from . import views 
urlpatterns = [ 
    path('menu-items',views.menu_items),
    path('menu-items/<int:id>',views.single_item)
    path('menu',views.menu),
]

```

# StaticHTMLRenderer

You can use the StaticHTMLRenderer if any of your API endpoints need to display some HTML content without using any DTL code inside an HTML file.  

## Step 1
The first step is to import the StaticHTMLRenderer class and renderer_classes decorator like before. 

```python
from rest_framework.decorators import api_view, renderer_classes
```

## Step 2
Then you need to create a new function called welcome in the views.py file. 
```python
@api_view(['GET'])
@renderer_classes([StaticHTMLRenderer])
def welcome(request):
    data = '<html><body><h1>Welcome To Little Lemon API Project</h1></body></html>'
    return Response(data)
```

## Step 3
- The final step is to map this endpoint to an API endpoint. This time, you want to display this message whenever someone visits the endpoint http://127.0.0.1:8000/api/welcome.
```python
path('welcome',views.welcome)
```

# CSV renderer
CSV, or comma-separated values, is another popular format used by API developers. Unlike JSON or XML, every field in a database record is displayed separated by a comma and every record is on a new line. 

## Step 1
DRF doesn’t come with a CSV renderer class by default. So the first step is to install a popular third-party package using pipenv. 
- pipenv install djangorestframework-csv

## Step 2
- Import this renderer in the views.py file.
- from rest_framework_csv.renderers import CSVRenderer

## Step 3
Add the renderer using the renderer_classes decorator to convert an API endpoint to display CSV instead of JSON. add below code in the menu-items function after the @api_view() decorator:

- @renderer_classes([CSVRenderer])

# YAML renderer
## Step 1
To display the output of your APIs in YAML, another popular data format, you need to install the djangorestframework-yaml using pipenv. 

- pipenv install djangorestframework-yaml

## Step 2
To test it with the menu-items function, import this YAML renderer in the views.py file.
- from rest_framework_yaml.renderers import YAMLRenderer

## Step 3
Pass the YAMLRenderer class inside the renderer_classes decorator, just below the api_view decorator above the menu-items function. 
- @renderer_classes([YAMLRenderer])

- Now if you visit the endpoint http://127.0.0.1:8000/api/menu-items in a REST API client like Insomnia, the menu items will be visible.

# Global settings

Instead of importing the CSV and YAML renderer classes individually in the views.py file and then passing them to the renderer_classes decorator above each function, you can make them available globally in your API project. In this way, the client can get the desired output with a valid Accept header. 

To make these renderers available globally, add the following two lines in the settings.py file in the DEFAULT_RENDERER_CLASSES section.

```python
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework_xml.renderers.XMLRenderer',
        'rest_framework_csv.renderers.CSVRenderer', 
        'rest_framework_yaml.renderers.YAMLRenderer', 
    ]
}
```
Now the client can send the following Accept headers to receive the API output in their desired format.

|Response type   |      Request header          |
|----------------|------------------------------|              
|CSV             |     Accept: text/csv         |
|YAML            |    Accept: application/yaml  |
