from django.contrib import admin
from .models import Invoice,InvoiceDetail
# Register your models here.



@admin.register(Invoice)
class Invoice(admin.ModelAdmin):
    list_display= ['invoice','date','customer_name']

@admin.register(InvoiceDetail)
class InvoiceDetail(admin.ModelAdmin):
    list_display= ['description','quantity','unit_price']