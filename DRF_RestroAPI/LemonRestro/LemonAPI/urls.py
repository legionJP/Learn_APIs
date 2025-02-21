from django.urls import URLPattern, path
from . import views

urlpatterns = [
    # path('menu-items/', views.MenuItemView.as_view()),
    #path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    #path('menu-items/', views.menu_items),
    path('menu-items/', views.menu_items1),

    # path('single-menu-item/<int:id>', views.single_menu_item),
    path('single-menu-item1/<int:id>', views.single_menu_item1),

]