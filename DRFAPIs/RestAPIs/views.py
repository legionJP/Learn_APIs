import json
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
from django.db import IntegrityError
from .models import Book
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict

@csrf_exempt
def books(request):
    if request.method =='GET':
        books = Book.objects.all().values()
        return JsonResponse({'books': list(books)})
    
    elif request.method =='POST':
# checking if the request is json or form data 
        if request.content_type=='application/json':
            data = json.loads(request.body.decode('utf-8'))
        else:
            data=request.POST

        # using the data in the place of request.POST
        # title = request.POST.get('title')

        title = data.get('title')
        author= data.get('author')
        price = data.get('price')
        inventory = data.get('inventory')

        book = Book(title=title,author=author,price=price,inventory=inventory)
        try:
            {
                book.save()
            }
        except IntegrityError:
            return JsonResponse({'error':'true','message':'required field missing'}, status=400)

        return JsonResponse(model_to_dict(book), status=201)

