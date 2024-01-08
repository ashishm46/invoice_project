from django.urls import path, include
from app.api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('invoice', views.InvoiceViews, basename='invoice')
router.register('invoicedetail', views.InvoiceDetailViews, basename='invoicedetail')

urlpatterns = [
    path('', include(router.urls))
]