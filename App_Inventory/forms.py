from django import forms
from .models import Attribute, AttributeTerm, Category, Brand, Tag, Items, ItemImage

# class CategoryForm(forms.ModelForm):
#     Category_parent = forms.ModelChoiceField(
#         queryset=Category.objects.all(), 
#         required=False,
#         empty_label="None",
#         widget=forms.Select(attrs={'class': 'form-select'})
#     )

#     class Meta:
#         model = Category
#         fields = ['name', 'slug', 'is_addons', 'Category_parent']
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'slug', 'is_addons', 'Category_parent']
        widgets = {
            'Category_parent': forms.Select(attrs={'class': 'form-select'}),
        }
        
class ItemForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = [
            'Category', 'Sub_Category', 'related_Items', 'title', 'sku', 'rack', 'slug', 
            'barcode', 'remarks', 'purchase_price', 'selling_price', 'discount_price', 
            'quantity', 'discount', 'Location', 'action_details', 'is_active'
        ]
class ItemImageForm(forms.ModelForm):
    class Meta:
        model = ItemImage
        fields = '__all__'


# class BrandForm(forms.ModelForm):
#     class Meta:
#         model = Brand
#         fields = '__all__'

# class TagForm(forms.ModelForm):
#     class Meta:
#         model = Tag
#         fields = '__all__'

# class AttributeForm(forms.ModelForm):
#     class Meta:
#         model = Attribute
#         fields = '__all__'

# class AttributeTermForm(forms.ModelForm):
#     class Meta:
#         model = AttributeTerm
#         fields = '__all__'

# class ItemVariationForm(forms.ModelForm):
#     class Meta:
#         model = ItemVariation
#         fields = '__all__'



