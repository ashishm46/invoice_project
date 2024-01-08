from app.api.serializers import InvoiceSerializer,InvoiceDetailSerializer
from rest_framework import viewsets
from app.models import Invoice,InvoiceDetail



class InvoiceViews(viewsets.ModelViewSet):
 queryset = Invoice.objects.all()
 serializer_class = InvoiceSerializer


class InvoiceDetailViews(viewsets.ModelViewSet):
 queryset = InvoiceDetail.objects.all()
 serializer_class = InvoiceDetailSerializer
