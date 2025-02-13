from django.urls import path 
from . import views

# urlpatterns = [
#     path('ratings', views.RatingView.as_view()),
# ]
urlpatterns= [
    path('api/', views.books),
    # path('books',views.books),
]