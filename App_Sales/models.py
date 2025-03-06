from django.db import models
from App_Inventory.models import Items

class Invoice(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('cash', 'Cash'),
        ('credit_card', 'Credit Card'),
        ('debit_card', 'Debit Card'),
        ('bank_transfer', 'Bank Transfer'),
        ('paypal', 'PayPal'),
    ]
    invoice_number = models.CharField(max_length=255, blank=True)
    order_number = models.CharField(max_length=255, blank=True)
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHOD_CHOICES)
    payment_amount = models.DecimalField(max_digits=20, decimal_places=2)
    discount = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Invoice {self.id} - {self.payment_method}"

class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='invoice_items')
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=20, decimal_places=2)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return f"{self.item.title} - {self.quantity} x {self.price}"  