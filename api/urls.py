from django.urls import path
from . import views

urlpatterns = [
    path('invoices/', views.InvoiceList.as_view(), name='invoices'),
    path('invoices/<int:pk>/', views.InvoiceDetail.as_view(), name='invoice-detail'),
]
