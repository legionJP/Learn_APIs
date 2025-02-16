from django.urls import  path, include
# from django.contrib import admin
from .import views

urlpatterns = [
    #path('books/', views.books),
    
# for class based 
    path('books/', views.BookList.as_view()),
    
]