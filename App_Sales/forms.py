from django import forms
from .models import Invoice, InvoiceItem
from App_Inventory.models import Items

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['payment_method', 'payment_amount', 'discount']

# class InvoiceItemForm(forms.ModelForm):
#     class Meta:
#         model = InvoiceItem
#         fields = ['item', 'quantity', 'price']
    
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['item'].queryset = Items.objects.all()  


class InvoiceItemForm(forms.ModelForm):
    class Meta:
        model = InvoiceItem
        fields = ['item', 'quantity', 'price']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['item'].queryset = Items.objects.all()
        self.fields['item'].widget.attrs.update({'onchange': 'updatePrice(this)'})
        
        # Add price as data attribute in options
        self.fields['item'].widget.choices = [
            (item.id, f"{item.title} - ${item.selling_price}") for item in Items.objects.all()
        ]
        
