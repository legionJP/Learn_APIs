from django.urls import URLPattern, path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # path('menu-items/', views.MenuItemView.as_view()),
    #path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    #path('menu-items/', views.menu_items),
    path('menu-items/', views.menu_items1),

    # path('single-menu-item/<int:id>', views.single_menu_item),
    path('single-menu-item1/<int:id>', views.single_menu_item1),
    path('category/<int:pk>', views.category_detail, name='category-detail'),
    path('menu', views.menu),
    path('welcome', views.welcome),
    # path for the filtering and pagination MenuItemViewSet
    path('menu-itemsV/', views.MenuItemViewSet.as_view(({'get':'list'}))),
    path('menu-itemsV/<int:pk>/', views.MenuItemViewSet.as_view(({'get':'retrieve'}
    ))),

    path('secret/', views.secret),
    path('api-token-auth/',obtain_auth_token) # api/api-token-auth/
]