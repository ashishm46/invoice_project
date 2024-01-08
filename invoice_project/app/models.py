from django.db import models

# Create your models here.

class Invoice(models.Model):
    invoice = models.CharField(max_length=50)
    date = models.DateField()
    customer_name = models.CharField(max_length=50)

    def __str__(self):
        return self.invoice
    


class InvoiceDetail(models.Model):
    Invoice = models.ForeignKey(Invoice,on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    quantity = models.IntegerField()
    unit_price = models.IntegerField()

   