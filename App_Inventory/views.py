from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Items, ItemImage
from .forms import CategoryForm, ItemForm, ItemImageForm
from django.contrib import messages
from django.http import JsonResponse

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
        form = ItemForm(request.POST, request.FILES) 
        
        if form.is_valid():
            item = form.save(commit=False)  
            item.save()  

            # Handle multiple images
            images = request.FILES.getlist('photos')  
            for img in images:
                ItemImage.objects.create(Item=item, photo=img)  

            return redirect('App_Inventory:item_list')
    else:
        form = ItemForm()
    
    categories = Category.objects.filter(is_addons=False)
    return render(request, 'App_Inventory/item.html', {'form': form, 'categories': categories})

def item_list(request):
    items = Items.objects.all()
    return render(request, 'App_Inventory/items_list.html', {'items': items})


# View Item
def view_item(request, pk):
    item = get_object_or_404(Items, pk=pk)
    images = item.itemimage_set.all()  # Get all images related to the item
    return render(request, 'App_Inventory/view_item.html', {'item': item, 'images': images})

# Edit Item
def edit_item(request, pk):
    item = get_object_or_404(Items, pk=pk)
    categories = Category.objects.filter(is_addons=False)

    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()

            # Handle images
            images = request.FILES.getlist('photos')  
            for img in images:
                ItemImage.objects.create(Item=item, photo=img)  

            messages.success(request, "Item updated successfully!")
            return redirect('App_Inventory:item_list')

    else:
        form = ItemForm(instance=item)

    images = item.itemimage_set.all()  # Fetch all images of the item
    return render(request, 'App_Inventory/edit_item.html', {'form': form, 'item': item, 'images': images,  "categories": categories})

# Delete Item
def delete_item(request, pk):
    if request.method == "POST":
        item = get_object_or_404(Items, pk=pk)
        item.delete()
        return JsonResponse({"success": True})
    return JsonResponse({"success": False}, status=400)