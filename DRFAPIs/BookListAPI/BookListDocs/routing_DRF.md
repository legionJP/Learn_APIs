# Different Types of  routing in DRF

# Introduction 

```markdown
The Django REST framework provides different ways of URL mapping or routing in an API project. Besides the traditional style of routing, there are other routing techniques that can save you time while developing.

Note: All the routings should be done in the urls.py file in your Django app.
```

# Regular routes
-It maps a function from a views.py file to an API endpoint
```python

from django.urls import path
from . import views
urlpatterns = [
	path('books’,views.books) ,
]

```
- This URL pattern maps the books function to the /api/books endpoint.
@api_view([‘GET’,’POST’])

# Routing to a class method

```markdown
If you map a specific method from a class, then you need to declare that method as a @staticmethod first. After that, you can map it in the urls.py file. Here’s an example of a class in the views.py file.
```
```python
class orders():
    @staticmethod
    @api_voew()
    def listorders():
        return Response({'message': 'list of orders'}, 200)
    
```
#### mapping this listOrders method in the urls.py file :
```python
from django.urls
    
```