from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Items
from .forms import CategoryForm, ItemForm

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'App_Inventory/category_list.html', {'categories': categories})

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('App_Inventory:category_list')  
    else:
        form = CategoryForm()
    return render(request, 'App_Inventory/category_list.html', {'form': form, 'categories': Category.objects.all()})

# Item Views
def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('App_Inventory:item_list')
    else:
        form = ItemForm()
    return render(request, 'App_Inventory/item.html', {'form': form})

def item_list(request):
    items = Items.objects.all()
    return render(request, 'App_Inventory/item_list.html', {'items': items})