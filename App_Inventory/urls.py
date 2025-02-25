from django.urls import path
from . import views

app_name = 'App_Inventory'

urlpatterns = [
    # Category URLs
    path('category/add/', views.add_category, name='add_category'),
    path('category/list/', views.category_list, name='category_list'),

    # Item URLs
    path('item/add/', views.add_item, name='add_item'),
    path('item/list/', views.item_list, name='item_list'),
]


