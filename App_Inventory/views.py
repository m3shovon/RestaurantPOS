from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Items
from .forms import CategoryForm, ItemForm

def category_list(request):
    main_categories = Category.objects.filter(Category_parent__isnull=True)  # Fetch only main categories
    categories = Category.objects.all()  # Fetch all categories for the dropdown
    return render(request, 'App_Inventory/category_list.html', {'main_categories': main_categories, 'categories': categories})

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('App_Inventory:category_list')  
    else:
        form = CategoryForm()
    
    categories = Category.objects.all()  # Fetch all categories for the dropdown
    return render(request, 'App_Inventory/category_list.html', {'form': form, 'categories': categories})

# Item Views
def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('App_Inventory:item_list')
    else:
        form = ItemForm()
    categories = Category.objects.all().filter(is_addons=False)
    return render(request, 'App_Inventory/item.html', {'form': form, 'categories': categories})

def item_list(request):
    items = Items.objects.all()
    return render(request, 'App_Inventory/items_list.html', {'items': items})