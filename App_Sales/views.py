from django.shortcuts import render, get_object_or_404, redirect
from .models import Invoice, InvoiceItem
from .forms import InvoiceForm, InvoiceItemForm
from django.forms import formset_factory

def invoice_list(request):
    invoices = Invoice.objects.all()
    return render(request, 'App_Sales/invoice_list.html', {'invoices': invoices})

def invoice_detail(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    return render(request, 'App_Sales/invoice_detail.html', {'invoice': invoice})

def create_invoice(request):
    InvoiceItemFormSet = formset_factory(InvoiceItemForm, extra=1)
    
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        formset = InvoiceItemFormSet(request.POST)
        
        if form.is_valid() and formset.is_valid():
            invoice = form.save()
            total_amount = 0
            
            for item_form in formset:
                item = item_form.cleaned_data.get('item')
                quantity = item_form.cleaned_data.get('quantity')
                if item:
                    price = item.selling_price * quantity
                    total_amount += price
                    InvoiceItem.objects.create(invoice=invoice, item=item, quantity=quantity, price=price)
            
            invoice.payment_amount = total_amount - invoice.discount
            invoice.save()
            return redirect('App_Sales:invoice_list')
    else:
        form = InvoiceForm()
        formset = InvoiceItemFormSet()
    
    return render(request, 'App_Sales/POS.html', {'form': form, 'formset': formset})