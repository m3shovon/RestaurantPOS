from django.urls import path
from . import views

app_name = 'App_Inventory'

urlpatterns = [

    # Attribute
    path('attribute/', views.AttributeListView.as_view(), name='attribute_list'),
    path('attribute/create/', views.AttributeCreateView.as_view(), name='attribute_create'),
    path('attribute/<int:pk>/update/', views.AttributeUpdateView.as_view(), name='attribute_update'),
    path('attribute/<int:pk>/delete/', views.AttributeDeleteView.as_view(), name='attribute_delete'),

    # AttributeTerm URLs
    path('attribute-term/', views.AttributeTermListView.as_view(), name='attribute_term_list'),
    path('attribute-term/add/<int:attribute_id>/', views.AttributeTermCreateView.as_view(), name='attribute_term_add'),
    path('attribute-term/<int:pk>/edit/', views.AttributeTermUpdateView.as_view(), name='attribute_term_edit'),
    path('attribute-term/<int:pk>/delete/', views.AttributeTermDeleteView.as_view(), name='attribute_term_delete'),

    # Category URLs
    path('category/', views.CategoryListView.as_view(), name='category_list'),
    path('category/add/', views.CategoryCreateView.as_view(), name='category_add'),
    path('category/<int:pk>/edit/', views.CategoryUpdateView.as_view(), name='category_edit'),
    path('category/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category_delete'),

    # Brand URLs
    path('brand/', views.BrandListView.as_view(), name='brand_list'),
    path('brand/add/', views.BrandCreateView.as_view(), name='brand_add'),
    path('brand/<int:pk>/edit/', views.BrandUpdateView.as_view(), name='brand_edit'),
    path('brand/<int:pk>/delete/', views.BrandDeleteView.as_view(), name='brand_delete'),

    # Tag URLs
    path('tag/', views.TagListView.as_view(), name='tag_list'),
    path('tag/add/', views.TagCreateView.as_view(), name='tag_add'),
    path('tag/<int:pk>/edit/', views.TagUpdateView.as_view(), name='tag_edit'),
    path('tag/<int:pk>/delete/', views.TagDeleteView.as_view(), name='tag_delete'),

    # Items URLs
    path('items/', views.ItemsListView.as_view(), name='items_list'),
    path('items/add/', views.ItemsCreateView.as_view(), name='items_add'),
    path('items/<int:pk>/edit/', views.ItemsUpdateView.as_view(), name='items_edit'),
    path('items/<int:pk>/delete/', views.ItemsDeleteView.as_view(), name='items_delete'),

    # ItemVariation URLs
    path('item-variation/', views.ItemVariationListView.as_view(), name='item_variation_list'),
    path('item-variation/add/', views.ItemVariationCreateView.as_view(), name='item_variation_add'),
    path('item-variation/<int:pk>/edit/', views.ItemVariationUpdateView.as_view(), name='item_variation_edit'),
    path('item-variation/<int:pk>/delete/', views.ItemVariationDeleteView.as_view(), name='item_variation_delete'),

]

