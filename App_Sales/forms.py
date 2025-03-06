from django import forms
from .models import Invoice, InvoiceItem
from App_Inventory.models import Items

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['payment_method', 'payment_amount', 'discount']

class InvoiceItemForm(forms.Form):
    item = forms.ModelChoiceField(queryset=Items.objects.all())
    quantity = forms.IntegerField(min_value=1)
