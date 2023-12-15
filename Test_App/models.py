from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Header(models.Model):

    Date = models.DateField(auto_now_add=True)
    InvoiceNumber = models.IntegerField(unique=True)
    CustomerName = models.CharField(max_length=255)
    BillingAddress = models.TextField()
    ShippingAddress = models.TextField
    GSTIN = models.TextField()
    TotalAmount = models.DecimalField(default=0.0, decimal_places=2, max_digits=8)

    def __str__(self) -> str:
        return self.InvoiceNumber


class Item(models.Model):

    invoice_header = models.ForeignKey(Header, on_delete=models.CASCADE)
    itemName = models.CharField(max_length=255)
    Quantity = models.DecimalField(default=0, decimal_places=2, max_digits=8)
    Price = models.DecimalField(default=0, decimal_places=2, max_digits=8)
    Amount = models.DecimalField(default=0, decimal_places=2, max_digits=8)

    def __str__(self) -> str:
        return self.InvoiceNumber

class BillSundry(models.Model):

    invoice_header = models.ForeignKey(Header, on_delete=models.CASCADE)
    billSundryName = models.CharField(max_length=255)
    Amount = models.DecimalField(default=0, decimal_places=2, max_digits=8)

    def __str__(self) -> str:
        return self.billSundryName

