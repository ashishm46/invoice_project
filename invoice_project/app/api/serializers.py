from app.models import InvoiceDetail,Invoice
from rest_framework import serializers

# from myshop.app.models import Product

class InvoiceSerializer(serializers.ModelSerializer):
 class Meta:
  model = Invoice
  fields = "__all__"


class InvoiceDetailSerializer(serializers.ModelSerializer):
 class Meta:
  model = InvoiceDetail
  fields = "__all__" 