from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# from App_Auth import models
from App_Inventory import models
from App_Inventory import forms
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages

class AttributeListView(ListView):
    model = models.Attribute
    template_name = 'App_Inventory/attribute_list.html'
    context_object_name = 'attributes'


class AttributeCreateView(CreateView):
    model = models.Attribute
    form_class = forms.AttributeForm
    template_name = 'App_Inventory/attribute_form.html'
    success_url = reverse_lazy('App_Inventory:attribute_list')

class AttributeUpdateView(UpdateView):
    model = models.Attribute
    form_class = forms.AttributeForm
    template_name = 'App_Inventory/attribute_form.html'
    success_url = reverse_lazy('App_Inventory:attribute_list')

class AttributeDeleteView(DeleteView):
    model = models.Attribute
    template_name = 'App_Inventory/attribute_confirm_delete.html'
    success_url = reverse_lazy('App_Inventory:attribute_list')


# AttributeTerm Views
class AttributeTermListView(ListView):
    model = models.AttributeTerm
    template_name = 'App_Inventory/attribute_term_list.html'
    context_object_name = 'attribute_terms'


class AttributeTermCreateView(CreateView):
    model = models.AttributeTerm
    form_class = forms.AttributeTermForm
    template_name = 'App_Inventory/attribute_term_form.html'
    success_url = reverse_lazy('App_Inventory:attribute_list')

    def get_initial(self):
        attribute_id = self.kwargs.get('attribute_id')
        return {'attribute': attribute_id}

    def form_valid(self, form):
        form.instance.attribute_id = self.kwargs.get('attribute_id')
        return super().form_valid(form)


class AttributeTermUpdateView(UpdateView):
    model = models.AttributeTerm
    form_class = forms.AttributeTermForm
    template_name = 'App_Inventory/attribute_term_form.html'
    success_url = reverse_lazy('App_Inventory:attribute_term_list')


class AttributeTermDeleteView(DeleteView):
    model = models.AttributeTerm
    template_name = 'App_Inventory/attribute_term_confirm_delete.html'
    success_url = reverse_lazy('App_Inventory:attribute_term_list')


# Category Views
class CategoryListView(ListView):
    model = models.Category
    template_name = 'App_Inventory/category_list.html'
    context_object_name = 'categories'


class CategoryCreateView(CreateView):
    model = models.Category
    form_class = forms.CategoryForm
    template_name = 'App_Inventory/category_form.html'
    success_url = reverse_lazy('App_Inventory:category_list')


class CategoryUpdateView(UpdateView):
    model = models.Category
    form_class = forms.CategoryForm
    template_name = 'App_Inventory/category_form.html'
    success_url = reverse_lazy('App_Inventory:category_list')


class CategoryDeleteView(DeleteView):
    model = models.Category
    template_name = 'App_Inventory/category_confirm_delete.html'
    success_url = reverse_lazy('App_Inventory:category_list')


# Brand Views
class BrandListView(ListView):
    model = models.Brand
    template_name = 'App_Inventory/brand_list.html'
    context_object_name = 'brands'


class BrandCreateView(CreateView):
    model = models.Brand
    form_class = forms.BrandForm
    template_name = 'App_Inventory/brand_form.html'
    success_url = reverse_lazy('App_Inventory:brand_list')


class BrandUpdateView(UpdateView):
    model = models.Brand
    form_class = forms.BrandForm
    template_name = 'App_Inventory/brand_form.html'
    success_url = reverse_lazy('App_Inventory:brand_list')


class BrandDeleteView(DeleteView):
    model = models.Brand
    template_name = 'App_Inventory/brand_confirm_delete.html'
    success_url = reverse_lazy('App_Inventory:brand_list')

    # def get_object(self, queryset=None):
    #     """Retrieve the brand instance."""
    #     return get_object_or_404(models.Brand, pk=self.kwargs['pk'])

    # def delete(self, request, *args, **kwargs):
    #     """Override delete to add messages."""
    #     self.object = self.get_object()
    #     self.object.delete()
    #     messages.success(request, "Brand deleted successfully!")
    #     return super().delete(request, *args, **kwargs)


# Tag Views
class TagListView(ListView):
    model = models.Tag
    template_name = 'App_Inventory/tag_list.html'
    context_object_name = 'tags'


class TagCreateView(CreateView):
    model = models.Tag
    form_class = forms.TagForm
    template_name = 'App_Inventory/tag_form.html'
    success_url = reverse_lazy('App_Inventory:tag_list')


class TagUpdateView(UpdateView):
    model = models.Tag
    form_class = forms.TagForm
    template_name = 'App_Inventory/tag_form.html'
    success_url = reverse_lazy('App_Inventory:tag_list')


class TagDeleteView(DeleteView):
    model = models.Tag
    template_name = 'App_Inventory/tag_confirm_delete.html'
    success_url = reverse_lazy('App_Inventory:tag_list')


# Items Views
class ItemsListView(ListView):
    model = models.Items
    template_name = 'App_Inventory/items_list.html'
    context_object_name = 'items'


class ItemsCreateView(CreateView):
    model = models.Items
    form_class = forms.ItemsForm
    template_name = 'App_Inventory/items_form.html'
    success_url = reverse_lazy('App_Inventory:items_list')


class ItemsUpdateView(UpdateView):
    model = models.Items
    form_class = forms.ItemsForm
    template_name = 'App_Inventory/items_form.html'
    success_url = reverse_lazy('App_Inventory:items_list')


class ItemsDeleteView(DeleteView):
    model = models.Items
    template_name = 'App_Inventory/items_confirm_delete.html'
    success_url = reverse_lazy('App_Inventory:items_list')


# ItemVariation Views
class ItemVariationListView(ListView):
    model = models.ItemVariation
    template_name = 'App_Inventory/item_variation_list.html'
    context_object_name = 'item_variations'


class ItemVariationCreateView(CreateView):
    model = models.ItemVariation
    form_class = forms.ItemVariationForm
    template_name = 'App_Inventory/item_variation_form.html'
    success_url = reverse_lazy('App_Inventory:item_variation_list')


class ItemVariationUpdateView(UpdateView):
    model = models.ItemVariation
    form_class = forms.ItemVariationForm
    template_name = 'App_Inventory/item_variation_form.html'
    success_url = reverse_lazy('App_Inventory:item_variation_list')


class ItemVariationDeleteView(DeleteView):
    model = models.ItemVariation
    template_name = 'App_Inventory/item_variation_confirm_delete.html'
    success_url = reverse_lazy('App_Inventory:item_variation_list')

