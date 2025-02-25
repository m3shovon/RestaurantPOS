from django import forms
from .models import Attribute, AttributeTerm, Category, Brand, Tag, Items, ItemVariation, ItemImage

class AttributeForm(forms.ModelForm):
    class Meta:
        model = Attribute
        fields = '__all__'

class AttributeTermForm(forms.ModelForm):
    class Meta:
        model = AttributeTerm
        fields = '__all__'

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'

class ItemsForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = '__all__'

class ItemVariationForm(forms.ModelForm):
    class Meta:
        model = ItemVariation
        fields = '__all__'

class ItemImageForm(forms.ModelForm):
    class Meta:
        model = ItemImage
        fields = '__all__'

