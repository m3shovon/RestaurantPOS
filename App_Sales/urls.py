from django.urls import path
from .views import invoice_list, invoice_detail, create_invoice

app_name = 'App_Sales'

urlpatterns = [
    path('invoices/', invoice_list, name='invoice_list'),
    path('invoice/<int:pk>/', invoice_detail, name='invoice_detail'),
    path('invoice/create/', create_invoice, name='create_invoice'),
]